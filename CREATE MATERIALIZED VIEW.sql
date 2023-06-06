--Question A--
CREATE MATERIALIZED VIEW QuestionAView AS 
SELECT *
FROM "Tweet"
WHERE likes_number =
    (SELECT max(likes_number)
    FROM "Tweet");

--Question R--
CREATE MATERIALIZED VIEW QuestionRView AS 
Select "Hashtag".hashtag_name AS "Hashtag Name","Contains".tweeter_id "Tweeter ID"
from "Hashtag","Contains","Tweet"
where "Hashtag".hashtag_name = "Contains".hashtag_name 
AND "Contains".tweeter_id  = "Tweet".tid
AND EXISTS (
  SELECT 1 FROM (
    SELECT regexp_matches("Hashtag".hashtag_name, '((.).*?\2.*?\2)') AS matches
  ) AS repeated_chars
  WHERE array_length(repeated_chars.matches, 1) > 0
);