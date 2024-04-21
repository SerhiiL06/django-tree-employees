<h1>Django Tree Project</h1>


<h2>Getting started</h2>

1. Clone git repository
```
git clone https://github.com/SerhiiL06/django-tree-employees.git
```

2. Change current repository
```
cd django-tree-employees
```

3. Install all dependensies for this project
```
pip install -r requirements.txt
```

4. Enter your database data to .env_example file
5. Load fake data from fixtures
```
python manage.py loaddata fixtures/employees.json
```

6. Run django server
```
python manage.py runserver
```


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
