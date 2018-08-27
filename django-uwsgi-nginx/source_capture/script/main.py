from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys


if __name__ == '__main__':



    driver = webdriver.Remote(
        command_executor='http://selenium-hub:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)
    driver.get("http://www.python.org")
    print("take a screenshot")
    driver.save_screenshot('screenshot.png')

    print("show title")
    print(driver.title)

    driver.quit()