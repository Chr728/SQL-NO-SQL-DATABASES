--q--
--iii--
select "Hashtag".hashtag_name,"Contains".tweeter_id
from "Hashtag" FULL OUTER JOIN "Contains"  ON "Hashtag".hashtag_name= "Contains".hashtag_name;
