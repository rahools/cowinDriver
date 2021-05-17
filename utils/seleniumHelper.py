#%%
from selenium import webdriver
from .otpHelper import OTP
import time

#%%
class CoWinDriver:
    def __init__(self, regURL = 'https://selfregistration.cowin.gov.in/register'):
        self.driver = webdriver.Chrome()
        self.driver.get(regURL)
        assert "Co-WIN" in self.driver.title

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
            scheduleElement = self.driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-beneficiary-dashboard/ion-content/div/div/ion-grid/ion-row/ion-col/ion-grid[1]/ion-row[2]/ion-col/ion-grid/ion-row[4]/ion-col[2]/ul/li/a')
            scheduleElement.click()
            time.sleep(1)

            # final schedule click
            finalScheduleElement = self.driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-beneficiary-dashboard/ion-content/div/div/ion-grid/ion-row/ion-col/ion-grid[1]/ion-row[4]/ion-col/div/div[2]/div/ion-button')
            finalScheduleElement.click()
            time.sleep(1)

            # switch center selection to district
            filterElement = self.driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[1]/div/label/div')
            webdriver.ActionChains(self.driver).move_to_element_with_offset(filterElement, 249, 1).click().perform()
            time.sleep(1)

            # select state
            stateElement = self.driver.find_element_by_xpath('//*[@id="mat-select-0"]')
            stateElement.click()
            stateElement = self.driver.find_element_by_xpath(f"//*[text() = ' {state} ']")
            stateElement.click()
            time.sleep(1)

            # select district
            districtElement = self.driver.find_element_by_xpath('//*[@id="mat-select-2"]')
            districtElement.click()
            districtElement = self.driver.find_element_by_xpath(f"//*[text() = ' {district} ']")
            districtElement.click()
            time.sleep(1)

            # submit selection
            submitElement = self.driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[2]/ion-row/ion-col[3]/ion-button')
            submitElement.click()
            # time.sleep(1)

        except:
            print("Can't navigate to booking.")





#%%
