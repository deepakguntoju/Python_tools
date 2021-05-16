import hashlib as hash
#s=input("Enter_String:	")

with open("wordlist.txt","r") as file:
    m=file.readlines()
x=input("Enter hash")
for _ in m:
    res=hash.md5(_.strip().encode())
    if (res.hexdigest()==x):
        print("success"+res.hexdigest()+"   :"+_+"\n")
        break


print("Finshed")
#res=hash.md5(s.encode())
#print("MD5: ",res.hexdigest().upper())