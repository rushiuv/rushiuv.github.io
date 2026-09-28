---
title: "Melexis推进Tactaxis指尖模组，磁传感芯片正在进入机器人触觉系统"
date: 2026-04-25T00:00:00+08:00
slug: "E1vGJvbiO1rFzSbltPf4TQ"
description: "4月21日，Melexis 和 OYMotion 宣布把 Tactaxis 磁触觉传感技术推进到下一代机器人手的工业化指尖模组里。表面上看，这是一条机器人触觉新闻；真正刺人的地方在于，它把传感器竞争从“单颗器件参数”推向了“系统入口定义权”…"
original: "https://mp.weixin.qq.com/s/E1vGJvbiO1rFzSbltPf4TQ"
---

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIXpWZd6rTD0qkmrKTRoGsiasbRic06icmQiaeeQpiaE0spciaeD7Gxu51AVwYQIBec8HRz5J3Py87kib4qMQEDW9ubYLM65ex3ktfGPd0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIWbkpK73pL0C4ggWnsBxc2EJ31zAYdUeFOwibGEzmYxkAOib8KBCdSDXDcdgzfNZxooBJkCz90HZ3HH3UNBOGhBaBCzA7RibsvVAI/640?wx_fmt=png&from=appmsg)

4月21日，Melexis 和 OYMotion 宣布把 Tactaxis 磁触觉传感技术推进到下一代机器人手的工业化指尖模组里。表面上看，这是一条机器人触觉新闻；真正刺人的地方在于，它把传感器竞争从“单颗器件参数”推向了“系统入口定义权”。

过去传感器公司最爱讲参数：分辨率、精度、噪声、带宽、功耗、尺寸、抗干扰。编码器讲 、、；触觉传感器讲三维力、阵列密度；磁传感器讲三轴、温漂、采样率。这些都重要，但机器人厂真正量产时，最怕的往往不是某一个参数差一点，而是这东西接进系统以后太麻烦。

结构怎么装？线怎么走？标定怎么做？温漂怎么补？批量一致性怎么保证？客户换了手指材料，数据还能不能用？现场出了问题，是芯片问题、磁体问题、结构问题，还是算法问题？传感器厂商想卖“我的芯片很好”，机器人厂真正想买的是“**这东西我能不能直接用，而且出了问题能不能查清楚**”(这事在我公众号里面已经叨叨好多次了)。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DBrlpXS1RIVo5VaCXPTnIJzdjUz4ibnbgia4FdMSpIibmWD4cb30S2XeF4AUGcbqrTH1acwVMv3f4ThfD2IiaJsDKUkdJ6Lw8q9PUCDv5LMBMZQ/640?wx_fmt=jpeg&from=appmsg)

### 一、Tactaxis不是在卖“能摸”，而是在卖“能被机器人手使用”

Tactaxis 的公开资料里有几个关键数字：尺寸约 ，可以输出作用在表面的 3D 力矢量，采用磁感应原理，强调 fully integrated，并计划用半导体工艺量产，同时主打对杂散磁场和温度变化的鲁棒性。

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIUzypIib2q6bTK6OSJTTXibZp3JtEmLXMh3CicBmjNHVUzHp9nIb0ZQwibCanrYA4rI46SNOIAxFfLl2oCicLibbujCEKP7Uy9ZufUXU/640?wx_fmt=png&from=appmsg)

普通开关只能告诉你“碰了”还是“没碰”。普通压力传感器大多只能告诉你“压得轻”还是“压得重”。但机器人手抓东西时，真正需要的是更细的信息：**力从哪个方向来，有没有侧向滑移，物体是不是快掉了，手指是不是压得太狠。**

所谓**3D力矢量**，说白了就是把接触力拆成几个方向来看。比如一个杯子被机器人手拿着，竖直方向是重力，手指正向要提供夹持力，侧向变化可能意味着杯子开始滑。人手能抓稳东西，不是因为皮肤会喊“我要掉了”，而是皮肤在很早的时候就感到了微小滑移和剪切力变化。

![](https://mmbiz.qpic.cn/mmbiz_jpg/DBrlpXS1RIVxbOrE66pjCF5nTibY4ibCZqq3o1qiaDCbqWnnPqMDpeIh5Ut0bK6OSKFhBrhACQSEQcT0cp26YeR0lzdxuXtGMhUib2uIPgia1lXk/640?wx_fmt=jpeg&from=appmsg)

Tactaxis 最值得看的地方，不是它把触觉讲得多玄，而是 Melexis 在强调小型化、集成化、可量产、抗干扰、抗温度变化。这些词不炫，但很工业。它针对的不是展会上摸一下就完事的样机，而是机器人手未来能不能批量交付。

实验室里做出一个“能摸到”的触觉样机不难。真正难的是，批量生产以后，每一只手指、每一批软胶、每一个安装位置，都能保持足够稳定的输出。机器人手不是展台玩具，它最终要在工厂、家庭、仓储、医疗这些场景里长期工作。触觉信号如果今天准、明天飘，低温准、高温飘，新手指准、老化以后飘，整机厂就不敢把它放进真正的控制闭环。

所以 Tactaxis 的价值不是“有触觉”，而是把触觉往工业化、模组化、可交付方向推了一步。

### 二、真正的价值不在芯片，而在“指尖模组”这一步

这次新闻里最关键的词，是**fingertip modules，也就是指尖模组**。

一颗触觉传感器只是一个点。指尖模组则是一小套系统。它至少包括软材料、受力结构、传感芯片、磁体或磁结构、信号处理、电气接口、安装方式、标定数据，甚至还包括怎么和机器人手的控制软件对接。

这就像手机摄像头。手机厂真正采购的通常不是一颗裸图像传感器，而是一个摄像头模组。里面有镜头、传感器、结构、调焦、标定、图像处理配合。因为手机厂要的是“这东西装上去能拍照”，不是“我拿到一颗芯片以后自己从头折腾”。

机器人手也是一样。如果供应商只给一颗触觉芯片，整机厂还要自己设计软胶结构、磁体位置、线路板、标定夹具、算法补偿、接口协议和软件驱动。最后芯片再便宜，系统成本也可能很高。真正贵的不是那几颗料，而是工程师反复调试、返工、排故的时间。

**谁定义了模组结构，谁就影响机械设计**。谁定义了标定流程，谁就影响量产方法。谁定义了接口和软件，谁就影响客户的开发习惯。谁先进入这些位置，谁就不再只是 BOM 表里的一颗芯片，而是机器人系统的一部分。

这就是系统入口。

OYMotion 的意义也不只是提供一只机器人手。它公开资料里已经有 ROHand 的固件、协议、ROS/ROS2 包、URDF 和 demo 例程, 很多已经开源。也就是说，Melexis 不是把 Tactaxis 塞进一个孤立硬件里，而是把触觉传感接进一个已经有开发接口和机器人软件入口的平台里。触觉数据一旦进入控制、仿真和开发工具链，就不再只是芯片输出，而开始变成系统能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIVIqPN3bHN2wRGzMJ8EQa6wQupQLUZR3cUIqmMcBBoXNib8kRiaElk9MAUNNTUkAusRialaPQwocDGq5dPBf9VneBVibj5lFyRw0NM/640?wx_fmt=png&from=appmsg)

硬件做出来，只是第一步。客户能顺利用起来，才是第二步。客户以后默认按你的接口和流程设计系统，才是第三步。

真正的卡位战，发生在第二步和第三步。

### 三、磁触觉说穿了并不神秘：小磁体动一下，芯片读出来

很多人一听机器人触觉，脑子里容易出现“电子皮肤”“仿生神经”“柔性阵列”这些词，听起来很高级，但也容易飘。Tactaxis 这类磁触觉路线，其实很朴素。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DBrlpXS1RIU3r7sxicu8EZMS9U9UrotsT3l0icVib4bF1QY6sSS1aCtibTJQKZKPrj7k49Q2U8dj2NZRdFdW4BicvodA2RpndSvJTRcNO2Uv1jrM/640?wx_fmt=jpeg&from=appmsg)

在机器人指尖里放一个小磁体，再放一个三轴磁传感器。外面包一层软胶或者弹性结构。手指碰到物体以后，软结构变形，小磁体的位置也跟着发生极小变化。磁体一动，传感器读到的 、、 三轴磁场就变了。算法再把这些变化翻译成按压力、侧向力、滑移趋势和接触方向。

![](https://mmbiz.qpic.cn/mmbiz_jpg/DBrlpXS1RIV0lMSOAcKPOkQ192Ar0N9oddbeGhKWN7EycsgP45NY55c4rhKCWDKlDB66c8dkQSqXOMBK2lCjSpBISHm4z0CGHvlFslOpOJM/640?wx_fmt=jpeg&from=appmsg)

手指受力不是直接被芯片“摸到”的，而是先让一个小磁体微微动了一下；芯片测到磁场变化，再反推出手指受了什么力。

这条路线有几个工程优点。磁场可以隔着软材料测，芯片不一定要暴露在外面；传感器可以藏进结构内部，外面只负责受力和变形；如果结构和算法设计得好，它不仅能测按压，也可以测侧向滑移和接近；磁传感器本身也适合小型化和半导体量产。

机器人磁触觉不只是 Melexis 一家的故事。今天很多三轴磁传感芯片，本质上都能做“磁体位置变化检测”。区别在于，有的厂商把它做成通用位置芯片，有的做成摇杆、旋钮、滑块方案，有的进一步往机器人指尖触觉模组里推。

磁触觉真正要做的，是把这类能力从“读磁体位置”推进到“读软结构受力后的微位移”。

### 四、从TI、Infineon到昆泰芯：三轴磁传感正在走向“微位移反推”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIV3Qrnv52LJTjEXy4WrxE4wrSdjMlwwa2Rh5UXs9wsS7fs3CeNsZ1L3JACZABlKQToudOrcCFKuHcmtrSwlqae49kb1uzXsAmo/640?wx_fmt=png&from=appmsg)

TI 的 TMAG5170 是一颗高精度三轴线性霍尔传感器，单轴转换速率可达 ，支持 SPI 接口，内置温度传感器，线性测量总误差在  下最大为 ，还带 CORDIC 角度计算能力。它并不是专门为机器人触觉定义的芯片，但三轴磁传感器早就不只是“感应有没有磁铁”，而是在往高速、高精度、位置解算方向走。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIXiaTTmAYqsJYC29MS4kjUB8Xz7cbeRzCSRbXWV0eJIcF3nvwOic1FFRSias6PYms3lZq1qwN7GgqgfZ6icUZPtZR9ZXqYeA71icUv0/640?wx_fmt=png&from=appmsg)

Infineon 的 TLI493D-W2BW 也是三轴磁传感器，可以测量 、、 三个方向的磁通密度，量程到 ，封装尺寸约 ，每个方向提供  数据分辨率，掉电模式典型功耗只有 。这类芯片适合小空间、低功耗、接近检测、滑块、旋钮、摇杆等应用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIWib0JxFgyOEmbR4bcRDe4cOavKp9GIT9icwY5WhA8zUrsysJSS6tortmp02sHkTiaU2ej7sG4gC2uSoBxwLDjnQD2lHfe7mWic1ias/640?wx_fmt=png&from=appmsg)

这些芯片不等于触觉模组，但它们说明同一类底层能力已经成熟：小封装三轴磁场检测、高速采样、低功耗和温度补偿。磁触觉真正要完成的，是把这些能力从“磁体运动检测”推进到“接触状态识别”。

昆泰芯 KTH5701 同样属于这条技术线上。它是数字输出型三轴线性霍尔传感器芯片，可以测量 、、 三个方向的磁场分量，支持 I2C 和 SPI 通信。昆泰芯官网还写到，用户可以开启一轴或多轴组合的磁场测量，获取磁场原始数据后，结合软件算法提取磁铁的运动信息，适用于摇杆、旋钮、位移测量等应用场景。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIU8HTDS6rltvs1DB1R4vmfpMlyGAUwibhBA1CflHDasF2dYicyoMdxr3tfNoynpa7YIGXSDTtWWZYzE589GqOV0l8jeVe4eU70k0/640?wx_fmt=png&from=appmsg)

摇杆是什么？小磁体相对芯片移动，芯片读出三轴磁场变化。位移测量是什么？磁体位置变化，带来磁场变化。机器人指尖触觉是什么？工程上翻译一下，也可以是软结构受力后，小磁体发生微位移，芯片读出三轴磁场变化，再由算法反推出接触状态。

三者底层都是“磁体位置变化—磁场变化—算法反推”。区别在于，摇杆和旋钮的运动比较规则，机器人手指里的触觉变化更小、更乱、更容易受温度、结构、材料和装配影响。所以前者更像芯片应用，后者更像系统工程。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DBrlpXS1RIUlibpIB7DVFIUtTZzSKTkn9FqRN8b2HJZ96orcRfQTRhz0VT62AgFQ7Vbp72KiaYPMRicwJApSkZDTJXWncfWtTeTr4RqjNQB2icc/640?wx_fmt=jpeg&from=appmsg)

KTH5701 的一些数字放在机器人末端小型化场景里很值得看：QFN  小封装，供电范围 ，三轴  测量，待机功耗 ，典型工作频率 ，工作温度范围 。这些数字说明它不是只能做一个粗糙开关，而是有机会捕捉比较细的磁体运动变化。

KTH5701 符合 Tactaxis 路线的地方，不是“它已经等于 Tactaxis”，而是它具备磁触觉所需的几个底层条件。

-

**第一，它能读三轴磁场**。机器人手指受力以后，小磁体不是只沿一个方向运动，而可能同时有下压、侧向偏移和扭转。只读单轴磁场，很难区分这些复杂变化。KTH5701 可以测量 、、 三个方向磁场分量，这就给后续算法留下了空间。

-

**第二，它是数字输出**，支持 I2C 和 SPI。机器人手指空间小、节点多，如果要在一只灵巧手里布多个触觉点，接口和系统集成会很关键。KTH5701 直接输出数字量，外部主控可以通过 I2C 或 SPI 读取数据，比纯模拟输出更容易进入小型控制板和嵌入式系统。

-

**第三，它有温度补偿基础**。触觉模组里最麻烦的东西之一就是温度。温度变了，磁传感器灵敏度会变，磁体磁性会变，软胶弹性也会变。KTH5701 集成温度传感器，并用于磁场温度补偿，这至少解决了芯片自身测量链路的一部分温漂问题。

-

**第四，它的小封装和低功耗适合往手指里塞**。 QFN 封装、低功耗和数字接口，意味着它具备多点布置和嵌入式读取的基础。机器人手指不是一个宽敞的实验平台，任何能塞进去、功耗压得住、数据能直接读的器件，都有现实意义。

-

**第五，它已经明确面向“磁铁运动信息提取”**。官网没有只把 KTH5701 写成“测磁场强度”的芯片，而是明确提到结合软件算法提取磁铁运动信息。磁触觉的核心也不是测磁场本身，而是用磁场变化反推出结构运动，再进一步反推出接触力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIVQbj9jT6perg4scoicqefoicIUGNAnMX7mtgwQKsCUfQJk8CuOGtsggKibDCWibB0ZkQtTRgG5DylJA92VSA63ibUoCsp90yADhicn8/640?wx_fmt=png&from=appmsg)

但必须说清楚：KTH5701 不能直接等同于一个完整的机器人指尖触觉模组。公开资料能证明的是，它具备三轴磁感知和磁体运动检测的底层能力；还不能直接说昆泰芯已经发布了一个 Tactaxis 式的工业化指尖模组。

差距主要在系统工程上。

**第一，缺软结构定义**。机器人指尖触觉不是芯片单独完成的，软胶厚度、硬度、形状、磁体位置、受力路径都会影响输出。没有软结构，芯片只能读磁场，不能天然知道“这是多少牛的力”。

**第二，缺磁路和机械耦合设计**。小磁体放在传感器正上方、侧方，还是偏心位置，得到的三轴曲线完全不同。要把按压和滑移区分开，磁路设计必须服务于力解耦，而不能只是“能读到变化”。

**第三，缺抗杂散场体系**。Tactaxis 特别强调 robust against stray field and temperature changes。KTH5701 有温度补偿基础，但机器人手指靠近电机、线束、磁编码器、永磁体时，外部磁场干扰会很复杂。要做到工业化触觉模组，可能需要差分结构、参考传感器、磁场梯度算法，甚至机械屏蔽。

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIVRHGwcQVfqUSJsLT7Ms8Og1vaudYA4aB4YHFSBoLmke02oPmrShZ1Cu5pjL4ww2pkaFxhMVqlcIZoxvtOdJkialMZLLnUiaILz8/640?wx_fmt=png&from=appmsg)

KTH5701 站在通往磁触觉模组的第一块地基上。真正要补的，不是再讲一遍“三轴霍尔”，而是把这颗芯片推进机器人手指的系统链条里。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DBrlpXS1RIUW03Y8NtAhBbXh4A9URic53v50VnLHsf0coCR96YJVhUg7LKv6DYhuviaiaLc2Yet9jcVHC3fNP9sfUtGyP9Go1qN1qpYUaeu39g/640?wx_fmt=jpeg&from=appmsg)

### 五、传感器厂商下一步卖的，是客户少踩坑

传感器厂商以为自己在卖芯片，机器人厂真正需要的是这颗芯片被系统接受的方式。

Melexis 用 Tactaxis 往前走了一步，**把触觉从一个传感器功能，推向了机器人指尖模组**。它抢的不是一颗芯片的位置，而是机器人手的系统入口。

昆泰芯这样的国内磁传感厂商，也有自己的位置。KTH5701 这类三轴霍尔芯片，已经具备检测三维磁场和提取磁体运动信息的底层能力；机器人关节位置感知和磁编码器算法，又让昆泰芯本来就接近机器人运动控制场景。下一步真正值得做的，不是简单多讲一个“触觉传感器”概念，而是**把三轴磁感知、软结构、磁路、标定、接口、软件和机器人应用连成一条链**。

**机器人手指最怕的是传感器太像实验品**。真正能进入量产的东西，必须能装、能调、能测、能复现、能维护、能被系统相信。

以后传感器厂商卖的，可能不再只是器件，而是器件被系统接受的方式。

谁把这种方式做成模组，做成接口，做成标定流程，做成软件包，做成默认方案，谁就不再只是供应链上的一个料号，而是机器人生态里的规则参与者。

一旦规则被别人先写好，后面很多单点参数优势，就未必还能换来同等的话语权。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIUhb8KdtDukkQQzTvlAs69gqWq1ibr7eiaUtr4yZEnLGOxiboCPiceOOytWG6EA1LS0LksdtVqwQfX3ictdNhNYoDfMobK51f2PNu3o/640?wx_fmt=png&from=appmsg)
