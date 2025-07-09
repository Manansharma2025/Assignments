#If each $1 spent equates to 10 points and sushi has a 2x points multiplier — how many points would each customer have?

SELECT 
  s.customer_id,
  SUM(
    IF(m.product_name = 'sushi', 20 * m.price, 10 * m.price)
  ) AS total_points
FROM sales AS s
JOIN menu AS m ON s.product_id = m.product_id
GROUP BY s.customer_id;
