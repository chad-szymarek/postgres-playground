# postgres-playground

A repository for playing around in postgres with psycopg2

# How to set up the project

1. Install Postgres in your system

2. Connect to Postgres and create a user with these commands and credentials:
   `CREATE USER admin PASSWORD admin CREATEDB;`

3. Connect to Postgres using the user that you previously created

4. Create a new table using this command
   ```
   CREATE TABLE person (
        firstname varchar(50),
        lastname varchar(50)
   );
   ```
5. Exit out of the Postgres shell.

6. In the root folder of the project, run `python server.js`
