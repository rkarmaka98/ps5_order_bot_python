import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





class Flipkart:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument('disable-infobars')

        #Enter your chromedrive exe path here
        self.browser=webdriver.Chrome(executable_path=r"",options=options)    
    
    
    def add_to_card(self,email,password,link):
        self.browser.get(link)
        login=self.browser.find_element_by_xpath("//a[text()='Login']")
        login.click()
        time.sleep(1)
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Enter Email/Mobile number')]//preceding::input[1]"))).send_keys(email)
        self.browser.find_element_by_xpath("//span[contains(.,'Enter Password')]//preceding::input[1]").send_keys(password)
        self.browser.find_element_by_xpath("//button[@type='submit']//span[contains(.,'Login')]").click()
        time.sleep(0.5)
        
    
        buyButton=False
        while not buyButton:
            try:
                add_to_cart=self.browser.find_element_by_xpath("//button[text()='BUY NOW']")
                add_to_cart.click()
                buyButton=True
            except:
                time.sleep(0.1)
                self.browser.refresh()





if __name__=="__main__":
    checkoutbot_fk=Flipkart()
#################################################################################################
#Enter your email id and password here inside qoutes
    email=""
    password=""
##################################################################################################
    checkoutbot_fk.add_to_card(email,password,"https://www.flipkart.com/sony-playstation-5-cfi-1008a01r-825-gb-astro-s-playroom/p/itma0201bdea62fa")

