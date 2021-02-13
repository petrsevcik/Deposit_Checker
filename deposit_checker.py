# we need to make deposit checker for airlines via KIU
# KIU Portal - http://kiu.click
#credentials - Confidential
# email, office id, pass - just examples in this code = Fake
from selenium import webdriver
import time
def kiu_deposit_checker(passwd):
#opening url and inserting credentials
    PATH = "./chromedriver"
    driver = webdriver.Chrome(PATH)
    driver.get("http://kiu.click")
    username = driver.find_element_by_name('username')
    username.send_keys('email@email.com') #example for GitHub,
    checkbox = driver.find_element_by_class_name('checkbox')
    checkbox.click()
    office = driver.find_element_by_name('office')
    office.send_keys('BRQPRGVIE') #example for GitHub
    password = driver.find_element_by_name('password')
    password.send_keys(passwd)
    time.sleep(3)
    submit = driver.find_element_by_xpath('//*[@id="form_login"]/div[2]/div/div/div[4]/button')
    submit.click()
#login done
    time.sleep(5)
    electronic_account = driver.find_element_by_xpath('//*[@id="electronic_account"]/div[1]')
    electronic_account.click()
#getting to the overviews
    time.sleep(5)
    air_century = driver.find_element_by_xpath('/html/body/div/main/div/div/div[3]/div/div[2]/div[2]/table/tbody/tr[1]/td[5]/div')
    IATAy2 = air_century.text
    atsa = driver.find_element_by_xpath('/html/body/div/main/div/div/div[3]/div/div[2]/div[2]/table/tbody/tr[2]/td[5]/div')
    IATA4a = atsa.text
    estelar = driver.find_element_by_xpath ('/html/body/div/main/div/div/div[3]/div/div[2]/div[2]/table/tbody/tr[3]/td[5]/div')
    IATAes = estelar.text
    star_peru = driver.find_element_by_xpath('/html/body/div/main/div/div/div[3]/div/div[2]/div[2]/table/tbody/tr[4]/td[5]/div')
    IATA2i = star_peru.text
    tar_aerolineas = driver.find_element_by_xpath ('/html/body/div/main/div/div/div[3]/div/div[2]/div[2]/table/tbody/tr[5]/td[5]/div')
    IATAyq = tar_aerolineas.text
    #getting results
    result = {"Air Century":IATAy2, "ATSA":IATA4a, "Estelar":IATAes, "Star Peru":IATA2i, "TAR Aerolineas":IATAyq}
    driver.close()
    return result