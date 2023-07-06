from app.src.dbmanager import DBManager
from app.src.hh_api import HeadHunterAPI
from app.src.utils import create_tables, add_to_table
from app.src.constants import employers_list

dbm = DBManager()
hh = HeadHunterAPI()


def interface():

    create_tables()
    add_to_table(employers_list)

    while True:

        task = input(
            "Введите 1, чтобы получить список всех компаний и количество вакансий у каждой компании\n"
            "Введите 2, чтобы получить список всех вакансий с указанием названия компании, "
            "названия вакансии и зарплаты и ссылки на вакансию\n"
            "Введите 3, чтобы получить среднюю зарплату по вакансиям\n"
            "Введите 4, чтобы получить список всех вакансий, у которых зарплата выше средней по всем вакансиям\n"
            "Введите 5, чтобы получить список всех вакансий, в названии которых содержатся переданные в метод слова\n"
            "Введите Стоп, чтобы завершить работу\n"
        )

        if task == "Стоп":
            break
        elif task == '1':
            print(dbm.get_companies_and_vacancies_count())
            print()
        elif task == '2':
            print(dbm.get_all_vacancies())
            print()
        elif task == '3':
            print(dbm.get_avg_salary())
            print()
        elif task == '4':
            print(dbm.get_vacancies_with_higher_salary())
            print()
        elif task == '5':
            keyword = input('Введите ключевое слово: ')
            print(dbm.get_vacancies_with_keyword(keyword))
            print()
        else:
            print('Неправильный запрос')


if __name__ == '__main__':
    interface()
