# FastAPI + MySQL

A simple FastAPI app that stores users in MySQL.

## Project files

```text
.env
main.py
requirements.txt
```

## 1. Create the MySQL database

In MySQL Shell, switch to SQL mode:

```text
\sql
```

Connect to MySQL:

```text
\connect root@localhost
```

Create the database:

```sql
CREATE DATABASE mydatabase;
```

## 2. Configure the connection

Create a file named `.env` in the project folder:

```env
MYSQL_DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost/mydatabase
```

Replace `YOUR_PASSWORD` with your MySQL password.

## 3. Install the packages

Open PowerShell in this project folder:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
```

## 4. Start the app

```powershell
.\.venv\Scripts\python.exe -m uvicorn main:app --port 8001
```

## 5. Use the app

Open the stored-users page:

```text
http://127.0.0.1:8001/
```

Open the API page to create a user:

```text
http://127.0.0.1:8001/docs
```

In `POST /users`, enter a name and email, then click **Execute**.

The saved users appear at:

```text
http://127.0.0.1:8001/
```

You can also view the JSON data at:

```text
http://127.0.0.1:8001/users
```

## Check the data in MySQL

```sql
USE mydatabase;
SELECT * FROM users;
```

The `users` table is created automatically when the app starts.


