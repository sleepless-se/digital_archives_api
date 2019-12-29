from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import logging
logging.basicConfig(level=logging.INFO)
import time
def save_url(url:str)->bool:
    result = True
    driver = webdriver.Remote(
        command_executor='http://selenium-hub:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)
    try:
        driver.get("https://web.archive.org/")
        driver.execute_script("window.scrollTo(0, 500)")
        driver.find_element_by_name("url_preload").send_keys(url)
        driver.find_element_by_xpath("//*[@class='web-save-button web_button web_text']").click()
        driver.execute_script("window.scrollTo(0, 500)")
        driver.find_element_by_xpath("//*[@class='web-save-button web_button web_text']").click()
        driver.execute_script("window.scrollTo(0, 500)")
        for i in range(20):
            success_button = driver.find_elements_by_xpath("//*[@class='label label-success']")
            if len(success_button) != 0:break
            time.sleep(1)
        driver.execute_script("window.scrollTo(0, 500)")
    except Exception as e:
        result = False
        logging.error(e)
    finally:
        driver.save_screenshot('screenshot.png')
        driver.quit()
    logging.info(f'result:{result}')
    return result

if __name__ == '__main__':
    url = "https://qiita.com/OD3/items/f9988fe89c7665e933b4"
    save_url(url)