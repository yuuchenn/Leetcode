with exams as (
select student_id,
       subject_name,
       count(*) as attended_exams 
  from Examinations
 group by student_id, subject_name
), full_table as (
select a.*,
       b.*
  from Students a, Subjects b
 where 1 = 1
)
select a.*, 
       case when b.attended_exams is null then 0 else b.attended_exams end as attended_exams 
  from full_table a, exams b
 where a.student_id = b.student_id(+)
   and a.subject_name = b.subject_name(+)
order by a.student_id , a.subject_name
