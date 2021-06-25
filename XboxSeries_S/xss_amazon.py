import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





class Amazon:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument('disable-infobars')
        
        #Enter your chromedriver exe file path
        self.browser=webdriver.Chrome(executable_path=r"",options=options)    
    
    def sign_in(self,link,email,password):
        self.browser.get(link)
        login=self.browser.find_element_by_id("ap_email")
        login.send_keys(email)
        sign_contd=self.browser.find_element_by_id("continue")
        sign_contd.click()
        login_pass=self.browser.find_element_by_id("ap_password")
        login_pass.send_keys(password)
        sign_final=self.browser.find_element_by_id("signInSubmit")
        sign_final.click()



    def add_to_card(self,link):
        time.sleep(1)
        self.browser.get(link)

        buyButton=False
        while not buyButton:
            try:
                add_to_cart=self.browser.find_element_by_xpath("//input[@value='Add to Cart']")
                add_to_cart.click()
                buyButton=True
            except:
                self.browser.refresh()
        time.sleep(1)

    def go_to_cart(self,link):
        self.browser.get(link)
        checkout=self.browser.find_element_by_xpath("//input[@value='Proceed to checkout']")
        checkout.click()
        

if __name__=="__main__":
    checkoutbot_az=Amazon()
############################################################################
#Enter your email Id and password here inside qoutes

    email=""
    password=""

############################################################################
    checkoutbot_az.sign_in("https://www.amazon.in/gp/sign-in.html",email,password)

    checkoutbot_az.add_to_card("https://www.amazon.in/Xbox-Series-S/dp/B08J89D6BW")


    checkoutbot_az.go_to_cart("https://www.amazon.in/gp/cart/view.html?ref_=nav_cart")
