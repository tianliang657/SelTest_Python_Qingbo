from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
    
    '''

    用户登录页面
    
    '''
    
    url='/'

    baidu_login=(By.XPATH,".//*[@id='u1']/a[7]")
    baidu_login_username=(By.ID,"TANGRAM__PSP_10__userName")
    baidu_login_password=(By.ID,"TANGRAM__PSP_10__password")
    baidu_login_submit=(By.ID,"TANGRAM__PSP_10__submit")
    login_error_message=(By.ID,"TANGRAM__PSP_10__error")

    def login_link(self):
        self.find_element(*self.baidu_login).click()

    def login_username(self,username):
        self.find_element(*self.baidu_login_username).send_keys(username)

    def login_password(self,password):
        self.find_element(*self.baidu_login_password).send_keys(password)

    def login_submit(self):
        self.find_element(*self.baidu_login_submit).click()

##    def user_login(self,username="username",password="password"):
    def user_login(self,username,password):
        self.open()
        sleep(5)
        self.login_link()
        sleep(5)
        self.login_username(username)
        self.login_password(password)
        self.login_submit()
        sleep(5)

    def error_message(self):
        return self.find_element(*self.login_error_message).text
