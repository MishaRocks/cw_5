from app.src.dbmanager import DBManager
from app.src.hh_api import HeadHunterAPI

dbm = DBManager()
hh = HeadHunterAPI()

if __name__ == '__main__':
    print(hh.get_companies())
