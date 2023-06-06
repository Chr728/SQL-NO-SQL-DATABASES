<<<<<<< HEAD
select t.likes_number, t.author_id
from "Tweet" t
order by t.likes_number desc, t.author_id asc
=======
SELECT t.likes_number, t.retweets_number
FROM "Tweet" t
ORDER BY t.likes_number DESC, t.retweets_number
>>>>>>> 53efbf5b478b2eb8a7c5edc2ba059eddbac662ea
