
--o--
Select "Hashtag".hashtag_name AS "The Name of the Hashtag","Contains".tweeter_id AS "Tweet ID"
from "Hashtag","Tweet","Contains"
where "Hashtag".hashtag_name = "Contains".hashtag_name
AND "Hashtag".hashtag_name like 'm_%'
AND "Contains".tweeter_id = "Tweet".tid;
