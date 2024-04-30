import requests

def submit(name: str, tmax: float, tmax_date: str, tdiff_max: float, tdiff_max_date: str) -> None:
    URL = "https://script.google.com/macros/s/AKfycbybB2LSi0F85FkC4KmI0XgjMqvhn7-6eJjZQi0oucbgbEvwDmNVRoyMMnd5UyezpqJp/exec"
    PARAMS = {
        '제출자': name,
        '최고온도': tmax,
        '최고온도날짜': tmax_date,
        '최대일교차': tdiff_max,
        '최대일교차날짜': tdiff_max_date,
    }

    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)
    if r.status_code != 200:
        print("과제가 정상적으로 제출되지 않았습니다.")


if __name__ == "__main__":
    submit("박은빈", 340.1, "2011-08-04", 25.2, "1978-01-04")