# coding=utf-8
'''
@author: Angie

@desc: 统一配置

'''
import behave2cucumber
import json,datetime
from steps.common import login,tools
import sys

def before_all(context):
    context.baseEUrl = 'http://test.xx.cn'
    context.baseHUrl = 'http://test.xxx.cn'
    context.mobile = ''
    # context.token = str(login.homeLogin(context.mobile))
    # if context.token == None:
    #     print (u'登录失败')
    #     sys.exit()
    context.bookTime = str(datetime.date.today()+datetime.timedelta(days=1)) + ' ' + '08:00:00'
    context.timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def after_all(context):

    file = r'.\reports\jsonDumps\testResult.json'
    with open(file) as behave_json:
        cucumberJson = behave2cucumber.convert(json.load(behave_json))
        jsonStr = json.dumps(cucumberJson)

    jsonReport = open(r'.\reports\jsonReports\jsonReport.json','w')
    jsonReport.write(jsonStr)
    jsonReport.close()