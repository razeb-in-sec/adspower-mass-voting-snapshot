import requests
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from termcolor import cprint



def find_element_by_class(driver, name, ignore_message=False):
    element = None

    try:
        element = driver.find_element(By.CLASS_NAME, name)
    except Exception as e:
        if not ignore_message:
            cprint(f"Не смогли найти элемент имени класса '{name}'", 'red')

    return element

def find_element_by_tag_name(driver, name, ignore_message=False):
    element = None

    try:
        element = driver.find_element(By.TAG_NAME, name)
    except Exception as e:
        if not ignore_message:
            cprint(f"Не смогли найти элемент по имени тэга '{name}'", 'red')

    return element

def find_element_by_css_selector(driver, name, ignore_message=False):
    element = None

    try:
        element = driver.find_element(By.CSS_SELECTOR, name)
    except Exception as e:
        if not ignore_message:
            cprint(f"Не смогли найти элемент по имени CSS селектора '{name}'", 'red')

    return element

def find_element_by_xpath(driver, name, ignore_message=False):
    element = None
    try:
        element = driver.find_element(By.XPATH, name)
    except Exception as e:
        if not ignore_message:
            cprint(f"Не смогли найти элемент по имени XPATH '{name}'", 'red')

    return element

def find_element_by_id(driver, name, ignore_message=False):
    element = None

    try:
        element = driver.find_element(By.ID, name)
    except Exception as e:
        if not ignore_message:
            cprint(f"Не смогли найти элемент по имени ID '{name}'", 'red')

    return element

def find_tab(driver, name):
    for i in driver.window_handles:
        f=1

def change_on_last_tab(driver):
    quantity_tab = len(driver.window_handles)

    if quantity_tab > 0:  # переходим на самую крайнюю вкладку
        driver.switch_to.window(driver.window_handles[quantity_tab - 1])

def read_param():

    id_pass_l = []
    urls_l = []

    with open("id_passw.txt") as file:
        for line in file:
            list = line.split('|')
            data = {}
            data['ads_id'] = list[0]
            data['mm_pass'] = list[1].replace('\n', '')
            id_pass_l.append(data)

    random.shuffle(id_pass_l)

    with open("urls.txt") as file:
        for line in file:
            list = line.split('|')
            data = {}
            data['url'] = list[0]
            data['voice_name_b'] = list[1].replace('\n', '')
            urls_l.append(data)

    return (id_pass_l, urls_l)


def main():

    res = read_param()
    id_passw_l = res[0]
    urls_l = res[1]

    cprint(f'-----------------------------------------------------------------------------------------------', 'green')
    cprint(f'------------------------>      Chanel https://t.me/web3_python        <------------------------', 'green')
    cprint(f'------------------------>     Chat https://t.me/chat_web3_python      <------------------------', 'green')
    cprint(f'------------------------>        Helped you? You can help me.         <------------------------', 'green')
    cprint(f'------------------------>  0x82D2A27A961392125e0253449EcedC43677F7d9F <------------------------', 'green')
    cprint(f'-----------------------------------------------------------------------------------------------', 'green')


    for param_data in id_passw_l:
        try:
            ads_id = param_data['ads_id']
            mm_passw = param_data['mm_pass']
            open_url = "http://local.adspower.net:50325/api/v1/browser/start?user_id=" + ads_id
            close_url = "http://local.adspower.net:50325/api/v1/browser/stop?user_id=" + ads_id

            resp = requests.get(open_url).json()

            if resp['code'] != 0:
                cprint(f"Не смогли запустить Adspower id#{ads_id} по причине {resp['msg']}", 'red')
                return

            chrome_driver = Service(resp["data"]["webdriver"])
            chrome_options = Options()
            chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
            driver = webdriver.Chrome(service=chrome_driver, options=chrome_options)
            wait = WebDriverWait(driver, 10)

            for urls_data in urls_l:
                # открываем новую вкладку
                url = urls_data['url']
                voice_name_b = urls_data['voice_name_b']

                time.sleep(random.randint(7, 12))
                driver.switch_to.new_window('tab')
                driver.get(url)

                connect_el = find_element_by_class(driver, 'space-x-2')
                wait.until(EC.element_to_be_clickable(connect_el))

                if connect_el != None and connect_el.text == 'Connect wallet':
                    time.sleep(random.randint(1, 4))
                    connect_el.click()

                    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" MetaMask"]'))).click()
                    time.sleep(random.randint(7, 12))

                    change_on_last_tab(driver)
                    input = wait.until(EC.element_to_be_clickable((By.ID, 'password')))
                    input.clear()
                    time.sleep(1)
                    input.send_keys(mm_passw)
                    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Разблокировать"]'))).click()
                    time.sleep(random.randint(7, 12))
                    change_on_last_tab(driver)


                # начинаем голосовать
                wait.until(EC.element_to_be_clickable((By.XPATH, f'//button[text()="{voice_name_b}"]'))).click()
                time.sleep(random.randint(2, 4))
                wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Vote"]'))).click()
                wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Confirm"]'))).click()
                time.sleep(random.randint(8, 12))

                # подтверждаем подписью
                driver.switch_to.new_window('tab')
                driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
                time.sleep(random.randint(8, 12))

                el = find_element_by_class(driver, 'fa-arrow-down', True)     # стрелки может и не быть
                if el != None:
                    el.click()

                wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Подписать"]'))).click()
                time.sleep(random.randint(8, 12))
                driver.close()
                time.sleep(2)

                change_on_last_tab(driver)
                time.sleep(random.randint(3, 7))
                el = find_element_by_xpath(driver, '//h3[text()="Your vote is in!"]')

                if el != None:
                    cprint(f'ОК --- Успешно проголосовали для акканута с ID {ads_id} по url {url}', 'green')
                else:
                    cprint(f'FAIL --- Неудачно проголосовали для акканута с ID {ads_id} по url {url}', 'red')



        except Exception as ex:
            cprint(f'{ex}', 'red')
            cprint(f'FAIL --- Неудачно проголосовали для акканута с ID {ads_id} по url {url}', 'red')

        finally:
            driver.close()
            driver.quit()
            requests.get(close_url)
            time.sleep(1)
            continue


if __name__ == "__main__":
    main()



