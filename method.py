from datetime import datetime
from time import sleep
import date as Info
from selenium.webdriver.common.keys import Keys
 
message=""
def mailLogin(driver):
    roginMail = driver.find_element_by_name(Info.mailName)
    roginMail.send_keys(Info.mail)
    sleep(3)
    driver.find_element_by_xpath("//*[@data-testid='next_button']").click()

def passLogin(driver):
    roginPass = driver.find_element_by_name(Info.passwordName)
    roginPass.send_keys(Info.password)
    sleep(4)
    driver.find_element_by_xpath("//*[@data-testid='login_button']").click()
    sleep(2)
    
def report(driver):
    nowTime=datetime.now().hour
    if  nowTime==9:
         message=Info.start
    elif nowTime==12:
         message=Info.restStart
    elif nowTime==13:
         message=Info.restDone
    else:
         message=Info.Done   

    driver.get(Info.openWeb)
    report=driver.find_element_by_xpath(Info.areaLavel)
    sleep(4)
    report.send_keys(message)
    sleep(1)
    report.send_keys(Keys.ENTER)
    sleep(3)
    driver.close()
