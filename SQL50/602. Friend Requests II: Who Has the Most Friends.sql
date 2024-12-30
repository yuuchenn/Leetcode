with query as (
select id, 
       count(*) as num
  from(select requester_id as id from RequestAccepted
        union all 
       select accepter_id as id from RequestAccepted)
 group by id
order by num desc
)
select id,
       num
  from query
 where rownum = 1
