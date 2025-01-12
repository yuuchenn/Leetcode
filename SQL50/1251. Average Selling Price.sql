with avg_price as 
(
select a.product_id,
       round(sum(price * units)/sum(units),2) as average_price
  from Prices a, UnitsSold b
 where a.product_id = b.product_id(+)
   and b.purchase_date between a.start_date and a.end_date
 group by a.product_id
), all_product as 
(
select distinct product_id 
  from Prices
)
select a.product_id,
       nvl(b.average_price,0) as average_price
  from all_product a, avg_price b
 where a.product_id = b.product_id(+)

/*
1. get average_price table
2. all_product left join avg_price on product_id 
   if matched average_price else nvl(average_price,0) 
*/
