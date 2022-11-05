import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# Driver file path
os.environ['PATH'] += r"C:/selenium_drivers/"

# finding the website
driver = webdriver.Chrome()
driver.get("https://izone.sunway.edu.my/login")
driver.implicitly_wait(3)

# finding the input and button
user_name = driver.find_element(By.NAME , "student_uid")
password = driver.find_element(By.NAME , "password")
submit = driver.find_element(By.ID , "submit")

# keying in the input
user_name.send_keys("Your_email_address")
password.send_keys("your_student_password")

# checking tht its working
print(user_name.text)
print(password.text)

# submitting it
submit.click()

# finding the icheckin button
icheckin = driver.find_element(By.ID , "iCheckInUrl")
icheckin.click()

checkin_code_box = driver.find_element(By.ID , "checkin_code")
checkin_button = driver.find_element(By.ID , "iCheckin")
# code = input("put in the code")
checkin_code_box.send_keys("")

checkin_button.click()