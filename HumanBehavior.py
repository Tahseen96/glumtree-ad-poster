from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

import random
from time import sleep

def find_element_attribute(driver_arg, xpath, attribute):
    element = WebDriverWait(driver_arg, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    link = element.get_attribute(attribute)
    return link
    
def move_to_element(driver_arg,xpath):
    actions = ActionChains(driver_arg)
    element = WebDriverWait(driver_arg, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    actions.move_to_element(element).perform()

def find_element_text(driver_arg, xpath):
    element = WebDriverWait(driver_arg, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    return element.text

def wait_for_element(driver_arg, xpath):
    WebDriverWait(driver_arg, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath)))

def wait_for_elements(driver_arg, xpath):
    WebDriverWait(driver_arg, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath)))

def human_clicker_click(driver_arg, xpath):
    element = WebDriverWait(driver_arg, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()

def human_clicker_click_by_id(driver_arg, id):
    element = WebDriverWait(driver_arg, 10).until(
        EC.presence_of_element_located((By.ID, id)))
    element.click()


def human_clicker_js3(driver_arg, xpath, index):
    element = WebDriverWait(driver_arg, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath)))
    driver_arg.execute_script("arguments[0].click();", element[index])
    
def get_element(driver_arg,xpath):
    element = WebDriverWait(driver_arg, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    return element
    
def get_element_text(driver_arg,xpath,wait=10):
    element = WebDriverWait(driver_arg, wait).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    return element.text

def select_option(driver_arg,xpath,option):
    select = Select(get_element(driver_arg,xpath))
    select.select_by_visible_text(option)
    pass

def human_clicker_js_single_el(driver_arg, xpath):
    element = WebDriverWait(driver_arg, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath)))
    randomIndex = random.randrange(len(element))
    driver_arg.execute_script("arguments[0].click();", element[randomIndex])


def human_typer(driver_arg, xpath, text: str):
    element = WebDriverWait(driver_arg, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    for s in text:
        element.send_keys(s)
        sleep(random.uniform(0.07, 0.12))
        
def clear_field(driver_arg,element_id):
    driver_arg.execute_script("""
    let element = document.getElementById('{}')
    element.value = ''
    """.format(element_id))

def human_clicker_js(driver_arg, xpath):
    element = WebDriverWait(driver_arg, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    driver_arg.execute_script("arguments[0].click();", element)


def random_wait(lower_limit, uper_limit):
    time_wait = random.randint(lower_limit, uper_limit)
    sleep(time_wait)

def get_elements_attributes(driver_arg, xpath, attribute='href'):
    data = []
    elements = WebDriverWait(driver_arg, 30).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath)))
    for element in elements:
        data.append(element.get_attribute(attribute))
    return data
    
def get_elements_text(driver_arg, xpath):
    data = []
    elements = WebDriverWait(driver_arg, 30).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath)))
    for element in elements:
        data.append(element.text)
    return data
    
def send_keys_interval(el, string):
    for char in string:
        el.send_keys(char)
        rand_wait = random.uniform(0.04, 0.1)
        sleep(rand_wait)
