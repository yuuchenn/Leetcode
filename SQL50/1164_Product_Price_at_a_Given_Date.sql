-- find the nearest change day before 2019-08-16'
with before_the_date as (
    select product_id,
           new_price as price,
           row_number() over(partition by product_id order by change_date desc) as rn 
      from Products
     where change_date <= to_date('2019-08-16','YYYY-MM-DD')
)
-- if not match means change after the day, so the price was 10
select a.product_id,
       (case when b.product_id is null then 10 else b.price end) as price
  from (select distinct product_id from Products) a,
       (select * from before_the_date where rn = 1) b
 where a.product_id = b.product_id(+)

