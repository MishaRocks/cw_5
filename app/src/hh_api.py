import requests


class HeadHunterAPI:

    def get_vacancies(self, keyword=''):
        """
            Отправляем запрос к Апи HeadHunter
            :return: ответ от сервера
        """
        params = {
            'text': f'NAME:{keyword}',  # Текст фильтра.
            'area': 1,  # Поиск осуществляется по вакансиям города Москва(1)
            'page': 0,  # Индекс страницы поиска на HH
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        data = req.json()

        return data

    def get_companies(self):
        """
            Поиск компании в Апи HeadHunter
            :return: ответ от сервера
        """
        params = {
            'area': 1,  # Поиск осуществляется по компаниям города Москва(1)
            'only_with_vacancies': True, # Выводим только компании с открытыми вакансиями
            'page': 0,  # Индекс страницы поиска на HH
            'per_page': 100  # Кол-во компаний на 1 странице
        }
        req = requests.get('https://api.hh.ru/employers', params)  # Посылаем запрос к API
        data = req.json()

        return data
