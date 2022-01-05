# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from time import sleep
from selenium import webdriver
from scrapy.http import HtmlResponse
from scrapy import signals

import random
from covid.settings import USER_AGENT_LIST
import time

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class CovidDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def __init__(self):
        driver_executable_path = 'V:\Code\Py_projects\spiders\chromedriver.exe'
        driver_options = webdriver.ChromeOptions()
        # driver_options.add_argument('--headless')
        driver_options.add_argument('--ignore-certificate-errors-spki-list')
        driver_options.add_argument('log-level=3')
        self.driver = webdriver.Chrome(executable_path=driver_executable_path,
                                       options=driver_options)

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        rand_use = random.choice(USER_AGENT_LIST)
        if rand_use:
            request.headers.setdefault('User-Agent', rand_use)
        self.driver.implicitly_wait(30)
        self.driver.get(request.url)

        time.sleep(2)

        # yesterday
        # target = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[5]/ul/li[2]/a")
        # 2 days ago
        target = self.driver.find_element_by_xpath(
            "/html/body/div[3]/div[3]/div/div[5]/ul/li[3]/a")
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        target.click()
        time.sleep(2)
        for cookie_name, cookie_value in request.cookies.items():
            self.driver.add_cookie({
                'name': cookie_name,
                'value': cookie_value
            })

        # if request.wait_until:
        #     WebDriverWait(self.driver, request.wait_time).until(
        #         request.wait_until
        #     )

        body = str.encode(self.driver.page_source)

        # Expose the driver via the "meta" attribute
        request.meta.update({'driver': self.driver})

        return HtmlResponse(self.driver.current_url,
                            body=body,
                            encoding='utf-8',
                            request=request)
        return None

    # def process_exception(self, request, exception, spider):
    #     # Called when a download handler or a process_request()
    #     # (from other downloader middleware) raises an exception.

    #     # Must either:
    #     # - return None: continue processing this exception
    #     # - return a Response object: stops process_exception() chain
    #     # - return a Request object: stops process_exception() chain
    #     pass

    def spider_closed(self):
        """Shutdown the driver when spider is closed"""
        self.driver.quit()