/* 
1. salary rank of each department 
2. filter out the mathced employees
3. join the Department name
*/

with temp as (
select salary,
       departmentId,
       dense_rank() over(partition by departmentId order by salary desc) as rnk
  from Employee
)
select c.name as Department,
       a.name as Employee,
       a.salary as Salary
  from Employee a,
       (select distinct salary, departmentId from temp where rnk <= 3) b,
       Department c
 where a.salary = b.salary
   and a.departmentId = b.departmentId
   and a.departmentId = c.id(+)
