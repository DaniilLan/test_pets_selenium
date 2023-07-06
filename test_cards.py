from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAllPets:

    def test_pet_cards(self, login_all_pets):
        """Проверка количества карточек без фото/имени/породы/возраста"""
        wait = WebDriverWait(login_all_pets, 3)
        images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img[class='card-img-top']")))
        names = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.card-title')))
        descriptions = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.card-text')))

        date_cards = {
            "Без фото": 0,
            "Без имени": 0,
            "Без породы": 0,
            "Без возраста": 0,
        }

        for i in range(len(names)):
            if images[i].get_attribute('src') == '':
                date_cards["Без фото"] += 1
            if names[i].text == '':
                date_cards["Без имени"] += 1
            parts = descriptions[i].text.split(", ")
            '''Если в породе присутствует запятая он делит описание на 'n' элементов
            => порода и возраст могут не соответствовать ожидаемому результату'''
            if len(parts[0]) == 0:
                date_cards["Без породы"] += 1
            if parts[1] == "лет":
                date_cards["Без возраста"] += 1
            # assert images[i].get_attribute('src') != '', f"У {i} питомца нет фото"
            # assert names[i].text != '', f"У {i} питомца нет имени"
            # assert descriptions[i].text != '', f"У {i} питомца нет описания"
            # assert len(parts[0]) != 0, f"У {i} питомца нет породы"
            # assert len(parts[1]) != 0, f"У {i} питомца нет возраста"
        print(date_cards)

    def test_pet_total(self, login_my_pets):
        """Присутствуют все питомцы"""
        wait = WebDriverWait(login_my_pets, 3)
        total_tr_pets = len(wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr'))))
        total_pets = int(wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]'))).text.split('\n')[1].split(' ')[1])
        assert total_tr_pets == total_pets, "Количество питомцев в тоблице не соответствует количеству в статистике"

    def test_photo_of_pets(self, login_my_pets):
        """Хотя бы у половины питомцев есть фото"""
        wait = WebDriverWait(login_my_pets, 3)
        photo_pets = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/th/img')))
        pet_without_photo = 0
        pet_with_photo = 0
        for i in range(len(photo_pets)):
            if photo_pets[i].get_attribute('src') == '':
                pet_without_photo += 1
            else:
                pet_with_photo += 1
        assert pet_with_photo >= pet_without_photo, "Питомцев без фото больше половины"

    def test_name_age_type(self, login_my_pets):
        """У всех питомцев есть имя, возраст и порода"""
        wait = WebDriverWait(login_my_pets, 3)
        pets_name = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')))
        pets_type = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[2]')))
        pets_age = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[3]')))
        for i in range(len(pets_type)):
            assert pets_name[i].text != '', f"У {i + 1} питомца нет имени"
            assert pets_type[i].text != '', f"У {i + 1} питомца нет породы"
            assert pets_age[i].text != '', f"У {i + 1} питомца нет возраста"

    def test_difference_name(self, login_my_pets):
        """У всех питомцев разные имена"""
        wait = WebDriverWait(login_my_pets, 3)
        pets_name = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')))
        list_name = []
        for i in pets_name:
            list_name.append(i.text)
        assert len(list_name) == len(set(list_name))

    def test_unique_pets(self, login_my_pets):
        """В списке нет повторяющихся питомцев (фото/имя/порода/возраст)"""
        wait = WebDriverWait(login_my_pets, 3)
        photo_pets = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/th/img')))
        list_pets = []
        in_list_pet = []
        for i in range(len(photo_pets)):
            in_list_pet.append(photo_pets[i].get_attribute('src'))
            pet = wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                              f'//*[@id="all_my_pets"]/table/tbody/tr[{i + 1}]/td[1 <= position() and position() < 4]')))
            for j in pet:
                in_list_pet.append(j.text)
            list_pets.append(in_list_pet)
            in_list_pet = []
        assert len(list_pets) == len(set(map(tuple, list_pets)))
