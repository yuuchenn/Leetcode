select contest_id,
       round(count(user_id)/(select count(*) from Users)*100,2) as percentage 
  from Register
 group by contest_id
order by round(count(user_id)/(select count(*) from Users)*100,2) desc, contest_id
