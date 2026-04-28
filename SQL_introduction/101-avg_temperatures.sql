-- Select city and calculate the average of the 'value' column
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY temperatue ORDER BY temperature DESC;
