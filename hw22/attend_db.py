import os
import pickle

DB_FILE = "./hw22/attend_db.pkl"


def read_db():
    attend_db = {}
    if not os.path.exists(DB_FILE):
        return attend_db

    with open(DB_FILE, "rb") as f:
        attend_db = pickle.load(f)
    return attend_db


def write_db(attend_db):
    with open(DB_FILE, "wb") as fout:
        pickle.dump(attend_db, fout)


def main():
    attend_days = read_db()

    print(f"현재까지 목록은 {attend_days}입니다. 날짜에 '0'을 입력하면 현재까지의 정보가 저장됩니다.")
    while True:
        date = (input("날짜를 입력하세요."))
        if date == "0":
            break
        attend = input("출석 여부를 입력하세요.")
        name = input("이름을 입력하세요.")
        attend_days[date] = name, attend
    print(f"현재까지 목록은 {attend_days}입니다.")

    write_db(attend_days)


if __name__ == "__main__":
    main()