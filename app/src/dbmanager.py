import psycopg2
from app.src.config import config


class DBManager:

    def get_companies_and_vacancies_count(self):
        """
        получает список всех компаний и количество вакансий у каждой компании.
        :return: list
        """
        conn = psycopg2.connect(**config())
        with conn.cursor() as cur:
            cur.execute(f"SELECT employees.title, count(vacancies.*) "
                        f"FROM employees JOIN vacancies USING (employer_id) GROUP BY employees.title")
            result = cur.fetchall()
        return result

    def get_all_vacancies(self):
        """
        получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
        :return: list
        """
        conn = psycopg2.connect(**config())
        with conn.cursor() as cur:
            cur.execute("""
            SELECT employees.title, vacancies.title, vacancies.payment, vacancies.url
            FROM employees
            JOIN vacancies USING (employer_id)
            """)
            result = cur.fetchall()
        return result

    def get_avg_salary(self):
        """
        получает среднюю зарплату по вакансиям.
        :return: int
        """
        conn = psycopg2.connect(**config())
        with conn.cursor() as cur:
            cur.execute("""SELECT CAST(ROUND(AVG(payment)) as INTEGER) FROM vacancies""")
            result = cur.fetchall()
        return result[0][0]

    def get_vacancies_with_higher_salary(self):
        """
        получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        :return: list
        """
        conn = psycopg2.connect(**config())
        with conn.cursor() as cur:
            cur.execute("""SELECT * FROM vacancies WHERE payment > (SELECT AVG(payment) FROM vacancies)""")
            result = cur.fetchall()
        return result

    def get_vacancies_with_keyword(self, keyword):
        """
        получает список всех вакансий, в названии которых содержатся переданные в метод слова.
        :return: list
        """
        conn = psycopg2.connect(**config())
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM vacancies WHERE title LIKE('%{keyword}%')")
            result = cur.fetchall()
        return result
