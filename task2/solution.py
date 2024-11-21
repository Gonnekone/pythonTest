import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"

def fetch_animals_count():
    alphabet_counts = dict(А=0, Б=0, В=0, Г=0, Д=0, Е=0, Ё=0, Ж=0, З=0, И=0, Й=0, К=0, Л=0, М=0, Н=0, О=0, П=0, Р=0,
                           С=0, Т=0, У=0, Ф=0, Х=0, Ц=0, Ч=0, Ш=0, Щ=0, Ъ=0, Ы=0, Ь=0, Э=0, Ю=0, Я=0)
    next_page = BASE_URL

    while next_page:
        response = requests.get(next_page)
        soup = BeautifulSoup(response.content, 'html.parser')
        all_animals = soup.find("div", id="mw-pages")

        for animal in all_animals.find_all(class_="mw-category-group"):
            letter = animal.find("h3").text.strip()

            if letter not in alphabet_counts:
                return alphabet_counts

            alphabet_counts[letter] += len(animal.find_all("li"))

        next_page = "https://ru.wikipedia.org" + soup.find('div', id='mw-pages').contents[-2].get('href')

def save_to_csv(data, filename="animals.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Буква", "Количество животных"])
        for letter, count in data.items():
            writer.writerow([letter, count])


print("Скачивание данных с википедии...")
animals_count = fetch_animals_count()

print(f"Запись данных в файл...")
save_to_csv(animals_count)

print("Готово! Данные сохранены")
