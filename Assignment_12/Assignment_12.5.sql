#Which item was the most popular for each customer?

SELECT * FROM (
  SELECT s.customer_id, m.product_name, COUNT(*) order_count,
         ROW_NUMBER() OVER (PARTITION BY s.customer_id ORDER BY COUNT(*) DESC) rn
  FROM sales s
  JOIN menu m ON s.product_id = m.product_id
  GROUP BY s.customer_id, m.product_name
) x
WHERE rn = 1;

