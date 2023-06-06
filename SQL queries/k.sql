-- Gets 6th highest liked tweet
(SELECT *
FROM "Tweet" t
ORDER BY t.likes_number DESC
LIMIT 6)
EXCEPT
(SELECT *
FROM "Tweet" t
ORDER BY t.likes_number DESC
LIMIT 5)