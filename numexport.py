from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import xlsxwriter

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
time.sleep(20)

try:
    workbook = xlsxwriter.Workbook("contactList.xlsx")
    workSheet = workbook.add_worksheet()
    workSheet.write(0, 0, "Contact Number")
    getGroupName = input("Enter The Group Name:")
    row=1
    for groupName in list(getGroupName.split(',')):
        time.sleep(5)
        driver.implicitly_wait(5)
        # --------------Search contact title-------------------------
        searchBtnSelector = '//div[contains(@class,"_2_1wd copyable-text selectable-text")]'
        searchGroup = driver.find_element_by_xpath(searchBtnSelector)
        searchGroup.send_keys(groupName)
        searchGroup.send_keys(Keys.ENTER)

        time.sleep(5)
        driver.implicitly_wait(5)
        numList = '//span[contains(@class,"_7yrSq _3-8er selectable-text copyable-text")]'
        childSpanNum = driver.find_element_by_xpath(numList)
        contactStr = childSpanNum.text
        contactList = contactStr.split(',')
        # -----------------------iterate contact list------------------------------------
        numbers = list()
        for i in range(len(contactList)):
            stringNum = contactList[i]
            special_characters = "0123456789()-+"
            if any(c in special_characters for c in stringNum):
                numbers.append(stringNum)
        # ---------------------export data in xlsx format--------------------------------
        for k in range(len(numbers)):
            workSheet.write(row, 0, numbers[k])
            row=row+1
    workbook.close()
    driver.quit()
except Exception as e:
    print(e)