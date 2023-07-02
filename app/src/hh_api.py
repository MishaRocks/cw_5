import requests


class HeadHunterAPI:

    def _get_company_vacancies(self, employer_id: int) -> list:
        """
                    Отправляем запрос на получение списка вакансий по работодателю к Апи HeadHunter
                    :return: список вакансий
                """
        params = {
            'area': 1,  # Поиск осуществляется по вакансиям города Москва(1)
            'page': 0,  # Индекс страницы поиска на HH
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        req = requests.get(f'https://api.hh.ru/vacancies?employer_id={employer_id}', params)  # Посылаем запрос к API
        data = req.json()
        return data

    def _get_company_by_id(self, employer_id: int) -> dict:
        """
                            Отправляем запрос на получение списка вакансий по работодателю к Апи HeadHunter
                            :return: список вакансий
                        """
        req = requests.get(f'https://api.hh.ru/employers/{employer_id}')
        data = req.json()
        return data
