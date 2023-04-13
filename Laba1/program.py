from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
cafedry = []
def parse():
    url = 'https://www.omgtu.ru/general_information/the-structure/the-department-of-university.php'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    print(page.status_code)  # смотрим ответ

    for caf in soup.select('div#pagecontent > ul > li > a'):
        cafedry.append(caf.text)

def WriteFile():
    with open('cafedry.txt', 'w', encoding='utf-8') as f:
        for caf in cafedry:
            f.write(caf + '\n')
