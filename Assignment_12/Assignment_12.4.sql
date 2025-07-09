#What is the most purchased item on the menu and how many times was it purchased by all customers?

SELECT m.product_name, COUNT(*) AS total_orders
FROM sales s
JOIN menu m ON s.product_id = m.product_id
GROUP BY m.product_name
ORDER BY total_orders DESC
LIMIT 1;
