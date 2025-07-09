select ph.page_name, count(*) as v_c
FROM events e
JOIN page_hierarchy ph ON e.page_id = ph.page_id
WHERE e.event_type = 3
GROUP BY ph.page_name;
 