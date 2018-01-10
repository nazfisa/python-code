dic={'name':'nazim','age':200}
def dict(dic):
    dictt={'name1':'asif','asif':2000}
    dic.update(dictt)
    print("Inside the value",dic)
    return
dict(dic)
print("Outside the value",dic)
