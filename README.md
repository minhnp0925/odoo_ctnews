CTNews project based on Odoo

PostgreSQL db config
Step 1: Select server
Step 2: Object -> Create -> Login/Group Role 
Step 3: 
- General: Name = odoo
- Definition: Password = odoo
- Privileges: Can login, create databases
(username: odoo, password: odoo, if you change this then change the corresponding vars in run-odoo.bat)
Step 4: Import sql (will be added later, no data for now)

Install:
pip install setuptools wheel
pip install watchdog
pip install -r requirements.txt

start server:
./run-odoo (-u ctnews)

