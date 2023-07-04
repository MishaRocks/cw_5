from app.src.dbmanager import DBManager
from app.src.hh_api import HeadHunterAPI
from app.src.utils import create_tables, add_to_table
from app.src.constants import employers_list


dbm = DBManager()
hh = HeadHunterAPI()

if __name__ == '__main__':
    create_tables()
    add_to_table(employers_list)
