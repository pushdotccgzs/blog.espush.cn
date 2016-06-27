Title: ESPUSH新一键烧录工具
Date: 2016-06-27 12:27:53
Modified: 2016-06-27 12:27:57
Category: Blog
Tags: ESP8266
Slug: new_onekey_rom_flash
Authors: espush
Summary: ESPUSH开发板已上线，同时使用一键烧录工具更方便，推荐使用。


- 一键刷写工具已经没有多少可说的了， **比把大象关进冰箱** 还要简单，把开发板接入机器，驱动装好后设备管理器应该是这样的：


![ESPUSH 蘑菇云 开发板 设备管理器]({filename}/images/onekeyflasher/devmanager.png)


- 下载一键烧录工具，主页点击下载，一键烧录 即可，完成后打开，长这样：


![ESPUSH 蘑菇云 开发板 新一键烧录工具]({filename}/images/onekeyflasher/firstimage.png)


- 选择正确的COM口，我这里COM3，固件类型选择 专属开发固件。烧录拨码开关打至GND，按RESET按钮，点击烧录。完成！

![ESPUSH 蘑菇云 开发板 烧录完成]({filename}/images/onekeyflasher/flash_complete.png)

其中，APPID与APPKEY可填可不填，现在填入则烧入后都不用单独连接开发串口，只需要配置网络即可功能方便


