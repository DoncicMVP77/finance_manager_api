 # Тестовое задание SQL   

# Задание 1
Напишите запрос, который подсчитает какое количество ноутбуков представлено в каждом бренде. Отсортируйте данные по убыванию.
```
SELECT notebooks_brand.title, COUNT(notebooks_notebook.brand_id) as count from notebooks_brand
	INNER JOIN notebooks_notebook
	ON notebooks_brand.id = notebooks_notebook.brand_id
GROUP BY notebooks_brand.title
ORDER BY COUNT(notebooks_notebook.brand_id) DESC;
```
# Задание 2
Вам необходимо выделить группы ноутбуков по размерам. Для этого размеры предварительно нужно округлить в большую сторону до ближайшего 0 или 5 и затем сгруппировать по одинаковым размерам, подсчитав количество ноутбуков в каждой группе. Отсортируйте данные по размерам
```
SELECT 
	ROUND(CAST(width as NUMERIC), -1) AS width_n,
	ROUND(CAST(depth as NUMERIC), -1) AS depth_n, 
	ROUND(CAST(height as NUMERIC), -1) AS height_n,
	COUNT(*) AS count_n
FROM notebooks_notebook
GROUP BY width, depth, height
ORDER BY width, depth, height DESC;
```