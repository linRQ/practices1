import os

testpath = 'D:\datacatch\lrq\\2.1a'

# 获取指定路径下的 全部log
def catchFile(pathname):
    list = os.listdir(pathname)
    for i in range(0, len(list)):
        path = os.path.join(pathname, list[i])
        if(path.endswith(".log") and path.find('ycs')>-1):
            print(path)
    pass

# catchFile(testpath)

import re
def catchNsrsbhAndSid(str):
    print("Run catchNsrsbhAndSid(str)")
    matchNsrsbh = re.search(r'(<nsrsbh>)(.*?)(</nsrsbh>)', str)
    matchSid = re.search(r'(<serviceId>)(.*?)(</serviceId>)', str)
    if(matchNsrsbh):
        print(matchNsrsbh.group(2))
    if(matchSid):
        print(matchSid.group(2))
    pass

def catchxml(str):
    if(str.startswith('<?xml')):
        return True
    return False

def readLog(pathname):
    fo = open(pathname,"r", encoding="utf-8", errors="ignore")
    for line in fo:
        if(catchxml(line)):
            # print(line)
            catchNsrsbhAndSid(line)
    pass

# readLog("D:\datacatch\lrq\\2.1a\ycs.2017-10-25.0.log")


def creatdir(pathname):
    os.mkdir(pathname)
    pass


def createfile(savepath, nsrsbh, sid, xml):
    pathname = savepath + nsrsbh+'_'+sid+'.xml'
    f = open(pathname,'w')
    f.write(xml)
    f.close()
    pass

savepath = 'D:\datacatch\\result\\'
# createfile(savepath, "abc","efg","xmlfile")

def simplexml(str):
    rindex = str.rindex('，')
    return str[0:rindex]

xml = '<?xml version="1.0" encoding="UTF-8"?><tiripPackage version="1" xsi:type="tiripPackage" xmlns:xsi="http://www.w3.org/2001/XMLSchema" xmlns="http://www.chinatax.gov.cn/dataspec/"><appSessionId>07475cf7c069419eba083733076cd3d9</appSessionId><sessionId>GD_GS_6c32162ae0184382a688dc1ae6543a2e</sessionId><service><serviceId>SJJZ.TY.DZSWJ.nsrdlyz</serviceId><clientNo></clientNo><tranSeq>frse99999999999000002017102500041688</tranSeq><repeatFlag>0</repeatFlag><tranReqDate>2017-10-25</tranReqDate><areaCode>44</areaCode></service><identity><application><applicationId>frse</applicationId><supplier>frse</supplier><version>1</version><authenticateType>2</authenticateType><cert></cert><password></password></application><customer><customerId>91441900MA4WBLER0W</customerId><authenticateType>2</authenticateType><password></password><cert></cert><nsrsbh>91441900MA4WBLER0W</nsrsbh><djxh></djxh><gdslxdm>1</gdslxdm></customer></identity><routerSession></routerSession><signData><signType></signType><signSource></signSource><signValue></signValue></signData><contentControl></contentControl><businessContent><subPackage><id>1</id><content><![CDATA[<?xml version="1.0" encoding="UTF-8"?><taxML xmlns="http://www.chinatax.gov.cn/dataspec/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><rtnCode>0000</rtnCode><rtnMsg>登录成功！</rtnMsg><body>&lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;taxML xmlns="http://www.chinatax.gov.cn/dataspec/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"&gt;&lt;clientNo&gt;NSA4WBLER0W&lt;/clientNo&gt;&lt;yhxx&gt;&lt;nc&gt;&lt;/nc&gt;&lt;sjh&gt;15279544856&lt;/sjh&gt;&lt;smxxid&gt;680752E1ACCF4D9F8C43CFA17FED81ED&lt;/smxxid&gt;&lt;xm&gt;彭国良&lt;/xm&gt;&lt;yhid&gt;5c3521fd0cff4f39a77e033283e5c6b9&lt;/yhid&gt;&lt;yhm&gt;农鲜乐&lt;/yhm&gt;&lt;yx&gt;&lt;/yx&gt;&lt;zcrq&gt;Wed Oct 25 00:03:34 CST 2017&lt;/zcrq&gt;&lt;zjhm&gt;362203198110213534&lt;/zjhm&gt;&lt;zz&gt;&lt;/zz&gt;&lt;/yhxx&gt;&lt;nsrs&gt;&lt;nsr&gt;&lt;dsNsrmc&gt;东莞市农鲜乐生态农业有限公司&lt;/dsNsrmc&gt;&lt;dsnsrsbh&gt;91441900MA4WBLER0W&lt;/dsnsrsbh&gt;&lt;dszdjxh&gt;10124419010000276100&lt;/dszdjxh&gt;&lt;gsnsrsbh&gt;91441900MA4WBLER0W&lt;/gsnsrsbh&gt;&lt;gszdjxh&gt;10114419010000256312&lt;/gszdjxh&gt;&lt;nsrmc&gt;东莞市农鲜乐生态农业有限公司&lt;/nsrmc&gt;&lt;nsrztid&gt;4B3BA5F121E6012AE053C0A814186865&lt;/nsrztid&gt;&lt;qybdid&gt;1A1A2DD542384F42B9B617EA22DC6397&lt;/qybdid&gt;&lt;shxydm&gt;91441900MA4WBLER0W&lt;/shxydm&gt;&lt;ssdabh&gt;91441900MA4WBLER0W&lt;/ssdabh&gt;&lt;yhid&gt;5c3521fd0cff4f39a77e033283e5c6b9&lt;/yhid&gt;&lt;yhsfdm&gt;01&lt;/yhsfdm&gt;&lt;yhsfmc&gt;法定代表人&lt;/yhsfmc&gt;&lt;zjjgbz&gt;N&lt;/zjjgbz&gt;&lt;zzNsrmc&gt;东莞市农鲜乐生态农业有限公司&lt;/zzNsrmc&gt;&lt;zzNsrztid&gt;4B3BA5F121E6012AE053C0A814186865&lt;/zzNsrztid&gt;&lt;tybz&gt;N&lt;/tybz&gt;&lt;/nsr&gt;&lt;/nsrs&gt;&lt;/taxML&gt;</body></taxML>]]></content></subPackage></businessContent><returnState><returnCode>00000000</returnCode><returnMessage>处理成功！</returnMessage></returnState></tiripPackage>，此次调用耗时：0.288秒'

# print(simplexml(xml))
def savefile(savepath, nsrsbh, sid ,xml):
    # nsr = savepath+'\\'+nsrsbh
    nsr = os.path.join(savepath, nsrsbh)
    if(not os.path.exists(nsr)):
        os.mkdir(nsr)
    filename = nsrsbh + '_' + sid +'.xml'
    path = os.path.join(nsr, filename)
    print(path)
    if(not os.path.exists(path)):
        f = open(filename, 'w')
        f.write(xml)
        f.close()
    pass

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is ", result)
    finally:
        print("executing finally clause")

class MyClass:
    def __int__(self):
        self.data = []
        print("call MyClass __init__")

    def prt(self):
        print(self)
        print(self.__class__)

# x = MyClass()
# print(x)
# x.prt()

class people:
    name = ''
    age = 0
    __weight = 0
    def __int__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说：我 %d 岁。"% (self.name, self.age))


def createGenerator():
    mylist = range(4)
    for i in mylist:
        yield i*i

mygenerator = createGenerator()
print(mygenerator)
for i in mygenerator:
    print(i)

def test():
    print("test print1")
    return
    print("test print2")


def init(data):
    data['first'] = {}
    data['second'] = {}
    data['third'] = {}


def lookup(data, label, name):
    return data[label].get(name)


def store(data, full_name):
    names = full_name.split()
    if len(names) == 2:
        names.insert(1, '')
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


def changenum(num):
    num += 1
    print(num)


n = 10
changenum(n)
print(n)

print(10*"**")


def add(t, y):
    return t+y


def mul(t, y):
    return t*y

l1 = [1, 2, 3, 4]
l2 = [6, 7, 8, 9]

res = map(add, l1, l2)
for i in res:
    print(i)

from functools import reduce
res1 = reduce(mul, l1)
print(res1)

class Sercretive:

    def __inaccessible(self):
        print("Bet you can't see me ......")

    def accessible(self):
        print("You can see me ......")


class Bird:
    def __int__(self):
        self.hungry = True

    def eat(self):
        if(self.hungry):
            print("Aaaah...")
            self.hungry = False
        else:
            print("No, thanks!")


class SongBird(Bird):
    def __init__(self):
        super.__init__()
        self.sound = 'Squawk!'

    def sing(self):
        print(self.sound)


print("test log data basic")
import log_data_basic as ld

xmlstr = '<?xml version="1.0" encoding="UTF-8"?><tiripPackage version="1" xsi:type="tiripPackage" xmlns:xsi="http://www.' \
         'w3.org/2001/XMLSchema" xmlns="http://www.chinatax.gov.cn/dataspec/"><appSessionId>dce1a26f89344975bcfdabc36df7' \
         '8a4e</appSessionId><sessionId>GD_GS_b94076acf442446a9e01fa83636b3afb</sessionId><service>' \
         '<serviceId>SJJZ.TY.DZSWJ.nsrdlyz</serviceId><clientNo></clientNo><tranSeq>frse99999999999000002018020100010137</tranSeq><repeatFlag' \
         '>0</repeatFlag><tranReqDate>2018-02-01</tranReqDate><areaCode>44</areaCode></service><identity><application><' \
         'applicationId>frse</applicationId><supplier>frse</supplier><version>1</version><authenticateType>2</authentica' \
         'teType><cert></cert><password></password></application><customer><customerId>35052419860920800000</customerId><a' \
         'uthenticateType>2</authenticateType><password></password><cert></cert><nsrsbh>35052419860920800000</nsrsbh><djxh' \
         '></djxh><gdslxdm>1</gdslxdm></customer></identity><routerSession></routerSession><signData><signType></signTy' \
         'pe><signSource></signSource><signValue></signValue></signData><contentControl></contentControl><businessContent' \
         '><subPackage><id>1</id><content><![CDATA[<?xml version="1.0" encoding="UTF-8"?><taxML xmlns="http://www.chinat' \
         'ax.gov.cn/dataspec/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><rtnCode>0000</rtnCode><rtnMsg>' \
         '登录成功！</rtnMsg><body>&lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;taxML xmlns="http://www.chinatax.gov' \
         '.cn/dataspec/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"&gt;&lt;clientNo&gt;NS867743723&lt;/clien' \
         'tNo&gt;&lt;yhxx&gt;&lt;nc&gt;&lt;/nc&gt;&lt;sjh&gt;13714287045&lt;/sjh&gt;&lt;smxxid&gt;836BB766E9BC47D3AE53A' \
         '0D9D783FC5B&lt;/smxxid&gt;&lt;xm&gt;肖辉军&lt;/xm&gt;&lt;yhid&gt;c748177496d94ad9932cec22d8b1af49&lt;/yhid&gt' \
         ';&lt;yhm&gt;宗生包装2008&lt;/yhm&gt;&lt;yx&gt;&lt;/yx&gt;&lt;zcrq&gt;Thu Feb 01 08:35:59 CST 2018&lt;/zcrq&gt' \
         ';&lt;zjhm&gt;430421198301072674&lt;/zjhm&gt;&lt;zjlx&gt;201&lt;/zjlx&gt;&lt;zz&gt;&lt;/zz&gt;&lt;/yhxx&gt;&lt' \
         ';nsrs&gt;&lt;nsr&gt;&lt;dsNsrmc&gt;东莞市宗生包装制品有限公司&lt;/dsNsrmc&gt;&lt;dsnsrsbh&gt;441900086774372&l'

matchNsrsbh = re.search(r'(<nsrsbh>)(.*?)(</nsrsbh>)', xmlstr)
matchSid = re.search(r'(<serviceId>)(.*?)(</serviceId>)', xmlstr)
matchFrse = re.search(r'(<tranSeq>)(.*?)(</tranSeq>)', xmlstr)
nsrsbh = matchNsrsbh.group(2)
sid = matchSid.group(2)
frse = matchFrse.group(2)

print("*********************************")
for i in ld.sid_list:
    if sid == i:
        print("%s is in sid_list"% sid)
print("*********************************")
if ld.sid_is_need(sid):
    print("%s is need sid"% sid)
print("*********************************")



if ld.sid_is_need(sid):
    print("%s is need" % sid)
    print(type(sid))
else:
    print("%s is not need" % sid)
    print("%s type is %s " % (sid, type(sid)))

if not ld.nsr_is_need(nsrsbh):
    print("%s is not need"% nsrsbh)
else:
    print("%s is need nsrsbh"% nsrsbh)

print(type(ld.nsr_list))
if nsrsbh in ld.nsr_list:
    print("nsrsbh %s in ld.nsr_list" % nsrsbh)
else:
    print(len(ld.nsr_list))
    print(len(ld.nsr_frse_list))
    print(ld.nsr_frse_list[1][0])


def catchFile1(pathname, savepath):
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

