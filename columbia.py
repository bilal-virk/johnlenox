import os, sys, time, csv
import traceback
from selenium import webdriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from undetected_chromedriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from faker import Faker

fake = Faker()
import random
from datetime import datetime
import string

import random
from random import choice
if getattr(sys, 'frozen', False):
    script_directory = os.path.dirname(sys.executable)
else:
    script_directory = os.path.dirname(os.path.abspath(__file__))
def subscribe_pop_up_closer():
    try:
        driver.find_element(By.XPATH, '//*[@class="bx-close bx-close-link bx-close-inside"]').click()
        time.sleep(1)
    except:
        pass

# try:
#     driver = Chrome(driver_executable_path= ChromeDriverManager().install() ,options=options)
# except:
def cookies_loader():
    cookies_str = 'QSI_SI_79uu00NpHXNK8rs_intercept=true;dwsid=3JRJCD_9CMxEY0O4LDz5jcn-QCb5Xtf_XQAfWh1zFZD5GtPiNmwNGTW8yPt-YLsTRgU3lMbkpepUMBHrrAufaw==;_attn_=eyJ1Ijoie1wiY29cIjoxNzEwNDExMzYwNjgzLFwidW9cIjoxNzEwNDExMzYwNjgzLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjc3ZWQwN2YzZTgxMTQyYWJiYjI0ODg5YjQ5OWVkNDdhXCJ9In0=;cquid=||;__attentive_dv=1;__attentive_id=77ed07f3e81142abbb24889b499ed47a;__attentive_pv=6;__attentive_ss_referrer=ORGANIC;__cq_dnt=0;_pxhd=RD0d8CDxmrWdDkvAuCx3Mq9U0jEdw//AsoQI9bcKh2Who4v8Gu5BDTloNUkJ7DMvSRPrXdH9tjJZ5t1puAu8gQ==:wlWX6iiNUFtsZrSgUXeMjQO42apArr/LF6s/-P/vHm4Q-ZxeVUKIEcSyqVbrDHBVVofDN64Pmi2nw2WNDhYIVazpcwW9Dk1t0iJK2ZClPk4=;BVBRANDID=02cdf21f-53d0-4d89-9254-b06672b8b6ce;BVImplmain_site=20425;cqcid=bcPVNOwjWTqfnhLqWNDRVNK71a;dl_cud=c;dw_dnt=0;dwac_fda2d388bbd237d68a4b025507=rr6NlC2NsmB13phTPcgw3LvUhLrrLm1TbL0%3D|dw-only|||USD|false|US%2FPacific|true;dwanonymous_6148ff3835e27262c32d6dc123dc430d=bcPVNOwjWTqfnhLqWNDRVNK71a;dwpersonalization_6148ff3835e27262c32d6dc123dc430d=c8ef6f41808e71e564a2fbb2ee20240319190000000;fs_uid=#15X7RY#5652447455948800:172704833336661539:::#/1741947354;sid=rr6NlC2NsmB13phTPcgw3LvUhLrrLm1TbL0'
    cookies_list = cookies_str.split(';')
    cookies = {}
    for cookie in cookies_list:
        parts = cookie.split('=')
        if len(parts) == 2:
            key = parts[0].strip()
            value = parts[1].strip()
            cookies[key] = value
    driver.get("https://columbia.com")
    time.sleep(1)
    for key, value in cookies.items():
        time.sleep(0.1)
        driver.add_cookie({'name': key, 'value': value})
def random_email(first_name, last_name):
    first_name = first_name[:4]  # Maximum 8 characters
    last_name = last_name[:4]
    random_number_1 = random.randint(10, 99)
    random_number_2 = random.randint(10, 99)
    email_domains = ["@outlook.com", "@yahoo.com", "@aol.com", "@hotmail.com"]
    selected_domain = random.choice(email_domains)
    email = f"{first_name.lower()}{random_number_1}{last_name.lower()}{random_number_2}{selected_domain}"
    return email
def generate_random_phone_number():
    digits = [random.randint(0, 9) for _ in range(10)]
    while digits[0] == 0:
        digits[0] = random.randint(1, 9)
    phone_number = ''.join(map(str, digits))
    return phone_number
def pop_up_closer():
    try:
        btns = driver.find_elements(By.XPATH, '//div[@class="modal-header"]//button[@aria-label="Close"]')
        for btn in btns:
            btn.click()
    except:
        pass
    try:
        driver.find_element(By.XPATH, '//*[@aria-label="Decline chat"]').click()
    except:
        pass
def wait_animation_to_end():
    time.sleep(1)
    pop_up_closer()
    WebDriverWait(driver, 100).until_not(EC.visibility_of_any_elements_located((By.XPATH, '//*[@class="loader-animation"]')))
    pop_up_closer()
def make_click(xpathe, t=10, sleep_time=None, pop=None):                                        
    WebDriverWait(driver, t).until(EC.presence_of_element_located((By.XPATH, xpathe)))
    if pop is None:
        pop_up_closer()
    if sleep_time is not None:
            time.sleep(sleep_time)
    try:
            driver.find_element(By.XPATH, "//button[contains(@class, 'accept-all')]").click()
    except:
            pass
    element =WebDriverWait(driver, t).until(EC.element_to_be_clickable((By.XPATH, xpathe)))
    try:
            action = ActionChains(driver)
            action.click(element).perform()
    except:
            try:
                    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });", element)
                    time.sleep(1)
                    element.click()
            except:
                    driver.execute_script("arguments[0].click();", element)    
csv_file = os.path.join(script_directory, "columbia.csv")
with open(csv_file, newline='') as file:
    reader = csv.reader(file)
    next(reader)
    d = 0
    for row in reader:
        if d==0:
             d +=1
             continue
        first_name = fake.first_name()
        last_name = fake.last_name()
        try:
            options = ChromeOptions()
            driver = Chrome(driver_executable_path= ChromeDriverManager().install() ,options=options)
            cookies_loader()
            driver.get(row[0])
            size = row[4]
            stule_or_sku = row[1]
            name = row[2]
            color = row[3]
            price = row[6]
            quantity = int(row[5])
            time.sleep(5)
            WebDriverWait(driver, 100).until_not(EC.visibility_of_any_elements_located((By.XPATH, '//*[@class="loader-animation"]')))
            print("Wait End")
            try:
                closebtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@style="height: auto;"]//div[@class="modal-header"]/button[@aria-label="Close"]')))
                closebtn.send_keys(Keys.ENTER)
                
            except:
                pass
            size_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@data-attr-value="{size}" or @data-attr-hover="{size}"]')))
            size_element.send_keys(Keys.ENTER)
            time.sleep(2)
            WebDriverWait(driver, 100).until_not(EC.visibility_of_any_elements_located((By.XPATH, '//*[@class="loader-animation"]')))
            pop_up_closer()
            try:
                stock_status = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '(//*[@class="attribute-value js-attr-label-value text-danger"])[2]'))).text
                print(stock_status)
                if 'Out of Stock' in stock_status:
                    print("Product is Out of Stock Skipping it")
                    try:
                        driver.close()
                        driver.quit()
                    except:
                        pass
                    continue
            except:
                pass
            print(quantity)
            for it in range(int(quantity)):
                wait_animation_to_end()
                make_click('//button[@class="btn btn-block add-to-cart btn-add-to-cart"]')
                wait_animation_to_end()
                make_click('//*[@class="backdrop "]')
                wait_animation_to_end()
                pop_up_closer()
            print("Done")
            #//*[@class="backdrop "]
            pop_up_closer()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '(//*[@title="Bag"])[1]'))).click()
            make_click('(//*[@class="btn btn-checkout checkout-btn btn-block px-0 "])[1]', 10, 2, pop=True)
            email_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkoutEmail"]')))
            time.sleep(2)
            random_email_ = random_email(first_name, last_name)
            email_input.send_keys(random_email_)
            time.sleep(1)
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@aria-label="First Name"]'))).send_keys(first_name)
            time.sleep(1)
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Last Name"]'))).send_keys(last_name)
            time.sleep(1)
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Address 1"]'))).send_keys('2400 MULDOON RD ANCHORAGE AK 99504-3673 USA')
            time.sleep(1)
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@list="cityList"]'))).send_keys('ANCHORAGE')
            time.sleep(1)
            state_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shippingStatedefault"]')))
            time.sleep(1)
            select = Select(state_input)
            select.select_by_visible_text('Alaska')
            time.sleep(1)
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="ZIP Code"]'))).send_keys('99504-3673')
            time.sleep(1)
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Phone Number"]'))).send_keys(generate_random_phone_number())
            time.sleep(1)
            make_click('//*[@class="form-row"]//button[@type="submit"]')
            iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//iframe[@title="Iframe for card number"]')))
            driver.switch_to.frame(iframe)
            card_number_input  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@aria-label="Card number"]')))
            driver.switch_to.default_content()
            iframe = WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[@title="Iframe for expiry date"]')))
            expiry_date_input  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Expiry date"]')))
            driver.switch_to.default_content()
            iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//iframe[@title="Iframe for security code"]')))
            driver.switch_to.frame(iframe)
            security_code_input  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Security code"]')))
            driver.switch_to.default_content()
    
            name_on_card_input  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@name="holderName"]')))
      
        except:
            print(traceback.format_exc())
            time.sleep(10)
        