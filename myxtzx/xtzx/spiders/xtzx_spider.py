import scrapy
from xtzx.http import MyRequest
from xtzx.items import XtzxItem

class XtzxSpider(scrapy.Spider):
    name = 'xtzx'

    def start_requests(self):
        self.id = 1
        self.page = 1
        self.max_page = 52

        yield MyRequest(
            url=
            r'https://www.xuetangx.com/search?query=&org=&classify=1&type=&status=&page=1',
            callback=self.parse,
            dont_filter=True)

    def parse(self, response):
        # courses make list of all items that came in this xpath
        print("res:", response)
        courses = response.xpath(
            "/html/body/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div")

        # course is each course in the courses list
        for course in courses:
            course_name = course.xpath("./div[2]/p[1]/span[1]/text()").get()
            if course_name is None:
                continue
            teachers = course.xpath("./div[2]/p[2]/span[1]/span[@class]")
            teacher = []
            for t in teachers:
                tmp = t.xpath('./text()').get()
                if tmp != "等":
                    teacher.append(tmp)

            school = course.xpath("./div[2]/p[2]/span[2]/span/text()").get()
            number = course.xpath("./div[2]/p[2]/span[3]/text()").get()
            if number != None:
                number = number.split('\n')[1]
                number = number.strip()

            item = XtzxItem()
            item['id'] = self.id
            item['page'] = self.page
            self.id += 1
            item['course_name'] = course_name
            item['teachers'] = teacher
            item['school'] = school
            item['number'] = number
            yield item

        if self.page + 1 <= self.max_page:
            self.page += 1
            nxt_url = f'https://www.xuetangx.com/search?query=&org=&classify=1&type=&status=&page={self.page}'
            # Expect.title_is("学堂在线 - 精品在线课程学习平台")

            yield MyRequest(url=nxt_url,
                            callback=self.parse,
                            dont_filter=True)
