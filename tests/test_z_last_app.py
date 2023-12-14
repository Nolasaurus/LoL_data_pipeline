import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    # Setup: Start a browser session
    browser = webdriver.Firefox()
    yield browser
    # Teardown: End the browser session
    browser.quit()

class TestApp:
    def test_summoner_lookup(self, driver):
        # Access the Streamlit app
        driver.get("http://localhost:8501/")

        # Wait for the page to load using explicit wait
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter summoner name']")))

        # Find the text input field and enter a summoner name
        summoner_name_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter summoner name']")
        summoner_name_input.send_keys("links")
        summoner_name_input.send_keys(Keys.RETURN)

        # Wait for the response to load
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[1]/div/div/div/section/div[1]/div/div/div[3]/div/div/div/div/div")))

        # Verify the output
        output_element = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/div/div/section/div[1]/div/div/div[3]/div/div/div/div/div")
        output_text = output_element.text

        # Check if the output text is a list
        assert "[" in output_text and "]" in output_text, "Output is not a list"


    @pytest.mark.parametrize("sql_query, expected_result, expected_behavior", [
        ("ALTER TABLE match_metadata ADD COLUMN test_column VARCHAR(255)", "must be owner of table match_metadata", "error"),
        ("SELECT * FROM teams", "[]", "list")
    ])
    def test_sql_query(self, driver, sql_query, expected_result, expected_behavior):
        # Access the Streamlit app
        driver.get("http://localhost:8501/")

        # Wait for the page to load using explicit wait
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//textarea")))

        # Input the SQL query
        sql_query_input = driver.find_element(By.XPATH, "//textarea")
        sql_query_input.send_keys(sql_query)
        sql_query_input.send_keys(Keys.CONTROL, Keys.ENTER)

        def assert_text_at_xpath(driver, xpath, expected_text):
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            assert expected_text in driver.find_element(By.XPATH, xpath).text, f"{expected_text} not found at {xpath}"

        if expected_behavior == "list":
            # Use the helper function to assert text presence
            assert_text_at_xpath(driver, "//span[contains(text(), '[')]", '[')
            assert_text_at_xpath(driver, "//span[contains(text(), ']')]", ']')

        if expected_behavior == "error":
            # Use the helper function to assert text presence
            assert_text_at_xpath(driver, "//div[@role='alert']//p", expected_result)
