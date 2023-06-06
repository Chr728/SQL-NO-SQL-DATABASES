SELECT sum(t.retweets_number), u.username
FROM "Tweet" t, "User" u
WHERE t.author_id = u.uid
GROUP BY u.username
