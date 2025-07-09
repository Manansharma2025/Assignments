SELECT AVG(cookie_count) AS avg_cookie_count
FROM (
    SELECT user_id, COUNT(cookie_id) AS cookie_count
    FROM users
    GROUP BY user_id
) AS user_cookie_counts;
