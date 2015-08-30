Title: 十分钟的智能插座
Date: 2015-08-30 11:45
Modified: 2015-08-30 11:45
Category: Blog
Tags: ESP8266
Slug: ten_minute_socket
Authors: espush
Summary: 使用espush云平台，外加一个继电器，再买个插座，利用espush自带的手机app就可以实时远控啦，构成了最简单的智能插座，麻雀虽小可五脏俱全。至于十分钟内是否能搞定，手快有手慢无啦。

教程开始前，先放一段录像：

<embed src="http://www.tudou.com/v/XjgzHzcjWAI/&bid=05&rpid=341255089&resourceId=341255089_05_05_99/v.swf" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" wmode="opaque" width="480" height="400"></embed>

电路比较乱的一个原因是，电源模块没有用上，所以依然需要从适配器中给ESP8266供电，就像《国产零零漆》中那伟大的太阳能手电发明一样，还是得从外部插座取电。不过如果你愿意，配上一个电源模块就可以随时取代现有设计了。

##准备工作##

- ESP8266全IO口引出板，或其他任意ESP8266开发板均可，需要将此开发板刷espush.cn的固件，参考[这里]({filename}/rom_flash_2015_08_29.md)，并且需要接入ESPUSH云平台，参考[这里]({filename}/connect_espush_2015_08_29.md)
- 继电器一枚，这里是  [1路继电器模块带光耦隔离 支持高低电平触发 5V(C7B1)](https://item.taobao.com/item.htm?id=43242402152)


##电路连接##

下图是继电器的电路连接方式：

![继电器 电路]({filename}/images/jdq_dl.png)

只需要将继电器的信号触发端接到ESP8266开发板的某个IO口上，我这里取12口，将继电器的DC+接入开发板的VCC，DC-接入开发板的GND，将插座中间的火线剪开，置于继电器COM口与NO口，将继电器的短接帽接在H极（高电平触发）上，即可！

Update: 发现有好多童鞋都在问为啥 GPIO9和GPIO10为啥不行，为啥error，偶也不知，暂时先将GPIO9与10从IO端口列表里去掉了，[点击重新下载APK](https://espush.cn/web/down_apk/)就可以了。
