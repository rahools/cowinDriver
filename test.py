
#%%
from utils.seleniumHelper import CoWinDriver
import time

# %%
if __name__ == '__main__':
    driver = CoWinDriver()
    webdriver = driver.getDriver()

    mobileNumber = ''   # mobile Number
    ip = '192.168.x.x'             # Phone/airmore ipv4 addr
    state = 'Madhya Pradesh'          # State (Camel cased w/ spaces eg: 'Madhya Pradesh')
    district = 'Indore'       # District (Camel cased w/ spaces eg: 'Indore')


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
