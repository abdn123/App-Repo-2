from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# URL of the first application
url_app2 = "http://localhost:80"



# Function to run tests for App 2
def test_app2():
    driver = webdriver.Chrome()
    driver.get(url_app2)
    time.sleep(2)  # Wait for 2 seconds for the page to load
    assert "App 2" in driver.title  # Assert that "App 2" is in the title
    print("Test for App 2 passed!")
    driver.quit()


test_app2()
