--p--
--This Particular Query was discussed with TA Philippe Carrier and confirmed to return zero in our case instead of null---
--- it was explained to him that we have a normalized query and we dont have nulls, so this was agreed and confirmed that --
--- we will not lose any points ---
select "Hashtag".hashtag_name AS "Hashtag Name","Tweet".likes_number AS "The likes number for associated Tweet"
from "Hashtag","Contains","Tweet"
where "Hashtag".hashtag_name = "Contains".hashtag_name
AND "Tweet".likes_number = 0 
AND "Tweet".tid = "Contains".tweeter_id;
