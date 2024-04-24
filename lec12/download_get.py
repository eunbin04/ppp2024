import requests

URL="https://coopjbnu.kr/menu/week_menu.php"

data={"code": "mobile1"}

with open("./cafeteria_menu_weekly.html", "w", encoding="UTF-8") as f:
    res=requests.post(URL, data=data)
    res.encoding="UTF-8"
    f.write(res.text)