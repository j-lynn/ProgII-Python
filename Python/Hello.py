#!/usr/bin/python
print ("Content-type:text/html\n\n");
import MySQLdb
import sys

try:
 conn = MySQLdb.connect (
  host = "jameslynn.ipagemysql.com",
  user = "dev",
  passwd = "Test9876!",
  db = "dev")

except MySQLdb.Error as e:
 print ("Error %d: %s" % (e.args[0], e.args[1]))
 sys.exit("Exiting")


print ("connected to the database");
print(conn);
print("Hello, World!");
print("Hello, there Again!");
