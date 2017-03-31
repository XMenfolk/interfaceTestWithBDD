功能: 接口测试
  @autoTest
  场景大纲: <caseName>
    假如 请求类型为<type>,前置条件为<beforeStep>
    当 接口域名为<host>,地址为<url>,参数为<parameters>
    而且 后置条件为<afterStep>
    那么 接口响应code为<code>,message为<message>


   例子: getOrderTips
    |caseName      |beforeStep       |afterStep|type |host|url                           |parameters                    |code             |message|
    |预约时间早于9:00|login.homeLogin()|None     |post |exam|/order/create|{'timestamp':context.timestamp,'token':'dynamicValues','mobile':context.mobile,'bookTime':context.bookTime,'customerId':'CH0310000225'}|5001|营业时间范围:09:00-21:00|