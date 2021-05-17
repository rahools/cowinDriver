
#%%
from utils.seleniumHelper import CoWinDriver
import time

# %%
if __name__ == '__main__':
    driver = CoWinDriver()

    mobileNumber = ''   # mobile Number
    ip = ''             # Phone/airmore ip addr
    state = ''          # State (Camel cased)
    district = ''       # District (Camel cased)


    driver.inputMobile(mobileNumber)
    time.sleep(10)
    driver.inputOTP(ip)
    time.sleep(10)
    driver.autoBookingNav(state, district)

# %%
