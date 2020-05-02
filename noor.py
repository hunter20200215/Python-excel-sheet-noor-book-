import time
import pickle
import selenium.webdriver 
import csv
from lxml import html
import xlsxwriter


default_timeout = 50


workbook   = xlsxwriter.Workbook('test1.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0, 0, 'Title')
worksheet.write(0, 1, 'Category')
worksheet.write(0, 2, 'Author')
worksheet.write(0, 3, 'File_type')
worksheet.write(0, 4, 'Language')
worksheet.write(0, 5, 'Pages')
worksheet.write(0, 6, 'description')



driver = selenium.webdriver.Chrome()
url='https://www.noor-book.com/en/ebook-%D8%A7%D9%84%D8%B1%D8%AD%D9%84%D9%87-%D8%A7%D9%84%D8%A7%D8%AE%D9%8A%D8%B1%D9%87--pdf'
driver.get(url)
driver.implicitly_wait(default_timeout)
time.sleep(5)
row = 1
col = 0
i = 1
while i < 90000:
	title=driver.find_element_by_xpath('//h2[@class]').text
	
	category=driver.find_element_by_xpath('//span[@id="book-category"]').text
	
	author=driver.find_element_by_xpath('//span[@id="book-writer"]').text
	
	file_type="PDF"
	language=driver.find_elements_by_xpath('//span[@id="book-category"]')[1].text
	

	pages=driver.find_element_by_xpath('//span[text()="Pages"]/../following-sibling::td').text
	

	description=driver.find_element_by_xpath('//span[@class="more"]').text

	array=[title,category,author,file_type,language,pages,description]
	
	

	worksheet.write(row, col, title)
	worksheet.write(row, col + 1, category)
	worksheet.write(row, col + 2, author)
	worksheet.write(row, col + 3, file_type)
	worksheet.write(row, col + 4, language)
	worksheet.write(row, col + 5, pages)
	worksheet.write(row, col + 6, description)

	row += 1


	download_link=driver.find_element_by_xpath('//a[@data-target="#downloadModal"]')
	download_link.click()
	time.sleep(15)

	try:
		download=driver.find_element_by_xpath('//a[@class="internal_download_link"]')
	except:
		time.sleep(10)
	if download is None:
		time.sleep(10)

	download=driver.find_element_by_xpath('//a[@class="internal_download_link"]')
	download.click()
	time.sleep(15)

	driver.find_element_by_xpath('//button[@data-dismiss="modal"][@class="close"]').click()

	next=driver.find_element_by_xpath('//a[@class="next_book"]').click()
	
	driver.implicitly_wait(default_timeout)
	time.sleep(5)
	i += 1
	print('---------------------')

workbook.close()


print("done")

