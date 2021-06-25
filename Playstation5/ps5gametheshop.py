import time
from selenium import webdriver 



class CheckOut:
    def __init__(self):

        #Enter your chromedrive exe path here
        self.browser=webdriver.Chrome(executable_path=r"")    
    
    def log_in(self,email,password):
        self.browser.get("https://www.gamestheshop.com/sign-in")
        email_in=self.browser.find_element_by_xpath("//input[@value='E-mail']")
        email_in.send_keys(email)
        pass_in=self.browser.find_element_by_xpath("//input[@value='Password']")
        pass_in.send_keys(password)
        sign_in=self.browser.find_element_by_xpath("//input[@value='Sign In']")
        sign_in.click()

    def add_to_card(self,link,pincode):

        self.browser.get(link)
        addPinCode=self.browser.find_element_by_xpath("//span[text()='Check Pincode Serviceability']")
        addPinCode.click()
        enterPinCode=self.browser.find_element_by_class_name("acc-pin-txt")
        enterPinCode.send_keys("pincode")
        submitPincode=self.browser.find_element_by_xpath("//input[@value='SUBMIT']")
        submitPincode.click()
        closePop=self.browser.find_element_by_class_name("close-pop")
        closePop.click()
        
        buyButton=False
        while not buyButton:
            try:
                addToCart=self.browser.find_element_by_xpath("//div[text()='ADD TO CART']")
                addToCart.click()
                buyButton=True
            except:
                self.browser.refresh()
                        
    def go_to_cart(self,cart):
        time.sleep(0.5)
        self.browser.get(cart)
        proceedCheckOut=self.browser.find_element_by_class_name("cls-Proc-Chkout")
        proceedCheckOut.click()
        
    def checkout(self):  

        log_in_continue=self.browser.find_element_by_xpath("//input[@value='Continue']")
        log_in_continue.click()
        
        ship_add=self.browser.find_element_by_xpath("//div[text()='SHIP MY ORDER TO THIS ADDRESS']")
        ship_add.click()

        ship_continue=self.browser.find_element_by_id("btnShippingContinue")
        ship_continue.click()
        time.sleep(0.1)
        payment=self.browser.find_element_by_id("btnProceedToPayment")
        payment.click()




if __name__=="__main__":
    checkoutbot=CheckOut()
######################################################################################
    #Enter your email and password here
    email=""
    password=""
######################################################################################
    checkoutbot.log_in(email,password)

    #Enter pincode here
    pincode="" 
    
    checkoutbot.add_to_card("https://www.gamestheshop.com/PlayStation-5-Console/5111",pincode)



    checkoutbot.go_to_cart("https://www.gamestheshop.com/my-cart")

    checkoutbot.checkout()
