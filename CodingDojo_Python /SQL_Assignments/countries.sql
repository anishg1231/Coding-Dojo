SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
ORDER BY languages.percentage DESC;

SELECT countries.name, COUNT(cities.id) 
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY COUNT(cities.id) DESC;

SELECT cities.population, cities.name
FROM cities
JOIN countries ON cities.id = cities.country_id
WHERE cities.population >= 500000
ORDER BY cities.population DESC;

SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

SELECT countries.name, countries.surface_area, countries.population
FROM countries 
WHERE countries.surface_area < 501 AND countries.population > 100000;


SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy
FROM countries
WHERE countries.government_form = 'Constitutional Monarchy'
AND countries.capital > 200
AND countries.life_expectancy > 75;



SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
LEFT JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Argentina'
AND cities.district = 'Buenos Aires'
AND cities.population > 500000;


SELECT countries.region, COUNT(countries.id) as country_num
FROM countries
GROUP BY countries.region
ORDER BY country_num DESC;
