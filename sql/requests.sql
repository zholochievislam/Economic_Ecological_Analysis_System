-- CAST(gdp.Value AS DECIMAL(20,4)) AS gdp_per_capita,

Use eco_econ_system;


-- Top-10 High GDP countries
SELECT
c.CountryName,
ed.Year,
ed.Value AS gdp_per_capita
FROM Econ_Data ed
JOIN Economic_Indicator ei
	ON ed.EconomicID = ei.EconomicID
JOIN Country c
	ON ed.CountryID = c.CountryID
WHERE ei.Name = "GDP_per_capita"
	AND ed.Year = 2024
ORDER BY ed.Value DESC
LIMIT 10;

-- GDP and CO2 of Countries in a given year
SELECT
c.CountryName,
el.Year,
en.Value AS gdp_per_capita,
el.Value AS co2_emissions
FROM Econ_Data en
JOIN Economic_Indicator eni
	ON en.EconomicID = eni.EconomicID
JOIN Ecol_Data el
	ON el.Year = en.Year
JOIN Ecologic_Indicator eli
	ON el.EcologicID = eli.EcologicID
JOIN Country c
	ON c.CountryID = el.CountryID AND c.CountryID = en.CountryID
WHERE eni.Name = "GDP_per_capita"
	AND eli.Name = "CO2_Emissions"
    AND el.Year = 2024
ORDER BY c.CountryName DESC;


-- Population & Safe Water ALSO: People without safe water

SELECT
C.CountryName,
en.Year,
CAST(en.Value AS DECIMAL(20,4)) AS population,
CAST(el.Value AS DECIMAL(20,4)) AS safe_water,
en.Value * (1 - el.Value / 100.0) AS people_without_safe_water
FROM Econ_Data en
JOIN Economic_Indicator eni
	ON en.EconomicID = eni.EconomicID
JOIN Ecol_Data el
	ON el.Year = en.Year 
	AND el.CountryID = en.CountryID
JOIN Ecologic_Indicator eli
	ON el.EcologicID = eli.EcologicID
JOIN Country c
	ON c.CountryID = en.CountryID
WHERE eni.Name = 'Population'
	AND eli.Name = 'Safe water access' 
	AND en.Year = 2020
ORDER BY people_without_safe_water DESC
LIMIT 10;

-- Green Paradox 

SELECT 
c.CountryName,
CAST(ed.Value AS DECIMAL(20,4)) AS gdp_2020
From Econ_Data ed
Join Economic_Indicator eni
	On eni.EconomicID = ed.EconomicID
join Country c
	ON c.CountryID = ed.CountryID
WHERE eni.Name = "GDP_per_capita" AND ed.Year = 2020
order by gdp_2020 desc;

describe Econ_Data;

-- CO2 and GDP
 select 
 c.CountryName,
 c.CountryID,
 CAST(SUM(CASE WHEN ed.Year = 2015 THEN ed.Value END) AS DECIMAL(20, 4)) AS gdp_2015,
 CAST(SUM(CASE WHEN ed.Year = 2020 THEN ed.Value END) AS DECIMAL (20, 4)) AS gdp_2020,
 (CAST(SUM(CASE WHEN ed.Year = 2020 THEN ed.Value END) AS DECIMAL(20,4))- CAST(SUM(CASE WHEN ed.Year = 2015 THEN ed.Value END) AS DECIMAL(20,4)))
 /NULLIF(CAST(SUM(CASE WHEN ed.Year = 2015 THEN ed.Value END) AS DECIMAL(20,4)),0) * 100 AS gdp_growth_pct
FROM Econ_Data ed
JOIN Economic_Indicator eni
	ON eni.EconomicID = ed.EconomicID
JOIN Country c
	ON c.CountryID = ed.CountryID 
WHERE eni.Name = "GDP_per_capita" AND ed.Year IN (2015, 2020)
GROUP BY c.CountryName
ORDER BY gdp_growth_pct;


SELECT ed.Year, ed.Value
FROM Econ_Data ed
JOIN Economic_Indicator eni ON eni.EconomicID = ed.EconomicID
JOIN Country c              ON c.CountryID    = ed.CountryID
WHERE eni.Name = 'GDP_per_capita'
  AND c.CountryName = 'United States'
  AND ed.Year BETWEEN 2010 AND 2020
ORDER BY ed.Year;


-- GDP high, CO2 low

WITH gdp AS(
	SELECT
		ed.CountryID,
        MIN(CASE WHEN ed.Year = 2015 THEN CAST(ed.Value AS DECIMAL(20, 4)) END) as gdp_min,
        MAX(CASE WHEN ed.Year = 2020 THEN CAST(ed.Value AS DECIMAL(20, 4))END) as gdp_max
        FROM Econ_Data ed
        JOIN Economic_Indicator eni
			ON ed.EconomicID = eni.EconomicID
		JOIN Country c
			ON c.CountryID = ed.CountryID
		WHERE eni.Name = "GDP_per_capita"
			AND ed.Year BETWEEN 2015 AND 2020
		GROUP BY ed.CountryID
),
 co2 AS(
	SELECT
		el.CountryID,
        MIN(CASE WHEN el.Year = 2015 THEN CAST(el.Value AS DECIMAL(20, 4)) END) as co2_min,
        MAX(CASE WHEN el.Year = 2020 THEN CAST(EL.Value AS DECIMAL(20, 4)) END) as co2_max
        FROM Ecol_Data el
        JOIN Ecologic_Indicator eli
			ON el.EcologicID = eli.EcologicID
		JOIN Country c
			ON c.CountryID = el.CountryID
		WHERE eli.Name = "CO2_Emissions"
			AND el.Year BETWEEN 2015 AND 2020
		group by el.CountryID
)

SELECT 
c.CountryName,
g.gdp_min,
g.gdp_max,
ROUND((g.gdp_max-g.gdp_min)/g.gdp_min * 100, 2) AS GDP_Change,
co.co2_min,
co.co2_max,
ROUND((co.co2_max-co.co2_min)/co.co2_min * 100, 2) AS CO2_Change

FROM gdp g
JOIN co2 co 
	ON g.CountryID = co.CountryID
JOIN Country c
	ON c.CountryID = g.CountryID
WHERE g.gdp_max > g.gdp_min AND co.co2_min > co.co2_max
ORDER BY GDP_Change DESC;


-- GDP low, CO2 high

WITH co2 AS(
	SELECT
    el.CountryID,
    MIN(CASE WHEN el.Year = 2015 THEN CAST(el.Value AS DECIMAL (20, 4)) END) AS co2_2015,
    MAX(CASE WHEN el.Year = 2020 THEN CAST(el.Value AS DECIMAL (20, 4)) END) AS co2_2020
    FROM Ecol_Data el
    JOIN Ecologic_Indicator eli ON el.EcologicID = eli.EcologicID
    WHERE eli.Name = "CO2_Emissions" AND el.Year BETWEEN 2015 AND 2020
    GROUP BY el.CountryID
),
gdp AS(
	SELECT 
    ed.CountryID,
    MIN(CASE WHEN ed.Year = 2015 THEN CAST(ed.Value AS DECIMAL(20, 4)) END) AS gdp_2015,
    MAX(CASE WHEN ed.Year = 2020 THEN CAST(ed.Value AS DECIMAL(20, 4)) END) AS gdp_2020
    FROM Econ_Data ed
    JOIN Economic_Indicator eni ON ed.EconomicID = eni.EconomicID
    WHERE eni.Name = "GDP_per_capita" AND ed.Year BETWEEN 2015 AND 2020
    GROUP BY ed.CountryID
)

SELECT
c.CountryName,
co.co2_2015,
co.co2_2020,
ROUND((co.co2_2020 - co.co2_2015)/co.co2_2015 * 100, 2) AS CO2_Change,
g.gdp_2015,
g.gdp_2020,
ROUND((g.gdp_2020 - g.gdp_2015)/g.gdp_2015 * 100, 2) AS GDP_Change

FROM gdp g
JOIN co2 co ON g.CountryID = co.CountryID
JOIN Country c ON c.CountryID = co.CountryID
WHERE co.co2_2015<co.co2_2020 AND g.gdp_2015>g.gdp_2020
ORDER BY GDP_Change DESC,
	CO2_Change ASC;

-- TOP 10 WITH HIGH INFLATION RATE

SELECT
c.CountryName,
ed.Year AS Year,
CAST(ed.Value AS DECIMAL(20, 4) ) AS Inflation_Rate,
RANK() OVER(ORDER BY ed.Value DESC) AS Rang

FROM Econ_Data ed
JOIN Economic_Indicator eni ON ed.EconomicID = eni.EconomicID
JOIN Country c ON c.CountryID = ed.CountryID
WHERE ed.EconomicID = 2 AND ed.Year = 2021
ORDER BY Inflation_Rate DESC
Limit 10;

-- GDP1 vs GDP2

SELECT
ed.Year AS Year,
CAST(SUM(CASE WHEN c.CountryName = "Italy" THEN ed.Value END)AS DECIMAL(20, 4)) AS Italy_GDP,
CAST(SUM(CASE WHEN c.CountryName = "France" THEN ed.Value END) AS DECIMAL(20, 4)) AS France_GDP
FROM Econ_Data ed 
JOIN Country c 
	ON c.CountryID = ed.CountryID
JOIN Economic_Indicator ei 
	ON ei.EconomicID = ed.EconomicID 
WHERE ei.Name = "GDP_per_capita"
	AND c.CountryName in("Italy", "Spain", "France")
    AND ed.Year between 2014 AND 2024
GROUP BY ed.Year
ORDER BY Year DESC;

-- Population vs Population



-- ALL COUNTRY GDP

WITH tot AS(
	SELECT
	ed.CountryID,
	SUM(CASE WHEN ed.Year = 2018 THEN ed.Value END) AS,
)

SELECT
c.CountryName,
ed.Year AS Year,
CAST(ed.Value AS DECIMAL(20, 4)) AS GDP,
ROUND(CAST(ed.Value AS DECIMAL(20, 4))/(
	SELECT SUM(CAST(ed2.Value AS DECIMAL(20, 4)))
    FROM Econ_data ed2
    WHERE ed2.EconomicID = ed.EconomicID 
		AND ed2.Year = ed.Year
    ) * 100, 2) AS Percentage

FROM Econ_Data ed
JOIN Country c
	ON c.CountryID = ed.CountryID
WHERE ed.EconomicID = 1 AND ed.Year = 2018
ORDER BY c.CountryName ASC;


-- All Countries Population

SELECT
c.CountryName,
SUM(CAST(ed.Value AS DECIMAL(20, 4))) AS Population,
ROUND(SUM(CAST(ed.Value AS DECIMAL(20, 4)))/SUM(SUM(CAST(ed.Value AS DECIMAL(20, 4))))OVER()*100, 2 ),
 ROUND(CAST(ed.Value AS DECIMAL(20, 4))/ (
 	SELECT
   SUM(CAST(ed2.Value AS DECIMAL(20, 4)))
   FROM Econ_Data ed2
	WHERE ed.Year = ed2.Year)*100, 2) AS Percentage
FROM Econ_data ed
JOIN Country c ON ed.CountryID = c.CountryID
WHERE ed.EconomicID = 3 AND ed.Year = 2018
ORDER BY c.CountryName ASC;

SELECT 
c.Region,
SUM(CAST(el.Value AS DECIMAL(20, 4))) AS ree,
ROUND(SUM(CAST(el.Value AS DECIMAL(20, 4)))/SUM(SUM(CAST(el.Value AS DECIMAL(20, 4))))OVER()*100, 2 ) AS Percentage
-- ROUND(SUM(CAST(el.Value AS DECIMAL(20, 4)))/
-- 		(	
-- 			SELECT
-- 			SUM(CAST(el2.Value as decimal(20, 4)))
--             FROM Ecol_Data el2
--             WHERE el2.EcologicID = 3)*100, 2) AS Percentage
FROM Ecol_Data el
JOIN Country c ON c.CountryID = el.CountryID
WHERE el.EcologicID = 3
Group BY c.Region
ORDER BY Percentage;


-- Forest Loss by Region

select c.Region, sum(cast(eld.value as decimal(20,4))) as TotalFireLoss, 
round
(
	100 * sum(cast(eld.value as decimal(20,4))) / sum(sum(cast(eld.value as decimal(20,4)))) over(), 2
) as percentage
from ecol_data eld join country c
	on c.CountryID = eld.CountryID
    and EcologicID = 3
group by c.Region
order by percentage desc;




