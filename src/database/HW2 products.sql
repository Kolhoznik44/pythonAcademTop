-- CREATE TABLE products (
--     id          SERIAL PRIMARY KEY,
--     name        VARCHAR(100),
--     type        VARCHAR(10),      -- 'овощ' или 'фрукт'
--     calories    INT,              -- калорийность
--     description TEXT,
--     color       VARCHAR(20)
-- );

-- INSERT INTO products (name, type, calories, description, color)
-- VALUES
--   ('Морковка',    'овощ', 41,  'Богата витамином А',           'оранжевый'),
--   ('Яблоко',      'фрукт', 52,  'Повышает гемоглобин',          'зелёный'),
--   ('Капуста',     'овощ', 25,  'Содержит витамин C',            'зелёный'),
--   ('Помидор',     'овощ', 20,  'Полезен для сердца',            'красный'),
--   ('Банан',       'фрукт', 96,  'Источник калия',                'жёлтый'),
--   ('Персик',      'фрукт', 39,  'Содержит антиоксиданты',        'жёлтый');



-- SELECT *
-- FROM products
-- WHERE type = 'овощ'
--   AND calories < 50;

-- SELECT *
-- FROM products
-- WHERE color IN ('жёлтый', 'красный');

-- Показать фрукт с максимальной калорийностью
-- SELECT *
-- FROM products
-- WHERE type = 'фрукт'
--   AND calories = (SELECT MAX(calories) FROM products WHERE type = 'фрукт');

-- Показать фрукт с минимальной калорийностью
-- SELECT *
-- FROM products
-- WHERE type = 'фрукт'
--   AND calories = (SELECT MIN(calories) FROM products WHERE type = 'фрукт');

-- Показать среднюю калорийность овощей и фруктов
-- SELECT AVG(calories) AS avg_calories
-- FROM products;


-- Показать максимальную калорийность овощей и фруктов
-- SELECT MAX(calories) AS max_calories
-- FROM products;

 -- Показать минимальную калорийность овощей и фруктов
-- SELECT MIN(calories) AS min_calories
-- FROM products;

-- Показать цвет с максимальным количеством овощей и фруктов
-- SELECT color, COUNT(*) AS cnt
-- FROM products
-- GROUP BY color
-- ORDER BY cnt DESC
-- LIMIT 1;


-- Показать цвет с минимальным количеством овощей и фруктов
-- SELECT color, COUNT(*) AS cnt
-- FROM products
-- GROUP BY color
-- ORDER BY cnt ASC
-- LIMIT 1;

-- Показать количество овощей
-- SELECT COUNT(*) AS vegetable_count
-- FROM products
-- WHERE type = 'овощ';

-- Показать количество фруктов
-- SELECT COUNT(*) AS fruit_count
-- FROM products
-- WHERE type = 'фрукт';



