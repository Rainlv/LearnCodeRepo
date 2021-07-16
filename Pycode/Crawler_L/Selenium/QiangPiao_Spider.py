from selenium import webdriver
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class TicketSpider(object):
    def __init__(self):
        self.drive_path = r'E:\Anaconda\chromedriver.exe'
        self.drive = webdriver.Chrome(executable_path=self.drive_path)

    def _info(self):
        self.fromStation = input('请输入出发地:')
        self.toStation = input('请输入目的地:')
        self.train_date = input('请输入出发日期(格式如:2020-02-17):')
        self.train_number = input('请输入车次(多列车次用“,”分隔):').split(',')
        self.passenger = input('请输入乘客名(多名乘客用“,”分隔):').split(',')

    def run(self):
        self._info()
        self._login()
        self._goto_ticket_page()
        self._choose_ticket()
        self._buy_ticket()

    def _login(self):
        self.drive.get('https://kyfw.12306.cn/otn/resources/login.html')
        login_way_button = self.drive.find_element_by_class_name('login-hd-account')
        login_way_button.click()
        WebDriverWait(self.drive, 100).until(
            Ec.visibility_of_element_located((By.ID, 'J-userName'))
        )
        usernameTag = self.drive.find_element_by_id('J-userName')
        usernameTag.send_keys('15858604775')
        passwordTag = self.drive.find_element_by_id('J-password')
        passwordTag.send_keys('wxh172706002')
        WebDriverWait(self.drive, 1000).until(
            Ec.url_to_be('https://kyfw.12306.cn/otn/view/index.html')
        )
        self.drive.get('https://www.12306.cn/index/index.html')

    def _goto_ticket_page(self):
        WebDriverWait(self.drive, 1000).until(
            Ec.text_to_be_present_in_element_value((By.ID, 'fromStationText'), self.fromStation)
        )
        WebDriverWait(self.drive, 1000).until(
            Ec.text_to_be_present_in_element_value((By.ID, 'toStationText'), self.toStation)
        )
        WebDriverWait(self.drive, 1000).until(
            Ec.text_to_be_present_in_element_value((By.ID, 'train_date'), self.train_date)
        )
        search_button = self.drive.find_element_by_id('search_one')
        WebDriverWait(self.drive, 1000).until(
            Ec.element_to_be_clickable((By.ID, 'search_one'))
        )
        search_button.click()
        self.drive.switch_to.window(self.drive.window_handles[-1])

    def _choose_ticket(self):
        trs = self.drive.find_elements_by_xpath('//tbody[@id="queryLeftTable"]/tr[not(@datatran)]')
        for tr in trs:
            WebDriverWait(self.drive, 100).until(
                Ec.visibility_of_element_located((By.ID, 'queryLeftTable'))
            )
            t_num = tr.find_element_by_xpath('.//td//a')
            if t_num.text in self.train_number:
                ticket_info = tr.find_element_by_xpath('.//td[4]').text
                if ticket_info == '有' or ticket_info.isdigit():
                    print('{}{}余票'.format(t_num.text, ticket_info))
                    buy_button = tr.find_element_by_xpath('.//td[last()]/a')
                    buy_button.click()
                    break
                else:
                    print('{}无余票'.format(t_num.text))
                    re_serchBtn = self.drive.find_elements_by_id('query_ticket')
                    re_serchBtn.click()
                    self._choose_ticket()
    def _buy_ticket(self):
        WebDriverWait(self.drive, 1000).until(
            Ec.url_to_be('https://kyfw.12306.cn/otn/confirmPassenger/initDc')
        )
        WebDriverWait(self.drive, 1000).until(
            Ec.visibility_of_element_located((By.ID, 'normal_passenger_id'))
        )
        name_li = self.drive.find_elements_by_xpath('//ul[@id="normal_passenger_id"]//li')
        for name_infos in name_li:
            name = name_infos.find_element_by_xpath('.//label')
            if name.text in self.passenger:
                name_checkbox = name_infos.find_element_by_xpath('.//input')
                name_checkbox.click()
                if '学生' in name.text:
                    WebDriverWait(self.drive, 100).until(
                        Ec.visibility_of_element_located((By.ID, 'dialog_xsertcj_ok'))
                    )
                    confirm_button = self.drive.find_element_by_id('dialog_xsertcj_ok')
                    confirm_button.click()

                WebDriverWait(self.drive, 1000).until(
                    Ec.element_to_be_clickable((By.ID, 'submitOrder_id'))
                )
                submit_button = self.drive.find_element_by_id('submitOrder_id')
                submit_button.click()
                WebDriverWait(self.drive, 100).until(
                    Ec.visibility_of_element_located((By.ID, 'qr_submit_id'))
                )
                submit_confirm_button = self.drive.find_element_by_id('qr_submit_id')
                submit_confirm_button.click()
                print('订票成功')


if __name__ == '__main__':
    s = TicketSpider()
    s.run()
