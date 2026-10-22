---
title: "Hengstler"
wiki: true
wiki_type: "company"
wiki_rank: 122
seed_count: 1
lastmod: "2026-10-22"
description: "Hengstler（亨士乐）：德国 Aldingen 的整机编码器厂，ACURO 绝对值、RI58 增量系列覆盖 SSI、BiSS、EtherCAT 等接口。"
official_url: "https://www.hengstler.com/"
wiki_category: "位置测量与编码器"
related_models: []
---

Hengstler 是德国巴登-符腾堡州 Aldingen 的编码器与工业计数器件制造商，做的是**可以直接装在轴上、直接对外的整机编码器**，不是编码器芯片厂。对做芯片或做选型的人来说，它的价值在于公开的规格页：同一家公司同时给光学单圈、光学多圈、无齿轮磁多圈和增量四个方向，型号族之间的取舍写得比多数厂商清楚。

## 公司与品牌

公司名为 Hengstler GmbH，地址 Uhlandstr. 49, D-78554 Aldingen，官网自述建于 1846 年，创始人是当地钟表匠 Johannes Hengstler，最早批量生产的是钟表音簧。此后产品线沿"计数与工业控制"展开：1912 年开始精密车削件，1926 年收购 Efunda 进入计数装置，1957 年推出 400 meter 系统，1961 年卖掉钟簧产线，1962 年在英国设立第一家海外子公司，1969 年起做考勤计时（Flextime）。[公司概况](https://www.hengstler.com/company)；[历史年表](https://www.hengstler.com/about-us/history)

股权关系在官方页面写得很直白：1995 年起属于 Danaher，2016 年 7 月随 Fortive 分拆，2025 年 6 月 Fortive 再把传感业务整体拆出为独立公司（Ralliant）。这条链条对采购的意义是：**品牌名与法律主体、售后归属可能分属不同法人**，询价与文档入口要先确认走哪一个实体，不要把 Fortive 时代的资料当成当前主体签的条款。[公司概况](https://www.hengstler.com/company)

它在中国的常见叫法是"亨士乐"。同一集团在美国还有 Dynapar 品牌，部分 ACURO 页面由 Dynapar 站点承载，例如 AM34 的英文产品页落在 dynapar.com 上，型号命名一致但文档入口不同。

## 编码器产品线与公开规格

官网把旋转编码器分成绝对值、增量、伺服电机编码器、SinCos 四类。下表数值全部取自各系列产品页的公开参数，用来判断"这一族大概在什么档位"，不是选型保证——分辨率与接口的组合还要看具体订货型号。

| 系列 | 类型 | 公开分辨率 | 其他公开参数 |
| --- | --- | --- | --- |
| [ACURO AC36](https://www.hengstler.com/products/rotary-encoders/absolute-encoders/ac36) | 光学绝对值，实心轴 6 mm | 单圈最高 22 位 | −40…+100 °C、连续 10000 rpm、齿轮式光学多圈、BiSS 或 SSI、可选 1 Vss 正余弦、500 kHz 带宽 |
| [ACURO AD36](https://www.hengstler.com/products/rotary-encoders/absolute-encoders/ad36) | AC36 的空心轴版，面向无刷伺服 | 22 位单圈 + 12 位多圈 | 8 mm 通孔、安装与 15 号旋变兼容、−40…+120 °C、10000 rpm、SSI 或 BiSS、1 Vpp 正弦、500 kHz 带宽 |
| [ACURO AM34](https://www.hengstler.com/products/rotary-encoders/absolute-encoders/am34) | 超薄安装深度 | 单圈 16~20 位，多圈 12 位（4096 转） | 最高 12000 rpm、温度到 120 °C、SSI/BiSS 带电子铭牌、模拟输出 256 SinCos 周期/转 |
| [ACURO AR60](https://www.hengstler.com/products/rotary-encoders/absolute-encoders/ar60) | 磁式，电子多圈 | 最高 28 位 | 免维护无电池电子多圈、−40…+100 °C、安装深度 32 mm、铝壳 |
| [ACURO AC58](https://www.hengstler.com/products/rotary-encoders/absolute-encoders/ac58) | 50 mm 外壳绝对值 | 最高 34 位（22 位单圈 + 12 位多圈，视接口） | −40…+100 °C、SSI、BiSS、EtherCAT、Profinet、Profibus、CANopen、CANlayer2、DeviceNet、Interbus、SUCOnet |
| [ICURO RI58](https://www.hengstler.com/products/rotary-encoders/incremental-encoders/ri58) | 通用增量 | 10000 线，四倍频后 40000 步 | 最高 IP67、耐冲击、法兰与接插件选项多、RI58-T 到 100 °C；防爆场合见 RX 70-71 |

三个值得注意的公开差异：**AM34 是唯一明确给 256 SinCos 周期/转的系列**，模拟输出自成一路，便于外部独立做安全评估；**AD36 的卖点是"与 15 号旋变同安装界面"**，替换旋变不用改电机端结构；**AR60 是无齿轮、无电池的电子多圈**，靠磁感应而不是齿轮组记圈，官方给的安装深度 32 mm。这三条都是从产品页抄下来的，不是同类产品都具备的共性。

官网产品页给的是系列级典型参数：分辨率上限、温度范围、转速、接口清单、外壳与轴径。**没有公开**的是逐型号的精度（±角秒）、重复性、启动扭矩、轴承载荷曲线，以及各接口下的实际输出延时；这些要下对应订货号的 datasheet 才能拿到，系列页只写 Download Datasheet。需要跨品牌比较时，先把两边的误差定义（±角秒、±LSB、重复性）对齐，再谈数字。

## 在编码器链上的位置

Hengstler 站在"整机编码器"这一层：它采购光学或磁的敏感元件、专用解算芯片与光电元件，做成带壳体、轴承、法兰和现场总线的成品。所以看到"Hengstler 用某方案"时，**能推理的是它对精度、温度、接口和成本的取舍，不能推理出它内部具体用哪家的裸片**——官网不公布 BOM。反过来，做芯片的人看它的手册最有用的是三件事：多圈怎么实现（齿轮光学还是电子磁多圈）、模拟正弦通道留不留、以及现场总线那 11 种接口在同一系列里如何分档。

对整机厂与产线工程师，它的信息价值在"同尺寸不同原理"的横向对照：AC58 与 AR60 都是绝对值，前者光学 34 位、后者磁式 28 位但无齿轮无电池；AC36 与 AD36 是同一代光学的实心轴与空心轴两种装法。这些差异在选型时会直接决定轴端结构、线缆，以及是否接受多圈停电后要靠电池维持。

## 官方资料

- [Hengstler 官网](https://www.hengstler.com/)
- [公司概况与集团归属](https://www.hengstler.com/company)
- [历史年表](https://www.hengstler.com/about-us/history)
- [绝对值编码器目录](https://www.hengstler.com/rotary-encoders/absolute-encoders)
- [ACURO AC58 系列页](https://www.hengstler.com/products/rotary-encoders/absolute-encoders/ac58)
- [ACURO AC36 系列页](https://www.hengstler.com/products/rotary-encoders/absolute-encoders/ac36)
- [ACURO AD36 系列页](https://www.hengstler.com/products/rotary-encoders/absolute-encoders/ad36)
- [ACURO AM34 系列页](https://www.hengstler.com/products/rotary-encoders/absolute-encoders/am34)
- [ACURO AR60 系列页](https://www.hengstler.com/products/rotary-encoders/absolute-encoders/ar60)
- [ICURO RI58 系列页](https://www.hengstler.com/products/rotary-encoders/incremental-encoders/ri58)
