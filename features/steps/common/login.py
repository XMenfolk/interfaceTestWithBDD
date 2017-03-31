# coding=utf-8
'''
@author: Angie

@desc: 登录接口

'''
import requests
import doMysql
import time,json
import sys

def homeLogin(mobile):
    getCaptchaUrl = 'http://xxx/getCaptcha'
    loginUrl = 'http://xxx/login'
    getCaptchaParams = {'appkey':'51000031',
                        'timestamp':'2017-03-06 10:07:23',
                        'mobile':mobile,
                        'sig':	'2ff1d93ac8c1db0ad1a73f3a97c827'}

    loginParams = {"appkey":"51000031",
                   "timestamp":"2017-03-06 10:07:52",
                   "openId":"",
                   "mobile":mobile,
                   "code":"439"}
    getCaptcha = requests.get(getCaptchaUrl,getCaptchaParams)
    time.sleep(5)
    loginParams['code'] = doMysql.mobileCode(mobile)
    loginRequest = requests.post(loginUrl,loginParams)
    try:
        token = json.loads(loginRequest.text).get('data')
    except Exception as e:
        print (u'登录接口异常'),e

    if token == None:
        print (u'登录失败')
        sys.exit()

    return token

if __name__ == '__main__':
    homeLogin(mobile)