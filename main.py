zip_code = input("Please Input Zip Code: ") #44122
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
def amake_click(driver, xpathe, t=100, sleep_time=None):
    WebDriverWait(driver, t).until(EC.presence_of_element_located((By.XPATH, xpathe)))
    if sleep_time is not None:
            time.sleep(sleep_time)
    element =WebDriverWait(driver, t).until(EC.element_to_be_clickable((By.XPATH, xpathe)))
    try:
        try:
            element.send_keys(Keys.ENTER)
        except:
                
            element.click()
    except:
        try:
            driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });", element)
            time.sleep(1)
            element.click()
        except:
            driver.execute_script("arguments[0].click();", element)
def write_t(driver, xpathe, text, t=10, sleep_time=None, min_delay=0.005, max_delay=0.01):
    driver.wait_for_element(xpathe, timeout=t)
    if sleep_time is not None:
        time.sleep(sleep_time)

    driver.send_keys(xpathe, text)
def extract_text(driver, xpathe, t=10):
    element_text = driver.get_text(xpathe, timeout=t)
    return element_text.strip()        
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
def google_maps(zip_code):
    options = ChromeOptions()
    driver = Chrome(driver_executable_path= ChromeDriverManager().install() ,options=options)
    driver.get("https://www.google.com/maps")
    search_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchboxinput')))
    search_input.click()
    search_input.send_keys(str(zip_code))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//*[@role="row"])[1]'))).click()
    time.sleep(2)
    amake_click(driver, '(//*[@aria-label="Hotels" or text()="Hotels"])[1]')
    #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Hotels"]'))).click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".Nv2PK.THOPZb.CpccDe")))
    hotel_ads = driver.find_elements(By.CSS_SELECTOR, ".Nv2PK.THOPZb.CpccDe")
    if len(hotel_ads) <=3:pass
    data = []
    for ad in hotel_ads[:3]:
        ad.click()
        time.sleep(5)
        name = (WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".DUwDvf.lfPIob"))).get_attribute("innerText"))
        phone =str((WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-tooltip="Copy phone number"]')))).get_attribute("innerText")).replace("Phone:", "").strip()
        address = str((WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-item-id="address"]')))).get_attribute("aria-label")).replace("Address: ", "").strip()
        #print(address)
        data.append({'name': name, 'phone': phone, 'address': address})
        print(address)
        #print(name, phone, address)
    try:
        driver.close()
        driver.quit()
    except:
        pass
    return data

def ae(ae_name,ae_phone, ae_address):
    print(ae_address)
    def subscribe_pop_up_closer():
        try:
            #driver.find_element(By.XPATH, '//*[@class="bx-close bx-close-link bx-close-inside"]').click()
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="bx-close bx-close-link bx-close-inside"]'))).click()
            time.sleep(1)
        except:
            pass
        
    def click_able(xpathe, t=10, sleep_time=None):
        WebDriverWait(driver, t).until(EC.presence_of_element_located((By.XPATH, xpathe)))
        if sleep_time is not None:
                time.sleep(sleep_time)
        element =WebDriverWait(driver, t).until(EC.element_to_be_clickable((By.XPATH, xpathe)))
        try:
            try:
                element.click()
            except:
                    try:
                        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });", element)
                        time.sleep(1)
                        element.click()
                    except:
                        driver.execute_script("arguments[0].click();", element)
        except:
            element.send_keys(Keys.ENTER)
    #options = ChromeOptions()
    #options.add_argument(f'--proxy-server={proxy}')
    #driver = Chrome(driver_executable_path= ChromeDriverManager().install() ,options=options)
    driver = Driver(uc=True) #proxy=proxy
    driver.get("https://www.ae.com/")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))).click()
    except:
        pass
    try:
        subscribe_pop_up_closer()
    except:
        pass
    try:
        make_click(driver, '//*[@id="onetrust-accept-btn-handler"]')
    except:
        pass
    csv_file = os.path.join(script_directory, "ae.csv")
    first_name = "John"
    last_name = "Lenox"
    address = ae_address
    city, state = get_city_state(zip_code)
    

    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            try:
                
                driver.get(row[0])
                size = row[4]
                stule_or_sku = row[1]
                name = row[2]
                color = row[3]
                price = row[6]
                quantity = int(row[5]) -1
                #subscribe_pop_up_closer()
                
                # size_selecter = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Size"]')))
                
                # try:
                #     size_selecter.click()
                # except:
                    
                #     size_selecter.click()
                #driver.click('//*[@aria-label="Size"]',)
                make_click(driver, '//*[@aria-label="Size"]', 20)
                
                # desied_size = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f'//a[@role="menuitem" and text()="{size}"]')))
                # try:
                #     desied_size.click()
                # except:
                    
                #     desied_size.click()
                make_click(driver, f'//a[@role="menuitem" and text()="{size}"]')
                
                
                time.sleep(5)
                try:
                    driver.find_element('//*[@data-test-btn="addToBag"]/..//*[text()="Out of Stock Online"]')
                    print("Out of Stock Online")
                    continue
                except:
                    pass
                for plus in range(quantity):
                    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="increase"]'))).click()
                    make_click(driver, '//button[@aria-label="increase"]')
                    time.sleep(0.5)
                try:
                    #click_able(f'//*[@alt="{color}"]/../..', 5)
                    make_click(driver, f'//*[@alt="{color}"]/../..')
                except:
                    print("Target Color Not Found")
                    try:
                        driver.close_window()
                        driver.quit()
                    except:
                        pass
                    continue
                try:
                    try:
                        sale_price = extract_text(driver, '(//*[@data-test-sale-price or @data-test-product-sale-price])[1]') # WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '(//*[@data-test-sale-price])[1]'))).text
                        selling_price = sale_price.replace('Now', '').strip()
                    except:
                        selling_price = extract_text('//*[@data-test-sticky-container]//*[@data-test-list-price]') #WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@data-test-sticky-container]//*[@data-test-list-price]'))).text
                        selling_price = selling_price.strip()
                    print(f'Price: {selling_price}')
                    if selling_price.strip().lower()==price.strip().lower():
                        print("Product Price Matched")
                    else:
                        print("Product Price Not Matched with CSV data skipping Product")
                        # try:
                        #     driver.close()
                        #     driver.quit()
                        # except:
                        #     pass
                        # continue
                except:
                    pass
                make_click(driver, '//*[@data-test-sticky-container]//*[@name="addToBag"]', 10)
                time.sleep(5)

            except:
                print(traceback.format_exc())
                time.sleep(400)
    #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@name="viewBag"]'))).click()
    make_click(driver,'//*[@name="viewBag"]')
    try:
        subscribe_pop_up_closer()
    except:
        pass
    make_click(driver, '//*[@name="go2checkout"]') #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@name="go2checkout"]'))).click()
    email  = random_email(first_name, last_name)
    write_t(driver, '//*[@name="email"]', email) #WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@name="email"]'))).send_keys(email)
    write_t(driver, '//*[@name="firstname"]', first_name) #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="firstname"]'))).send_keys(first_name)
    write_t(driver, '//*[@name="lastname"]', last_name)#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="lastname"]'))).send_keys(last_name)
    write_t(driver, '//*[@name="streetAddress1"]', address)
    write_t(driver, '//*[@name="streetAddress1"]', " ")
    time.sleep(3)
    make_click(driver, '(//*[@data-test-pac-item])[1]')
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="streetAddress1"]'))).send_keys(address)
    #write_t(driver, '//*[@name="city"]', city)  #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="city"]'))).send_keys(city)
    try:
        select_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="states"]')))
        select = Select(select_element)
        select.select_by_visible_text(state)
    except:
        driver.type('//*[@name="states"]', state)
    
    time.sleep(0.5)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="postalCode"]'))).send_keys(zip_code)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="city"]'))).send_keys(city)
        
    except:
        pass

    
    try:
        WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="useEnteredAddress"]'))).click()
    except:
        pass
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[contains(@title,"card number")]')))
    click_able('//*[@aria-label="Card number"]')
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Card number"]'))).send_keys(card_number)

    driver.switch_to.default_content()
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[contains(@title,"expiry date")]')))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Expiry date"]'))).send_keys(expiry_date)
    driver.switch_to.default_content()
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[contains(@title,"security code")]')))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Security code"]'))).send_keys(security_code)
    driver.switch_to.default_content()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="phoneNumber"]'))).send_keys(generate_random_phone_number())
    time.sleep(10)
def columbia(name, phone, address):
    def cookies_loader():
        cookies_str = 'dwsid=YxAYvaQ1NNWzMaC526DifJoy6vhP7BnDGtfsBsf-aki8_m-6kFY4paweZEeLYPy-cBFJe9iwqgK9WK8a_HnaPg==;_attn_=eyJ1Ijoie1wiY29cIjoxNzE2MjAzNzM0MTczLFwidW9cIjoxNzE2MjAzNzM0MTczLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjkwMmRjZDVjMGM3NDQ0ZWM4NmFjZWYzZTRiN2I2OGZiXCJ9In0=;__attentive_dv=1;BVBRANDSID=aae28991-30e7-4bcf-ab09-3cd9751eaf31;__attentive_id=902dcd5c0c7444ec86acef3e4b7b68fb;__attentive_pv=6;__attentive_ss_referrer=https://www.columbia.com/;__cq_dnt=1;_pxhd=Dmwd5H9gg8/i-DblEyd2jJy4bn/Uczst7vh1eePWsgrhPtSZSYQdHJNP2uKXdALZFBi9H9KerSDPY3raD8tmGA==:OWbKwvDuoYIjvAj7nBLx0J3-qDBRSyUkA8j-lZjfIF8gymqynQe5/SHO8N-veqOMGPND-JfwE/PBBiZjbiA9OwPNh26eU2y590EuTmeYp1c=;bm=c1031aec-2aac-461a-8952-64f919fd3b59;BVBRANDID=f14becec-f830-457a-9527-a2ddeba7f268;dl_cud=c;dw_dnt=1;dwanonymous_6148ff3835e27262c32d6dc123dc430d=abUPfzHizWEQ87RZ3r4fhMTSt2;dwapupreq=1716203761501;sid=moeIAt2pKA5Pl5-RCh7Q_2Olekc2cAUY5nE'
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
    
    def wait_animation_to_end():
        time.sleep(1)
        pop_up_closer(driver)
        WebDriverWait(driver, 100).until_not(EC.visibility_of_any_elements_located((By.XPATH, '//*[@class="loader-animation"]')))
        pop_up_closer(driver)
    
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
                #options.add_argument(f'--proxy-server={proxy}')
                #driver = Chrome(driver_executable_path= ChromeDriverManager().install() ,options=options)
                driver = Driver(uc=True)
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
                pop_up_closer(driver)
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
                    make_click(driver, '//button[@class="btn btn-block add-to-cart btn-add-to-cart"]')
                    wait_animation_to_end()
                    make_click(driver, '//*[@class="backdrop "]', t=100)
                    wait_animation_to_end()
                    pop_up_closer(driver)
                print("Done")
                #//*[@class="backdrop "]
                pop_up_closer(driver)
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '(//*[@title="Bag"])[1]'))).click()
                make_click(driver, '(//*[@class="btn btn-checkout checkout-btn btn-block px-0 "])[1]', 10, 2, pop=True)
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
                make_click(driver, '//*[@class="form-row"]//button[@type="submit"]')
                iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//iframe[@title="Iframe for card number"]')))
                driver.switch_to.frame(iframe)
                card_number_input  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@aria-label="Card number"]')))
                card_number_input.send_keys(card_number)
                driver.switch_to.default_content()
                iframe = WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[@title="Iframe for expiry date"]')))
                expiry_date_input  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Expiry date"]')))
                expiry_date_input.send_keys(expiry_date)
                driver.switch_to.default_content()
                iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//iframe[@title="Iframe for security code"]')))
                driver.switch_to.frame(iframe)
                security_code_input  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Security code"]')))
                security_code_input.send_keys(security_code)
                driver.switch_to.default_content()
        
                name_on_card_input  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@name="holderName"]')))
                name_on_card_input.send_keys(first_name)
        
            except:
                print(traceback.format_exc())
                time.sleep(10)
def timberland(name, phone, address):
    csv_file = os.path.join(script_directory, "Timberland.csv")
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        next(reader)
        first_name = fake.first_name()
        last_name = fake.last_name()
        options = ChromeOptions()
        #options.add_argument(f'--proxy-server={proxy}')
        #driver = Chrome(driver_executable_path= ChromeDriverManager().install() ,options=options)
        driver = Driver(uc=True)
        
        def pop_closer():
            try:
                driver.find_element(By.XPATH, '//*[@aria-label="Close Survey" and @neb-tab-boundary="first"]').send_keys(Keys.ENTER)
            except:
                pass
        d = 0
        for row in reader:
            
            driver.get(row[0])
            #time.sleep(100)
            size = row[4]
            stule_or_sku = row[1]
            name = row[2]
            color = row[3]
            price = row[6]
            quantity = int(row[5]) -1
            time.sleep(1)
      
        
            pop_closer()
            size_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@data-test-id="vf-size-picker-text" and text()="{size.upper()}"]')))
            make_click(driver, f'//*[@data-test-id="vf-size-picker-text" and text()="{size.upper()}"]', 10,1)
            time.sleep(2)
            color_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//button[@aria-label="{color}" and @data-test-id="vf-color-picker"]')))
            #color_element.click()
            make_click(driver, f'//button[@aria-label="{color}" and @data-test-id="vf-color-picker"]')
            time.sleep(1)
            pop_closer()
            try:
                style_element =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@title="Description"]//p[@class="bold"]'))).text
                style = style_element.replace('Style ', '')
                if style.strip().lower() == stule_or_sku.lower():
                    print("Style Matched")
                else:
                    print(f"Product Style {style_element} Does not Matched with CSV data skipping Product")
            except:
                pass
                # try:
                #     driver.close()
                #     driver.quit()
                # except:
                #     pass
                # continue
            name_element =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@data-test-id="product-name"]'))).text
            pop_closer()
            if name_element.strip().lower()==name.strip().lower():
                print("Product Name Matched")
            else:
                print("Product Name Not Matched with CSV data skipping Product")
                # try:
                #     driver.close()
                #     driver.quit()
                # except:
                #     pass
                # continue
            pop_closer()
            price_element =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//*[@data-test-id="product-pricing"]/span/span[not(contains(@class, "line-through") and contains(@class, "c-grey-30"))])[1]'))).text
            print(price_element)
            pop_closer()
            if price_element.strip().lower()==price.strip().lower():
                print("Product Price Matched")
            else:
                print("Product Price Not Matched with CSV data skipping Product")
                # try:
                #     driver.close()
                #     driver.quit()
                # except:
                #     pass
                # continue
            pop_closer()
            add_to_cart_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="pdp-add-to-cart"]')))
            time.sleep(0.5)
            add_to_cart_btn.click()
            pop_closer()
            # cart_close_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@data-test-id="vf-panel-close"]')))
            # time.sleep(0.5)
            # cart_close_btn.click()
            make_click(driver, '//*[@data-test-id="vf-panel-close"]', 10, 1)
            pop_closer()
            make_click(driver, '//a[contains(@href, "/cart")]')
            d +=1
            #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "/cart")]'))).click()
            for _ in range(quantity):
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'(//*[@aria-label="Increase Quantity"])[{str(d)}]'))).click()
                time.sleep(5)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@data-test-id="cart-checkout-button"]'))).click()
            time.sleep(3)
            pop_closer()
            if d==2:
                break
        pop_closer()
        f_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="First Name"]/..//input')))
        f_name.send_keys(first_name)
        l_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Last Name"]/..//input')))
        l_name.send_keys(last_name)
        try:
            driver.find_element(By.XPATH, '//*[@class="bcCloseWrapper"]//*[@class="bcClose"]').click()
        except:
            pass
        l_name.send_keys("John")
        address_1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//*[@data-test-id="base-input"])[3]')))
        address_1.send_keys(address)
        print(address)
        try:
            make_click(driver, '(//*[@class="pac-item"])[1]', 5, 2)
        except:
            
            city_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//*[@data-test-id="base-input"])[5]')))
            city_input.send_keys("Alaska")
            time.sleep(2)
            #state_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//*[@data-test-id="base-input"])[6]')))
            select_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//*[@data-test-id="base-select"])[1]')))
            select = Select(select_element)
            select.select_by_visible_text('Alaska')
            zip_code_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//*[@data-test-id="base-input"])[6]')))
            zip_code_2, zz = zip_code.split(" ")
            zip_code_input.send_keys(zip_code_2)
        email_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//*[@data-test-id="base-input"])[7]')))
        random_email_ = random_email(first_name, last_name)
        email_input.send_keys(random_email_)
        ph_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//*[@data-test-id="base-input"])[8]')))
        phone_number = generate_random_phone_number()
        ph_input.send_keys(phone_number)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@data-test-id="checkout-shipping-continue"]'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '(//iframe[@title="secure payment field"])[1]')))
        card_number_input  = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Card number"]')))
        card_number_input.send_keys(card_number)
        driver.switch_to.default_content()
        #WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[@title="Iframe for secured card security code"]')))
        expiry_date_input  = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//span[contains(text(), " *")]/../..//input)[3]')))
        expiry_date_input.send_keys(expiry_date)
        #driver.switch_to.default_content()
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '(//iframe[@title="secure payment field"])[2]')))
        security_code_input  = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@name="securityCode"]')))
        security_code_input.send_keys(security_code)
        driver.switch_to.default_content()
        time.sleep(10)

result = google_maps(zip_code)
#proxy =  input("Please Enter Proxy (ip:port): ") #'124.243.133.226:80' #
payment_details =  input("Please Enter Payment Details: ") #'5442764142194527|06|27|046' # 
card_number, expiry_month, expiry_year , security_code = payment_details.split('|')
expiry_date = f'{expiry_month}/{expiry_year}'
ae_name, ae_phone, ae_address = "", "", ""
columbia_name, columbia_phone, columbia_address = "", "", ""
timberland_name, timberland_phone, timberland_address = "", "", ""

for idx, item in enumerate(result):
    name = item['name']
    phone = item['phone']
    address = item['address']
    if idx ==0:
        ae_name = name
        ae_phone = phone
        ae_address = address
  
    elif idx== 1:
        columbia_name = name
        columbia_phone = phone
        columbia_address = address
    else:
        timberland_name = name
        timberland_phone = phone
        timberland_address = address
# try:
#     ae(ae_name,ae_phone, ae_address)
# except:
#     print(traceback.format_exc())
#     time.sleep(10)
# try:
#     timberland(timberland_name, timberland_phone, timberland_address)
# except:
#     print(traceback.format_exc())
#     time.sleep(10)
try:
    columbia(columbia_name, columbia_phone, columbia_address)
except:
    print(traceback.format_exc())
    time.sleep(10)
    
    
    
    
# ae_thread = threading.Thread(target=ae, args=("ae_name", "ae_phone", "ae_address"))
# timberland_thread = threading.Thread(target=timberland, args=("timberland_name", "timberland_phone", "timberland_address"))
# columbia_thread = threading.Thread(target=columbia, args=("columbia_name", "columbia_phone", "columbia_address"))

# # Start the threads
# ae_thread.start()
# timberland_thread.start()
# columbia_thread.start()

# # Wait for all threads to complete
# ae_thread.join()
# timberland_thread.join()
# columbia_thread.join()
