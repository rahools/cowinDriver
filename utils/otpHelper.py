#%%
from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService
import re
import datetime
import time

#%%
class OTP:
    def __init__(self, ip):
        self.ip = IPv4Address(ip)
        self.session = AirmoreSession(self.ip)
        self.messageService = MessagingService(self.session)
        self.otpStart = 'Your OTP to register/access CoWIN is'

    def getOTP(self, retries = 5, delay = 5):
        for _ in range(retries):
            messages = self.messageService.fetch_message_history()
            rangenum = 3
            for i in range(rangenum):
                messageTime = messages[i].datetime
                messageTime += datetime.timedelta(minutes=3)
                if messageTime > datetime.datetime.now():
                    if messages[i].content.startswith(self.otpStart):
                        return re.findall(r'[0-9]{6}', messages[i].content)
                else:
                    rangenum -= 1

            if delay:
                time.sleep(delay)

        return None

#%%
if __name__ == '__main__':
    otphelp = OTP('192.168.29.243')
    print(otphelp.getOTP())

# %%
