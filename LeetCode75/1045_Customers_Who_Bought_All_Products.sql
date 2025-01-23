
select a.customer_id
  from Customer a, Product b
-- owned product in Product table
 where a.product_key = b.product_key
 group by a.customer_id
-- product nums = total nums of product in Product table
having count(distinct a.product_key) = (select count(*) from Product)
