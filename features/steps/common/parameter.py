# coding=utf-8
'''
@author: Angie

@desc: 参数签名及拼接

'''
import md5
import urllib



def parameters(param):
    """

    :param param:请求参数
    :return:拼接好的参数串
    """
    paramk = param.keys()  # 获取键，即参数名
    paramk.sort()  # 按照键值字典序由小到大排列
    params = ""
    for i in paramk:
        kvalue = param.get(i)  # 获取键值
        params = '%s%s=%s' % (params, i, kvalue)  # 按照key1=value1key2=values2方式拼接，没有分割符
    sign = paramSign(params)  # 调用签名方法
    param['sign'] = sign  # 加入参数sign
    return param


def paramSign(params):
    """

    :param params:按照key1=value1key2=values2方式拼接的参数串
    :return:返回最终的签名值sign
    """
    m1 = md5.new()
    m1.update(params)
    sign1 = m1.hexdigest()  # 首次对拼接结果取一次md5
    sign2 = "%s%s" % (sign1, 'a')  # 将md5结果尾部拼接渠道的私钥内容
    m2 = md5.new()
    m2.update(sign2)
    sign = m2.hexdigest()  # 对拼接结果再做一次md5获得最终签名
    return sign  # 返回最终的签名值
