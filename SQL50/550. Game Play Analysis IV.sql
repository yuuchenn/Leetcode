/* method 1: use join to check if the day next to fisrt_day is exist or not*/
with first_day as(
select t.*,
       row_number() over(partition by player_id order by event_date) as rn
  from Activity t
)
select round(count(distinct case when b.event_date is not null then a.player_id else null end)/count(distinct a.player_id),2) as fraction
  from (select * from first_day where rn = 1) a, Activity b
 where a.player_id = b.player_id(+)
   and a.event_date+1 = b.event_date(+)
  
/* method 2 :create first_day column and check if the day next to fisrt_day is exist or not */
with first_day as(
select t.*,
       min(event_date) over(partition by player_id) as first_day
  from Activity t
)
select round(count(distinct case when first_day+1 = event_date then player_id else null end)/count(distinct player_id),2) as fraction
  from first_day
