--q--
--ii--
select "Hashtag".hashtag_name,"Contains".tweeter_id
from "Hashtag" RIGHT JOIN "Contains"  ON "Hashtag".hashtag_name= "Contains".hashtag_name;
