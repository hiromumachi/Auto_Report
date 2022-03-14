from lib2to3.pgen2 import driver
from selenium import webdriver
from time import sleep
from selenium import webdriver
import date as Info
import method 
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

def reportAuto():
    driver=webdriver.Chrome("/Library/Frameworks/Python.framework/Versions/3.10/bin/chromedriver")   
    driver.get(Info.rogin_page)
    sleep(3)
    method.mailLogin(driver)
    sleep(4)
    method.passLogin(driver)
    sleep(5)
    method.report(driver)

scheduler.add_job(reportAuto, 'cron', hour=9,minute=25,day_of_week='mon-fri')
scheduler.add_job(reportAuto, 'cron', hour=12,minute=32,day_of_week='mon-fri')
scheduler.add_job(reportAuto, 'cron', hour=13,minute=25,day_of_week='mon-fri')
scheduler.add_job(reportAuto, 'cron', hour=18,minute=31,day_of_week='mon-fri')

try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    print("error")
    scheduler.remove_all_jobs()
    driver.close()
