
#!/usr/bin/python

import MySQLdb


def getKnownDevicesList():
# Open database connection
    db = MySQLdb.connect("localhost","testuser","test623","network_analyzer" )

    known_hosts = dict()
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "select * from hosts"
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Fetch all the rows in a list of lists.
       results = cursor.fetchall()
       for row in results:
          mac = row[1]
          name = row[2]
          # Now print fetched result
          known_hosts[name.title()] = [mac.upper() for row in results]

          # print "name=%s,mac=%s" % \
          #        (name, mac)

       # disconnect from server
       db.close()
       return known_hosts
    except:
       print "Error: unable to fecth data"

