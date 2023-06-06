drop table if exists "User" cascade;
drop table if exists "Tweet" cascade;
drop table if exists "Creates" cascade;
drop table if exists "Hashtag" cascade;
drop table if exists "Contains" cascade;
drop table if exists "Emotion" cascade;
drop table if exists "Sentiment" cascade;
drop table if exists "RedditUser" cascade;
drop table if exists "RedditPost" cascade;
drop table if exists "RedditEmotion" cascade;
drop table if exists "RedditSentiment" cascade;

CREATE TABLE "User" (
    uid BIGINT PRIMARY KEY,
    username text NOT NULL,
    name text NOT NULL
);
CREATE TABLE "Tweet" (
    tid BIGINT PRIMARY KEY,
    author_id BIGINT NOT NULL,
    content text NOT NULL,
    tweet_date TIMESTAMP NOT NULL,
    likes_number int,
    retweets_number int,
    Foreign key(author_id) references "User"(uid)on DELETE CASCADE on Update CASCADE
);


CREATE TABLE "Hashtag" (
    hashtag_name text PRIMARY KEY
);
CREATE TABLE "Contains" (
    tweeter_id BIGINT NOT NULL,
    hashtag_name text NOT NULL,
    PRIMARY KEY (tweeter_id, hashtag_name),
    Foreign key(tweeter_id) references "Tweet"(tid)on DELETE CASCADE on Update CASCADE,
    Foreign key(hashtag_name) references "Hashtag"(hashtag_name)on DELETE CASCADE on Update CASCADE
);

CREATE TABLE "Emotion" (
    tweeter_id BIGINT NOT NULL,
    emotion_model_name text NOT NULL,
    joy_prob float NOT NULL,
    optimism_prob float NOT NULL,
    sadness_prob float NOT NULL,
    anger_prob float NOT NULL,
    PRIMARY KEY (tweeter_id, emotion_model_name),
    Foreign key(tweeter_id) references "Tweet"(tid)on DELETE CASCADE on Update CASCADE
);
CREATE TABLE "Sentiment" (
    tweeter_id BIGINT NOT NULL,
    sentiment_model_name text NOT NULL,
    positive_prob float NOT NULL,
    negative_prob float NOT NULL,
    neutral_prob float NOT NULL,
    PRIMARY KEY (tweeter_id, sentiment_model_name),
    Foreign key(tweeter_id) references "Tweet"(tid)on DELETE CASCADE on Update CASCADE
);



--- Data Enrichement ---

CREATE TABLE "RedditUser" (
    user_name TEXT PRIMARY KEY
);

CREATE TABLE "RedditPost" (
    pid TEXT PRIMARY KEY,
    author_name TEXT NOT NULL,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    subreddit TEXT NOT NULL,
    post_date TIMESTAMP NOT NULL,
    FOREIGN KEY(author_name) REFERENCES "RedditUser"(user_name) ON DELETE CASCADE ON Update CASCADE
);

CREATE TABLE "RedditEmotion" (
    post_id TEXT NOT NULL,
    emotion_model_name TEXT NOT NULL,
    joy_prob float NOT NULL,
    optimism_prob float NOT NULL,
    sadness_prob float NOT NULL,
    anger_prob float NOT NULL,
    PRIMARY KEY (post_id, emotion_model_name),
    FOREIGN KEY(post_id) REFERENCES "RedditPost"(pid) ON DELETE CASCADE ON Update CASCADE
);

CREATE TABLE "RedditSentiment" (
    post_id TEXT NOT NULL,
    sentiment_model_name TEXT NOT NULL,
    positive_prob float NOT NULL,
    negative_prob float NOT NULL,
    neutral_prob float NOT NULL,
    PRIMARY KEY (post_id, sentiment_model_name),
    FOREIGN KEY(post_id) REFERENCES "RedditPost"(pid) ON DELETE CASCADE ON Update CASCADE
);
