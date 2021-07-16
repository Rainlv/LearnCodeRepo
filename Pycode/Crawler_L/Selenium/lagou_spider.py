import random
from time import sleep
import re
from selenium import webdriver
from lxml import etree
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By
import csv


class LagoSpider(object):

    def __init__(self):
        self.url = 'https://www.lagou.com/jobs/list_python/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput='
        self.drive_path = r'E:\Anaconda\chromedriver.exe'
        self.drive = webdriver.Chrome(executable_path=self.drive_path)
        self.detail_page_url_list = []
        self.job_requests = []
        self.drive.get(self.url)
        self.page_num = 0

    def run(self):
        while True:
            try:
                turnoff_btn = self.drive.find_element_by_class_name('body-btn')
                turnoff_btn.click()
            except Exception as e:
                print(e)
            self.parse_list_page()
            # print(self.detail_page_url_list)
            self.parse_detail_page()
            self.save_data()
            if self.drive.find_element_by_xpath('//div[@class="pager_container"]/span[@class="pager_is_current"]').get_attribute('textContent') != '30':
                next_page_button = self.drive.find_element_by_xpath(r'//div[@class="pager_container"]/span[last()]')
                next_page_button.click()
                self.page_num += 1
                print('*' * 30)
                print('第{}页爬取完成'.format(self.page_num))
                print('*' * 30)
            else:
                print('所有页面爬取完成')
                self.drive.quit()
                break

    def parse_list_page(self):
        source = self.drive.page_source
        list_page = etree.HTML(source)
        self.detail_page_url_list = list_page.xpath('//a[@class="position_link"]/@href')
        # print(self.detail_page_url_list)

    def parse_detail_page(self):
        for detail_url in self.detail_page_url_list:
            print(detail_url)
            self.drive.execute_script("window.open('%s')" % detail_url)
            self.drive.switch_to.window(self.drive.window_handles[-1])
            source = self.drive.page_source
            detail_page = etree.HTML(source)
            salary = detail_page.xpath('//dd[@class="job_request"]//span/text()')[0]
            work_place = detail_page.xpath('//dd[@class="job_request"]//span/text()')[1]
            experience = detail_page.xpath('//dd[@class="job_request"]//span/text()')[2]
            education = detail_page.xpath('//dd[@class="job_request"]//span/text()')[3]
            part_time = detail_page.xpath('//dd[@class="job_request"]//span/text()')[4]
            salary = re.sub(r'[\s/]', '', salary)
            work_place = re.sub(r'[\s/]', '', work_place)
            experience = re.sub(r'[\s/]', '', experience)
            education = re.sub(r'[\s/]', '', education)
            part_time = re.sub(r'[\s/]', '', part_time)
            job_detail = "".join(detail_page.xpath('//div[@class="job-detail"]/p/text()'))
            job_requests = {
                'salary': salary,
                'experience': experience,
                'work_place': work_place,
                'education': education,
                'part_time': part_time,
                'job_detail': job_detail
            }
            self.job_requests.append(job_requests)
            print(job_requests)
            self.drive.close()
            self.drive.switch_to.window(self.drive.window_handles[0])
            sleep(random.randint(1, 2))

    def save_data(self):
        with open(r'lago.csv', 'a', encoding='utf-8') as w_csv:
            csv_head = ['salary', 'experience', 'work_place', 'education', 'part_time', 'job_detail']
            csv_writer = csv.DictWriter(w_csv, csv_head)
            csv_writer.writeheader()
            csv_writer.writerows(self.job_requests)


if __name__ == '__main__':
    with open(r'lago.csv', 'w', encoding='utf-8') as w:
        head = ['salary', 'experience', 'work_place', 'education', 'part_time', 'job_detail']
        writer = csv.DictWriter(w, head)
        writer.writeheader()

    s = LagoSpider()
    s.run()
