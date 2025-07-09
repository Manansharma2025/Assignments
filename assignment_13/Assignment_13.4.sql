SELECT event_type, COUNT(event_type) 
FROM events 
GROUP BY event_type;
