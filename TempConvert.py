# TempConvert.py
Tempstr = input("请输入带有符号的温度值例如40C/40F：")
if Tempstr[-1] in ['F' , 'f']:
   #字符串最后一个字符为F或f
   C = (eval(Tempstr[0:-1]) - 32)/1.8
   print("转换后的温度是{:.2f}C".format(C))
elif Tempstr[-1] in ['C' , 'c']:
   #字符串最后一个字符为C或c
   F = 1.8*eval(Tempstr[0:-1]) + 32
   print("转换后的温度是{:.2f}F".format(F))
else :
   #字符串最后一个字符为其他
   print("输入格式错误")
