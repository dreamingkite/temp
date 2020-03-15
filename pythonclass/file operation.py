import argparse
import pathlib
import os
import pwd
import grp
import datetime



def _get_file_name_list(path=None):
    rst = []
    if path == None:
        path = pathlib.Path(".")
    path = pathlib.Path(path)
    rst.append(".")
    rst.append("..")

    for file in path.iterdir():
        rst.append(file.name)
    rst = sorted(rst)
    return rst

# for x in _get_file_name_list("/home/python"):
#     print(x)

# print(_get_file_name_list("/home/python"))

def _get_file_stat_info(path=None ,human_readable=False)  :  # path不是一个Path对象，而是path的字符串
    rst = []
    path_stat = os.stat(path)

    def _tran_st_mode():
        st_mode = str(bin(path_stat.st_mode))[-9:]
        pri_str = "rwx " *3
        return "".join(["-" if value == "0" else pri_str[index] for index ,value in enumerate(st_mode)])

    def _define_file_type(path):
        path = pathlib.Path(path)
        if path.is_dir():
            return "d"
        elif path.is_file():
            return "-"
        else:
            return "c"

    def _tran_st_nlink():
        return path_stat.st_nlink

    def _tran_user():
        return pwd.getpwuid(path_stat.st_uid)[0]

    def _tran_group():
        return grp.getgrgid(path_stat.st_gid)[0]

    def _tran_size():
        if not human_readable:
            return str(path_stat.st_size)
        else:
            if 0 < path_stat.st_size < 1000:
                return path_stat.st_size
            elif 1000 <= path_stat.st_size < 1000000:
                return str(path_stat.st_size /1000)[:3 ] +"K" if not str(path_stat.st_size /1000)[:3].endswith \
                    (".") else str(path_stat.st_size /1000)[:2 ] +"K"
            elif 1000000 <= path_stat.st_size < 1000000000:
                return str(path_stat.st_size /1000000)[:3 ] +"M" if not str(path_stat.st_size /1000000)[:3].endswith \
                    (".") else str(path_stat.st_size /1000000)[:2 ] +"M"
            else:
                return "big"

    def _tran_time():
        return "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.fromtimestamp(path_stat.st_atime))

    return [_define_file_type(path ) +_tran_st_mode() ,_tran_st_nlink() ,_tran_user() ,_tran_group() ,_tran_size()
            ,_tran_time()]



# a = _get_file_stat_info("/home/python/python_project/exercise/Untitled.ipynb",human_readable=True)

# print(len(a))
# 获取命令行的信息


ls_file = argparse.ArgumentParser(add_help=False)

ls_file.add_argument('-a' ,'--all' ,action='store_true' ,help="show all")
ls_file.add_argument('-h' ,action='store_true' ,help="show in human readable format")
ls_file.add_argument('-l' ,action='store_true' ,help='show in list')
ls_file.add_argument('dest_path')

# ls_file.print_help()
var_list = ["-a" ,'-h' ,'-l' ,"/etc"]
a = ls_file.parse_args(var_list)
# print(a)


# print("*"*30)

def show_files(path="." ,* ,all=False ,h=False ,l=False):
    if not all:
        dest_list = list(filter(lambda x :not x.startswith(".") ,_get_file_name_list(path)))
    else:
        dest_list = _get_file_name_list(path)

    max_file_name_length = len(max(dest_list ,key=lambda x :len(x)) ) +3



    if not l:
        # print(*dest_list,sep="\t")
        print(("{:<{width}} " *len(dest_list)).format(*dest_list ,width=max_file_name_length))
        return
    else:
        files_info_list = []
        for file_name in dest_list:
            files_info_list.append(_get_file_stat_info(path=path +"/ " +file_name ,human_readable=h))

        files_info_length = []
        for index in range(6):
            files_info_length.append(len(str(max(files_info_list ,key=lambda x :len(str(x[index])))[index]) ) +2)

        for line in range(len(files_info_list)):
            for index ,value in enumerate(files_info_list[line]):
                print("{:<{length}}".format(value ,length=files_info_length[index]) ,end="")
            else:
                print(dest_list[line])

show_files("/home/python" ,all=True ,l=True ,h=True)
