from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# URL of the first application
url_app1 = "http://<app1-url>"

# URL of the second application
url_app2 = "http://<app2-url>"

# Function to run tests for App 1
def test_app1():
    driver = webdriver.Chrome()
    driver.get(url_app1)
    time.sleep(2)  # Wait for 2 seconds for the page to load
    assert "App 1" in driver.title  # Assert that "App 1" is in the title
    print("Test for App 1 passed!")
    driver.quit()

# Function to run tests for App 2
def test_app2():
    driver = webdriver.Chrome()
    driver.get(url_app2)
    time.sleep(2)  # Wait for 2 seconds for the page to load
    assert "App 2" in driver.title  # Assert that "App 2" is in the title
    print("Test for App 2 passed!")
    driver.quit()

# Run tests for both applications
test_app1()
test_app2()
