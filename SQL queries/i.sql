-- all tweets from author_id that appears most frequently
SELECT *
FROM "Tweet" t1
WHERE t1.author_id IN
    (SELECT t.author_id
    FROM "Tweet" t
    GROUP BY t.author_id
    ORDER BY COUNT(*) DESC
    LIMIT 1)