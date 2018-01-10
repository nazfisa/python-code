import re
str="12345"
print("match:", len(re.findall("\d{5}",str)))
