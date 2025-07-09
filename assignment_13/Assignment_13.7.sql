
select p.page_name, count(1) as total from
events e join page_hierarchy p 
on e.page_id = p.page_id
group by page_name
order by total desc
limit 3;
