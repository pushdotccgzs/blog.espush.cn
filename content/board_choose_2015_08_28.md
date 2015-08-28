Title: ESP8266开发入门指引之开发板选择
Date: 2015-08-28 21:31
Modified: 2015-08-28 21:31
Category: Blog
Tags: ESP8266
Slug: board_choose
Authors: espush
Summary: 自乐鑫推出其串口WIFI芯片ESP8266以来，有大量的厂家为其定制了完整的开发板，使用不同的模组型号，从ESP8266-01 至 ESP8266-12都有，在芯片基础上定制自己不同的电路。有方便开发者的如内置电源模块的，有内置串口芯片的，也有直接将大量外部模块如继电器、温湿度传感器一起集成的模块。可谓玲琅满目，又该如何选择。

按官方的介绍：

> ESP8266 是一款高度集成的芯片，该芯片专门针对无线连接的需求而开发，是一个完整且自成系统的 WiFi 网络解决方案。

官方只生成核心芯片模组，并不直接负责外部电路，这就像Intel只生产CPU与样机，你要是想买电脑仍然得找联想或戴尔。

不同的厂家使用不同的模组型号，从ESP8266-01 至 ESP8266-12都有，在芯片基础上定制自己不同的电路。有方便开发者的如内置电源模块的，有内置串口芯片的，也有直接将大量外部模块如继电器、温湿度传感器一起集成的模块。可谓玲琅满目，让人顿生选择恐惧。

![该选哪一个]({filename}/images/board_choose.png)

关于使用什么版本的模组芯片，安信可科技有一组图片详细的展示了各模块，并对齐封装工艺、天线设计等做了简单评估，参考如此：[ESP8266系列模块选型指南](http://www.ai-thinker.com/forum.php?mod=viewthread&tid=23)，此处贴出各款特点：

* ESP-01 PCB 天线，经过匹配，距离做到空旷400米左右，简单易用
* ESP-02 贴片封装，适合体积限制，天线可以用 IPX 头引出壳体
* ESP-03 贴片封装，内置陶瓷天线工艺。所有可用 IO 引出
* ESP-04 贴片封装，客户可自定义天线类型，灵活设计  所有可用IO 引出
* ESP-05 贴片封装，只引出串口和 RST 脚，体积小，天线可外置。
* ESP-06 底贴工艺，所有 IO 口引出， 带金属屏蔽可， 可过 FCC CE  认证  推荐使用
* ESP-07 半孔贴片工艺，所有 IO 口引出，带金属屏蔽罩，可过 FCC CE认证，可外接 IPX 天线，也可用内置陶瓷天线。
* ESP-08 同 ESP-07，不同在于天线形式客户可自己定义
* ESP-09 超小体积封装，只有 10*10 毫米，四层板工艺！1M 字节 FLASH 阻抗经过匹配，底贴工艺，适合对体积严格限制的产品！
* ESP-10 贴片接口，窄体设计，10 毫米宽。适合做灯带控制器
* ESP-11 贴片接口，陶瓷天线，小体积。

而关于应该选择什么样的开发板，可简单参考下述建议：

如果你熟悉使用Lua编程语言或者你患上了指针恐惧症（C恐惧症），可以考虑使用NodeMCU开发板，[NodeMCU](http://nodemcu.com/index_cn.html)提供了一个使用脚本进行嵌入式编程的环境，比Arduino还要简单的语法，且espush提供对NodeMCU的适配，淘宝搜索NodeMCU即可。

如果你需要使用espush提供的在线升级功能（或官方AT固件的在线升级），则需要至少1MB的Flash空间，可自行焊接flash，亦可直接购买大容量的，如ESP8266-12E。

如果你是新手入门开发，不知道如何连接设置串口，也不知道如何使用何种电源，则可以使用大多数的集成开发版，如安信可提供的全功能测试版等。

espush.cn开发使用的是安信可公司的全IO引出板，为方便开发，引出了全部的IO针脚，并将固件升级所用的串口单独置出，配置了方便刷写固件的短接帽，淘宝搜索全IO引出即可，如下图所示：

![全IO引出板]({filename}/images/yellow_board.jpg)

放个结论吧，如果你实在不知道你要买什么但又想入坑的，买NodeMCU提供的吧，因为没人付我广告费，就不给链接了。