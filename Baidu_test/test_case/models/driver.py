from selenium.webdriver import Remote
from selenium import webdriver

def browser():
##    host='127.0.0.1:4444'
##    dc={'browserName':'chrome'}
##    driver=Remote(command_executor='http://'+host+'/wd/hub',
##                  desired_capabilities=dc)
    driver=webdriver.Chrome()
    return driver

if __name__=='__main__':
    dr=browser()
    dr.get("https://www.baidu.com")
    dr.quit()
