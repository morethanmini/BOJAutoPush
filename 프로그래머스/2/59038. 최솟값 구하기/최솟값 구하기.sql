-- 코드를 입력하세요
# SELECT DATE_FORMAT(DATETIME, '%Y-%m-%m %T') AS 시간
# FROM ANIMAL_INS
# ORDER BY DATETIME
# LIMIT 1;

SELECT MIN(DATETIME) AS "시간"
FROM ANIMAL_INS