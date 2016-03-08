Title: 使用ESPUSH的WIFI云透传
Date: 2015-11-08 18:07
Modified: 2015-11-08 18:00
Category: Blog
Tags: pelican, publishing
Slug: wifi_uart_trans
Authors: webmaster@espush.cn
Summary: WIFI透传指的是连接WIFI芯片的设备产生的数据，通过WIFI芯片直接传输到接收数据的上位机，而espush的WIFI云透传，可直接将数据透传到平台，本文介绍如何使用espush的WIFI云透传功能。


## 功能概览

在开始这篇教程文章前，先简要介绍WIFI云透传的效果与应用场景。所谓WIFI云透传，指的是通过串口连接WIFI芯片的设备，产生的数据透明的传输至数据的接收端，这里的WIFI芯片仅仅像是一根透明的电缆一般，承担着简单的数据转发的服务。一般的WIFI透传功能都是将数据透传至局域网的收发设备，但espush平台的WIFI透传却是直接将数据传输到云端平台，并提供第三方API与Demo App，可直接设计最终的产品应用。

WIFI云透传可应用于智能温控告警、传感器的实时数据收集领域，如有需要可与我取得联系。

## 应用步骤

espush云透传功能使用极为简单，简言之，刷好固件，打开设备控制台，右键单击设备项目选择数据透传，输入数据点击透传至设备即可。设备端的使用同样简便，在设备端执行AT+PUSHMSG=data，云端将收到数据的实时通知。或者执行AT+UARTRANS命令后，将自动进入完全透传模式，任何输出将不会再串口回显，直接透传至云端。

但考虑到初次接触WIFI物联网芯片开发的人，将详述应用步骤。

按[此处文档](http://docs.espush.cn/quickstart.html)所示，连接WIFI模组，刷入espush AT固件，刷入完成后打开串口调试工具，连接，输入AT+GMR，得到OK与espush的提示即可，如下图：

![ESP8266 espush 串口调试工具]({filename}/images/wifi_uart_trans/serial.png)

老规矩，平台[注册帐号](https://espush.cn/)（已有账号的可略过），[新增设备分类](https://espush.cn/web/apps/)（同样，已完成的可忽略），将WIFI开发板连入云平台，如下图所示：


![ESP8266 连入云平台 espush]({filename}/images/wifi_uart_trans/connect.png)

打开设备控制台，点击在线设备，此时将可以看到在线的设备列表，在其上右击鼠标，选择 **透传 通知** ，随后弹出WIFI透传与实时通知的功能窗口，如下图。

![ESP8266 WIFI云透传 espush]({filename}/images/wifi_uart_trans/step2.png)

在串口透传工具里，使用 **AT+UARTRANS** 指令，开启透传模式，设备返回透传提示符 **>** 时，透传模式开启成功。

![ESP8266 WIFI云透传 espush]({filename}/images/wifi_uart_trans/trans_serial.png)

随后任何发往串口的数据，将实时透传到espush云平台，尝试输入字符H，浏览器将会弹出权限管理提示框，使用Firefox的提示框如下图，选择允许提示框，随后的串口透传实时提示也将出现。

![ESP8266 WIFI云透传 espush]({filename}/images/wifi_uart_trans/notifi_request.png)

选择允许后的提示，不同的浏览器有不同的提示框样式，请不要在IE浏览器下使用此功能，将不可用。

![ESP8266 WIFI云透传 espush]({filename}/images/wifi_uart_trans/Notification.png)

在平台的透传设备输入框中输入需要透传的数据，点击按钮，WIFI芯片串口将会收到指定的内容，很简单但实用的应用。

![ESP8266 WIFI云透传 espush]({filename}/images/wifi_uart_trans/uart_send.png)

**退出方式** ，串口收到的连续三个 **「+」（加号）** 符号将会退出透传模式，通过手工输入是不可行的（除非你手速够快），通常而言使用工具一次发送是个不错的办法，如使用XShell或SecureCRT等串口工具，将剪贴板中的内容粘贴到串口终端即可，退出后得到 **OK** 的提示符。

## 应用原理

应用原理实则也非常简单，浏览器客户端使用WebSocket连接到服务端后，即可实时接收服务器的数据透传/上传通知，浏览器部分核心代码如下图，下面简述其技术原理（等同API）

![ESP8266 WIFI云透传 espush]({filename}/images/wifi_uart_trans/code.png)

通过Websocket接收来自设备的透传数据，需要连接到平台指定的websocket url，平台websocket URL为 wss://espush.cn/noticed/peer ，也可以使用非安全连接 ws://espush.cn/noticed/peer 。

需要提供的连接参数有4个，分别是 appid, timestamp, chipid, sign，其计算方式如上代码所示，或参考文档 http://docs.espush.cn/server.html 。

连接成功后，收到的透传数据为JSON Object结构，取字段body，并使用base64解码即可得到串口数据，字段chipid、appid标识着数据的来源。


## 手机APP

开发中，请稍候......


