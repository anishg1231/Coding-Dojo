SELECT first_name, tweet
FROM users 
LEFT JOIN faves
ON users.id = faves.user_id
LEFT JOIN tweets
ON faves.tweet_id = tweets.id
where users.id = 2;

