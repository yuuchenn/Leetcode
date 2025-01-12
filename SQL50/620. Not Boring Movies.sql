select *
  from Cinema
 where mod(id,2) > 0
   and description != 'boring'
 order by rating desc

/* use mod() function to get the remainder*/
