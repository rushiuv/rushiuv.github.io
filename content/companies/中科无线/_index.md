---
title: "中科无线"
wiki: true
wiki_type: "company"
wiki_rank: 68
seed_count: 3
lastmod: "2026-10-22"
description: "中科（深圳）无线半导体：2018 年由中国科大校友团队创办，做机器人小脑 IDPU 与 GaN 关节驱动芯片，官网发展历程称 2026 年发布磁编码芯片 CT-21X。"
official_url: "https://www.ctunite.com/"
wiki_category: "芯片与信号链"
related_models: ["CT-21X"]
---

中科无线（CT-Unite）站的是"关节驱动与运动控制芯片"这一层。它把 FOC、电流环与角度输入塞进同一颗关节芯片，同时自己做 GaN 功率级；2026 年官网发展历程里又添了一句"发布我国首颗磁编码芯片 CT-21X"，等于从驱动端往反馈端伸了一只手。读它的资料要分清两类：一类有产品页与短规格（功率与驱控芯片），一类只有一句发布记录（磁编码芯片），两者不能用同一种可信度对待。

## 中国科大校友团队 2018 年在深圳起家

中科（深圳）无线半导体有限公司，2018 年成立，官网自述由中国科大校友团队创办，"基于化合物材料研发及生产的高端模拟芯片设计公司"，累计专利 100 余项、论文 250 篇，地址在深圳南山。子公司中科蓝谷半导体（广西）在 2022 年让南宁封装工厂投产，2026 年 4 月又设重庆特色工艺 wafer 制造中心。官网列出的奖项包括 2025 年科技部颠覆性技术奖与工信部"中国芯"年度重大突破奖，2025 年 11 月获第二十届"中国芯"芯火新锐产品奖。中文常叫"中科无线"或"中科半导体"。[公司概况与发展历程](https://www.ctunite.com/index.php?g=&m=index&a=about)

## 产品线分四块，磁编码芯片目前只有一句发布记录

| 型号 | 类型 | 公开关键指标 | 其他公开参数 |
| --- | --- | --- | --- |
| [CT-2001A](https://www.ctunite.com/index.php?g=product&m=index&a=products&id=9) | 机器人小脑 IDPU ASIC | 官网原文：多线程并发延时低于 20 ns；内置 FOC 模拟计算单元、可编程数字滤波、神经网络自适应控制 | 1 MB 片内 Flash、512 KB SRAM、21 个数字通讯接口、10 余种密码算法硬件加速 |
| [CT-1901](https://www.ctunite.com/index.php?g=product&m=index&a=products) | GaN HEMT | 650 V E-MODE，DFN 5 mm×6 mm | 增强型硅基 GaN 功率晶体管，主推超高开关频率 |
| [CT-2102](https://www.ctunite.com/index.php?g=product&m=index&a=products) | 同步整流功率开关 | 集成 60 V N 沟道功率 MOS | 官方写与 CT-1005 组合用于 PD 20 W 手机快充 |
| [CT-1005](https://www.ctunite.com/index.php?g=product&m=index&a=products) | PWM 控制器 | SOP8，4.9 mm×3.9 mm | 用于快充充电器、电池充电器与适配器电源 |
| [CT-21X](https://www.ctunite.com/index.php?g=&m=index&a=about) | 磁编码芯片 | 发展历程 2026 条目原文："发布我国首颗磁编码芯片 CT-21X" | 产品列表未见该型号规格页，位数、接口、精度、封装均未公开 |

同一条产品线上还有一组官方宣称的性能：智能体执行器系列"内置 FOC 算法"、"工作结温高达 225 °C"，小脑芯片在 40 mm 小型化关节里"扭矩提升 45%、硬件成本直降 30%"。这些是宣传口径，页面没给测试条件，本页不复述为结论。

## 在编码器链上的位置

它是"驱控一体"路线的代表之一：把角度输入、FOC 与功率级放进同一个关节模块，用一颗芯片决定整条反馈链的接口形状。这对编码器厂的含义很直接——角度不再是独立第三方器件，而是关节芯片定义的一个引脚功能，它说 ABZ 就是 ABZ，说 SPI 就是 SPI，编码器只能去适配。反过来，自研磁编码芯片说明它想把反馈端也握在自己手里：先定义接口，再自己供料。

能推理的是它的取舍方向：接口简单、成本低、能在片上做校准与温度补偿的方案更符合它的产品逻辑。**不能推理的是 CT-21X 的敏感原理、位数、精度与校准方式**——公开资料只有一句发布记录，连产品页都没有，任何具体参数都是猜的。

## 公开资料的边界

官网产品页给的是功率与驱控芯片的短规格（电压、封装、拓扑、接口数量），没有 datasheet 级参数表，也没有精度、温漂、可靠性数据。CT-21X 目前只有发展历程里的一句话：无产品页、无位数、无接口清单、无量产状态。产品列表可按分页翻到十余页，磁编码产品不在其中。报价、交期、月产能不公开。要拿到 CT-21X 的真实规格，只能等官网补产品页，或走样本申请通道要手册。

## 官方资料

- [CT-Unite 官网首页](https://www.ctunite.com/)
- [公司概况与发展历程](https://www.ctunite.com/index.php?g=&m=index&a=about)
- [产品列表](https://www.ctunite.com/index.php?g=product&m=index&a=products)
- [机器人运动控制（CT-2001A 小脑芯片）](https://www.ctunite.com/index.php?g=product&m=index&a=products&id=9)
- [智能体执行器分类页](https://www.ctunite.com/index.php?g=product&m=index&a=products&id=60)
- [新闻资讯](https://www.ctunite.com/index.php?g=news&m=index&a=news)
