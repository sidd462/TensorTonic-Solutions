-- Returns: name, salary.
select name, salary from employees where department in ('Engineering', 'Marketing') and salary > 70000;