Title: espush平台介绍
Date: 2015-08-25 10:01
Modified: 2015-08-25 10:01
Category: Blog
Tags: ESP8266
Slug: espush_description
Authors: espush
Summary: Hi，IoT Cloud on ESP8266, espush.cn更新了，这次更新加入了很多新功能，并对系统的稳定性做了进一步的优化，目前已经是一个比较完善的物联网设备的云平台了。对比两个月前的版本，详细的ChangeLog就像开发日志一样，我就懒得列了，这里使用一篇博客的形式，简单介绍下平台的功能与特色，算是一个release日志吧。


从第一次发现如此便宜的，带WIFI功能的，可编程的芯片开始，我就决心为其开发，简要将其功能概述如下：

1，快速的设备接入，为开发者提供了类似于推送库的C库，使用乐鑫SDK非OS版本开发，接入只需要一行代码即可，快速获得云端数据推送能力。关于如何使用SDK开发包开发自己的固件以及接入espush.cn，以及平台推送库提供的C API，建议参考头文件 push.h，已经有比较详尽的注释了。跳至<a href="https://github.com/pushdotccgzs/espush_at/blob/master/app/include/push.h">此文件</a>。

2，类似于信鸽等推送平台，espush.cn使用了设备类别APP的概念，提供了对大量设备的同时云端操控能力。当然，你如果只想操作某个指定的设备，也是完全可以的.

3，多固件适配，对于AT固件，espush.cn在官方基础上新增了方便云端远控的指令以及通用GPIO操作指令，并紧跟官方最新版本；另外同时提供NodeMCU的固件适配，并针对NodeMCU使用Lua编程的特性，添加了一些特定的API以更方便使用本平台。无论你使用哪一款固件，都可以最快的找回感觉，无缝接入。8266新手若不了解NodeMCU，可以参考这里：<a href="http://nodemcu.com/">NodeMCU官网</a>

4，云端指令推送，要是只能从云端向模块推送一些字符串用来在串口炫耀未免无用，espush.cn独创向模块在线直接推送指令，并涵盖AT指令（for AT固件）与Lua指令（for NodeMCU固件），你甚至能直接推送一个Lua文件到模块里，使之执行。针对AT固件推送AT指令的文档在这里，针对NodeMCU推送Lua指令的操作说明在这里，建议你试试，可以放飞你的想象力。另外，除了单独控制某一个模块，本平台设计的初衷就是同时控制大量的设备，所以可以同时向N台终端模块推送指令，这完全是可以的，甚至更简单。

5，终端状态实时获取，其实很简单的功能，手机上随时可以知道模块的任何状态（包括IO口电平态、可用内存、其他任何事情，反正使用回调函数，这个针对NodeMCU固件），看上去很简单对不对，是，我也这么认为，但这是第一个实现，而且很好用。文档在这里，你可以去试试，真的可以做很多事情。

6，终端数据上传后实时通知，不仅可以从云端直接推送数据到模块，模块同样可以将自身数据、环境数据、其他任何想上传至服务端的数据，任何时候通过一条指令就可以上传至云端，并能定义自己的服务器，实时接受数据通知。你可以在服务端接入，构建自己的wifi监控设备。

7，OTA支持，在线升级，这个目前只针对AT固件与SDK开发包的固件，并且由于目前大部分固件并未使用OTA模式编译，故暂未开放在espush.cn控制台中，但这个功能的确是可用的，如果你需要，可以联系开发者。espush.cn的在线升级不同于官方，自定义整个升级过程，失败后可以从上次失败的地方开始，逐区段进行升级，成功率较高。且升级过程中完全不需要客户端/模块的参与，开发者可以选择强制推送升级新版本。

8，提供服务端API，可以实现所有web控制台的功能，甚至更强大（譬如整Lua文件的推送就没有在web控制台中，但你可以自己实现他）。服务端API的文档在这里: http://docs.espush.cn/server.html，你要是觉得好用，可以帮忙弄更多的编程语言binding.

9，固件的代码很多都是开源的，你可以直接去这里看看，[有AT固件](https://github.com/pushdotccgzs/espush_at)、[NodeMCU固件的源码](https://github.com/pushdotccgzs/espush_nodemcu_，感谢 @[NodeMCU](https://github.com/nodemcu/)的成果，真的很赞，我只是站在巨人的肩膀上做了一点小小的改动而已。

10，我弄了个手机APP，你可以直接下载一个来试试，下载地址[在这里](https://espush.cn/web/down_apk/)，暂时只有for Android ，嗯，也是APK开源 的，代码托管在github上，地址[于此](https://github.com/pushdotccgzs/espush_android)，感谢@Every

有童鞋在QQ上问我平台稳定性如何，我不知道如何严格定义「稳定性」这个概念，因为平台本身线上运行也不过两三个月左右，用户还非常少，活跃用户更少，所以很难有大规模的真实测试。但是有些模块一直挂在平台上，可以随时控制算不算稳定，在线时间较长的也都半个多月的（中间设备未重启），对于wifi断线、设备电源不稳重启等情况，固件都有考虑，可以自动重连；服务端也可以随时升级重启，客户端仍然会自动重连，精简的协议设计也一定程度上减少了bug的可能。另外，如果你发现了bug，可以汇报给我。

对测试过程中的网友 @东奇，@风 ， @APK开源 表示感谢。

做这个缘于偶然的兴起，从开发其后台设备的网关服务器，到推送库以及AT固件、NodeMCU固件，最后到Web控制台界面，以及最后的手机APP，花掉了我这几个月主要的下班时间，另外害的科目二都挂了。另外，不要问我收不收费这种问题了，你肯用就是给了很大的面子了，这东东主要就是方便开发者不用重复造轮子而已，你要是愿意，也可以弄一个，并不复杂。

技术合作可以联系 webmaster@espush.cn，在ESP8266芯片上，我可以用最快的速度为您搭建包含所有的一整套的云平台技术体系，提供让您满意的技术支持，走「更少」的弯路。
