# Using Postgresql

#### Getting Data from a script
* Download Script Using Query Tool and Run

#### Getting Data from a .csv file
* Create Table <> and column names equal to columns in .csv file
* Copy data from .csv using command:
>    --COPY <tablename ?(specify-columns)> FROM '<path-to-csvfile>' DELIMITERS ',' CSV
*** Warning: Copy cmd updates the db anytime it's run. Run once or more to generate extra rows. ***

#### Transfering data from public schema to any other 
* Create new schema and populate tables from "public"
>    --ALTER TABLE <> SET SCHEMA <>

#### Changing search path to simplify queries
* --SHOW search_path;
    * If public exists: change search_path to new schema, public
    * If drop public: change search_path to new schema
>    --SET search_path TO <schemaname>;
* Try queries

#### Github commit message requirements
* Sending pull requests
    * if _update_: -m "patch: "
    * if _add_: -m "feat: "
    * if _fix_: -m "fix: "


