---
title: "maxon"
wiki: true
wiki_type: "company"
wiki_rank: 60
seed_count: 3
lastmod: "2026-10-22"
description: "maxon（瑞士，1961 年）做精密驱动系统，自研磁、光、电感三类编码器并只作为电机组合件出售；ENX EMT 22 mm 给 17 位单圈与 65536 圈无电池多圈。"
official_url: "https://www.maxongroup.com/"
wiki_category: "机械传动与精密驱动"
related_models: ["ENX 22 EMT"]
---

maxon 站在“精密驱动系统”这一层，编码器是它自己设计并生产的一类传感器件，但有一条关键商业规则写在官网上：**传感器只能作为电机组合的一部分出售**，并且按电机型号在供货工厂装机。这条规则决定了它在编码器链上的位置——不是可以单独供货的器件厂，而是把编码器锁进电机平台的一层。对做编码器芯片的人，这意味着入口在电机项目，不在器件询价单上。

## 1961 年起的瑞士驱动厂，家族控股、八个产地

官网公司页给出的数字很直接：1961 年起做精密驱动，全球 3200 名员工，在八个地点生产驱动系统的全部关键部件，用的是自研设备与产线；定位是瑞士质量、全球生产，应用覆盖医疗技术、航空航天、机器人、交通与工业 4.0。[maxon 公司页](https://www.maxongroup.com/en/company)

股权与人事在公开新闻里有明确记录：创始家族 Braun 家族正在换代，Karl-Walter Braun 博士留任董事会但让出主席位，由女儿 Bianca Braun 博士接任；运营端，任 CEO 十五年的 Eugen Elmiger 在服务公司 35 年后把运营管理交给 Andreas Richter。两条都来自官网新闻稿，对采购的含义是：合同主体与人名在变，产品平台与命名规则没变。[董事会与财年新闻](https://www.maxongroup.com/en/news-and-events/news/new-chair-of-the-board-of-directors-and-stable-fiscal-year-at-maxon-301688)

## 磁、光、电感三条原理并列在一张选型表里

官网传感器页把编码器、直流测速机与旋变放在一起，用一张对照表给出 12 个系列的原理、信号类型、分辨率与尺寸。下表照抄这张表的公开参数，cpt 是每转计数（counts per turn），属于官网自己的口径。

| 系列 | 原理 | 信号类型 | 公开分辨率 | 尺寸 | 其他公开属性 |
| --- | --- | --- | --- | --- | --- |
| [ENX MAG](https://www.maxongroup.com/en/drives-and-systems/sensors) | 磁 | 增量 | 1–256 cpt | 4–10 mm | 装在电机内、可在线配置 |
| [ENX GAMA](https://www.maxongroup.com/en/drives-and-systems/sensors) | 磁 | 增量 | 12–16 cpt | 10 或 13 mm | 抗辐射 |
| [ENX IMR](https://www.maxongroup.com/en/drives-and-systems/sensors) | 磁 | 增量 | 64–1024 cpt | 8–32 mm | 不集成在电机内、空心轴 |
| [ENX EASY](https://www.maxongroup.com/en/drives-and-systems/sensors) | 磁 | 增量或绝对 | 1–1024 cpt，或 4096 步 | 10 或 16 mm | 可配置 |
| [ENX EASY INT](https://www.maxongroup.com/en/drives-and-systems/sensors) | 磁 | 增量或绝对 | 1–1024 cpt，或 4096 步 | 13–22 mm | 可灭菌 |
| [ENX EMT](https://www.maxongroup.com/en/drives-and-systems/sensors) | 磁 | 绝对 | 17 位加 65536 圈 | 22 mm | 多圈、无电池 |
| [TSX MAG](https://www.maxongroup.com/en/drives-and-systems/sensors) | 磁 | 增量 | 1792–2560 cpt | 40 mm | 配 EC-i 与无框 DT 电机 |
| [Encoder EASY](https://www.maxongroup.com/en/drives-and-systems/sensors) | 磁 | 增量或绝对 | 128–1024 cpt，或 4096 步 | 16 mm | 与 ENX EASY 同档 |
| [ENX RIO](https://www.maxongroup.com/en/drives-and-systems/sensors) | 光学 | 增量 | 512–65536 cpt | 16 mm | 反射式结构 |
| [Encoder Rio](https://www.maxongroup.com/en/drives-and-systems/sensors) | 光学 | 增量 | 1024–32768 cpt | 16 mm | 与 ENX RIO 同族 |
| [Encoder HEDL](https://www.maxongroup.com/en/drives-and-systems/sensors) | 光学 | 增量 | 100–5000 cpt | 22–70 mm | RS422 线驱动 |
| [Encoder MILE](https://www.maxongroup.com/en/drives-and-systems/sensors) | 电感 | 增量 | 256–6400 cpt | 45–90 mm | 集成在 EC flat 电机内 |

三条原理的差别，官网自己写得比多数厂商清楚：磁编是转轴上一小块永磁体加定子侧磁通检测，卖点是抗脏污与性价比，同一原理也能做成绝对值；光编是 LED 透射码盘或反射码盘（RIO 系列走反射），卖点是分辨率上限与抗磁干扰；电感编码器（MILE）用变压器传高频交变场、由结构化铜盘做角度调制，官网把它定位为 EC flat 扁平电机的补充，卖点是抗脏污兼抗磁与电干扰、可高速。这三种原理出自同一家公司，是做原理取舍时最有用的对照样本。

## 组合件规则把编码器的决策权交给电机平台

官网写得很硬：传感器不能单独买，只能作为组合件的一部分；且因为共振原因，传感器主要装在带连续轴的电机上，安装方式按电机型号定，在供货工厂完成。这两句话的实际含义有三层：编码器与电机是同一个订货单元；客户拿不到“单买一颗编码器回去自己装”的路径；选型的谈判起点是电机型号而不是编码器型号。

因此**能推的是取舍，不能推的是裸片**：官网给出原理、分辨率档位、尺寸、可灭菌或抗辐射这类属性，能推出哪种应用该选哪条原理；但它不公布编码器内部的芯片来源、码盘工艺、精度指标（INL、重复性、延时），这些要拿具体型号的数据表。把它当“某家芯片的客户”来读是错的——它自己就是编码器的设计方。

官网给的是系列级参数：原理、信号类型、分辨率区间、尺寸、是否集成、是否可配置，以及应用受限项（只能随电机买、在工厂安装）。**没有公开**逐型号的精度（角秒或 mrad）、重复性、启动扭矩、最高转速与输出延时；磁编磁体的材料与充磁方式、光编码盘的线宽、电感铜盘的层数也不公开。这些在具体订货号的数据表与电机图纸里。

## 官方资料

- [maxon 官网](https://www.maxongroup.com/en)
- [公司页（1961 年、3200 人、八个产地）](https://www.maxongroup.com/en/company)
- [传感器总览与 12 系列对照表](https://www.maxongroup.com/en/drives-and-systems/sensors)
- [董事会主席交接新闻](https://www.maxongroup.com/en/news-and-events/news/new-chair-of-the-board-of-directors-and-stable-fiscal-year-at-maxon-301688)
- [CEO 交接新闻](https://www.maxongroup.com/en/news-and-events/news/leadership-change-at-the-maxon-group-ceo-eugen-elmiger-hands-over-operational-management-to-andreas-richter-306082)
