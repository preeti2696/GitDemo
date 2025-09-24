#import os.path
#import sys
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #This header ll used when we get error on 'pageObject' Module
import json
import pytest
from POM.Login import LoginPage

test_data_path='dataDriven/test_e2etestFramework.json'  # path travel for json file
with open(test_data_path) as f:
    test_data=json.load(f)
    test_list=test_data["data"]

@pytest.mark.smoke     #custom tag for smoke testing
@pytest.mark.parametrize("test_list_item",test_list)
def test_e2e(browserInstance,test_list_item):
    driver=browserInstance
   # driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginPage=LoginPage(driver)
    print(loginPage.getTitle()) #getting this error while running in terminal TypeError: 'str' object is not callable
    shop_page=loginPage.login(test_list_item["userEmail"],test_list_item["userPassword"])
    shop_page.add_product_to_cart(test_list_item["productName"])
    print(shop_page.getTitle()) #getting this error while running in terminal TypeError: 'str' object is not callable
    checkout_confirmation=shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()

    print(shop_page.getTitle()) #getting this error while running in terminal TypeError: 'str' object is not callable
    print(shop_page.getTitle())  # getting this error while running in terminal TypeError: 'str' object is not callable
    print(shop_page.getTitle())  # getting this error while running in terminal TypeError: 'str' object is not callable

    driver.find_element(By.ID,"username").send_keys("rahulshettyacademy")
    driver.find_element(By.NAME,"password").send_keys("learning")
    driver.find_element(By.ID,"signInBtn").click()

    driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
    products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    #for product in products:
     #   productName = product.find_element(By.XPATH, "div/h4/a").text
      #  if productName == "Blackberry":
#            product.find_element(By.XPATH, "div/button").click()

    #driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

   # driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
   # driver.find_element(By.ID, "country").send_keys("ind")
   # wait = WebDriverWait(driver, 10)
   # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
   # driver.find_element(By.LINK_TEXT, "India").click()
   # driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
   # driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    successText = driver.find_element(By.CLASS_NAME, "alert-success").text
    assert "Success! Thank you!" in successText
