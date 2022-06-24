from selenium import webdriver
import os
import Tinder.constants as const
from selenium.webdriver.common.keys import Keys
import time


class Tinder(webdriver.Chrome):
    def __init__(self, driver_path=r"/Users/kamyabfarokhi/PycharmProjects/Bot_Tinder/venv/bin", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Tinder, self).__init__()
        self.implicitly_wait(5)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def facebook_login(self):
        time.sleep(3)
        log_in_facebook = self.find_element_by_xpath(
            '/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]'
        )
        log_in_facebook.click()

        base_window = self.window_handles[0]
        self.switch_to.window(self.window_handles[1])

        cookie_btn = self.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[1]')
        cookie_btn.click()

        email = self.find_element_by_id("email")
        email.send_keys(const.EMAIL)

        password = self.find_element_by_id("pass")
        password.send_keys(const.PASSWORD)

        log_in_btn = self.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
        log_in_btn.click()
        time.sleep(5)

        self.switch_to.window(base_window)
        time.sleep(5)
        allow_loc = self.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]/span')
        allow_loc.click()

        acc_cookies = self.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/span')
        acc_cookies.click()

        notification_btn = self.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]/span')
        notification_btn.click()

        try:
            self.find_element_by_xpath('/html/body/div[2]/div/div/div/div[3]/button[2]/span').click()
        except:
            pass

    def sms_login(self):
        # time.sleep(3)
        smd_btn = self.find_element_by_xpath(
            '/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[3]/button/span[2]'
        )
        smd_btn.click()

        number = self.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[2]/div/input')
        number.send_keys(const.PHONE_NUMBER)

        continue_btn = self.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/button/span')
        continue_btn.click()

    def like(self):
        while True:
            time.sleep(1)
            try:
                self.find_element_by_xpath(
                    '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button'
                ).click()
            except Exception:
                try:
                    self.find_element_by_xpath('/html/body/div[2]/div/div/div/div[3]/button[2]/span').click()
                except:
                    print('Not working')
        


