from scrapy import Request

class MyRequest(Request):

    def __init__(self, wait_time=None, wait_until=None, *args, **cb_kwargs):
        self.wait_time = wait_time
        self.wait_until = wait_until
        super().__init__(*args, **cb_kwargs)