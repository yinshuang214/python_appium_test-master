import os

#写文件
def write_data(f, method='w+', data=""):
    if not os.path.isfile(f):
        print('文件不存在，写入数据失败')
    else:
        with open(f, method, encoding="utf-8") as fs:
            fs.write(data + "\n")

#创建文件
def mkdir_file(f, method='w+'):
    if not os.path.isfile(f):
        with open(f, method, encoding="utf-8") as fs:
            print("创建文件%s成功" % f)
            pass
    else:
        print("%s文件已经存在，创建失败" % f)
        pass

#删除文件
def remove_file(f):
    if os.path.isfile(f):
        os.remove(f)
    else:
        print("%s文件不存在，无法删除" % f)

#测试文件操作，只能在当前路径下
if __name__=="__main__":
    #mkdir_file("test.txt")
    #write_data("test.txt",data="lalalalla")
    remove_file("test.txt")

