from selenium.webdriver.common.by import By


def login_pets(browser_web):
    browser_web.get('https://petfriends.skillfactory.ru/')
    browser_web.implicitly_wait(5)

    browser_web.find_element(By.CLASS_NAME, 'btn.btn-success').click()
    browser_web.find_element(By.XPATH, '/html/body/div/div/form/div[4]/a').click()
    browser_web.find_element(By.ID, "email").send_keys("")
    browser_web.find_element(By.ID, "pass").send_keys("")
    browser_web.find_element(By.XPATH, "/html/body/div/div/form/div[3]/button").click()


class TestPets:

    def test_pet_cards(self, browser_web):
        login_pets(browser_web)
        browser_web.implicitly_wait(3)
        images = browser_web.find_elements(By.CSS_SELECTOR, "img[class='card-img-top']")
        names = browser_web.find_elements(By.CSS_SELECTOR, '.card-title')
        descriptions = browser_web.find_elements(By.CSS_SELECTOR, '.card-text')

        print('\n')
        print(len(images))
        for i in range(len(names)):
            print(f"У карточки {i + 1}")
            if images[i].get_attribute('src') == '':
                print(f"Фото -")
            else:
                print(f"Фото +")
            # assert images[i].get_attribute('src') == ''

            if names[i].text == '':
                print(f"Имя -")
            else:
                print(f"Имя +")
            # assert names[i].text == ''

            if descriptions[i].text == '':
                print(f"Описание -")
            else:
                parts = descriptions[i].text.split(", ")
                '''Если в породе присутствует запятая он делит описание на 'n' элементов
                => порода и возраст могут не соответствовать фактическому результату'''
                print("Описание +")
                print(f"Порода: {parts[0]}\nВозраст: {parts[1]}")
            # assert descriptions[i].text == ''
            # assert len(parts[0]) > 0
            # assert len(parts[1]) > 0
            print('\n')
