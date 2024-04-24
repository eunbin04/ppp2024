import requests

URL="https://coopjbnu.kr/function/ajax.get.rest.data.php"

data={"code": "mobile1"}

with open("./cafeteria_menu.html", "w", encoding="UTF-8") as f:
    res=requests.post(URL, data=data)
    res.encoding="UTF-8"
    f.write(res.text)