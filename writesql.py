import os
# import re
import MySQLdb

def writesql(nsrsbh):
    db = MySQLdb.connect("localhost", "root", "root", "foresee")
    cursor = db.cursor()
    sql = 'insert into logrecord(nsrsbh) values ("%s")' % (nsrsbh)
    cursor.execute(sql)


def writesqldetail(nsrsbh ,sid):
    db = MySQLdb.connect("localhost", "root", "root", "foresee")
    cursor = db.cursor()
    dict = {'SJJZ.TY.DZSWJ.nsrdlyz': 'nsrdlyz', 'SJJZ.SB.cx.cwbaxxCx': 'cwbaxxcx', 'C00.TY.YBSB.nsrsfxxcx': 'nsrsfxxcx', \
            'Fxsw.FP.cx.YbjcJxXxFpXx': 'ybjcjxxxfpxx', 'ETax.SB.SbSubmit3.91061001059': 'etax'}
    if (sid in dict):
        v = dict[sid]
        sql2 = 'update logrecord set %s="1" WHERE nsrsbh = "%s"' % (v, nsrsbh)
        cursor.execute(sql2)

def readLog(filename):
    a = filename.split('_')
    nsrsbh = a[0]
    sid = a[1][0:-4]
    # print(nsrsbh+" "+sid)
    writesqldetail(nsrsbh,sid)
    pass

def catchFile(pathname):
    list1 = os.listdir(pathname)
    for i in range(0, len(list1)):
        path = os.path.join(pathname, list1[i])
        writesql(list1[i])
        print(path)
        if(os.path.isfile(path)):
            continue
        listfile1 = os.listdir(path)
        for j in range(0, len(listfile1)):
            readLog(listfile1[j])
    pass


def main():
    # writesql('abc', 'efg')
    catchFile(r'D:\datacatch\cal')
    pass

main()