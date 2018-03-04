from time import sleep
import unittest,random,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.loginPage import login

class loginTest(myunit.MyTest):
    
    '''

    百度登录测试
    
    '''
    def user_login_verify(self,username,password):
        login(self.driver).user_login(username,password)

    def test_login(self):
        self.user_login_verify("username111","password111")
        function.screenshot_name(self.driver)
        text=login(self.driver).error_message()
        self.assertEqual(text,"请XX输入验证码",msg="Qingbo登录失败！")
        

if __name__=="__main__":
    unittest.main()
