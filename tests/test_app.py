import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture(scope="function")
def driver():
    # Setup: Start a browser session
    browser = webdriver.Firefox()
    yield browser
    # Teardown: End the browser session
    browser.quit()

def test_summoner_lookup(driver):
    # Access the Streamlit app
    driver.get("http://localhost:8501/")

    # Wait for the page to load
    time.sleep(2)

    # Find the text input field and enter a summoner name
    summoner_name_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter summoner name']")
    summoner_name_input.send_keys("links")
    summoner_name_input.send_keys(Keys.RETURN)

    # Wait for the response to load
    time.sleep(2)

    # Verify the output
    # Uncomment one of the following lines based on the correct XPath
    output_element = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/div/div/section/div[1]/div/div/div[3]/div/div/div/div/div")
    output_text = output_element.text

    # Check if the output text is a list
    assert "[" in output_text and "]" in output_text, "Output is not a list"
