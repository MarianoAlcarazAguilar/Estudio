# Estudio

## Joins

### Inner Join

Regresa los registros de la tabla `A` que hagan match con los registros de la tabla `B`

 ```sql
 SELECT *
 FROM pacientes p JOIN paciente_doctor USING (id_paciente);
 ```
 También podemos usar el comando `intersect`
  ```sql
  select c.city
  from customers c intersect 
      select s.city 
      from suppliers s;
   ```
 
### Full Outer Join
   
Regresa TODOS los registros tanto de la tabla `A` como de la tabla `B`

 ```sql
 SELECT *
 FROM pacientes p  FULL JOIN paciente_doctor USING (id_paciente);
 ```
También podemos usar el comando UNION

```sql
select c.contact_name, c.city
from customers c UNION
  select s.contact_name, s.city
  from suppliers s;
```

### Left Join

Regresa todos los registros de la tabla `A` y los registros que hagan match con la tabla `B`
 ```sql
 SELECT *
 FROM pacientes p  LEFT JOIN paciente_doctor USING (id_paciente);
 ```
Si solo queremos los de la tabla `A` que **no** hagan match con `B`
```sql
select s.company_name, o.order_id 
from shipers s left join orders on (s.shipper_id = o.ship_via)
where o.ship_via is null;
--En este caso la tabla B es orders y no queremos los que hagan match ahí.
```




 
