import sys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument('--ignore-certificated-errors')
chrome_options.add_argument('--ignore-ssl-errors')
#chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='some random path')
driver.get('https://ts2.clubinterconnect.com/cvt/home/reportView.do?id=136&history=clear')
#driver.set_window_size(1300,1000)
wait = WebDriverWait(driver,10)

selectTime = sys.argv[1]
selectAMPM = sys.argv[2]

def login():
    wait.until(EC.visibility_of_element_located((By.ID,'userid')))
    driver.find_element_by_id('userid').send_keys('some random email')
    driver.find_element_by_id('password').send_keys('some random password')
    driver.find_element_by_id('submit').click()
login()

def firstPage():
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'a[href="calendarDayView.do?id=7"]'))).click()
    print('first page done')
firstPage()

def courtsPage():
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'calheaderdaylink'))).click()
    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'td[bgcolor="#FFFFFF"]')))
    openSpots = driver.find_elements_by_css_selector('td[bgcolor="#FFFFFF"]')
    for i in openSpots:
        timeAvailable = i.find_element_by_css_selector('font[color="green"]').text
        print(timeAvailable)

        if selectTime in timeAvailable and selectAMPM in timeAvailable:
            i.find_element_by_class_name('calendarDayItemsLink').click()
            print('courts page done')
            break
        else:
            continue   
courtsPage()

def courtBookingPage():
    try:
        wait.until(EC.visibility_of_element_located((By.ID,'Team_Two_Auto'))).send_keys('some random name')
        driver.find_element_by_id('final').click()
        print('court booked')
        time.sleep(5)
    except TimeoutException:
        print('not available')
        driver.quit()
courtBookingPage()

driver.quit()
