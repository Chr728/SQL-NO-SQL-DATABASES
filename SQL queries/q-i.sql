--q--
--i--
select "Hashtag".hashtag_name,"Contains".tweeter_id
from "Hashtag" LEFT JOIN "Contains"  ON "Hashtag".hashtag_name= "Contains".hashtag_name;
