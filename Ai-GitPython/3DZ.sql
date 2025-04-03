-- Створіть наступні запити для бази даних з інформацією 
-- про овочі та фрукти з попереднього домашнього завдання:
-- ■ Відображення усіх овочів з калорійністю, менше вказаної.

SELECT *
FROM FRUITS_AND_VEGETABLES
WHERE CALORIAS < 20

-- ■ Відображення усіх фруктів з калорійністю у вказаному
-- діапазоні.
SELECT *
FROM FRUITS_AND_VEGETABLES
WHERE CALORIAS BETWEEN 20 AND 30

-- ■ Відображення усіх овочів, у назві яких є вказане слово.
-- Наприклад, слово: капуста.
SELECT *
FROM FRUITS_AND_VEGETABLES
WHERE NAME_VEG LIKE '%перець%'

-- ■ Відображення усіх овочів та фруктів, у короткому описі
-- яких є вказане слово. Наприклад, слово: гемоглобін.
SELECT *
FROM FRUITS_AND_VEGETABLES
WHERE DESCRIPTION LIKE '%антиоксидант%'

-- ■ Показати усі овочі та фрукти жовтого або червоного
-- кольору.
SELECT *
FROM FRUITS_AND_VEGETABLES
WHERE COLOUR = 'Червоний' OR COLOUR = 'Оранжевий'

-- Завдання 2
-- Створіть наступні запити для бази даних з інформацією 
-- про овочі та фрукти з попереднього домашнього завдання:
-- ■ Показати кількість овочів.
SELECT COUNT(NAME_VEG)
FROM FRUITS_AND_VEGETABLES

-- ■ Показати кількість фруктів.
SELECT COUNT(NAME_VEG)
FROM FRUITS_AND_VEGETABLES
WHERE TYPE_ID='Фрукт'

-- ■ Показати кількість овочів та фруктів заданого кольору.
SELECT COUNT(NAME_VEG)
FROM FRUITS_AND_VEGETABLES
WHERE COLOUR = 'Оранжевий'

-- ■ Показати кількість овочів та фруктів кожного кольору.
SELECT  COLOUR, COUNT(NAME_VEG)
FROM FRUITS_AND_VEGETABLES
GROUP BY COLOUR

-- ■ Показати колір мінімальної кількості овочів та фруктів.
WITH COLOUR_COUNT AS	
	(SELECT COLOUR, COUNT(*) AS MAX_COUNT
	FROM FRUITS_AND_VEGETABLES
	GROUP BY COLOUR)
SELECT COLOUR
FROM COLOUR_COUNT
WHERE MAX_COUNT  = (SELECT MIN(MAX_COUNT)
FROM COLOUR_COUNT)


-- ■ Показати колір максимальної кількості овочів та фруктів.
WITH COLOUR_COUNT AS	
	(SELECT COLOUR, COUNT(*) AS MAX_COUNT
	FROM FRUITS_AND_VEGETABLES
	GROUP BY COLOUR)
SELECT COLOUR
FROM COLOUR_COUNT
WHERE MAX_COUNT  = (SELECT MAX(MAX_COUNT)
FROM COLOUR_COUNT)


SELECT *
FROM FRUITS_AND_VEGETABLES


-- ■ Показати мінімальну калорійність овочів та фруктів.
SELECT MIN(CALORIAS)
FROM FRUITS_AND_VEGETABLES

-- ■ Показати максимальну калорійність овочів та фруктів.
SELECT MAX(CALORIAS)
FROM FRUITS_AND_VEGETABLES

-- ■ Показати середню калорійність овочів та фруктів.
SELECT AVG(CALORIAS)
FROM FRUITS_AND_VEGETABLES

-- ■ Показати фрукт з мінімальною калорійністю.
SELECT NAME_VEG
FROM FRUITS_AND_VEGETABLES
WHERE CALORIAS = (SELECT MIN(CALORIAS)
FROM FRUITS_AND_VEGETABLES)

-- ■ Показати фрукт з максимальною калорійністю.
SELECT NAME_VEG
FROM FRUITS_AND_VEGETABLES
WHERE CALORIAS = (SELECT MAX(CALORIAS)
FROM FRUITS_AND_VEGETABLES)


