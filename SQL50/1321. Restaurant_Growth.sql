with query as (
select visited_on,
       sum(amount) over(order by visited_on rows between 6 preceding and current row) as amount, 
       row_number() over(order by visited_on) as rn
  from (select visited_on, sum(amount) as amount from Customer group by visited_on)
  order by visited_on
)
select to_char(visited_on,'YYYY-MM-DD') as visited_on,
       amount,
       round(amount/7,2) as average_amount
  from query 
where rn >= 7

/*
1. sum(...) over(order by... rows between [n_frames] preceding and [current] row):
to cumulative sum of the values in the range of rows(start from [current]-[n_frames] to [current], so it will contain [n_frames+1] values)

2. sum(...) over(order by...):
like the excel cumsum function, to cumulative sum of the values in the whole table

3. sum(...) over(partition by... order by...):
by group to cumulative sum of values 
*/
