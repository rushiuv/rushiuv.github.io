---
title: "iC-Haus"
description: "德国 Bodenheim 的编码器芯片厂，1984 年创办、BiSS 接口的发起方；iC-MU128 是 1.28 mm 极距的离轴磁绝对位置编码器，iC-TW29 是 26 位插值处理器。"
wiki: true
wiki_type: "company"
wiki_rank: 3
seed_count: 27
lastmod: "2026-10-22"
official_url: "https://www.ichaus.de/"
related_models: []
related_companies: []
---

iC-Haus 是那种「编码器厂背后的人」：它不做整机，卖的是感应前端、插值处理器、多圈计数与接口芯片，还能按客户规格做定制 ASIC。所以它的产品目录读起来像一条测量链的分解图——霍尔角度前端（iC-MA、iC-MA3、iC-MH16、iC-MHM）、离轴磁绝对位置（iC-MU128）、编码器处理器与 BiSS 接口（iC-TW29）。读它的资料要先认「这颗片子在哪一段」：传感器、插值、接口分属不同层，不能拿目录名当功能等价。

## 1984 年两位工程师在 Bodenheim 创办，BiSS 从这里出去

iC-Haus GmbH 成立于 1984 年，创始人是 Dr. Heiner Flocke 与 Manfred Herz，总部在德国 Bodenheim（法兰克福/莱茵-美因都会区），自有厂房与后道封装洁净室。官网自述业务是标准产品加客户定制芯片，工艺覆盖混合信号 CMOS、功率 BCD、高压与双极，并可在片上做感光或霍尔结构，形成「带传感器的单片微系统」；除塑料封装外，还能用 PCB 或柔性板做模块。BiSS 是它做出来的开放接口标准，官网的说法是「已成为传感器、执行器与控制器之间数字实时通信的全球性标准」。奖项方面：EncoderBlue® 位置传感器拿过 2017 年莱茵兰-法尔茨创新奖，能量采集多圈编码器拿过 2012 年 AMA 创新奖。公司通过 ISO 9001 认证。[公司介绍与历史](https://www.ichaus.de/about-us/)

## 六颗能核对的料，官方每颗只有一句话

产品页给出的是一句定位描述加「Download Specification」入口；完整规格书需要登录或单独申请，所以下表只写官方那句话里的信息，不补任何没写过的数字。

| 型号 | 类型 | 官方描述原文 | 其他可核对信息 |
| --- | --- | --- | --- |
| [iC-MU128](https://www.ichaus.de/product/ic-mu128/) | 离轴磁绝对位置编码器 | Magnetic Off-Axis Absolute Position Encoder，极距 1.28 mm | 片内集成霍尔用于双轨扫描；霍尔针对 1.28 mm 极距的主轨优化；片内做偏移、幅值与相位调理 |
| [iC-MHM](https://www.ichaus.de/product/ic-mhm/) | 霍尔角度编码器 | 14-Bit Absolute Angle Hall Encoder | 绝对角度输出，14 位 |
| [iC-MH16](https://www.ichaus.de/product/ic-mh16/) | 霍尔角度编码器 | 12-Bit Angular Hall Encoder, FlexCount® | 12 位；带 FlexCount 功能 |
| [iC-MA](https://www.ichaus.de/product/ic-ma/) | 霍尔角度编码器 | 8-Bit Angular Hall Encoder, Cascadable | 8 位；可级联 |
| [iC-MA3](https://www.ichaus.de/product/ic-ma3/) | 霍尔角度传感器 | Angular Hall Sensor with Sin/Cos Output, Cascadable | 输出正余弦；可级联 |
| [iC-TW29](https://www.ichaus.de/product/ic-tw29/) | 编码器处理器 | 26-Bit Encoder Processor with Interpolation and BiSS Interface | 26 位；带插值；带 BiSS 接口 |

这六颗的顺序本身就是一条链：iC-MA3 只出模拟正余弦，iC-MA 出 8 位数字角，iC-MH16 出 12 位，iC-MHM 出 14 位绝对角，iC-MU128 换成离轴磁轨的双轨扫描，iC-TW29 则站在最末端做插值与 BiSS 输出。客户可以整条链都买，也可以只买其中一段接自己的前端。

## 在编码器链上的位置

它站在「给编码器厂供零件」这一层：往上买晶圆代工，往下卖给光编与磁编整机厂、电机反馈系统厂，以及需要片上霍尔结构的工业客户。iC-MU128 的离轴（off-axis）定位很关键——它承认了「磁环装在轴侧、芯片不在轴端」这种装法，用双轨扫描（主轨定极距、副轨给绝对信息）解决离轴下的绝对位置。这对整机厂意味着磁环直径、极距与安装偏心成了设计变量，而不是芯片能吸收的误差。

能推理的是它的取舍：把校准（偏移、幅值、相位）尽量放进片内，把接口做成自家标准 BiSS 并推动它成为开放标准——接口一旦被主站接受，芯片就更容易被写进整机规格。**不能推理的是各整机厂内部用哪颗**，也不能从「iC-Haus 供货某厂」推出某款编码器的裸片来源，官网不公布客户名单与 BOM。

## 公开资料的边界

官网产品页只给一句话定位（含位数或极距），**未公开**：INL、角秒级精度、噪声密度、温漂、最大转速、延迟、供电与封装的完整参数——这些在需要登录下载的 Specification 里。产品组页面（Magnetic Encoder iCs）是前端渲染，本次没有取到完整料号表，上面六颗是逐页核对能打开的。BiSS 官方站 biss-interface.com 在核对日返回 503（维护中），因此本页只用 iC-Haus 公司页对 BiSS 的表述，不外链该站。报价与交期不公开。

## 官方资料

- [iC-Haus 官网](https://www.ichaus.de/)
- [公司介绍与历史（1984 年创办、BiSS、奖项）](https://www.ichaus.de/about-us/)
- [磁性编码器 IC 产品组](https://www.ichaus.de/productgroup/magnetic-encoder-ics/)
- [iC-MU128 产品页](https://www.ichaus.de/product/ic-mu128/)
- [iC-MHM 产品页](https://www.ichaus.de/product/ic-mhm/)
- [iC-MH16 产品页](https://www.ichaus.de/product/ic-mh16/)
- [iC-MA 产品页](https://www.ichaus.de/product/ic-ma/)
- [iC-MA3 产品页](https://www.ichaus.de/product/ic-ma3/)
- [iC-TW29 产品页](https://www.ichaus.de/product/ic-tw29/)
