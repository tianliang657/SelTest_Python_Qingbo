from selenium import webdriver
import os,time


def screenshot_name(driver):
    timestr = time.strftime('%Y-%m-%d %H_%M',time.localtime(time.time())) 
    img_name = timestr + '.png'
    insert_img(driver,img_name)

def insert_img(driver,file_name):
    base_dir=os.path.dirname(os.path.dirname(__file__))
    base_dir=str(base_dir)
    base_dir=base_dir.replace('\\','/')
    base=base_dir.split('/test_case')[0]
    file_path=base + "/report/screenshot/" + file_name
    driver.get_screenshot_as_file(file_path)

if __name__=='__main__':
    driver=webdriver.Chrome()
    driver.get("http://www.baidu.com")
    insert_img(driver,'baidu.png')
    driver.quit()
