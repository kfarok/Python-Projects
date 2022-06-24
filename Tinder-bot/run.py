
from Tinder.tinder import Tinder

with Tinder() as bot:
    bot.land_first_page()
    bot.facebook_login()
    # bot.sms_login()
    # time.sleep(120)
    time.sleep(20)
    bot.like()
