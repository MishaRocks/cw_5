import requests


class HeadHunterAPI:

    def get_company_vacancies(self, employer_id: int) -> list:
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

        hh_list = []
        for v in data["items"]:
            hh_dict = {
                'id': int(v['id']),
                'title': v["name"],
                'payment': v["salary"]["from"] if v["salary"] else None,
                'date': v["published_at"],
                'description': v["snippet"]["responsibility"],
                'candidate': v["snippet"]["requirement"],
                'url': v["alternate_url"],
                'employer_id': employer_id
            }
            if hh_dict['payment'] is not None:
                hh_list.append(hh_dict)

        return hh_list

    def get_company_by_id(self, employer_id: int) -> dict:
        """
        Отправляем запрос на получение списка вакансий по работодателю к Апи HeadHunter
        :return: словарь с данными о компании
        """
        req = requests.get(f'https://api.hh.ru/employers/{employer_id}')
        data = req.json()
        hh_company = {
            "employer_id": int(employer_id),
            "title": data['name'],
            "industries": data['industries'][0]['name'] if data['industries'] else None,
            "area": data['area']['name'],
            "open_vacancies": data['open_vacancies'],
            "url": data['alternate_url']
        }

        return hh_company
