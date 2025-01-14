with first_order as (
select delivery_id,
       row_number() over(partition by customer_id order by order_date) as rn
  from Delivery
)
select round(sum(case when order_date = customer_pref_delivery_date then 1 else 0 end)*100 / count(*),2) as immediate_percentage
  from Delivery a,
       (select * from first_order where rn = 1) b
 where a.delivery_id = b.delivery_id
