import re
sr=re.search("inform","inform the information")
print("there is information")

#------find all------------------------------------------
print("#------find all------------------------------------------")
findall=re.findall("inform","inform the information")
for i in findall:
    print(i)
#-----iterator-------------------------------------------
print("#------iterator------------------------------------------")
str="inform the information"
for j in re.finditer("inform",str):
    loctup=j.span()  #for seeing accordig to tuple
    print(loctup)
#---------first letter and last letter----------
print("#------first letter and last letter------------------------------------------")    
str="sat,hat,mat,lat,at"
all=re.findall("[shml]at",str) #[shml]at means find all whos first character is s,h,m,l  and last tow characters are at.
for i in all:
    print(i)
#----again-------------------------------------------------------
print("#------again------------------------------------------")
str="sat,hat,mat,lat,at"
all=re.findall("[h-m]at",str) #[h-m]at means find all whos first character is h to m  and last tow characters are at.
for i in all:
    print(i)
#-----print without those range-------------------
print("#------print without those range------------------------------------------")
str="sat,hat,mat,lat,at"
all=re.findall("[^h-m]at",str) #[^h-m]at means find all whos first character is not h to m  and last tow characters are at.
for i in all:
    print(i)
#-----replace one word-------------------
print("#------replace one word------------------------------------------")
str="sat,hat,mat,lat,at"
alll=re.compile("[h]at") #[^h-m]at means replace whos first character is h  and last twe characters are at.
sub= alll.sub("food",str)
print(sub)
#----------------------match--------------------------------------------------------#it works other window
str="12345"
print("Matches:", len(re.findall("\d[{4}", str))) #print how many times it match

