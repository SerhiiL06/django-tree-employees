<h1>Django Tree Project</h1>


<h2>Getting started</h2>

1. Clone git repository
```
git clone https://github.com/SerhiiL06/django-tree-employees.git
```

2. Change current directory
```
cd django-tree-employees
```

3. Install all dependencies for this project
```
pip install -r requirements.txt
```

4. Create database using psql or another UI
``` 
CREATE DATABASE <db_name> WITH owner <owner_name>
```

5. Rename env file
```
mv .env_example .env
```

6. Enter your database connection data in the .env file

7. Do run migrate command
```
python manage.py migrate
```

7. Load fake data from fixtures
```
python manage.py loaddata fixtures/employees.json
```

8. Run django server
```
python manage.py runserver
```å


<h2>Usage</h2>

1. Employees application
   - **/list/**  displays a list of all employees;
   - **/tree/** displays tree of all employees. Сlicking on employees of the second level of the hierarchy lazily loads all other levels;
   - **/create/** page for creating employee (available only for authenticated users);
   - **/list/<empl_id>/edit** page for updating employee information (available only for authenticated users);
   - **/list/<empl_id>/delete** delete employee action (available only for authenticated users);
2. Users application
   - **/register/** register page;
   - **/login/** login page;
