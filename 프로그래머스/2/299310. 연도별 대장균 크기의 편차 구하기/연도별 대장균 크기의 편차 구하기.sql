SELECT 
    YEAR(E.DIFFERENTIATION_DATE) AS YEAR,
    M.MAX_SIZE - E.SIZE_OF_COLONY AS YEAR_DEV,
    E.ID
FROM ECOLI_DATA E
JOIN (
    SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, MAX(SIZE_OF_COLONY) AS MAX_SIZE
    FROM ECOLI_DATA
    GROUP BY YEAR(DIFFERENTIATION_DATE)
) M ON YEAR(E.DIFFERENTIATION_DATE) = M.YEAR
ORDER BY YEAR ASC, YEAR_DEV ASC