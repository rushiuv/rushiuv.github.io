---
title: "中芯国际"
wiki: true
wiki_type: "company"
wiki_rank: 51
seed_count: 4
lastmod: "2026-10-22"
description: "中芯国际（00981.HK/688981.SH）总部上海的纯晶圆代工厂，官网按电源模拟、混合信号射频与 eNVM 分平台，不列各平台节点数字。"
official_url: "https://www.smics.com/"
wiki_category: "制造工艺与产业分工"
related_models: []
---

中芯国际在编码器链上不测角度，它站在"把角度芯片做成硅片"那一步：霍尔或磁阻前端、ADC、驱动级、校准系数存储，都要落到某条工艺平台上流片。看它有价值的不是排名，而是平台分类、8/12 英寸厂的地理分布，以及它明确不公开的那几项。

## 公司与品牌

中芯国际集成电路制造有限公司，证券代码 00981.HK / 688981.SH，总部上海。官网自述为"世界领先的集成电路晶圆代工企业之一"，向全球客户提供 8 英寸和 12 英寸晶圆代工与技术服务，在美、欧、日与中国台湾设营销办事处。纯代工，不做自有品牌芯片。[公司简介](https://www.smics.com/site/about_summary)

厂房按尺寸分列：上海 200mm 厂与 300mm 厂、北京 300mm 一期与二期、天津 200mm 厂、深圳 200mm 厂。流片之外，光罩、IP、后段辅助设计（凸块、晶圆探测、封测）与多项目晶圆也列为配套。[厂房清单](https://www.smics.com/site/factory_summary)

## 平台按用途分类，节点数字要另找

官网工艺平台页只按用途切块，不给制程节点、金属层数或电压档位表。下表是各平台页写的覆盖内容：

| 平台 | 官网公开写的覆盖内容 |
| --- | --- |
| [电源/模拟](https://www.smics.com/site/productdetail/2886) | 双极、高压 LDMOS、精密模拟无源器件，eFuse/OTP/MTP |
| [混合信号/射频](https://www.smics.com/site/productdetail/2991) | 与逻辑工艺兼容，提供 RF SPICE 模型与 PDK |
| [eNVM](https://www.smics.com/site/productdetail/2964) | OTP、MTP、嵌入式 EEPROM、嵌入式闪存四类 |
| 功率器件 IGBT | 工业变频、白电、轨交、电动汽车、电网与光伏 |
| [汽车电子](https://www.smics.com/site/productdetail/3023) | 按 IATF 16949 与 AEC-Q100 管控，多次通过 VDA 6.3 审核 |

前两类定噪声与驱动能力，eNVM 决定校准系数怎么存；但 0.18 µm、55 nm、40 nm 这类节点，各平台页一个字都没有。

## 在编码器链上的位置

代工厂卖工艺与设计套件，不参与决定光学还是磁。做芯片的一侧，影响排期的是多项目晶圆与光罩服务：一次 MPW 拿几颗 die、几层掩模、多久回片，比平台宣传更能解释项目节奏。反过来，从"某颗角度芯片在中芯流片"推不出精度——精度由码盘、敏感元件与校准算法定，工艺只左右匹配、温漂与噪声底。设计侧要拿的是 PDK，官网写明与 EDA 供应商合作提供逻辑、混合信号与射频 PDK。[制程/技术文件](https://www.smics.com/site/design_process)

## 官方资料

- [中芯国际官网](https://www.smics.com/)
- [公司简介](https://www.smics.com/site/about_summary)
- [晶圆代工厂介绍（厂房清单）](https://www.smics.com/site/factory_summary)
- [晶圆代工解决方案](https://www.smics.com/site/solution)
- [制程/技术文件与 PDK](https://www.smics.com/site/design_process)
- [电源/模拟平台](https://www.smics.com/site/productdetail/2886)
- [混合信号/射频平台](https://www.smics.com/site/productdetail/2991)
- [嵌入式存储 eNVM 平台](https://www.smics.com/site/productdetail/2964)
- [汽车电子平台](https://www.smics.com/site/productdetail/3023)
