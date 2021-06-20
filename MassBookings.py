import selenium
from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as ECa
import time
import urllib
from urllib.request import urlopen
import requests
import json
import tkinter


#Firebase Service Token Code 
serverToken = 'AAAAHDIP_V4:APA91bE172pIKfeO7fwZxigRqyeKGwH-_AY43a_jIOpqs7zYv64Ye8j_k0jga2h3c2XK11JMDrDM3ZxvHaLdQ3sNbqcO25AKBvO5Lda4Z3Tn9JMkyDyOCanBu9i92OehHgejTSkeyu5O'

# REPLACE THIS WITH YOUR DEVICE TOKEN FROM THE APP
deviceToken ='es7Qi0kkQ0q6uSZfUL-MLu:APA91bH-LmSFL0n2BXmFkVuG-Y6Uc77B-LIGoiu0Kdlgw4CijvzwwPNQkAvnBYb3kd6lzIGtLW3U15XmcfavcAOY-OvHjlcuGoyo4KPsXUAi3KmUS9WBo_WihkIAVISPPI9uKd4ZWDkz'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'key=' + serverToken,
}

#Customisation of Push notification of Mobile App
def pushapp(body):
    response = requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps({
    'notification': {'title': 'Masss has been booked',
                     'body': body
                     },
    'to':
    deviceToken,
    'priority': 'high',
    #   'data': dataPayLoad,
    }))

    print(response.status_code)
    print(response.json())

email = ''
password = ''

xpathformonth='/html/body/div/div[2]/div/main/div[5]/div/a[1]'

massid = ['selectedTime_G9iz3ePeje0ZWEDatpXX','selectedTime_hNtcApjaqAAXgXKDwuse','selectedTime_0zJgg54H95VjoGC28IZk','selectedTime_pcEQJL0ALHk2xJ3VtyoJ','selectedTime_rY8HmGOkSGpI2OVISrZM']

masslist = 'https://mycatholic.sg/masses/holytrinity/2021/may'

# Using Chrome to access web
driver = webdriver.Chrome(r'C:\Users\Verghese\Desktop\chromedriver(1).exe')

# Open the website
driver.get('https://mycatholic.sg')

#Wait for Page to Load
driver.implicitly_wait(10)

# Select the id box 
id_box = driver.find_element_by_id('email')

# Send id information
id_box.send_keys(email)

# Find password box
pass_box = driver.find_element_by_id('password')

# Send password
pass_box.send_keys(password)

# Find login button
login_button = driver.find_element_by_xpath('/html/body/div/div[1]/div/main/div[1]/form/button')

# Click login
login_button.click()

#Wait for Page to Load
driver.implicitly_wait(10)

#Navigate to Mass bookings Page
mass_booking = driver.find_element_by_xpath('/html/body/div/div[3]/div/main/div[3]/div/a')

#Click Mass Bookings
mass_booking.click()


#Navigate to specific bookings Page
specific_booking = driver.find_element_by_xpath(xpathformonth)


#Click Currrent Month Bookings
specific_booking.click()

#Wait for Page to Load
driver.implicitly_wait(10)

def masspage():
    driver.get(masslist)
    driver.implicitly_wait(10)
    mass_booking = driver.find_element_by_xpath('/html/body/div/div[3]/div/main/div[3]/div/a')
    mass_booking.click()
    specific_booking = driver.find_element_by_xpath(xpathformonth)
    specific_booking.click()
    driver.implicitly_wait(10)


while True :
    time.sleep(60)
    driver.refresh()     

    #Wait for Page to Load
    driver.implicitly_wait(10)

    for i in massid:
        button = driver.find_element_by_id(i)
        class_data = button.get_attribute('class')
        print(i)
        
        if class_data == 'btn btn-outline-success btn-block my-3 py-2':

            pushapp('mass has become available')

            #highlight 5:30pm
            selectmass = driver.find_element_by_id(i)
            selectmass.click()
            print("mass available for" + i )

            #select & continue
            selectcontinue = driver.find_element_by_xpath('/html/body/div/div[2]/div/main/div/nav/div/div/button')
            selectcontinue.click()

            #Wait for Page to Load
            driver.implicitly_wait(10)

            #Find Confirm Button
            confirm_booking = driver.find_element_by_xpath('/html/body/div/div[2]/div/main/div/button[1]')
            confirm_booking.click()
        
            #Notification on Phone when done
            pushapp('A mass has been booked')

            #Wait for Page to Load
            driver.implicitly_wait(10)

            masspage()






