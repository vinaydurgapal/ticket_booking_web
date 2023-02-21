import time

from selenium.webdriver.common.by import By

from pageObjects.HOME_PAGE import HOME_PAGE
from pageObjects.TICKET_PAGE import TICKET_PAGE


class Test_Buyticket():

    baseURL='https://www.dummyticket.com/'
    def test_ticket(self,setup):
        self.driver=setup
        self.driver.get
        self.driver.get(self.baseURL)
        self.driver.maximize_window()


        self.hp = HOME_PAGE(self.driver)
        self.hp.click_buy_button()
        self.target=self.hp.Confirmation()
        if self.target=='Dummy ticket booking':
           self.TP=TICKET_PAGE(self.driver)
           self.lenght=self.TP.test_option()
           print("lenght of the option",len(self.lenght))
           for num in range(1,len(self.lenght)+1):
                #print(num)
                texts=self.driver.find_element(By.XPATH,'//*[@id="checkout-products"]/li['+str(num)+']/label/input').get_attribute('value')
                if texts=='3186':
                   # self.driver.find_element(By.XPATH,'//*[@id="checkout-products"]/li['+str(num)+']/label/input').click() ---> give error selenium.common.exceptions.ElementClickInterceptedException
                    button = self.driver.find_element(By.XPATH,'//*[@id="checkout-products"]/li['+str(num)+']/label/input')
                    self.driver.execute_script("arguments[0].click();", button)
                    break


        self.required=self.TP.test_required()
        if self.required=='*':
            self.TP.test_fName("Vinay")


        else:
            pass

        self.TP.test_lName("durgapal")
        self.TP.test_option_field("")
        
        self.All_option=self.TP.test_date_of_birth()
        print(len(self
              .All_option))

        for mon in self.All_option:
            print(mon.text)
            if mon.text == "Mar":
                print("mon.click()")
                mon.click()
                break








