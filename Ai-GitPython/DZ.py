#  Завдання 1
# Створіть клас Pet з атрибутами
#  name – ім’я тварини
#  satiety – рівень ситості(від 0 до 100, за замовчуванням 50)
#  energy – рівень енергії (від 0 до 100, за замовчуванням 50)
# Методи:
#  sleep() – збільшує energy до 100
#  eat(food_amont) – їсть, збільшує satiety на food_amount
#  play(activity_level) – абстрактний метод
#  make_sound() – просто pass
# Створіть клас Cat
# Методи:
#  play(activity_level) – якщо satiety > 60, зменшує energy на
# 2*acticity_level та satiety на acticity_level
#  make_sound() – виводить ‘Мяу’
#  catch_mouse() – якщо  energy > 30, ловить мишу. Якщо
# satiety > 40, то грається з мишею, інакше їсть
# Створіть клас Dog
# Методи:
#  play(activity_level) – якщо satiety > 15, зменшує energy на
# acticity_level//2 та satiety на acticity_level//2
#  make_sound() – виводить ‘Гав’
#  fetch_ball() – ловить м’яча якщо satiety>10, зменшує
# energy на 5
import abc from ABC

class Pet(ABC):
