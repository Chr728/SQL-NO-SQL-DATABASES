SELECT json_build_object(
    'username', ru.user_name,
    'Posts', (
        SELECT json_agg(json_build_object(
            'pid', rp.pid,
            'title', rp.title,
            'url', rp.url,
            'subreddit', rp.subreddit,
            'post_date', (
                SELECT json_build_object(
                    '$date', rp.post_date
                )
            ),
            'Sentiment', (
                SELECT json_build_object(
                    'sentiment_model_name', s.sentiment_model_name,
                    'positive_prob', s.positive_prob,
                    'negative_prob', s.negative_prob,
                    'neutral_prob', s.neutral_prob
                ) 
                FROM "RedditSentiment" s
                WHERE s.post_id = rp.pid
            ),
            'Emotion', (
                SELECT json_build_object(
                    'emotion_model_name', e.emotion_model_name,
                    'joy_prob', e.joy_prob,
                    'optimism_prob', e.optimism_prob,
                    'sadness_prob', e.sadness_prob,
                    'anger_prob', e.anger_prob
                ) 
                FROM "RedditEmotion" e
                WHERE e.post_id = rp.pid
            )
        ))
        FROM "RedditPost" rp
        WHERE rp.author_name = ru.user_name
    )
) AS results
FROM "RedditUser" ru;