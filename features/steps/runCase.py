# coding=utf-8

'''
@author: Angie

@desc: 执行测试用例

'''
from common import parameter as P
import requests
from behave import *
import json


@Given(u'请求类型为{type},前置条件为{beforeStep}')
def step_impl(context,type,beforeStep):
    context.requestType = type
    if beforeStep != 'None':
        context.theValue = str(eval(beforeStep))

@When(u'接口域名为{host},地址为{url},参数为{parameters}')
def step_impl(context,host,url,parameters):
    theValue = 'dynamicValues'
    dictParameters = eval(parameters)
    if theValue in dictParameters.values():
        newParams = {v:k for k,v in dictParameters.items()}
        dictParameters[str(newParams[theValue])] = context.theValue
    params = P.parameters(dictParameters)
    if host == 'home':
        context.url = context.baseHUrl + url
    else:
        context.url = context.baseEUrl + url
    context.parameters = params
    print (context.parameters)

@When(u'后置条件为{afterStep}')
def step_impl(context,afterStep):
    if afterStep != 'None':
        context.theValue = str(eval(afterStep))

@Then(u'接口响应code为{code},message为{message}')
def step_impl(context,code,message):
    if context.requestType =='get':
        r = requests.get(url=context.url,params=context.parameters)
    elif context.requestType == 'post':
        r = requests.post(url=context.url,data=context.parameters)
    rs = json.loads(r.text)
    assert rs.get('code') == int(code)
    assert rs.get('message') == message

