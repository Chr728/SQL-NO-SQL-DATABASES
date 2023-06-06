--m--
--tid matches with tweet id of emotion table, author id matches with user id of user table 
-- so some columns of these rows matches two other different tables
Select "Tweet".tid AS " The Tweet ID" ,"Tweet".likes_number AS "Likes Number of the Tweet"
from "Tweet"
where "Tweet".likes_number > 115 
Group  by "Tweet".tid 
order by "Tweet".likes_number desc ;

