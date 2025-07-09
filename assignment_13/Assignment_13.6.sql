select (count(visit_id)/(select count(distinct visit_id)
from events))*100 AS checkout_percnt
from events
where page_id = 12 and event_type != 3;