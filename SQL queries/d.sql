SELECT t.author_id, sum(t.likes_number), avg(t.likes_number)
FROM "Tweet" AS t
GROUP BY t.author_id