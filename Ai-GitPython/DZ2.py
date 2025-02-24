# Завдання 1
# Створіть клас Recipe з атрибутами  name – назва страви
#  ingredients – список продуктів  text – текст рецепту
#  time – час приготування
# методи:
#  __str__(self) – повертає назву страви
#  __contains__(self, item)  – перевіряє чи є інгредієнт в рецепті
#  __gt__(self, other)  – перевіряє чи є час приготування self більшим за other
#  display_info(self) – виводить всю інформацію про рецепт
# Створіть декілька рецептів та добавте їх у список. Виведіть назви тих рецептів, які містять інгредієнт томат
# Виведіть повну інформацію рецепта з найменшим часом приготування, скористайтесь функцією min


class Recipe:
    def __init__(self, name, ingredients, text, time):
        self.name = name
        self.ingredients = ingredients  # Fixed typo
        self.text = text
        self.time = time

    def __str__(self):
        return f"Назва страви: {self.name}"

    def __contains__(self, item):
        print(f'{item} ')
        return item in self.ingredients  # Fixed typo

    def __gt__(self, other):
        return self.time > other.time

    def display_info(self):
        print("-" * 20)
        print(f"Назва страви: \n '{self.name}'")
        print("-" * 20)
        print("Інгредієнти:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}", end=" ")



recipe1 = Recipe("Піца",
       ["борошно", "вода", "дріжджі", "томат", "сир"],
       "Готуємо тісто, додаємо інгредієнти та запікаємо",
       30)

recipe2 = Recipe("Салат",        ["томат", "огірок", "зелень", "олія"],
       "Нарізаємо овочі, додаємо зелень та поливаємо олією ", 10)

recipe3 = Recipe("Суп",        ["вода", "картопля", "морква", "м'ясо"],
       "Варимо всі інгредієнти до готовності",        45)

recipe1.display_info()

print("огірок" in recipe1)
print("----" *5 )
print(min(recipe1, recipe2))
print("+++++" *5 )

recipe1.display_info()

