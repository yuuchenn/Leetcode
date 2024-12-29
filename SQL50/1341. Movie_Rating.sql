select name as results
  from (select b.name,
               count(*) as nums
          from MovieRating a, users b
         where a.user_id = b.user_id(+)
         group by b.name
         order by count(*) desc, b.name)
 where rownum = 1
union all
select title as results
  from (select b.title,
               avg(rating) as avg_rating
        from MovieRating a, Movies b
        where a.movie_id = b.movie_id(+)
        and created_at between TO_DATE('2020-02-01','YYYY-MM-DD') AND TO_DATE('2020-02-29','YYYY-MM-DD')
        group by b.title
        order by avg(rating) desc, b.title)
 where rownum = 1

/* 
1.order function can do multiple conditions and default to aescending order
2.to_date('2020-02','YYYY-MM') equal to 2020-02-01, 
so have to change : to_char(created_at,'YYYY-MM') = to_date('2020-02','YYYY-MM')
but if it is a index key or partition key, the adjustment will make key invalid.
*/
