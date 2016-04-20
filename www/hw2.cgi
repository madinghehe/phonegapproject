#!/usr/bin/python
#
#  This is a cgi program (hw3.cgi) that can be used to list the contents of a users websys directory
#
#  It must be named hw3.cgi and have world read access in order to work.
# This is due o security restrictions on the Stern systems that
# will only allow execution of programs named .cgi
#
# the input is the netid of the user, provided by a form with a fieldname of userid
# The program then constructs the path to the users directory
# Stern student directories are located at:
# /homedir/grad/FCHAR/NETID/
# and their websys directories are located at:
# /homedir/grad/FCHAR/NETID/public_html/websys
# where FCHAR is the first character of the netid and NETID is the netid.
#
# import the cgi modules to be able to retrive the form parameters
import cgi, cgitb
#import the commands module to let us execute unix commands
# and retrieve the results

import commands


        

# print the html headers to standard output
print "Content-type:text/html"
print ""
print 
print '<head>'
print '<title>'
print 'Contents of a users websys directory'
print '</title>'
print '<link href="css/bootstrap.min.css" rel="stylesheet">'
print '</head>'
print '<body>'

form=cgi.FieldStorage()


if "userid" not in form:
   print "<H1>Error</H1>"
   print "userid field not provided"

# retrieve the value of the userid field from the form

Userid =form["userid"].value
Fchar = Userid[0]
# Now construct the full path to their websys directory
# it should be  /homedir/grad/fchar/userid/public_html/websys
# where FCHAR is the first character of the userid
# type 'pwd' at the unix prompt to see you full path

# Note that we can treat strings as an array of characters
# with the first element at location 0

webSysPath = "/homedir/grad/" + Fchar + "/"  + Userid + "/public_html/websys"
print 'List of user ' + Userid + "'s" + ' websys directory<p>'
print '<h>You can CLICK it to get to the Link</h>'

lscommand = 'ls ' + webSysPath
#
# tell html the next stuff is preformatted
# otherwise it ignores line breaks and will ruin it all together
#
print '<pre>'
status,lsresults = commands.getstatusoutput(lscommand)

j = 0

file = []
for i in range(len(lsresults)):
	if lsresults[i]=="\n":

		print '<a href="http://websys3.stern.nyu.edu/~'+Userid+'/websys/'+lsresults[j:i]+'">'+lsresults[j:i]+' </a>'
		j = i+1
print '<a href="http://websys3.stern.nyu.edu/~'+Userid+'/websys/'+lsresults[j:i+1]+'">'+lsresults[j:i+1]+' </a>'



print '</pre>'
print '</body>'
print '</html>'

