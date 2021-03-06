from scrapy import signals
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from scrapy.http import HtmlResponse
# from selenium.webdriver.support import expected_conditions as Expect
# from selenium.webdriver.common.by import By

class XtzxDownloaderMiddleware:
    """Scrapy middleware handling the requests using selenium"""

    def __init__(self):
        driver_executable_path = 'V:\Code\Py_projects\spiders\chromedriver.exe'
        driver_options = webdriver.ChromeOptions()
        driver_options.add_argument('--headless')
        driver_options.add_argument('--ignore-certificate-errors-spki-list')
        driver_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        driver_options.add_argument("disable-blink-features=AutomationControlled")
        driver_options.add_argument('log-level=3')
    
        self.driver = webdriver.Chrome(executable_path = driver_executable_path, options = driver_options)
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                })
            """
        })

    @classmethod
    def from_crawler(cls, crawler):
        """Initialize the middleware with the crawler settings"""
        
        middleware = cls()
        crawler.signals.connect(middleware.spider_closed, signals.spider_closed)
        return middleware

    def process_request(self, request, spider):
        self.driver.implicitly_wait(30)
        self.driver.get(request.url)
        self.driver.find_elements_by_class_name('result')
        # x = WebDriverWait(self.driver, 30).until(Expect.presence_of_element_located((By.CLASS_NAME, "result")))

        for cookie_name, cookie_value in request.cookies.items():
            self.driver.add_cookie(
                {
                    'name': cookie_name,
                    'value': cookie_value
                }
            )
        if request.wait_until:
            WebDriverWait(self.driver, request.wait_time).until(
                request.wait_until
            )

        body = str.encode(self.driver.page_source)

        # Expose the driver via the "meta" attribute
        request.meta.update({'driver': self.driver})

        return HtmlResponse(
            self.driver.current_url,
            body=body,
            encoding='utf-8',
            request=request
        )

    def spider_closed(self):
        """Shutdown the driver when spider is closed"""
        self.driver.quit()