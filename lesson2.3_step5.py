import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    # Нажимаем кнопку, которая открывает новую вкладку
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Переключаемся на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Решаем капчу на новой вкладке
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