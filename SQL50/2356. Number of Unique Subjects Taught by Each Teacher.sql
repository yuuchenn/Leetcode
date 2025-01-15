select teacher_id,
       count(distinct teacher_id||subject_id) as cnt
  from Teacher
 group by teacher_id
