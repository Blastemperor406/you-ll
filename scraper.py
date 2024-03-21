
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
inputs=pd.read_csv("repo_sync_YouCal/inputs.csv")
inputs["Expected Calories"]=None
service = Service(executable_path="/Users/yashagarwal/opt/geckodriver")
driver = webdriver.Firefox(service=service)
driver.get("https://www.mayoclinic.org/healthy-lifestyle/weight-loss/in-depth/calorie-calculator/itt-20402304")
units= driver.find_element(By.ID, "units")
units.click()
for i in range(len(inputs)):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "age")))
        time.sleep(2)
        age= driver.find_element(By.ID, "age")
        age.clear()
        age.send_keys(str(inputs["Age"][i]))
        height= driver.find_element(By.NAME, "height")
        height.clear()
        height.send_keys(str(inputs["Height"][i]))
        weight= driver.find_element(By.NAME, "weight")
        weight.clear()
        weight.send_keys(str(inputs["Weight"][i]))
        if inputs["Sex"][i]==0:
            sex= driver.find_element(By.ID,"male")
            sex.click()
        elif inputs["Sex"][i]==1:
            sex= driver.find_element(By.ID,"female")
            sex.click()
        next= driver.find_element(By.CLASS_NAME, "button.next")
        next.click()
    except:
        print("Error1")
        time.sleep(2)

    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "inactive")))
        time.sleep(2)
        if inputs["Activity"][i]==1:
            activity= driver.find_element(By.ID, "inactive")
            activity.click()
        elif inputs["Activity"][i]==2:
            activity= driver.find_element(By.ID, "somewhat-active")
            activity.click()
        elif inputs["Activity"][i]==3:
            activity= driver.find_element(By.ID, "active")
            activity.click()
        elif inputs["Activity"][i]==4:
            activity= driver.find_element(By.ID, "very-active")
            activity.click()
        calc= driver.find_element(By.CLASS_NAME, "button.submit")
        calc.click()
    except:
        print("Error2")
        time.sleep(2)
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='calorieCalc']/div[2]/div[2]/div[1]/h3/span/strong")))
        time.sleep(2)
        element = driver.find_element(By.XPATH,"//*[@id='calorieCalc']/div[2]/div[2]/div[1]/h3/span/strong")
        calories = element.text
        inputs.loc[i, "Expected Calories"] = calories
        print(calories)
        re= driver.find_element(By.CLASS_NAME, "button.reset")
        re.click()
    except:
        print("Error3")
        time.sleep(2)
inputs.to_csv("repo_sync_YouCal/inputs.csv")
time.sleep(10)
driver.quit()
