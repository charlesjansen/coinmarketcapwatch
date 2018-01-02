# -*- coding: utf-8 -*-
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


#searchType: XPATH, CLASS_NAME, CSS_SELECTOR 
def connectAndCheck(url, searchTypeString, browser, searchType):
    delay = 20
    if searchType == "CSS_SELECTOR" :
        BysearchType = By.CSS_SELECTOR
    elif searchType == "CLASS_NAME":
        BysearchType = By.CLASS_NAME
    elif searchType == "XPATH":
        BysearchType = By.XPATH
    
    
    
    while(1):
        try:
            browser.get(url)
            xpathTarget = WebDriverWait(browser, delay).until(EC.presence_of_element_located((BysearchType, searchTypeString)))
            print("Page is ready!")
            break
            return xpathTarget
        except TimeoutException:
            print("Loading took too much time!")
            continue




































