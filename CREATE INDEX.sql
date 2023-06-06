CREATE INDEX contains_tweeter_id ON "Contains"(tweeter_id);
CREATE INDEX contains_hashtag_name ON "Contains"(hashtag_name);
CREATE INDEX HashtagIndex ON "Hashtag"(hashtag_name);
CREATE INDEX user_uid ON "User"(uid);
CREATE INDEX user_username ON "User"(username);
CREATE INDEX user_name ON "User"(name);
CREATE INDEX tweet_tid ON "Tweet"(tid);
CREATE INDEX tweet_author_id ON "Tweet"(author_id);
CREATE INDEX tweet_content ON "Tweet"(content);
CREATE INDEX tweet_date ON "Tweet"(tweet_date);
CREATE INDEX tweet_likes ON "Tweet"(likes_number);
CREATE INDEX tweet_retweets ON "Tweet"(retweets_number);
CREATE INDEX emotion_tid ON "Emotion"(tweeter_id);
CREATE INDEX emotion_model ON "Emotion"(emotion_model_name);
CREATE INDEX emotion_joy ON "Emotion"(joy_prob);
CREATE INDEX emotion_optimism ON "Emotion"(optimism_prob);
CREATE INDEX emotion_sadness ON "Emotion"(sadness_prob);
CREATE INDEX emotion_anger ON "Emotion"(anger_prob);
CREATE INDEX sentiment_tid ON "Sentiment"(tweeter_id);
CREATE INDEX sentiment_model ON "Sentiment"(sentiment_model_name);
CREATE INDEX sentiment_positive ON "Sentiment"(positive_prob);
CREATE INDEX sentiment_negative ON "Sentiment"(negative_prob);
CREATE INDEX sentiment_neutral ON "Sentiment"(neutral_prob);


--TO SHOW EXISTING INDICES--
SELECT
    tablename,
    indexname,
    indexdef
FROM
    pg_indexes
WHERE
    schemaname = 'public'
ORDER BY
    tablename,
    indexname;