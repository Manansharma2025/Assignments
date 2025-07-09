select month(event_time),count(distinct visit_id ) from events 
group by month(event_time);