import json

from pprint import pprint

from site_passer.category import CategoryPasser
from site_passer.detail import DetailPasser

def main() -> None:
    category_passer = CategoryPasser()
    categories = category_passer.get_categories()

    detail_passer = DetailPasser()
    result = detail_passer.get_news(categories)

    pprint(result)
    return result

main()

with open('upl2.json', mode='w', encoding='utf-8') as file:
    json.dump(main(), file, indent=4, ensure_ascii=False)