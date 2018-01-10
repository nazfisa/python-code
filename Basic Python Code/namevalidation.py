import re
#---------------validate Full name------------------------------------------------------------
#\s=[\f=fromfeed,\n=newline,\t=tab,\v=vartical tab]
#\S=[^ \f=fromfeed,\n=newline,\t=tab,\v=vartical tab]
if re.search("\w{2,20}\s\w{2,20}", "Nazim Uddin"):
    print("full name is valid")
