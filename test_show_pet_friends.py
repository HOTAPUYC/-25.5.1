import pytest
from selenium.webdriver.common.by import By


def test_show_pet_friends():
   '''Проверка карточек питомцев'''

   # Устанавливаем неявное ожидание
   pytest.driver.implicitly_wait(10)

   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys('nijon@mail.ru')

   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys('Dim@9379992')

   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   # Нажимаем на кнопку Мои питомцы
   pytest.driver.find_element(By.CLASS_NAME, 'nav-link').click()

   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME, 'h2').text == "89275091500"

   # s = pytest.driver.find_element(By.XPATH,  '/html/body/div[1]/div/div[1]/h2')
   # n = int("".join(filter(str.isdigit, s)))
   # print(n)

   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
   names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
   descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0

