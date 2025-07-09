#What was the first item from the menu purchased by each customer?

select sales.customer_id, menu.product_name, sales.order_date
from sales
left join menu
on sales.product_id = menu.product_id
where order_date = '2021-01-11'
group by sales.customer_id, menu.product_name;