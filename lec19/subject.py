import os
import numpy as np
import pickle

DB_FILE = "./lec19/subject_db.pkl"

def read_db():
    grade_db = {}
    if not os.path.exists(DB_FILE):
        return grade_db
    
    with open(DB_FILE, "rb") as f:
        grade_db = pickle.load(f)
    return grade_db

def write_db(grade_db):
    with open(DB_FILE, "wb") as fout:
        pickle.dump(grade_db, fout)


def main():
    grade_total = read_db()

    print(f"현재까지 학점 목록은 {grade_total}입니다.")
    while True:
        grade = float(input("학점을 입력하세요."))
        if grade < 0:
            break
        subject = input("과목명을 입력하세요.")
        grade_total[subject] = grade
    print(f"현재까지 학점 목록은 {grade_total}입니다.")
    print(f"평균 학점은 {np.average(list(grade_total.values())):.2f}입니다.")

    write_db(grade_total)

if __name__ == "__main__":
    main()