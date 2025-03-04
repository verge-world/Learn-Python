first_name = "Mark"
last_name = "Two"
messag = f"\n\t   {first_name} {last_name}   "
length = len(messag)
#len意思是显示字符串长度
print(length)
message = messag.lstrip()
length = len(message)
print(message,length)
message = messag.rstrip()
length = len(message)
print(message,length)
message = messag.strip()
length = len(message)
print(message,length)