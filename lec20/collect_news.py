from bs4 import BeautifulSoup
import requests

def main():
    url = "https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=001"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    #print(soup.prettify())
    print(soup)
if __name__== "__main__":
    main()