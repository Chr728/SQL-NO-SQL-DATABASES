# SOEN 363

This project  was done in group of 5 people and it aims to analyze general sentiment towards gun control. This is done through an anlysis of tweets that involve the gun control topic. 

## Steps to run similar experiment with these scripts:

1. Run "TwitterAPIFetcher.py" several times to accumulate enough data to perform an adequate analysis (you have to add the token key in a file named .env)
2. Run "TweetNLPSentimentAnalyzer_json.py" on the .json file generated in step 2 (put the correct json file name in the script)
3. Run the "CompleteProcessWrapper.py" to clean and convert the data to INSERT queries (put the correct json file name(s) in the script)
4. Using the Schema, run the CREATE TABLE queries to create the database schema
5. Run the INSERT queries in an SQL database that you will use to analyze the results

Now all the data should be correctly formatted in your SQL database and can be analyzed using SQL qeuries. 
