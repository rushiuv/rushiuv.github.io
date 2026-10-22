---
title: "POSITAL"
wiki: true
wiki_type: "company"
wiki_rank: 94
seed_count: 2
lastmod: "2026-10-22"
description: "POSITAL 是 FRABA 集团的位置传感品牌，做整机与套件编码器；多圈靠韦根脉冲自供电、无电池无齿轮，36 mm 套件已改用 TMR 传感做到 18 位。"
official_url: "https://www.posital.com/"
wiki_category: "位置测量与编码器"
related_models: []
---

POSITAL 站在"整机编码器加套件编码器"这一层，背后是德国的 FRABA 集团。它最有辨识度的一件事是把韦根（Wiegand）效应做成了产品化的多圈计数方案：每转一个磁极翻转产生一个脉冲，脉冲本身既当信号又当能量，于是多圈不需要电池也不用齿轮组。读它的资料，重点看套件编码器的机械脚印和接口清单，而不是只看分辨率。

## 从 FRABA 的计数器件长出来的位置传感品牌

FRABA 官网把集团拆成三块：POSITAL 做位置与运动传感，UBITO 把韦根技术单独做成元件品牌，CODORMO 做商用门控自动化。POSITAL 官网自述有 60 年行业经验、产品在德国与美国设计、3 年质保、全球 50 多家分销商，标准生产周期 72 小时，部分产品可 24 小时加急；首页另写"超过 50 年位置与运动传感经验"、"超过一百万种可配置组合"、"20 多种通信接口"，绝对值编码器页面写的是"15 种以上接口"——同一家不同页面的口径并不完全一致，引用时按页看。[FRABA 集团](https://www.fraba.com/)；[为什么选 POSITAL](https://www.posital.com/en/why-posital)

韦根这条线的时间点官网写得很具体：2006 年开始把韦根技术做进产品，2013 年从当时全球最大的韦根丝制造商手里接过拉丝产线，2021 年另立 UBITO 品牌向外卖。官方给的参数是触发频率可到 40 kHz、脉冲能量不随频率衰减、无机械磨损。[韦根传感器页](https://www.posital.com/en/wiegand-sensors)

## 套件与整机两条产品线的公开规格

套件（kit）编码器是没有轴承、没有独立轴的模块：磁体环装在电机轴上，测量板装在机壳上。整机绝对值编码器则是带壳体与法兰的成品。下表数值取自各自系列页，属族级口径，具体订货型号还要再查。[套件编码器](https://www.posital.com/en/products/kit-encoders)；[绝对值编码器](https://www.posital.com/en/products/absolute-encoders)

| 系列/族 | 类型 | 公开分辨率 | 其他公开参数 |
| --- | --- | --- | --- |
| [36 mm 套件，实心轴](https://www.posital.com/en/products/kit-encoders) | 模块式绝对值 | 单圈 18 位（新一代 TMR 口径） | Ø36 mm、多种轴径、BiSS-C、BiSS Line、SSI |
| [36 mm 套件，空心轴](https://www.posital.com/en/products/kit-encoders) | 模块式绝对值 | 同上 | 轴 Ø4–10 mm（含 1/4" 与 3/8"）、与 E5 和 HEDS-5500 同安装脚印 |
| [22 mm 微型套件](https://www.posital.com/en/products/kit-encoders) | 模块式绝对值 | 页面写最高 33 位 | 轴 Ø2、3、4 mm、BiSS-C、BiSS Line、SSI |
| [通孔空心轴套件](https://www.posital.com/en/products/kit-encoders) | 模块式绝对值 | 最高 19 位 | 轴 30 mm 或 50 mm、BiSS-C、SSI |
| [多圈计数器](https://www.posital.com/en/products/kit-encoders) | 模块（供集成，官方注明不是给做编码器用） | 计数 40 位 | SPI、无电池无齿轮、带多圈错误检测与线检、温度 |
| [增量套件](https://www.posital.com/en/products/kit-encoders) | 模块式增量 | 最高 1024 PPR | 空心轴 Ø3–8 mm（含 1/4"）、兼容常见接口 |
| [现场总线经典整机](https://www.posital.com/en/products/absolute-encoders) | 整机绝对值 | 最高 31 位 | CANopen、Profibus、Modbus RTU、J1939、多种机械结构 |
| [增量整机](https://www.posital.com/en/products/kit-encoders) | 整机增量 | 任意脉冲数最高 32,768 PPR | 参数可编程 |

多圈怎么实现，官网给了两条口径：老一代是"每个磁极翻转触发一次韦根脉冲"，新一代 36 mm 套件则是"新 ASIC 加新一代韦根传感器"做自供电计数，转数记在非易失存储器里，断电期间转动也记；同时把位置敏感从霍尔换成了 TMR，官方新闻稿写明分辨率因此到 18 位、温漂与功耗更低。官方还单独写了一篇 TMR 原理页，说明 TMR 是两层铁磁层夹一层绝缘层的隧道磁阻结构。[36 mm 新一代套件](https://www.posital.com/en/news-events/36mm-kit-encoders-nextgen)；[TMR 技术说明](https://www.posital.com/en/the-benefits-of-tmr-technology-on-rotary-encoders)

## 在编码器链上的位置

POSITAL 是少见的把敏感材料做到上游的整机厂：韦根丝自产，传感器件自封，官方称"从合金熔炼到韦根传感器成品整条产线自控"。但它同样不公开 TMR 敏感元件与解算芯片的裸片来源——页面上只说"TMR 传感器"和"新 ASIC"，不写料号。所以看到"POSITAL 用 TMR"能推的是它接受了 TMR 的温漂与灵敏度特性，不能推出它内部用谁的桥。

下游决策权分两种：整机编码器由设备厂或系统集成商按法兰、接口、防护等级选；套件编码器的决策点在电机厂的定转子结构、板级空间和通信协议（BiSS-C 与 SSI 是主流），改一次封装要动电机端设计。对手方是同样做套件的海德汉、多摩川、iC-Haus 一类方案商。

## 公开资料的边界

系列页给分辨率上限、接口清单、轴径、安装脚印、多圈实现方式；**没有公开**逐型号的精度（±角秒或 ±度）、重复性、输出延时、抖动、启动转矩、轴承载荷，也没有报价与交期。要拿到这些必须用产品查找器生成具体型号再去下 datasheet；本页不填没有出处数字。

另有一处容易误读：套件页写增量 1024 PPR，而整机增量页写最高 32,768 PPR——两者是不同产品，不能互相套用。

## 官方资料

- [POSITAL 官网](https://www.posital.com/en/)
- [产品总览](https://www.posital.com/en/products)
- [套件编码器目录](https://www.posital.com/en/products/kit-encoders)
- [绝对值编码器目录](https://www.posital.com/en/products/absolute-encoders)
- [韦根传感器与产线](https://www.posital.com/en/wiegand-sensors)
- [TMR 技术在旋转编码器上的作用](https://www.posital.com/en/the-benefits-of-tmr-technology-on-rotary-encoders)
- [36 mm 套件新一代升级公告](https://www.posital.com/en/news-events/36mm-kit-encoders-nextgen)
- [为什么选 POSITAL（产能与交付口径）](https://www.posital.com/en/why-posital)
- [FRABA 集团与三个品牌](https://www.fraba.com/)
