select id,
       case when mod(id,2) = 1 and id = (select count(*) from seat) then student
            when mod(id,2) = 0 then lag(student,1) over(order by id)
            else lead(student,1) over(order by id) end as student
  from seat 
