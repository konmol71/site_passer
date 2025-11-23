from .base import BasePasser

class CategoryPasser(BasePasser):
    def get_categories(self) -> list[dict[str, str]]:
        soup = self.get_soup()

        nav_row = soup.find('div', class_='nav_row')
        categories = nav_row.find_all('li')
        result = []
        for category in categories:
            name = category.get_text(strip=True)

            if name.lower() in ['Контакты', 'Контакты', '']:
                continue

            href = category.find('a').get('href')

            result.append({
                'name': name,
                'href': href
            })
        return result