Title: 十分钟的远程温度传感器
Date: 2015-09-08 11:40
Modified: 2015-09-08 11:40
Category: Blog
Tags: ESP8266
Slug: ten_minute_humiture_sensor
Authors: espush
Summary: 前面使用espush平台快速搭建智能插座后，这次也希望能在10分钟内搭建一个温湿度的传感器应用。通过使用ESP8266的WIFI能力与espush的云平台，将温湿度数据上传至平台，并使用平台提供的数据图示观察室内温度变化，亦可使用espush.cn提供的api同步数据后在自己的APP上展示。


前面使用espush平台快速搭建智能插座后，这次演示在10分钟内搭建温度传感器应用。通过使用ESP8266的WIFI能力与espush的云平台，将温湿度数据上传至平台，并使用平台提供的数据图示观察室内温度变化，亦可使用espush.cn提供的api同步数据后在自己的APP上展示。

先show下最后成果，这便是设备某段时间内环境的温度图示，是不是有种“波澜不惊”的感觉(不要在意为什么我家里温度是2700摄氏度，后面我会说原因的。。。)，实话说，这温度还挺舒服的。

![温度图]({filename}/images/wd_graphic.png)

这里使用的传感器型号为DHT111，实测中表现似乎不是太好，在人的皮肤已经能感受到温差后仍然无动于衷，不过这并不影响我们的使用过程。在 [管理控制台](https://espush.cn/web/) ->[设备分类](https://espush.cn/web/apps/) 中新增一个温湿度传感器设备类型，记下其APPID与APPKEY，打开espush_sdk固件，修改user_init的初始化代码，如下：

```C
void ICACHE_FLASH_ATTR user_rf_pre_init()
{

}

//取出温湿度数据，此处只使用了温度数据
void push_wsd(void* param)
{
	struct sensor_reading *dht = readDHT(0);
	if(!dht->success) {
		ESP_DBG("reading failed.\n");
		return;
	}
	char buf[32] = { 0 };

	//温度数据乘以了100，因为乐鑫SDK的os_sprintf函数没有实现float浮点数类型的格式化
	//所以此处简单处理。
	uint32 temperature = dht->temperature * 100;
	//此处取了当前系统时间戳（只有连上平台后方有效，准确而言是连接过后有效）
	uint32 timestamp = get_timestamp();
	//将数据打上wd 标签，所谓标签即是在数居前增加的 逗号分隔的字符串，目前仅支持单标签
	os_sprintf(buf, "wd,%d", temperature);

	//将数据推送到平台。
	espush_msg_plan(buf, os_strlen(buf), timestamp);
}

void ICACHE_FLASH_ATTR user_init(void)
{
	uart_init(BIT_RATE_115200, BIT_RATE_115200);
	os_printf("\n\nready\n\n;");
	struct rst_info* rstInfo = system_get_rst_info();
	ESP_DBG("RST => reason: [%d], exccause: [%d], epc1: [%d], epc2: [%d], epc3: [%d], excvaddr: [%d], depc: [%d]\n",
			rstInfo->reason, rstInfo->exccause, rstInfo->epc1, rstInfo->epc2, rstInfo->epc3, rstInfo->excvaddr, rstInfo->depc);

    //修改配置，配置你本地的SSID与PWD
	struct station_config config;
	os_strcpy(config.ssid, "YOUR SSID");
	os_strcpy(config.password, "YOUR SSID PWD");

	wifi_set_opmode(STATION_MODE);
	wifi_station_set_config(&config);
	wifi_station_set_auto_connect(1);
	wifi_station_dhcpc_start();

	//修改成你的APPID与APPKEY
	espush_register(APPID, "APPKEY", "", VER_SDK, NULL);
	DHTInit(SENSOR_DHT11, 5000);

	//每分钟上传一次数据
	static os_timer_t sensor_timer;
	os_timer_disarm(&sensor_timer);
	os_timer_setfn(&sensor_timer, push_wsd, NULL);
	os_timer_arm(&sensor_timer, 60000, 1);
}
```

将附件中的 dht.h 与 dht.c 加入工程后编译烧录即可，或者直接 clone [这个git库](https://github.com/pushdotccgzs/espush_sdk) 后编译亦可。

来看看效果吧，展开管理控制台中的设备数据项，点击数据预览，可以看到每分钟有均匀的温度数据上传，但似乎全是同样的数据，如下图所示：

![温度上传数据展示]({filename}/images/wd_data.png)


点开数据图示，按下图所示

![数据图示]({filename}/images/data_graphic_src.png)

选择数据的起始日期，选择数据来源的设备类型，输入数据标签wd，点击图示，就可以看到你的房间温度变化图啦。

这是最简化的施工图：

![ESP8266连接DHT111]({filename}/images/esp8266_dht111.jpg)

