-- 7 task
SELECT  P_id, D_id, PR_id FROM lab12.spj
INNER JOIN lab12.детали_p d ON D = D_id
INNER JOIN lab12.поставщики_s p ON P = P_id
INNER JOIN lab12.проект_g pr ON PR = PR_id 
WHERE  (pr.Город <> p.Город) or (pr.Город <> d.Город) or (p.Город <> d.Город);

-- 8 task
SELECT P_id, D_id, PR_id FROM lab12.spj
INNER JOIN lab12.детали_p d ON D = D_id
INNER JOIN lab12.поставщики_s p ON P = P_id
INNER JOIN lab12.проект_g pr ON PR = PR_id 
WHERE (p.Город <> d.Город) and (d.Город <> pr.Город) and (p.Город <> pr.Город);

-- 10 task
SELECT D_id FROM lab12.spj
INNER JOIN lab12.поставщики_s as p ON P = P_id
INNER JOIN lab12.проект_g as pr ON PR = PR_id 
WHERE pr.Город = 'Таллинн' AND p.Город = 'Таллинн';

-- 11 task 
SELECT DISTINCT поставщики_s.Город AS First,  проект_g.Город AS Second FROM lab12.spj
INNER JOIN lab12.поставщики_s ON P = P_id
INNER JOIN lab12.проект_g ON PR = PR_id
WHERE поставщики_s.Город <= проект_g.Город;   

-- 17 task
SELECT D_id, PR_id, SUM(S) FROM lab12.spj
GROUP BY D_id, PR_id;

-- 20 task
SELECT DISTINCT Цвет FROM lab12.spj
INNER JOIN lab12.детали_p ON D_id = D
WHERE P_id = 'П1';

-- 24 task
SELECT P FROM lab12.поставщики_s
WHERE Статус < (SELECT Статус FROM lab12.поставщики_s WHERE P = 'П1');

-- 26 task
SELECT PR_id FROM lab12.spj
WHERE D_id = 'Д1'
GROUP BY PR_id
HAVING AVG(S) > (SELECT MAX(S) FROM lab12.spj WHERE PR_id = 'ПР1' GROUP BY PR_id);

 -- 32 task
SELECT DISTINCT PR_id FROM lab12.spj 
WHERE D_id IN (SELECT DISTINCT D_id FROM lab12.spj 
WHERE P_id = 'П1'); 

-- 36 task 
SELECT DISTINCT sub1.P1_id AS First, sub2.P2_id AS Second FROM (SELECT P_id AS P1_id, SUM(S) AS s FROM lab12.spj
GROUP BY P_id, PR_id) sub1 INNER JOIN (SELECT P_id as P2_id, SUM(S) AS s FROM lab12.spj
GROUP BY P_id, PR_id) sub2 USING(s)
WHERE P1_id < P2_id
ORDER BY P1_id, P2_id;

-- 31 task 
SELECT P_id FROM (SELECT DISTINCT P_id, D_id FROM lab12.spj 
GROUP BY P_id, D_id) sub
GROUP BY P_id
HAVING COUNT(*) = 1;

-- 22 task
SELECT DISTINCT PR_id FROM lab12.spj
WHERE D_id IN (SELECT D_id FROM lab12.spj WHERE P_id = 'П1');

-- 28 task
SELECT PR_id FROM lab12.spj 
GROUP BY PR_id
HAVING PR_id NOT IN (SELECT DISTINCT PR_id from lab12.spj		
INNER JOIN lab12.детали_p ON D_id = D 
INNER JOIN lab12.поставщики_s ON P_id = P
WHERE Цвет = 'Красный' AND поставщики_s.Город = 'Таллинн');

-- 4 task
SELECT P_id, D_id, PR_id FROM lab12.spj
WHERE S BETWEEN 400 and 750;

-- 16 task 
SELECT SUM(S) FROM lab12.spj
WHERE D_id = 'Д1' and P_id = 'П1'
GROUP BY D_id, P_id;

