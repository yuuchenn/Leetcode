with uni_loc as (
select lat||lon as loc
  from insurance 
 group by lat||lon 
having count(*) = 1
), uni_tiv_2015 as (
select tiv_2015 as tiv_2015
  from insurance 
 group by tiv_2015
having count(*) > 1
)
select sum(tiv_2016) as tiv_2016
  from insurance a, uni_loc b, uni_tiv_2015 c
 where a.tiv_2015 = c.tiv_2015
   and a.lat||a.lon = b.loc

/*
condition 1: have the same value of the tiv_2015, and must be have the rows greater than one 
condition 2: with unique (lat,lon) 
filter match condition2 fisrt, would not be able to determine if the condition 1 have more than 1 rows.

ex:
input:
tiv_2015  lat  lon
   20      10   10
   10      20   20
   10      20   20 

output:
1.(condition 2 first, then condition 1)
tiv_2015  lat  lon

*would be empty
--------------
(condition 2)
tiv_2015  lat  lon
   10      10   10 
   10      20   20 <- would be deleted 
   10      20   20 <- would be deleted  
(condition 1)
tiv_2015  lat  lon
   10      10   10 <- only one row, doesn't match the condition 1

2.(condition 1 first, then condition 2)
tiv_2015  lat  lon
   10      10   10
---------------
(condition 1)
tiv_2015  lat  lon
   10      10   10 
   10      20   20 
   10      20   20 
(condition 2)
tiv_2015  lat  lon
   10      10   10 
   10      20   20 <- would be deleted 
   10      20   20 <- would be deleted
*/
