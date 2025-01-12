select a.project_id,
       round(avg(b.experience_years),2) as average_years
  from Project a, Employee b
 where a.employee_id = b.employee_id
 group by a.project_id
