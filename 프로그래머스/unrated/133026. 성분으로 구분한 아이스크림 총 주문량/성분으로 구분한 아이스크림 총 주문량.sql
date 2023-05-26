-- 코드를 입력하세요
SELECT B.INGREDIENT_TYPE, sum(A.TOTAL_ORDER) as TOTAL_ORDER
from ICECREAM_INFO B, FIRST_HALF A
where A.FLAVOR = B.FLAVOR
GROUP BY B.INGREDIENT_TYPE
order by A.TOTAL_ORDER