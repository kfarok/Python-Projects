from time import sleep
from selenium import webdriver
import passwords
from selenium.webdriver.common.keys import Keys
import sys


class Tinder():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', value=True)
        self.driver = webdriver.Chrome(options=options)

    def landing_page(self):
        self.driver.get('https://tinder.com')
        self.driver.maximize_window()
        sleep(2)

        cookie_btn = self.driver.find_element('xpath',
                                              '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
        cookie_btn.click()

        login_btn = self.driver.find_element('xpath',
                                             '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
        login_btn.click()
        self.driver.implicitly_wait(1)
        self.facebook_login()

        for i in range(30, 0, -1):
            sys.stdout.write("\r{} seconds left to confirm Log in on your FaceBook app...".format(i))
            sys.stdout.flush()
            if self.driver.current_url == 'https://tinder.com/app/recs':
                break
            sleep(1)
        sys.stdout.write("\r" + " " * 50 + "\r")
        sys.stdout.flush()

        print("Log in via FaceBook app Confirmed!")
        sleep(2)
        self.location()

    def location(self):

        try:
            location_btn = self.driver.find_element('xpath',
                                                    '/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
            location_btn.click()
            print('Allowed Location!')
        except:
            print('No Location permission appeared!')

        sleep(1)

        try:
            notification_btn = self.driver.find_element('xpath',
                                                        '/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
            notification_btn.click()
            print("Disabled Notification!")
        except:
            print("No notification pop up")

    def facebook_login(self):
        sleep(1)
        log_btn = self.driver.find_element('xpath',
                                           '/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div')
        log_btn.click()
        sleep(3)

        base_window = self.driver.window_handles[0]
        fb_window = self.driver.window_handles[1]
        self.driver.switch_to.window(fb_window)
        sleep(1)

        pop_up_cookie = self.driver.find_element('xpath', '/html/body/div[2]/div[2]/div/div/div/div/div[4]/button[2]')
        pop_up_cookie.click()

        fb_email = self.driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
        fb_email.send_keys(passwords.facebook_email)

        fb_pass = self.driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
        fb_pass.send_keys(passwords.facebook_pass)

        self.driver.implicitly_wait(1)
        login_btn = self.driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
        login_btn.click()
        sleep(5)
        self.driver.switch_to.window(base_window)

    def get_profile_name(self):
        try:
            name = self.driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[2]/div[3]/div/div/div/div/div[1]/div/div[1]/span')
            return name.text
        except:
            return "N/A"

    def get_age(self):
        try:
            age = self.driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[2]/div[3]/div/div/div/div/div[1]/div/span[2]')
            return age.text
        except:
            return "N/A"

    def like(self):
        liked_profile = 0
        age = 0
        name = ''
        while True:
            age = self.get_age()
            name = self.get_profile_name()
            sys.stdout.write("\rLiked {} {} years old   ---- Total Liked Profiles: {}".format(
                self.get_profile_name(), self.get_age(), liked_profile))
            sys.stdout.flush()
            sleep(2)

            try:
                # rejecting "add website to the desktop"
                self.driver.find_element('id', '<div class="l17p5q9z">Not interested</div>')
            except Exception:
                try:
                    self.driver.find_element('xpath',
                                             '//*[@id="q-430111019"]/main/div/button[2]/div[2]/div[2]').click()
                except Exception:
                    try:
                        self.driver.find_element('/html/body/div[2]/main/div/button[2]/div[2]/div[2]').click()
                    except Exception:
                        try:
                            self.swipe_right()
                            if self.get_age() != age and self.get_profile_name() != name:
                                liked_profile += 1
                        except:
                            sys.stdout.write("\r{} Something went Wrong Be patient. ".format(i))
                            sys.stdout.flush()
                            sleep(1)

    def swipe_right(self):
        page = self.driver.find_element('xpath', '/html/body')
        page.send_keys(Keys.ARROW_RIGHT)






bot = Tinder()
bot.landing_page()
for i in range(30, 0, -1):
    sys.stdout.write("\r{} seconds left to start Liking...".format(i))
    sys.stdout.flush()
    sleep(1)
sys.stdout.write("\r" + " " * 50 + "\r")
sys.stdout.flush()
print()
bot.like()
