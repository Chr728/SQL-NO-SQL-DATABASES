SELECT t.author_id, MAX(t.likes_number)
FROM "Tweet" t
GROUP BY t.author_id
HAVING MAX(t.likes_number) > 10