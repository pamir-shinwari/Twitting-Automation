from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
import time

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)


class Internet_Speed_X_Bot:
    def __init__(self):
        self.x_username = "@codetesting7391"
        self.x_password = "cvN6-jg2&m@4C!Z"
        self.internet_up_speed = 150
        self.internet_down_speed = 150

    def get_speed(self):
        print(f"getting my current internet speed")
        driver.get("https://www.speedtest.net/result/16969141330")
        time.sleep(2)
        go_button = driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        time.sleep(60)
        down_speed = driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        up_speed = driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        if float(down_speed) < self.internet_down_speed or float(up_speed) < self.internet_up_speed:
            self.post_tweet(down_speed, up_speed)




    def post_tweet(self, current_down, current_up):
        print("posting a tweet on X")
        driver.get("https://x.com/i/flow/login")
        time.sleep(4)

        username_input = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        username_input.send_keys(self.x_username)
        time.sleep(2)

        next_button = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        next_button.click()
        time.sleep(2)

        password_intput = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_intput.send_keys(self.x_password)

        time.sleep(2)
        login_button = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
        login_button.click()

        time.sleep(2)
        post_textarea = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        post_textarea.send_keys(f"why my internet speed is down?  I was promised to have {self.internet_down_speed} down and {self.internet_up_speed} up but now I have {current_down} down and {current_up} up")

        time.sleep(3)

        post_button = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        post_button.click()





speed = Internet_Speed_X_Bot()
speed.get_speed()

