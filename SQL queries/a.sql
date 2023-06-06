SELECT *
FROM "Tweet"
WHERE likes_number =
    (SELECT max(likes_number)
    FROM "Tweet")