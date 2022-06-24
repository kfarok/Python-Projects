from selenium import webdriver
from time import sleep
import time
import os


class Bado(webdriver.Chrome):
    def __init__(self, driver_path=r"/Users/kamyabfarokhi/Desktop/Chromedriver"):
        self.driver_path = driver_path
        os.environ['PATH'] += driver_path
        self.implicitly_wait(15)
        self.maximize_window()
        super(Bado, self).__init__()

    def login(self):
        self.get('https://badoo.com/signin/?f=top')
        sleep(2)

        username = self.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/section/div/div/div[1]/form/div['
                                                    '1]/div[ '
                                         '2]/div/input')
        username.send_keys(USER)
        password = self.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/section/div/div/div[1]/form/div['
                                                    '2]/div[ '
                                         '2]/div/input')
        password.send_keys(PASS)

        sign_button = self.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[3]/section/div/div/div[1]/form/div[5]/div/div[1]/button')
        sign_button.click()
        sleep(2)
        self.fullscreen_window()

    def like(self):
        self.find_element_by_xpath('/html/body/div[2]/div[1]/main/div[1]/div/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]').click()

    def dislike(self):
        self.find_element_by_xpath('/html/body/div[2]/div[2]/main/div[1]/div/div[1]/section/div/div[2]/div/div['
                                         '2]/div[2]/div[1]').click()

    def unmatch(self):
        sleep(5)
        while True:
            try:
                message_btn = self.find_element_by_xpath(
                    '//*[@id="app_s"]/div/div/div/div[1]/div/div[3]/div/a[3]')
                message_btn.click()
                print("message check")
                sleep(1)
                user = self.find_element_by_id('id="u_787511995"> == $0')
                user.click()
                print('user check')
                sleep(1)
                dots = self.find_element_by_xpath('//*[@id="im_wrapper"]/header/div/div[1]/div[2]/div/div[1]')
                dots.click()
                print('dot checks')
                sleep(1)
                delete = self.find_element_by_xpath('/html/body/div[4]')
                delete.click()
                print("delete check")
                sleep(2)
                second_del = self.find_element_by_xpath('/html/body/aside/section/div['
                                                              '1]/div/form/div/section/div/div/div/div[1]')
                second_del.click()
                print('second check')
                sleep(2)

            except Exception:
                self.close()

    def auto_like(self):
        i = 1
        while i < 590:
            i += 1
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.find_element_by_xpath('/html/body/aside/section/div[1]/div/div/section/div/div/div/div[2]/div').click()
                except:
                    self.dislike()
