import os
import os.path
import gzip


def read_gz_file(path):
    """gzip读取得到的返回值type 为 bytes， 可使用 str(b, encoding='utf-8')转换为str"""
    if os.path.exists(path):
        with gzip.open(path, 'r') as pf:
            for line in pf:
                yield line
    else:
        print('the path [{}] is not exist!'.format(path))


# con = read_gz_file(r'E:\Practices\Python\practices1\testdata\ycsyth.2018-02-01.0.log.gz')
# if getattr(con, '__iter__', None):
#     num = 0
#     for line in con:
#         if num < 10:
#             num += 1
#             print(line)


import csv
# 所需的ServiceId列表
csv_data = csv.reader(open(r"testdata\needserviceid.csv"))


def sid_is_need(sid, data=csv_data):
    for i in data:
        if sid in i:
            return True
    return False


print(sid_is_need("abc"))


def test_pass(num):
    for i in range(num):
        print(i)
        if i > 3:
            return


test_pass(10)