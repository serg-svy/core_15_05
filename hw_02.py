articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    results = []
    for article in articles_dict:
        if letter_case:
            if key in article['title'] or key in article['author']:
                results.append({
                    'author': article['author'],
                    'title': article['title'],
                    'year': article['year']
                })
        else:
            if key.lower() in article['title'].lower() or key.lower() in article['author'].lower():
                results.append({
                    'author': article['author'],
                    'title': article['title'],
                    'year': article['year']
                })
    return results

    # Поиск статей, содержащих ключевое слово "ocean"
search_results = find_articles("ocean")
print(search_results)

# Поиск статей, содержащих ключевое слово "ocean" без учета регистра
search_results = find_articles("ocean", letter_case=False)
print(search_results)
