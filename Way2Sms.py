from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time
user = "login_number"
pwd = "login_password"
tonum = "to_number"
msg = "msg_to_send"
driver = webdriver.Chrome("E:\Softwares\Chromedriver.exe")  #path to firefox or chrome web driver
driver.get("http://www.way2sms.com")
elem = driver.find_element_by_id("mobileNo")
elem.send_keys(user)
elem = driver.find_element_by_id("password")
elem.send_keys(pwd)
elem = driver.find_element_by_class_name("fa-long-arrow-right").click()
time.sleep(3)
elem = driver.find_element_by_name("toMobile")
elem.send_keys(tonum)
elem = driver.find_element_by_class_name("free-sms-text")
elem.send_keys(msg)
elem = driver.find_element_by_id("sendButton").click()
time.sleep(3)
elem = driver.find_element_by_class_name("logout").click()
driver.close()
