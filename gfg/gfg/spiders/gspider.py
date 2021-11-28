import scrapy
from scrapy_selenium import SeleniumRequest

class GfgSpider(scrapy.Spider):
	name = 'gfg'
	def start_requests(self):
		yield SeleniumRequest(
			url = "https://practice.geeksforgeeks.org/courses/online",
			wait_time = 3,
			screenshot = True,
			callback = self.parse,
			dont_filter = True
		)

	def parse(self, response):
		# courses make list of all items that came in this xpath
		# this xpath is of cards containing courses details
		courses = response.xpath('/html/body/div[10]/div[6]/div[1]/div/div/div')
		
		print(courses)

		# course is each course in the courses list
		for course in courses:
			# xpath of course name is added in the course path
			# text() will scrape text from h4 tag that contains course name

			course_name = course.xpath('./div/div/a/div[2]/div/div[2]/h4/text()').get()

        
			# course_name is a string containing \n and extra spaces
			# these \n and extra spaces are removed

			course_name = course_name.split('\n')[1]
			course_name = course_name.strip()

			yield {
				'course Name':course_name
			}
		
		nxt_page = 