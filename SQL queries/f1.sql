SELECT t.tid, t.likes_number
FROM "Tweet" t
WHERE t.likes_number > 100 AND t.likes_number < 200