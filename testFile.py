
try:
    f = open("D:\\Git\\python\\test1.txt", 'r')
    str1 = f.read()
    print("文件内容是：" + str1)
finally:
    if f:
        f.close()
