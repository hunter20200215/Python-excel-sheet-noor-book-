import time
import pickle
import selenium.webdriver 
import csv

output_file = 'noor-book.csv'
default_timeout = 50


def add_csv_head():
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Title','Category','Author','File_Type','Language','Pages','Description'])

def add_csv_row(title, category,author,file_type, language,pages,description):
    with open(output_file, 'a', newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([title, category,author,file_type, language,pages,description])

add_csv_head()

driver = selenium.webdriver.Chrome()
url='https://www.noor-book.com/en/ebook-%D8%A7%D9%84%D8%B1%D8%AD%D9%84%D9%87-%D8%A7%D9%84%D8%A7%D8%AE%D9%8A%D8%B1%D9%87--pdf'
driver.get(url)
driver.implicitly_wait(default_timeout)
time.sleep(5)
i = 1
while i < 90000:
	title=driver.find_element_by_xpath('//h2[@class]').text
	
	category=driver.find_element_by_xpath('//span[@id="book-category"]').text
	
	author=driver.find_element_by_xpath('//span[@id="book-writer"]').text
	
	file_type="PDF"
	language=driver.find_elements_by_xpath('//span[@id="book-category"]')[1].text
	

	pages=driver.find_element_by_xpath('//span[text()="Pages"]/../following-sibling::td').text
	

	description=driver.find_element_by_xpath('//span[@class="more"]').text

	add_csv_row(title,category,author,file_type,language,pages,description)	
	time.sleep(1)
	download_link=driver.find_element_by_xpath('//a[@data-target="#downloadModal"]')
	download_link.click()
	time.sleep(15)
	try:
		download=driver.find_element_by_xpath('//a[@class="internal_download_link"]')
	except:
		time.sleep(15)
	if download is None:
		time.sleep(10)

	download=driver.find_element_by_xpath('//a[@class="internal_download_link"]')
	download.click()
	time.sleep(3)

	driver.find_element_by_xpath('//button[@data-dismiss="modal"][@class="close"]').click()
	time.sleep(5)
	next=driver.find_element_by_xpath('//a[@class="next_book"]').click()
	
	driver.implicitly_wait(default_timeout)
	time.sleep(10)
	
	i += 1
	
	print('---------------------')



print("done")

