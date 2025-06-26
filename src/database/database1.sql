delete from produce where id = '4';
SELECT * FROM produce;
INSERT INTO produce (name, kind, color, calories, description) VALUES
('Яблоко', 'Фрукт', 'Красный', 52, 'Сладкий и сочный фрукт.'),
('Морковь', 'Овощ', 'Оранжевый', 41, 'Корнеплод, богатый витаминами.'),
('Банан', 'Фрукт', 'Жёлтый', 89, 'Тропический сладкий фрукт.'),
('Огурец', 'Овощ', 'Зелёный', 15, 'Охлаждающий овощ для салатов.');
SELECT * FROM produce;
SELECT * FROM produce
WHERE kind = 'Овощ';
SELECT * FROM produce
WHERE kind = 'Фрукт';
SELECT name FROM produce;
SELECT DISTINCT color FROM produce;

SELECT * FROM produce
WHERE kind = 'Фрукт' AND color = 'Жёлтый';

SELECT * FROM produce
WHERE kind = 'Овощ' AND color = 'Зелёный';
