SELECT 
  100.0 * COUNT(DISTINCT CASE WHEN event_type = 3 THEN visit_id END) 
        / COUNT(DISTINCT visit_id) AS purchase_percentage
FROM events;