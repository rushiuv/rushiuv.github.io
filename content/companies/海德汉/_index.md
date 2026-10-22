---
title: "海德汉"
description: "海德汉 HEIDENHAIN：德国 Traunreut 的位置测量与数控厂，角度编码器按带轴承、模块式、与精密轴承组合三种结构分家，另有一条电机反馈线。"
wiki: true
wiki_type: "company"
wiki_rank: 13
seed_count: 15
lastmod: "2026-10-22"
official_url: "https://www.heidenhain.com/"
related_models: []
related_companies: []
---

海德汉站在位置测量器件这一层，做的是整机与模块，不是单颗芯片：带内置轴承的角度编码器、只有读头与刻度件的模块式编码器、给电机做反馈的旋转编码器，加上直线光栅与数控系统。读它的资料，第一件事是分清“角度编码器”和“旋转编码器”这两条目录——前者服务精密回转轴，后者服务电机反馈，精度与安装方式不是一回事。

## 公司与品牌

主体为 Dr. Johannes Heidenhain GmbH，私营企业，总部在德国巴伐利亚州 Traunreut。按公开的企业沿革：1889 年 Wilhelm Heidenhain 在柏林开金属蚀刻厂，做模板、铭牌与刻度尺；1948 年 Johannes Heidenhain 博士（Otto Hahn 的学生）在 Traunreut 创办现在的公司。维基百科记载，按公司自己的说法，2006 年它在 43 个国家设有销售点，员工约 7000 人，其中 2600 人在 Traunreut 主厂。[企业资料（维基百科）](https://en.wikipedia.org/wiki/Heidenhain)

产品面比编码器宽：直线编码器、角度编码器、旋转编码器、长度测量、测头、数控系统与数显装置。对编码器选型的人来说，这个宽度的意义是同一家公司把“机床的位置环”从上位控制一直到刻度尺都做了，器件的接口与协议因此是自洽的一套，不用跨厂商拼。[官网](https://www.heidenhain.com/)

中文常用叫法为海德汉。

## 编码器相关产品线与公开结构

官网把角度编码器按机械形式分三支，这个分法本身就是选型的第一个判断点：机械基准由谁提供。

| 系列族 | 结构形式 | 公开定位 | 其他公开信息 |
| --- | --- | --- | --- |
| [RCN 2001／5001、RCN 6000、RCN 8001](https://www.heidenhain.com/products/encoders/angle-encoders/integral-bearing/rcn-8001) | 带内置轴承的绝对式角度编码器 | 精密回转轴、机床转台 | 用户只需连轴与法兰，轴承与联轴误差由器件内部承担 |
| [RON 200、RON 785／786／886 与 RPN 886](https://www.heidenhain.com/products/encoders/angle-encoders/integral-bearing/ron-200) | 带内置轴承的增量式角度编码器 | 回转轴增量测量 | 与绝对式并列，靠参考点建立基准 |
| [ROD 200、ROD 780／880、ROC 2000、ROC 7000](https://www.heidenhain.com/products/encoders/angle-encoders/integral-bearing/rod-200) | 带内置轴承，增量与绝对两条 | 通用回转轴 | 同一机械形式下的不同测量原理 |
| [ECN 2000](https://www.heidenhain.com/products/encoders/angle-encoders/integral-bearing/ecn-2000) | 带内置轴承的绝对式，小尺寸 | 紧凑安装 | 与 RCN 系列同族但体积更小 |
| [ECA 4000、ECM 2400、ERA 4000](https://www.heidenhain.com/products/encoders/angle-encoders/modular/eca-4000) | 模块式：刻度鼓或刻度盘 + 读头 | 大直径与异形回转轴 | 机械基准由用户的轴与轴承提供，读头与刻度分开装 |
| [ERM 2000、ERO 2000、ERP 1000、ERP 1080 Dplus](https://www.heidenhain.com/products/encoders/angle-encoders/modular/erp-1000) | 模块式，增量与绝对 | 空间受限的回转轴 | 与 ECA 同属模块式，区别在测量原理与外形 |
| [MRP、MRS](https://www.heidenhain.com/products/encoders/angle-encoders/modules) | 角度编码器模块，与精密轴承组合 | 高精度回转轴 | 由用户提供轴承，厂商提供测量模块 |
| [ECN／EQN 400、ECN／EQN 1000、ERN 100／400／1000／1023、KCI 419 Dplus、HR 1120](https://www.heidenhain.com/products/encoders/rotary-encoders/external/overview) | 外置式旋转编码器 | 电机与一般自动化反馈 | 与角度编码器分属两条目录，绝对与增量并存 |

三支结构的差别不在分辨率，而在误差归谁。带内置轴承的产品把轴承误差、联轴偏心与刻度误差一起封在器件里，用户拿到的是一个系统精度；模块式把刻度装到用户的轴上，机械误差就回到机械设计那边，读头只对“看到的刻度”负责。这也是同一家公司的产品为什么能同时出现在转台和大型回转轴上。

要判断档位，必须打开对应系列的产品信息 PDF（各系列页的下载区），并把误差定义对齐——系统精度、刻度精度、信号周期误差、重复性是四个不同的量。中文资料里“角度编码器”与“旋转编码器”常被混用，检索时保留原厂分类才不会把电机反馈件和精密测角件放在一起比。

## 在编码器链上的位置

它买光学元件、专用解算芯片、轴承与刻度基材，做成的成品直接进机床与测量设备。对做芯片的人来说，海德汉是“整机与模块”那一层：能看到的是它对刻度周期、扫描方式、接口与功能安全的选择，看不到的是它内部用谁的裸片。

**不能推断**的是 BOM 与裸片来源。**可以推断**的是它在结构分家上的取舍：同一精度目标下，把机械基准放进器件还是留给用户，决定了它是卖给机床厂的总装线，还是卖给做转台本体的专业厂。

## 官方资料

- [海德汉官网](https://www.heidenhain.com/)
- [角度编码器目录](https://www.heidenhain.com/products/encoders/angle-encoders)
- [带内置轴承的角度编码器](https://www.heidenhain.com/products/encoders/angle-encoders/integral-bearing)
- [模块式角度编码器](https://www.heidenhain.com/products/encoders/angle-encoders/modular)
- [角度编码器模块（MRP／MRS）](https://www.heidenhain.com/products/encoders/angle-encoders/modules)
- [旋转编码器目录](https://www.heidenhain.com/products/encoders/rotary-encoders)
- [企业沿革与规模（维基百科）](https://en.wikipedia.org/wiki/Heidenhain)
