import re
#\w check all [a-z,A-Z,0-9]
#\W check all[^a-z,A-Z,0-9]
phn="412-555-1212"

if re.search("\w{3}-\w{3}-\w{4}",phn):
    print("it is a usa phone number")

phn="01885390090"
if re.search("018\w{9}"):
    print("it is a bd phone number")
#---------------validate Full name------------------------------------------------------------
#\s=[\f=fromfeed,\n=newline,\t=tab,\v=vartical tab]
#\S=[^ \f=fromfeed,\n=newline,\t=tab,\v=vartical tab]
if re.search("\w{2,20}\s\w{2,20}", "Nazim Uddin"):
    print("full name is valid")
#------------------------validation Email-------------------------------------------------------
email=input("enter your Email:")
print("EmailMatch:", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[a-zA-z]{2,3}",email)))
