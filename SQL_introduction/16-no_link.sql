-- List all non-blank names and their scores, sorted descending.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
