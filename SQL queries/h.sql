-- i.
SELECT t.content, t.retweets_number
FROM "Tweet" t
WHERE t.content LIKE 'g%'
-- ii.
SELECT t.content, t.retweets_number
FROM "Tweet" t
WHERE t.content NOT LIKE '%g'
-- iii.
SELECT t.content, t.retweets_number
FROM "Tweet" t
WHERE t.content LIKE '%gun%'