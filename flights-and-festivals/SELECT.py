import requests
from bs4 import BeautifulSoup

req = requests.get('https://code.s3.yandex.net/learning-materials/data-analyst/festival_news/index.html')
soup = BeautifulSoup(req.text, 'lxml')

table = soup.find('table',attrs={"id": "best_festivals"})
# применим метод find к тегу table
# укажем атрибут первой таблицы: ten_years_first 

heading_table = [] # Список, в котором будут храниться названия столбцов
for row in table.find_all('th'): # Названия столбцов прячутся в элементах th
        heading_table.append(row.text) # Добавляем контент из тега th в список heading_table методом append()

content=[] # Список, в котором будут храниться данные из таблицы
for row in table.find_all('tr'): 
# Каждая строка обрамляется тегом tr, необходимо пробежаться в цикле по всем строкам
    if not row.find_all('th'): 
# Эта проверка необходима, чтобы пропустить первую строку таблицы с заголовками
            content.append([element.text for element in row.find_all('td')])
            # В каждой строке контент ячейки обрамляется тегами <td> </td>

import pandas as pd
festivals = pd.DataFrame(content, columns=heading_table) 
print(festivals)