# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import random
import time
from wrdata.settings import USER_AGENT_LIST


class WrdataDownloaderMiddleware:
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
        # rand_use = random.choice(USER_AGENT_LIST)
        # if rand_use:
        #     request.headers.setdefault('User-Agent', rand_use)
        self.driver.implicitly_wait(30)
        self.driver.get(request.url)
        time.sleep(8)
        for cookie_name, cookie_value in request.cookies.items():
            self.driver.add_cookie({
                'name': cookie_name,
                'value': cookie_value
            })

        body = str.encode(self.driver.page_source)

        # Expose the driver via the "meta" attribute
        request.meta.update({'driver': self.driver})

        return HtmlResponse(self.driver.current_url,
                            body=body,
                            encoding='utf-8',
                            request=request)

    def spider_closed(self):
        """Shutdown the driver when spider is closed"""
        self.driver.quit()