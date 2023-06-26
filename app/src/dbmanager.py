import psycopg2


class DBManager:

    def get_companies_and_vacancies_count(self) -> list:
        """
        получает список всех компаний и количество вакансий у каждой компании.
        :return: list
        """
        ...

    def get_all_vacancies(self) -> list:
        """
        получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
        :return: list
        """
        ...

    def get_avg_salary(self) -> int:
        """
        получает среднюю зарплату по вакансиям.
        :return: int
        """
        ...

    def get_vacancies_with_higher_salary(self) -> list:
        """
        получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        :return: list
        """
        ...

    def get_vacancies_with_keyword(self) -> list:
        """
        получает список всех вакансий, в названии которых содержатся переданные в метод слова.
        :return: list
        """
        ...
