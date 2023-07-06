CREATE DATABASE cw_5

SELECT employees.title, count(vacancies.*)
FROM employees
JOIN vacancies USING (employer_id)
GROUP BY employees.title

SELECT employees.title, vacancies.title, vacancies.payment, vacancies.url
FROM employees
JOIN vacancies USING (employer_id)

SELECT AVG(payment) FROM vacancies

SELECT * FROM vacancies WHERE payment > (SELECT AVG(payment) FROM vacancies)

SELECT * FROM vacancies WHERE title LIKE('%{keyword}%')