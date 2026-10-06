import os
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    # Заполняем текстовые поля
    browser.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys("Иван")
    browser.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys("Иванов")
    browser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("ivan@example.com")

    # Создаём путь к файлу
    current_dir = os.path.abspath(os.path.dirname(__file__))  # папка со скриптом
    file_path = os.path.join(current_dir, "bio.txt")          # путь к файлу bio.txt

    # Создаём пустой файл, если его ещё нет
    with open(file_path, "w") as f:
        pass  # пустой файл

    # Загружаем файл
    browser.find_element(By.CSS_SELECTOR, "#file").send_keys(file_path)

    # Нажимаем Submit
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    import time
    time.sleep(10)
    browser.quit()