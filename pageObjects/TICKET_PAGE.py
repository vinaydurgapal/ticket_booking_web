from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TICKET_PAGE:
    # chose the correct option
    Correct_option = '//*[@id="checkout-products"]/li'
    fName='travname'
    lName='travlastname'
    optional_field='order_comments'
    birth_date='//select[@class="ui-datepicker-month"]'


    def __init__(self,driver):
        self.driver=driver


    def test_option(self):
        radio=self.driver.find_elements(By.XPATH,self.Correct_option)
        return radio
    def test_required(self):
        req=self.driver.find_element(By.XPATH,
                                 "//abbr[@title='required'][normalize-space()='*']").text
        return req
    def test_fName(self,fname):

        self.driver.find_element(By.NAME,self.fName).send_keys(fname)
        # flag= self.driver.find_element(By.NAME,self.fName)
        # self.driver.execute_script["arguments[0],scrollIntoView;",flag] #"arguments[0].scrollIntoView();


    def test_lName(self, lname):
        self.driver.find_element(By.NAME, self.lName).send_keys(lname)

    def test_option_field(self, textfield):
        self.driver.find_element(By.NAME, self.optional_field).send_keys(textfield)


    def test_date_of_birth(self):
        #self.driver.find_element(By.XPATH, self.birth_date).click()
        self.driver.find_element(By.XPATH, '//input[@name="dob"]').click()
        month_length=self.driver.find_element(By.XPATH,self.birth_date)
        drop_option=Select(month_length)
        All_option=drop_option.options
        return All_option




