from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Set up ChromeDriver path
import os, sys
from queue import Queue
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#GLOBAL VARIABLES THAT WILL BE SHARED FOR STATE
service = Service("C:\CODING\Projects\Python\seleniumProject\chromedriver.exe")  # Replace with the actual path to chromedriver
driver = webdriver.Chrome(service=service)
queue = Queue() #All HTTP requests go here, messages etc.
###################################################


def open_page():
    
    
    driver.get("https://www.jetpunk.com/quizzes/general-knowledge-quiz-231")
    cookie_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/button[1]"))
    ) 
    cookie_button.click()
    start_button = driver.find_element(By.ID, "start-button").click()


#pass stuff as arguments, share state that way.


def interact_with_quiz(answer):
    
    text_box = driver.find_element(By.ID, "txt-answer-box")
    text_box.clear()
    text_box.click()
    text_box.send_keys(answer)
#using a queue in selenium, and having a while loop here that checks that queue every 1 second, if it has smth in it, we process the message.!!!!!

#learn to import properly later. PROPER IMPORTS, lets make this structured as FUCK.
def process_queue():
    print("proces_queue")
    while True:
        time.sleep(1) #wait for updates
        try:
            
            message = queue.get(block=False)
            if message:
                print("processing message: '{0}' from queue".format(message))
                interact_with_quiz(message)
            
        except:
            print("queue empty...")
            print(queue)
 
def main():
    open_page()
    process_queue()
    
    





