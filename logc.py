import os
import re
import gzip
import log_data_basic as ld
"""提取log方法总体"""


def savefile(savepath, nsrsbh, sid, xml):
    # nsr = savepath+'\\'+nsrsbh
    nsr = os.path.join(savepath, nsrsbh)
    if not os.path.exists(nsr):
        os.mkdir(nsr)
    filename = nsrsbh + '_' + sid + '.xml'
    path = os.path.join(nsr, filename)
    print(path)
    if not os.path.exists(path):
        f = open(path, 'w', encoding='utf-8')
        f.write(xml)
        f.close()
    pass


def catchNsrsbhAndSid(str_line, savepath):
    print("Run catchNsrsbhAndSid(str)")
    print(ld.csv_data)
    matchNsrsbh = re.search(r'(<nsrsbh>)(.*?)(</nsrsbh>)', str_line)
    matchSid = re.search(r'(<serviceId>)(.*?)(</serviceId>)', str_line)
    # matchFrse = re.search(r'(<tranSeq>)(.*?)(</tranSeq>)', str_line)
    if matchNsrsbh and matchSid:
        nsrsbh = matchNsrsbh.group(2)
        sid = matchSid.group(2)
        # frse = matchFrse.group(2)
        if not ld.sid_is_need(sid):
            print("*%s* is not need" % sid)
            print("%s type is %s " % (sid, type(sid)))
            return
        else:
            print("%s is need" % sid)
        if not ld.nsr_is_need(nsrsbh):
            print("*%s* is not need nsrsbh" % nsrsbh)
            return
        if re.search(r'<returnState><returnCode>00000000</returnCode><returnMessage>处理成功！</returnMessage></returnState>', str_line):
            xml = simplexml(str_line)
            savefile(savepath, nsrsbh, sid, xml)


def catchxml(str1):
    if str1.startswith('<?xml'):
        print(str1)
        return True
    return False


def simplexml(str):
    xml = str.split('，此')[0]
    # xml = str
    return xml


def read_gz_file(path):
    """读取压缩gz log，迭代读取"""
    if os.path.exists(path):
        with gzip.open(path, 'r') as pf:
            for line in pf:
                yield line
    else:
        print('the path [{}] is not exist!'.format(path))


def readLog(pathname, savepath):
    # fo = open(pathname,"r", encoding="utf-8", errors="ignore")
    fo = read_gz_file(pathname)
    app_flag = False
    str_tmp = ''
    if getattr(fo, '__iter__', None):
        for line in fo:
            str_line = str(line, encoding='utf-8')
            if catchxml(str_line):
                if len(str_line) < 50:
                    app_flag = True
                    str_tmp += str_line
                else:
                    catchNsrsbhAndSid(simplexml(str_line), savepath)
            if app_flag:
                str_tmp += str_line
                if re.search(r'</tiripPackage>', str_tmp):
                    app_flag = False
                    catchNsrsbhAndSid(str_tmp, savepath)
    pass


def catchFile(pathname, savepath):
    """
    :param pathname: log文件保存文件夹路径
    :param savepath: 提取xml保存路径
    :return: 无
    """
    list1 = os.listdir(pathname)
    for i in list1:
        if i.endswith(".log.gz") and i.find('ycsyth') > -1:
            path = os.path.join(pathname, i)
            print(path)
            readLog(path, savepath)


