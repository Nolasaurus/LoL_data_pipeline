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
        ("ALTER TABLE match_metadata ADD COLUMN test_column VARCHAR(255)", "error", "error"),
        ("SELECT * FROM teams", "[", "list")
    ])
    def test_sql_query(self, driver, sql_query, expected_result, expected_behavior):
        # Access the Streamlit app
        driver.get("http://localhost:8501/")

        # Wait for the page to load using explicit wait
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//textarea")))

        # Input the SQL query
        sql_query_input = driver.find_element(By.XPATH, "//textarea")
        sql_query_input.send_keys(sql_query)
        sql_query_input.send_keys(Keys.RETURN)

        # Click the "Execute Query" button
        execute_query_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                            '/html/body/div/div[1]/div[1]/div/div/div/section/div[1]/div/div/div[5]/div/button')))
        execute_query_button.click()

        # Wait for the response to load
        object_content = '/html/body/div/div[1]/div[1]/div/div/div/section/div[1]/div/div/div[6]/div/div/div'
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "object_content")))
        # Verify the output
        output_element = driver.find_element(By.XPATH, "object_content")
        output_text = output_element.text

        if expected_behavior == "error":
            assert expected_result in output_text.lower(), "Expected error message not found"
        elif expected_behavior == "list":
            assert "[" in output_text and "]" in output_text, "Output is not a list"
        else:
            assert expected_result in output_text, "Expected result not found in output"