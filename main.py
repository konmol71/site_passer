import requests
import bs4

site_url = 'https://upl.uz'

page_html = requests.get(site_url).text
# print(page_html)

page_soup = bs4.BeautifulSoup(page_html, 'html.parser')

news_wrapper = page_soup.find('div', id='upl-content')
news_list = news_wrapper.find_all('div', class_='sh-news')
# print(len(news_list))

result = []

for i in news_list:
    title = i.find('h2', class_='sh-title').get_text()
    # print('title:', title)
    description = i.find('div', class_='sh-text').next.get_text(strip=True)
    # print('description:', description)
    img_link = i.find('img').get('data-src')
    # print(img_link)
    side_date = i.find('div', class_='side-date').find_all('span')
    side_date = [i.get_text() for i in side_date]
    if len(side_date) == 2:
        time, comments = side_date
    else:
        time = side_date[0]
        comments = 0
    # print(side_date)

    result.append({
        'title': title,
        'description': description,
        'img_link': img_link,
        'time': time,
        'comments': comments,
    })

print(result)

import json

with open('upl.json', mode='w', encoding='utf-8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)
