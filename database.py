
#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","test623","network_analyzer" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "select * from hosts"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      mac = row[1]
      name = row[2]
      # Now print fetched result
      print "name=%s,mac=%s,name=%s" % \
             (name, mac, name)
except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()