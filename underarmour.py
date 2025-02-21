zip_code='44122'
from seleniumbase import Driver
import random
import os, sys, time, csv
import traceback, requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import threading

fake = Faker()
if getattr(sys, 'frozen', False):
    script_directory = os.path.dirname(sys.executable)
else:
    script_directory = os.path.dirname(os.path.abspath(__file__))

def get_city_state(zip_code):
    url = f"http://api.zippopotam.us/us/{zip_code}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        city = data['places'][0]['place name']
        state = data['places'][0]['state']
        return city, state
    else:
        return None, None

def pop_up_closer(driver):
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

def make_click(driver, xpathe, t=10, sleep_time=None):
    try:
        driver.wait_for_element(xpathe, timeout=t)
        if sleep_time is not None:
            time.sleep(sleep_time)
        driver.click(xpathe, timeout=t)
    except:
        js_script = """
            var element = document.evaluate(arguments[0], document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            element.click();
        """
        driver.execute_script(js_script, xpathe)
def random_email(first_name, last_name):
    first_name = first_name
    last_name = last_name
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

def timberland(name, phone, address,zip_code):
    csv_file = os.path.join(script_directory, "Timberland.csv")
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        next(reader)
        first_name = fake.first_name()
        print(f'This is fake Uuser FirstName : {first_name}')
        last_name = fake.last_name()
        options = ChromeOptions()
        driver = Driver(uc=True)

        d = 0
        n=0
        for row in reader:
            n+=1
            driver.get(row[0])
            try:
                Dialog_Close=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//dialog[@aria-labelledby="on-right-site-title"]//button[@aria-label="Close Dialog"]')))
                Dialog_Close.click()
            except:
                pass
            size = row[4]
            stule_or_sku = row[1]
            name = row[2]
            color = row[3]
            price = row[6]
            quantity = int(row[5]) -1
            time.sleep(1)
            try:
                Close_Cookie=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//a[@id="truste-consent-close"]')))
                driver.execute_script("arguments[0].click();",Close_Cookie)
            except:
                pass
            # size_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//input[contains(@id,"{size.upper()}-R")]')))

            # (//input[@name="size"]/..//label[contains(.,'7')])[1]
            # make_click(driver, f'//input[contains(@id,"{size.upper()}-R")]', 10,1)
            
            size_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'(//input[@name="size"]/..//label[contains(.,"{size.upper()}")])[1]')))

            make_click(driver, f'(//input[@name="size"]/..//label[contains(.,"{size.upper()}")])[1]', 10,1)
            
            time.sleep(2)
            try:
                color_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//div[@data-testid="color-swatch"]//label[contains(.,"{color.capitalize()}")]')))
                
                make_click(driver, f'//div[@data-testid="color-swatch"]//label[contains(.,"{color.capitalize()}")]')
            except:
                pass
            
            time.sleep(1)
            # try:
            #     style_element =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="product-name"]'))).text
            #     style = style_element.replace('Style ', '')
            #     if style.strip().lower() == stule_or_sku.lower():
            #         print("Style Matched")
            #     else:
            #         print(f"Product Style {style_element} Does not Matched with CSV data skipping Product")
            # except:
            #     pass

            price_element =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@id="product-price"]'))).text
            print(price_element)
            # if price_element.strip().lower()==price.strip().lower():
            #     print("Product Price Matched")
            # else:
            #     print("Product Price Not Matched with CSV data skipping Product")
            #     continue
            add_to_cart_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//button[@data-testid="add-to-bag-button"]')))
            time.sleep(0.5)
            add_to_cart_btn.click()
            time.sleep(2)
                
            View_Bag=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(.,'View Bag')]")))
            driver.execute_script("arguments[0].click();",View_Bag)
            time.sleep(3)
            if n==1:
                Close_Dialog=WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,'//button[contains(.,"Join & Create an Account")]/../../../../../..//button[@data-testid="dialog-close-button"]')))
                driver.execute_script('arguments[0].click();',Close_Dialog)

            try:
                Quantity_Dropdown=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//button[@name="quantity-combobox"]')))
                driver.execute_script("arguments[0].click();",Quantity_Dropdown)

                Quantity_Dropdown_Options=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//ul[contains(@id,"quantity-listbox")]//li[@data-value="{quantity}"]')))
                driver.execute_script("arguments[0].click();",Quantity_Dropdown_Options)
            except:
                pass

       
        Checkout_Btn=WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,'(//a[@href="/en-us/checkout/"])[1]')))
        driver.execute_script("arguments[0].click();",Checkout_Btn)
        Guest_Checkout=WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(.,'Continue As Guest')]")))
        driver.execute_script("arguments[0].click();",Guest_Checkout)
            
        wait = WebDriverWait(driver, 40)  # 10-second timeout

        # Wait for and fill out the text inputs
        first_name_input = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        first_name_input.send_keys(first_name)

        last_name_input = wait.until(EC.presence_of_element_located((By.NAME, "lastName")))
        last_name_input.send_keys(last_name)

        address_1_input = wait.until(EC.presence_of_element_located((By.NAME, "address1")))
        address_1_input.send_keys(address)

        city_input = wait.until(EC.presence_of_element_located((By.NAME, "city")))
        city_input.send_keys("South Charleston")

        # Wait for and click the state button
        state_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@name="stateCode-combobox"]')))
        state_button.click()

        # Wait for and select the state from the dropdown
        state_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//ul[contains(@id,"stateCode-listbox")]//li[@data-value="AL"]')))
        state_option.click()
        zip_code_2 = zip_code
        # Wait for and fill out the postal code
        postal_code = wait.until(EC.presence_of_element_located((By.NAME, "postalCode")))
        postal_code.send_keys(zip_code_2)
        time.sleep(2)
        print("Form filled successfully!")
        # Wait for and click the shipping submit button
        shipping_submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="btn-shipping-submit"]')))
        driver.execute_script("arguments[0].click();",shipping_submit)
        # input('Please Verify your address and Press Enter to Continue')
        # Switch to the iframe for credit card input
        try:
            credit_card_iframe = WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[contains(@id,"credit-card")]')))
            driver.switch_to_frame(credit_card_iframe)
        except:
            driver.execute_script("document.body.click();")
            time.sleep(1)
            # Close_Dialog=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//dialog[@role="dialog"]//button[contains(.,"Review Address")]/../../..//button[@aria-label="Close Dialog"]')))
            # try:
            #     Close_Dialog.click()
            # except:
            #     driver.execute_script("arguments[0].click();", Close_Dialog)
            shipping_submit = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, '//button[@id="btn-shipping-submit"]')))
            driver.execute_script("arguments[0].click();",shipping_submit)
        # Fill out the credit card information
            credit_card_iframe = wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[contains(@id,"credit-card")]')))
            driver.switch_to_frame(credit_card_iframe)
        payment_details = "5442764142194527|06|27|046|John Doe"
        card_number, expiry_month, expiry_year , security_code,card_name = payment_details.split('|')
        expiry_date = f'{expiry_month}/{expiry_year}'
        
        card_number_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="cNumber"]')))
        card_number_input.send_keys(card_number)  # Example Visa test card number

        expiration_date_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="exDate"]')))
        expiration_date_input.send_keys(expiry_date)  # Example expiration date

        security_code_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="secCode"]')))
        security_code_input.send_keys(security_code)  # Example CVV

        cardholder_name_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="cName"]')))
        cardholder_name_input.send_keys(card_name)

        driver.switch_to.default_content()

        continue_to_contact = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="continue-to-contact"]')))
        continue_to_contact.click()
        # time.sleep(1000)
        time.sleep(10)
name=''
phone=''
address='6600 London Rd'
zip_code='44122'
timberland(name,phone,address,zip_code)
