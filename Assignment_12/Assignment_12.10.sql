#In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi — how many points do customer A and B have at the end of January?

SELECT s.customer_id,
       SUM(
         CASE 
           WHEN s.order_date BETWEEN mem.join_date AND DATE_ADD(mem.join_date, INTERVAL 6 DAY) THEN 
             m.price * 10 * 2
           WHEN m.product_name = 'sushi' THEN 
             m.price * 10 * 2
           ELSE m.price * 10
         END
       ) AS total_points
FROM sales s
JOIN menu m ON s.product_id = m.product_id
JOIN members mem ON s.customer_id = mem.customer_id
WHERE s.order_date <= '2021-01-31'
AND s.customer_id IN ('A', 'B')
GROUP BY s.customer_id;
