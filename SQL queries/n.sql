----n--
Select "User".uid AS "The ID of the User","Tweet".tid "The ID of the Tweet"
from "User","Tweet","Contains"
where "User".uid = "Tweet".author_id
AND "Tweet".tid = "Contains".tweeter_id;
