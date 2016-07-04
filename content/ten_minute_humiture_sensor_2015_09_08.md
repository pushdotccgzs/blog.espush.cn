Title: 十分钟的远程温度传感器
Date: 2015-09-08 11:40
Modified: 2016-06-27 20:34
Category: Blog
Tags: ESP8266
Slug: ten_minute_humiture_sensor
Authors: espush
Summary: 前面使用espush平台快速搭建智能插座后，这次也希望能在10分钟内搭建一个温湿度的传感器应用。通过使用ESP8266的WIFI能力与espush的云平台，将温湿度数据上传至平台，并使用平台提供的数据图示观察室内温度变化，亦可使用espush.cn提供的api同步数据后在自己的APP上展示。


**更新：已使用专属开发板更新全部内容，文中代码已更新，且代码重新上传到了github地址，可编译测试。**

##准备工作
1. 蘑菇云专属开发板，板载了温湿度传感器DHT11，购买链接如下：https://item.taobao.com/item.htm?id=534025556644 本篇文章及示例工程必须运行在蘑菇云专属开发板下，开发板自带IoT开发中常用的传感器与元件，推荐购买。
1. 蘑菇云平台帐号，如下地址注册：https://espush.cn/webv2/register/
1. 下载示例代码，蘑菇云网盘资料区即可下载，或clone以下工程：https://github.com/pushdotccgzs/espush_dht_demo

前面使用espush平台快速搭建智能插座后，这次演示在10分钟内搭建温度传感器应用。通过使用ESP8266的WIFI能力与espush的云平台，将温湿度数据上传至平台，并使用平台提供的数据图示观察室内温度变化，亦可使用espush.cn提供的api同步数据后在自己的APP上展示。

先show下最后成果，这便是设备某段时间内环境的温度图示，是不是有种“波澜不惊”的感觉(不要在意为什么我家里温度是2700摄氏度，后面我会说原因的。。。)，实话说，这温度还挺舒服的。

这里使用的传感器型号为DHT111，实测中表现似乎不是太好，在人的皮肤已经能感受到温差后仍然无动于衷，不过这并不影响我们的使用过程。在 [管理控制台](https://espush.cn/web/) ->[设备分类](https://espush.cn/web/apps/) 中新增一个温湿度传感器设备类型，记下其APPID与APPKEY，打开espush_sdk固件，修改user_init的初始化代码，如下：

```C
#include <osapi.h>
#include <os_type.h>
#include <at_custom.h>		//切记务必包含 at_custom.h
#include "driver/dht.h"		//DHT11的头文件，记得包含
#include "driver/espush.h"	//蘑菇云平台头文件

//取出温湿度数据，此处只使用了温度数据
void ICACHE_FLASH_ATTR push_temperature(void* param) {
    char buf[8] = { 0 };
    //读取DHT数据，参数0代表非强制读取，取1则强制同步DHT读数，此处不需要。
    struct sensor_reading *dht = readDHT(0);
    //如果读取DHT数据失败，或者未连接到平台，都放弃本次数据推送。
    if(!dht->success) return;
    if(espush_server_connect_status() != STATUS_CONNECTED) return;
    //温度数据乘以了100，因为乐鑫SDK的os_sprintf函数没有实现float浮点数类型的格式化，所以此处简单处理。将数据打上wd 标签，所谓标签即是在数居前增加的 逗号分隔的字符串，目前仅支持单标签
	uint32 temperature = dht->temperature * 100;
	os_sprintf(buf, "wd,%d", temperature);
    //将数据推送到平台。
    espush_msg_plan(buf, os_strlen(buf), get_timestamp());
}

//射频参数初始化，请留空
void ICACHE_FLASH_ATTR user_rf_pre_init(void){}

//入口初始化
void ICACHE_FLASH_ATTR user_init(void) {
    at_init();
    at_port_print("\r\nready\r\n");
    //初始化DHT11传感器，并配置每20秒更新一下数据
    //此处可适当调整，间隔周期不要高于向平台的数据推送时间间隔即可
    DHTInit(SENSOR_DHT11, 20000);
    //配置定时器，没60秒传输一次温度数据
    static os_timer_t temperature_timer;
    os_timer_disarm(&temperature_timer);
    os_timer_setfn(&temperature_timer, push_temperature, NULL);
    os_timer_arm(&temperature_timer, 60000, 1);
    //注册到平台，下面的APPID与APPKEy，请填写你对应的值。
    espush_register(APPID, "APPKEY", "", VER_SDK, NULL);
}
```

直接 clone [这个git库](https://github.com/pushdotccgzs/espush_dht_demo) 后编译（编译请使用`make BOOT=new APP=1 SPI_SIZE_MAP=4`进行）烧录即可：


![烧录程序]({filename}/images/temperature/flasher.png)


![网络配置]({filename}/images/temperature/netcfg.png)


来看看效果吧，展开管理控制台中的设备数据项，点击数据预览，可以看到每分钟有均匀的温度数据上传，但似乎全是同样的数据，如下图所示：

![温度上传数据展示]({filename}/images/wd_data.png)


点开数据图示，按下图所示

![数据图示]({filename}/images/data_graphic_src.png)



![结果展示]({filename}/images/temperature/result.png)

选择数据的起始日期，选择数据来源的设备类型，输入数据标签wd，点击图示，就可以看到你的房间温度变化图啦。

这是最简化的施工图：

![ESP8266连接DHT111]({filename}/images/temperature/board.jpg)

