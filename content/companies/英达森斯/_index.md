---
title: "英达森斯"
wiki: true
wiki_type: "company"
wiki_rank: 165
seed_count: 1
lastmod: "2026-10-22"
description: "英达森斯（Induxense）：做电感式编码器芯片的上海公司，IDX3531 公开 24bit 断电多圈与 660000 e-RPM。"
official_url: "https://www.induxense.com/?a=index&c=Lists&m=home&tid=2"
wiki_category: "传感器与测量前端"
related_models: []
---

英达森斯只做一件事：电感式编码器芯片。它在链条上的位置是"芯片 + 算法 + PCB 线圈工具链"——线圈不在片内，画在客户的 PCB 上，所以它卖的不只是硅片，还有一套让客户把线圈画对的设计工具。这条路线与磁编的最大区别就在这：误差链里最关键的几何量（线圈线宽、靶盘间隙、安装偏心）由客户自己掌握。

## 公司与品牌

英达森斯半导体（Induxense），中文站点在 induxense.com、上海备案主体。公开新闻自述：通过 ISO 26262 功能安全体系认证、多项电感式编码器芯片发明专利获授权、入选 2026 年度国家科技型中小企业名单、旗舰芯片 IDX3531 发布。官网还有一整套开发资源：评测套件、信号模拟测试输入平台、芯片配置工具 ICS、编程工具 IPS（原生支持 RISC-V）、PCB 线圈设计平台 iCoil Studio、AI 算法平台。

成立年份在本次取到的页面里没有出现，官网只提到"成立一周年"那次新闻，不写年份比写错年份好。中文品牌常写作"英达森斯"，英文域名与产品前缀分别是 induxense 与 IDX。[公司新闻与产品动态](https://www.induxense.com/index.php?m=home&c=Lists&a=index&tid=10)

## 编码器相关产品线与公开规格

四个在售族按输出形态分：单组线圈模拟输出、纯数字输出、混合信号输出、以及带多圈记忆的型号。参数集中给在数字侧，模拟型号只说用途。

| 系列 | 类型 | 公开分辨率/关键指标 | 其他公开参数 |
| --- | --- | --- | --- |
| [IDX3463 / IDX3463A](https://www.induxense.com/index.php?m=home&c=Lists&a=index&tid=71) | 单组线圈电感式编码器，模拟输出 | 分辨率未公开 | 简化线圈设计、面向成本敏感的高精度位置检测 |
| [IDX3551](https://www.induxense.com/index.php?m=home&c=View&a=index&aid=140) | 单圈绝对位置，纯数字输出 | 660000 e-RPM、最大测量更新速率 <1 µs | ABZ / UVW / SENT / PWM / SPI / SSI / RS485（兼多摩川协议）、内置 1 M SPI Flash、QFN 5×5 mm、−40~105 °C |
| [IDX3531](https://www.induxense.com/index.php?m=home&c=View&a=index&aid=266) | 多圈绝对位置，数字输出 | 24 bit 断电多圈计数、660000 e-RPM | 内置 RISC-V 可定制、QFN 5×5 mm、−40~105 °C、ABZ / UVW / SENT / PWM / SPI / SSI / RS485 |
| [IDX3550](https://www.induxense.com/index.php?m=home&c=Lists&a=index&tid=22) | 混合信号输出（模拟 + 数字） | 分辨率未公开 | 双输出模式，覆盖工业与汽车接口 |
| [IDX3560 / IDX3561](https://www.induxense.com/index.php?m=home&c=Lists&a=index&tid=70) | 数字输出（类目页列名） | 未公开 | 与 IDX3551 同族，页面未给参数 |

三个口径要分开读。**e-RPM 是电气转速**，660000 e-RPM 要除以极对数才是机械转速，不能当成机械转速指标；**24 bit 是 IDX3531 的断电多圈计数位宽**，而旗舰发布的新闻页写"20~22 位分辨率"，两者说的是不同东西——位宽、分辨率、精度在三处页面各说一部分；**延时也是两套说法**：IDX3551 页写"最大测量更新速率 <1 µs"，IDX3531 页的参数表写"角度输出延时 <3 µs、片内相位动态补偿实现 0.1 µs 以下的等效测量延迟"。[IDX3531 产品页](https://www.induxense.com/index.php?m=home&c=View&a=index&aid=266)

另一个值得记的公开信息是汽车线：官网写"电感编码器芯片满足 AEC-Q100 / ISO 26262 双认证，精准检测电机转速、踏板行程及方向盘转角"——这句是应用页口径，具体型号的认证证书号没有公开。[汽车电子应用](https://www.induxense.com/index.php?m=home&c=Lists&a=index&tid=100)

多数量产型号不给位数、INL、重复性与温漂；数据手册在站上是受限资源，需要登录并提交申请后才可下载，公开页只给文件名；IDX3560 / 3561 只出现在类目页，没有参数；模拟输出的 IDX3463 只写"单组线圈、成本敏感"，连分辨率一栏都是空的。还有一处要提醒：官网页面对"分辨率"和"输出延时"混用了位宽、更新速率、等效延迟三种表述，跨品牌比较前必须先把定义对齐。

## 在编码器链上的位置

它卖芯片加工具链：线圈设计平台（iCoil Studio）、寄存器配置工具、固件烧录与调试、AI 算法库一起给。客户是自制 PCB 线圈的编码器厂、电机厂与关节模组厂，它自己不做线圈、不做码盘、不做整机。

这条分工决定了误差归属：芯片端负责激励、解调、角度解算与补偿；客户负责线圈几何、靶盘材料与间隙、安装偏心。所以同一种芯片在两家的成品精度可以差很多，看到"某家用 IDX35xx"能推的是它选了无磁路线与这套接口，推不出它的实际精度。不能推断的：晶圆代工方、客户名单、各型号的实际分辨率。

## 官方资料

- [英达森斯官网](https://www.induxense.com/)
- [新闻与产品动态](https://www.induxense.com/index.php?m=home&c=Lists&a=index&tid=10)
- [电感式编码器产品列表](https://www.induxense.com/index.php?m=home&c=Lists&a=index&tid=70)
- [模拟输出型号 IDX3463](https://www.induxense.com/index.php?m=home&c=Lists&a=index&tid=71)
- [数字输出型号（IDX3531 / IDX3551）](https://www.induxense.com/index.php?m=home&c=Lists&a=index&tid=72)
- [IDX3531 产品页](https://www.induxense.com/index.php?m=home&c=View&a=index&aid=266)
- [IDX3551 产品页](https://www.induxense.com/index.php?m=home&c=View&a=index&aid=140)
- [混合信号输出型号](https://www.induxense.com/index.php?m=home&c=Lists&a=index&tid=22)
- [AI 算法平台](https://www.induxense.com/index.php?m=home&c=Lists&a=index&tid=5)
- [汽车电子应用（AEC-Q100 / ISO 26262）](https://www.induxense.com/index.php?m=home&c=Lists&a=index&tid=100)
