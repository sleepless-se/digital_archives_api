from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

#
# import mysql.connector
# from mysql.connector import errorcode
# try:
#     cnx = mysql.connector.connect(user='root', password='root',
#                                   database='django3',
#                                   host='localhost',
#                                   port='8889',
#                                   unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock',
#     )
# except mysql.connector.Error as err:
#     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("Something is wrong with your user name or password")
#     elif err.errno == errorcode.ER_BAD_DB_ERROR:
#         print("Database does not exists")
#     else:
#         print(err)
# else:
#     cnx.close()

if __name__ == '__main__':



    driver = webdriver.Remote(
        command_executor='http://selenium-hub:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)
    driver.get("http://www.python.org")
    print("take a screenshot")
    driver.save_screenshot('screenshot.png')

    print("show title")
    print(driver.title)

    driver.close()