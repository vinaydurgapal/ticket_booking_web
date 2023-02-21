from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class HOME_PAGE:

    buy_ticket="//a[contains(@class,'btn-w-auto fg-text-light ffb-button1-1')]//span[contains(@class,'btn-text')][normalize-space()='BUY TICKET']"
    page_confirmation="/html/body/div[1]/div/div/section[1]/div/div/div/section/h2/p[2]"

    def __init__(self,driver):
        self.driver=driver

    def click_buy_button(self):
        flag=self.driver.find_element(By.XPATH,self.buy_ticket)
        self.driver.execute_script("arguments[0].click();",flag)

    def Confirmation(self):
       #using webdriverwait giving and  time out exception exception error to resolve it we have to remove that wedriverwait
       #texts = WebDriverWait(self.driver,5).until(EC.text_to_be_present_in_element((By.XPATH,self.page_confirmation),'text'))
       texts=self.driver.find_element(By.XPATH,self.page_confirmation).text
       return texts