SELECT json_build_object(
    '_id', u.uid,
    'username', u.username,
    'name', u.name,
    'Tweets', (
        SELECT json_agg(json_build_object(
            'tid', t.tid,
            'CONTENT', t.CONTENT,
            'tweet_date', (
                SELECT json_build_object(
                    '$date', t.tweet_date
                )
            ),
            'likes_number', t.likes_number,
            'retweets_number', t.retweets_number,
            'Sentiment', (
                SELECT json_build_object(
                    'sentiment_model_name', s.sentiment_model_name,
                    'positive_prob', s.positive_prob,
                    'negative_prob', s.negative_prob,
                    'neutral_prob', s.neutral_prob
                ) 
                FROM "Sentiment" s
                WHERE s.tweeter_id = t.tid
            ),
            'Emotion', (
                SELECT json_build_object(
                    'emotion_model_name', e.emotion_model_name,
                    'joy_prob', e.joy_prob,
                    'optimism_prob', e.optimism_prob,
                    'sadness_prob', e.sadness_prob,
                    'anger_prob', e.anger_prob
                ) 
                FROM "Emotion" e
                WHERE e.tweeter_id = t.tid
            ),
            'Hashtags', (
                SELECT 
                    CASE 
                        WHEN count(*) > 0 
                        THEN json_agg(hashtag_name)
                        ELSE '[]'
                    END AS "Hashtags"
                FROM "Contains"
                WHERE tweeter_id = t.tid
            )
        ))
        FROM "Tweet" t
        WHERE t.author_id = u.uid
    )
) AS results
FROM "User" u;