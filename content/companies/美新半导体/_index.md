---
title: "美新半导体"
wiki: true
wiki_type: "company"
wiki_rank: 45
seed_count: 5
lastmod: "2026-11-05"
description: "美新半导体（MEMSIC）：1999 年成立的 MEMS IDM，AMR 磁编码器 MDA2000BT 给 21bit 绝对角、INL ±0.07°。"
official_url: "https://www.memsic.com/cn"
wiki_category: "传感器与测量前端"
related_models: ["MXC3638AL"]
---

美新半导体是编码器链上的芯片厂：AMR 磁敏元件与 ASIC 一体，出货形态是 TSSOP-16 的裸芯片，客户自己做板、自己配磁铁。它同时是惯性 MEMS 的老牌 IDM（热式加速度计起家），所以读它的资料要分清两条线——磁编码器这条线与角度测量直接相关，惯性那条线只在姿态与振动上间接相关。

## 公司与品牌

美新半导体（MEMSIC）官网自述 1999 年成立，有二十余年 MEMS 研发与量产积累，在中国、欧洲、美国设有生产与研发机构，自述为中国最早的 IDM 模式惯性传感器供应商之一。关键沿革：2007 年 12 月 14 日成为全球第一家纳斯达克上市的 MEMS 公司；2021 年 1 月完成十亿余元人民币 A 轮融资；累计 260 余项境内外专利。2025 年 10 月，美新半导体（天津）有限公司入选天津市第七批专精特新"小巨人"。

官网给出两项市占口径，属公司自述、无第三方数据：AMR 地磁传感器在全球安卓手机市场占有率超 40%，加速度传感器市占率突破 30%。在编码器方向，官网另有专门页面把"高精度 AMR 磁编码器"的角度测量精度写到 ±0.07°，并称其抗振动与低温漂适配工业机器人关节控制。[公司概况](https://www.memsic.com/cn/about)；[专精特新公告](https://www.memsic.com/cn/news-112)

## 编码器相关产品线与公开规格

磁编码器这条线的公开型号只有一个，但参数给得比多数同行细：SPI 绝对角位数、ABZ 线与 UVW 对极都写成了可编程范围。

| 系列 | 类型 | 公开分辨率/精度 | 其他公开参数 |
| --- | --- | --- | --- |
| [MDA2000BT](https://www.memsic.com/cn/mag-encoder-88) | AMR 磁编码器芯片 | SPI 绝对角 21 bit、PWM 12 bit、INL 典型值（自校准）<±0.07° | ABZ 增量 1~16384 线任意可编程、UVW 1~16 对极可编程、4 线 SPI、3.3~5.0 V、TSSOP-16 |
| [磁编码器芯片平台](https://www.memsic.com/cn/mag-encoder) | AMR + 集成 ASIC | 输出高精度绝对值角度位置 | 供电 3~5.5 V；官方称相较霍尔式精度高、噪声低、温漂低，可替代部分光编场景 |
| [MHA100KN / MHA182AS-S / MHA183AS](https://www.memsic.com/cn/hall-switch) | 低功耗霍尔开关 | 磁滞窗口 5 Gauss | 1.65~5.5 V、工作电流典型 2.5 µA、−45~85 °C、DFN 1.0×1.4×0.37 mm（另有 SOT23 / SOT553） |

三个可以拿来比对的点。[MDA2000BT 产品页](https://www.memsic.com/cn/mag-encoder-88)

2026 年 8 月 18 日芜湖产线启动的发布会上，美新又发了一颗新的 AMR 磁编码器方案，官方口径是角度 INL 小于 ±0.07°、分辨率 21 bit、最高可测 12 万 RPM，3×3 mm QFN 封装，内嵌自校准算法，接口覆盖 SPI、PWM、UVW、ABZ，并带模组参考设计，官方点名高端伺服、无人机云台与机器人灵巧手。发布稿没有给型号，封装与转速也都和上表的 MDA2000BT 不同，是否同族要等型号与手册公开后才能对上。

## 在编码器链上的位置

美新是芯片厂：它把 AMR 敏感元件与 ASIC 做在一颗里，卖裸芯片给编码器模组厂、电机厂与关节模组厂。

客户类型从规格能看出来：21 bit SPI 绝对角加 ABZ/UVW/PWM 三套输出、TSSOP-16 封装，买方属于"自己画板、自己装磁铁"的那一类。晶圆来源官网只写 IDM 全链条、未写具体产线；客户名也没点，只写"已与多家机器人头部企业展开合作"。

## 官方资料

- [美新半导体官网](https://www.memsic.com/cn)
- [公司概况](https://www.memsic.com/cn/about)
- [磁编码器芯片目录](https://www.memsic.com/cn/mag-encoder)
- [MDA2000BT 磁编码器芯片](https://www.memsic.com/cn/mag-encoder-88)
- [霍尔开关](https://www.memsic.com/cn/hall-switch)
- [国家级专精特新"小巨人"公告](https://www.memsic.com/cn/news-112)
- [2026 年 8 月芜湖新品发布（AMR 磁编码器、六轴 IMU、eOIS 驱动）](https://www.news.cn/tech/20260819/f62155f431ac44dfa9aacb4b594ab605/c.html)
