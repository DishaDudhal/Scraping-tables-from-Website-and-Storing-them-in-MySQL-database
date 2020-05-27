# Scraping-tables-from-Website-and-Storing-them-in-MySQL-database
Developed a web crawler/ scrapper/ spider to crawl a website with multiple tables and store the information form one of the tables into MySQL database using Python.<br>
<br>
Write a code to scrape data from a given url.<br> 
URL :  http://103.7.130.119:8181/GenOutageReportD.aspx <br>
Scrape 1st table form site i.e. A. Planned Outages and store data in mysql db <br>
Columns in mysql table <br>
● date (given in datepicker of site)<br>
● sector_type (can be Central Sector or State Sector it will appear at the start of table data)<br>
● station<br> 
● state<br>
● agency<br>
● unit_no<br> 
● capacity<br>
● reason<br> 
● outage_date<br>
● outage_time<br>
● expected_revival_date<br>
● inserted_at(time when data is inserted in db in format YYYY-MM-DD HH:MM:SS)<br>
<br>
Note: If value not available on site for any column insert null, also choose appropriate data types for columns. 
<br> 
Do not insert following row in mysql table 
● Central Sector (CS)<br> 
● Sub Total(CS)<br>
● State Sector (SS)<br>
● Sub Total(SS)<br>
● Total Planned Outage (CS+SS)<br>
<br>
Note: Only insert rows having S.no. in 1st column 
<br>
Libraries used for this project include
1) Beautifulsoup.   (pip install beautifulsoup4)
2) urllib           (pip install urllib)
3) requests         (pip install requests)
4) sauce            (pip install sauce)
5) mysqlclient      (pip install mysqlclient) 

Python Version used  - Python 3.6.6 64-bit<br>
MySQL version - 8.0.20 64 bit version (please install Visual Studio C++ 2019 redistributable version for this purpose beforehand)<br><br>

Steps for working:
1) I first created the desired table in MySQL. Code for which can be found in MySQL_queries.sql file. For the purpose of this project I have created two tables namely "planned_outages" and "Planned".
2) Both are essentially the same tables and just created for testing purposes.
3) Open MySQL Workbench, turn on the local server, create desired databse, tables, users and passwords prior to the code.
3) I have not handled the datatype of each value in the table and stroed everything as Text datatype. You can modify the code accordingly according to your requirements.
4) The entire Python code is commented and pretty much self explanatory.
5) After running the code succesfully.In the MySQL_queries.sql file you can also find commands for checking the data in the tables created and the number of rows.
6) Two csv output files are provoded which are nothing but the SQL database tables exported into CSV format from the Workbench.
<br>
Incase of queries feel free to contact me at : dishadudhal@gmail.com
<br>
References:
1) https://docs.python.org/3/library/urllib.html
2) https://github.com/aminazirani/Python-Scraping-to-Database-Sample/blob/master/scraping_single_web_page.py
3) https://howpcrules.com/step-by-step-guide-on-scraping-data-from-a-website-and-saving-it-to-a-database/
4) https://www.mysqltutorial.org/mysql-data-types.aspx/
5) https://dev.mysql.com/doc/refman/8.0/en/
6) https://pypi.org/project/sauce/
7) https://lxml.de/elementsoup.html
8) https://www.edureka.co/community/19715/programmingerror-arguments-converted-string-formatting
9) https://pythonprogramminglanguage.com/web-scraping-with-pandas-and-beautifulsoup/
10) https://www.youtube.com/watch?v=sAuGH1Kto2I
11) https://www.youtube.com/watch?v=ve_0h4Y8nuI&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t

Thanks to all the content creators on youtube, bloggers and github users which helped in the realization of this assignment.

Happy coding!
