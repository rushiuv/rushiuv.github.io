---
title: "希磁"
wiki: true
wiki_type: "company"
wiki_rank: 28
seed_count: 8
lastmod: "2026-10-22"
description: "希磁（Sinomags）：2013 年成立的磁传感 IDM，埃斯特磁做磁编码器，公开 PRBS 与游标码两套绝对角、30kHz 刷新。"
official_url: "https://www.sinomags.com/Index/index.html"
wiki_category: "传感器与测量前端"
related_models: []
---

希磁是磁传感的 IDM：晶圆自己做，芯片、码盘、编码器套件也自己做。2023 年单独成立的无锡埃斯特磁专做磁编码器，于是它有两条对外口径——希磁站点讲电流与运动传感器，埃斯特磁站点讲 PRBS 与游标码的编码器套件。读它的资料，先把这两个域名的分工分清，否则会把"同一颗料"当成两家公司的产品。

## 公司与品牌

安徽希磁科技股份有限公司（Sinomags），官网自述 2013 年成立，定位磁性传感器 IDM，技术覆盖霍尔与 AMR、GMR、TMR 全系列 xMR，业务布局为"德国先进晶圆制造 + 中国全面运营"。国内机构：蚌埠（传感器制造，经济开发区传感谷）、宁波（传感器研发，镇海区北欧工业园）、无锡（滨湖区高浪路 999 号）；德国主体为全资子公司 Sensitec GmbH，1999 年成立于韦茨拉尔，另在美因茨设机构，承担传感器晶圆设计与制造、以及编码器设计与制造。

集团结构：母公司安徽希磁科技旗下三家子公司——无锡乐尔科技、宁波希磁电子科技、德国 Sensitec；2023 年另投资成立无锡埃斯特磁科技有限公司，专做磁编码器研发。埃斯特磁的站点自述"承袭 Sensitec 晶圆设计制造实力"，并明确其产品包括磁性角度编码器、线性位移磁性编码器与磁传感器芯片。[希磁公司介绍](https://www.sinomags.com/Index/index.html)；[埃斯特磁关于我们](https://www.esstmags.com/about/)

## 编码器相关产品线与公开规格

两套站点的分辨率口径不一致，这点先说明：埃斯特磁产品总览写"23-26 位分辨率，支持 30 kHz 高刷新率"，角度编码器类目页写"最高 24 位分辨率，支持 30kHz"。下表按类目抄，两个数字都保留。

| 系列 | 类型 | 公开分辨率 | 其他公开参数 |
| --- | --- | --- | --- |
| [EAS-110 / EAS-111 / EAS-102](https://www.esstmags.com/products/angle-encoder/) | 标准型磁性角度编码器 | 类目页最高 24 位，总览页 23~26 位 | 大中空关节款与在轴款、30 kHz 刷新、PRBS 或游标码、抗冲击振动与油污粉尘 |
| [EAS-006A / EAS-006B / EAS-010B](https://www.esstmags.com/products/angle-encoder/integrated/single-turn-abs/270.html) | 一体式单圈绝对值 | 未逐型号公开位数 | 另有分体式，含电池多圈与机械有限多圈两种方案 |
| [EAS-J030KP-HD / J034 / J048 / J068](https://www.esstmags.com/products/encoder-kit/chip/prbs-dual/) | 关节中空式编码器套件（芯片级，PRBS 内外双编） | 未公开位数 | 按 30、34~48、48~68、68 以上关节分档、成套交付芯片与解码芯片、码盘与磁铁 BOM |
| [EAS-J034ZP-HD](https://www.esstmags.com/products/encoder-kit/chip/prbs-dual/) | 34~48 关节在轴式套件 | 未公开位数 | 与中空式同族，安装方式不同 |
| [ELS-001 / 004 / 005 / 008](https://www.esstmags.com/products/linear-encoder/) | 线性位移磁性编码器（TMR 读头 + 磁栅） | 未公开分辨率 | BiSS-C 与 SPI、长行程与微型短行程两类、面向灵巧手电缸与直线电机 |
| [BBT-A903P8-SM03P / BBT-A907D16JR / BBT-A907D0805 等](https://www.esstmags.com/products/sensor-chip/angle/) | xMR 角度与线性芯片 | 未公开位数 | 模拟或数字输出、部分型号支持功能安全、可单卖也可配套件 |
| [功能安全磁性角度编码器](https://www.esstmags.com/products/) | 双通道冗余 + 故障自检 | 未公开位数 | 满足 ISO 13849 PL d（官网口径）、覆盖单圈 / 机械有限多圈 / 电池多圈、分体式与可集成式两种形态 |

三条差异要点。**编码方案有两套**：PRBS 码与游标码并存，且都做成"内圈 + 外圈双编"，这是公开页面上少见的明确写法；**多圈有三条路**：电池多圈、机械有限多圈、以及单圈，官方按关节型号分档给；**接口清单是 SPI、BiSS-C、RS485、模拟量**，与光编常见的 SSI 不在同一套习惯里。

功能安全版只写"满足 ISO 13849 PL d"，没有给证书编号与评估机构；线性系列的 ELS-001 / 004 / 005 / 008 只给了型号与"长行程 / 短行程"的定位，具体量程与分辨率需索取样本。

## 在编码器链上的位置

希磁是少数把编码器直接卖给关节模组厂的磁传感 IDM：晶圆在 Sensitec 做，码盘自己做，套件按关节尺寸（30 / 34~48 / 48~68 / 68 以上）分档交付。这意味着它的客户是关节模组厂、人形与协作机器人整机，而不是散件分销商；套件里连码盘与磁铁的 BOM 都一起给，把客户的机械设计工作量降到装上去就行。

不能推断的：套件里那颗解码芯片的型号与来源（自研、Sensitec 老料还是第三方，公开页面都没写）；某家关节客户用了它——公开资料只给应用领域，不给客户名；也不能把"23-26 位"当作有效精度，它只是分辨率口径。

## 官方资料

- [希磁科技官网](https://www.sinomags.com/Index/index.html)
- [希磁芯片电流传感器目录](https://www.sinomags.com/iproducts/107.html)
- [埃斯特磁产品总览](https://www.esstmags.com/products/)
- [埃斯特磁关于我们（集团与 Sensitec）](https://www.esstmags.com/about/)
- [磁性角度编码器类目](https://www.esstmags.com/products/angle-encoder/)
- [一体式单圈绝对值 EAS-006A](https://www.esstmags.com/products/angle-encoder/integrated/single-turn-abs/270.html)
- [PRBS 内外双编芯片级套件](https://www.esstmags.com/products/encoder-kit/chip/prbs-dual/)
- [xMR 角度传感器芯片](https://www.esstmags.com/products/sensor-chip/angle/)
- [线性位移磁性编码器](https://www.esstmags.com/products/linear-encoder/)
