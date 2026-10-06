import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ждём, пока цена уменьшится до $100 (не меньше 12 секунд)
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажимаем кнопку "Book"
    browser.find_element(By.ID, "book").click()

    # Решаем математическую задачу
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # Вводим ответ
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    # Нажимаем Submit
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    import time
    time.sleep(10)
    browser.quit()