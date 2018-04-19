import csv
'''log提取数据配置以及相关方法'''


# log file path
pathname = r'D:\datacatch\20180326\data\logs'
# r"D:\datacatch\lrq"
# r'D:\datacatch\20180326\app1ab\data\logs'
# r'D:\datacatch\20180326\data\logs'
# path of result
savepath = 'D:\datacatch\cal'

# 所需的ServiceId列表
csv_data = csv.reader(open(r"testdata\needserviceid.csv"))
sid_list = []
for l in csv_data:
    for ele in l:
        sid_list.append(ele+'')



def sid_is_need(sid, data=sid_list):
    """
    :param sid: 需要判断的服务ID
    :param data: 需要的全部服务ID
    :return: sid存在于data中返回True，否则返回False
    """
    if sid in data:
        return True
    else:
        return False


# 申报成功的客户纳税人识别号
nsr_frse_data = csv.reader(open(r"testdata\nsrsbh4.csv"))
nsr_frse_list = []
for i in nsr_frse_data:
    nsr_frse_list.append(i)
nsr_list = []
for i in nsr_frse_list:
    nsr_list.append(i[0])


def nsr_frse_is_need(nsr_frse, data=nsr_frse_list):
    '''判断纳税人识别号+流水号是否存在
        :var nsr_frse 传入列表【nsrsbh_str, frse_str】
        :return 返回判断结果布尔值
    '''
    if nsr_frse in data:
        return True
    else:
        return False


def nsr_is_need(nsr, data=nsr_list):
    """
    判断纳税人是否是需要的！
    :param nsr: 纳税人识别号
    :param data: 纳税人识别号列表
    :return: 存在列表中返回True，不存在的返回False
    """
    if nsr in data:
        return True
    else:
        return False
