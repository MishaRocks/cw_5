import psycopg2
from app.src.hh_api import HeadHunterAPI


hh = HeadHunterAPI()


def create_tables():
    """
    Создаём базу данных и таблицы
    :return: ничего
    """
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="qadratura")

    conn.autocommit = True

    with conn.cursor() as cur:
        cur.execute(f"DROP DATABASE cw_5")
        cur.execute(f"CREATE DATABASE cw_5")

    cur.close()
    conn.close()

    with psycopg2.connect(
            host="localhost",
            database="cw_5",
            user="postgres",
            password="qadratura"
    ) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                        CREATE TABLE employees (
                        employer_id int PRIMARY KEY,
                        title varchar(255),
                        industries text,
                        area text,
                        open_vacancies int,
                        url text
                    )""")

        with conn.cursor() as cur:
            cur.execute("""
                        CREATE TABLE vacancies (
                        vacancy_id SERIAL PRIMARY KEY,
                        title varchar(255),
                        payment integer,
                        date date,
                        description text,
                        candidate text,
                        url text,
                        employer_id int REFERENCES employees(employer_id)
                    )
            """)

    conn.close()


def add_to_table(employers_list: list):
    """
    Добавляем данные в базу данных
    :return: ничего
    """

    with psycopg2.connect(
            host="localhost",
            database="cw_5",
            user="postgres",
            password="qadratura"
    ) as conn:

        with conn.cursor() as cur:

            cur.execute(f'TRUNCATE TABLE employees, vacancies RESTART IDENTITY;')

            for employer in employers_list:
                c = hh.get_company_by_id(employer)
                cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                            (c["employer_id"], c["title"], c["industries"], c["area"], c["open_vacancies"], c["url"]))

            for employer in employers_list:
                vacancy_list = hh.get_company_vacancies(employer)
                for v in vacancy_list:
                    cur.execute('INSERT INTO vacancies (title, payment, date, description, candidate, url, employer_id) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                                (v["title"], v["payment"], v["date"], v["description"], v["candidate"], v["url"], v["employer_id"]))

    conn.close()
