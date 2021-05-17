
#%%
from utils.seleniumHelper import CoWinDriver
import time

# %%
if __name__ == '__main__':
    driver = CoWinDriver()
    webdriver = driver.getDriver()

    mobileNumber = ''   # mobile Number
    ip = ''             # Phone/airmore ip addr
    state = ''          # State (Camel cased)
    district = ''       # District (Camel cased)


    driver.inputMobile(mobileNumber)
    time.sleep(10)
    driver.inputOTP(ip)
    time.sleep(10)

    # idk why login returns a blank page. might have to look into it.
    # for now here's a shoddy work around.
    webdriver.refresh()
    time.sleep(5)

    driver.inputMobile(mobileNumber)
    time.sleep(10)
    driver.inputOTP(ip)
    time.sleep(10)

    driver.autoBookingNav(state, district)

# %%
