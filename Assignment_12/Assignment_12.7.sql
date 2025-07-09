#Which item was purchased just before the customer became a member?

SELECT s.customer_id, s.order_date, m.product_name
FROM sales s
JOIN members mem ON s.customer_id = mem.customer_id
JOIN menu m ON s.product_id = m.product_id
JOIN (
    SELECT s2.customer_id, MAX(s2.order_date) AS last_date
    FROM sales s2
    JOIN members mem2 ON s2.customer_id = mem2.customer_id
    WHERE s2.order_date < mem2.join_date
    GROUP BY s2.customer_id
) latest_order
  ON s.customer_id = latest_order.customer_id
  AND s.order_date = latest_order.last_date
WHERE s.order_date < mem.join_date;
