SELECT 
  page_hierarchy.product_category,
  COUNT(CASE WHEN events.event_type = 1 THEN 1 END),
  COUNT(CASE WHEN events.event_type = 2 THEN 1 END)
FROM events
JOIN page_hierarchy 
  ON events.page_id = page_hierarchy.page_id
WHERE page_hierarchy.product_category IS NOT NULL
GROUP BY page_hierarchy.product_category;
