import urllib.request
import pandas as pd
import MySQLdb
from bs4 import BeautifulSoup
import datetime

# ------------- Prerequisites -------------------------------------------------------------------------#
# Author : Disha J Dudhal
# Institute : Indian Institute of Information Technology, Pune, India 
# For this project I first created a database named scrapping_sample
# Followed by that I created a table named "planned_outages"
# The structure of the table can be viewed in the text file named "Table Structure for Planned Outages"
# Version of MySQL = 8.0.20 64-bit
# Version of Python used = 3.6.6
# Author contact = dishadudhal@gmail.com 
#-------------------------------------------------------------------------------------------------------#

#SQL connection parameters to save the data
HOST = "localhost"
USERNAME = "root"
PASSWORD = "root"
DATABASE = "scraping_sample"

#URL to be scraped
URL = "http://103.7.130.119:8181/GenOutageReportD.aspx"

#Load Html's plain data into a vairable
#SAUCE is a block of meta data that can be appended to various art works made by the scene. - source(https://pypi.org/project/sauce/)
sauce = urllib.request.urlopen(URL).read()
soup = BeautifulSoup(sauce, 'lxml') 

#Identify the table you want to scrap from the webpage using the table id
table = soup.find("table",{"id": "table1"})
#Extract all table rows from the table into table_rows variable
table_rows = table.find_all('tr')

#The following two lines of code are used to obtain the Select date at the top of the page
date_input = soup.find("input", {"id" : "txtOnDate"})
date = date_input['value']

#Some global variables required by the for loop
all_rows=[]
sector_type = ""

#Open database connection
db = MySQLdb.connect(HOST, USERNAME, PASSWORD, DATABASE)
#Prepare a cursor object using cursor method
cursor = db.cursor()
try:
    for tr in table_rows:
        #Extract all table data from each row
        td  = tr.find_all('td')
        # create a list "row" which contains each item from the table row
        row = [i.text.strip() for i in td]
        
        #Since the Sector type is mentioned at the top of each sectionof the table obtain the sector type.
        if len(row) == 2:
           sector_type = td[1].text.strip()

        #Obtain all the values from each table row which contain data such as station, state, agency, unit_no, capacity, reason, outage_date, outage_time, expected revival date
        if len(row) > 8:
            #now is used to obtain the timestamp for each row entered into the database in YYYY-MM-DD HH:MM:SS format
            now = datetime.datetime.now().isoformat()   
            #Form the SQL query to insert a record into the table
            sql_query = "insert into Planned values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            #Execute the sql command
            cursor.execute(sql_query, [date, sector_type, row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], str(now)])
            #Commit your changes in the database
            db.commit()
except:
    db.rollback()
    db.close()
    print("Data loading unsuccessful!!")
    
finally:
    #Close the database connecttion
    db.close()

print("Data loaded into Mysql successfully")
        
