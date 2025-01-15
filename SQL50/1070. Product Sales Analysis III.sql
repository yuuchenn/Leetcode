with first_year as (
select a.*,
       min(year) over(partition by product_id) as first_year
  from Sales a
)
select product_id,
       first_year,
       sum(quantity) as quantity,
       price
  from first_year
 where year = first_year
 group by product_id, first_year, price
