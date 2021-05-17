#%%
from enum import auto
from selenium import webdriver
from .otpHelper import OTP
import time

#%%
class CoWinDriver:
    def __init__(self, regURL = 'https://selfregistration.cowin.gov.in/register'):
        self.driver = webdriver.Chrome()
        self.driver.get(regURL)
        assert "Co-WIN" in self.driver.title

    def getDriver(self):
        return self.driver

    def inputMobile(self, mobile):
        try:
            # find and set input as mobile number
            mobileInputElement = self.driver.find_element_by_id("mat-input-0")
            mobileInputElement.clear()
            mobileInputElement.send_keys(mobile)

            # find and click next button
            nextButtonElement = self.driver.find_element_by_class_name("next-btn")
            nextButtonElement.click()

        except:
            print("Can't populate mobile number field.")

    def inputOTP(self, ip):
        try:
            # fetch otp from mobile
            otp = OTP(ip).getOTP()

            if otp is None:
                print("Can't fetch OTP. Check phone's connection or retry after some time.")

            # find otp field and set OTP
            otpInputElement = self.driver.find_element_by_id("mat-input-1")
            otpInputElement.clear()
            otpInputElement.send_keys(otp[0])

            # find and click next button
            nextButtonElement = self.driver.find_element_by_class_name("next-btn")
            nextButtonElement.click()

        except:
            print("Can't populate OTP field.")

    def autoBookingNav(self, state, district):
        try:
            # click schedule
            scheduleElement = self.driver.find_element_by_xpath("//a[@href = '/dashboard']")
            scheduleElement.click()
            time.sleep(3)

            # switch center selection to district
            filterElement = self.driver.find_element_by_css_selector('.status-switch')
            filterElement.click()
            time.sleep(3)

            # select state
            stateElement = self.driver.find_elements_by_class_name('mat-select')[0]
            stateElement.click()
            stateElement = self.driver.find_element_by_xpath(f"//*[text() = ' {state} ']")
            stateElement.click()
            time.sleep(3)

            # select district
            districtElement = self.driver.find_elements_by_class_name('mat-select')[1]
            districtElement.click()
            districtElement = self.driver.find_element_by_xpath(f"//*[text() = ' {district} ']")
            districtElement.click()
            time.sleep(3)

            # submit selection
            submitElement = self.driver.find_element_by_xpath('//ion-button')
            submitElement.click()
            # time.sleep(1)

        except:
            print("Can't navigate to booking.")





#%%
