<h1>Курсовая работа 5</h1>

 Задача: необходимо получить данные о компаниях и вакансиях с сайта hh.ru, спроектировать таблицы в БД PostgreSQL и загрузить полученные данные в созданные таблицы.

<h2>Реализация:</h2>
- файл main запускаем приложение
- файл hh_api.py получает данные о вакансиях и компаниях с HH.ru
- файл constants.py содержит список id компаний, вакансии которых получаем
- файл utils:
  - функция create_tables создаёт базу данных и таблицы в ней
  - функция add_to_table заполняет базу данных данными, полученными в hh_api.py
- файл dbmanager позволяет работать с базой из интерфейса:
  - get_companies_and_vacancies_count получает список всех компаний и количество вакансий у каждой компании.
  - get_all_vacancies получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
  - get_avg_salary получает среднюю зарплату по вакансиям.
  - get_vacancies_with_higher_salary получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
  - get_vacancies_with_keyword получает список всех вакансий, в названии которых содержатся переданные в метод слова.

<h2>Работа с проектом: </h2>

Установка: 
- загрузить репозиторий
- выполнить установку зависимостей через файл pyproject.toml
- указать данные для доступа к базе данных

Работа осуществляется через функцию интерфейс в файле main.py, после запуска которого пользователь может указать запросы, которые хочет получить.
Список компаний, по вакансиям которых осуществляется поиск, указан в файле constants.py
