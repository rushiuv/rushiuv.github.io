---
title: VCS2395
description: VCS2395 是平面二维全极AMR开关，采用开漏输出，60Hz采样和典型0.45µA平均电流；接入方式与VCS238x推挽输出不同。
wiki: true
wiki_type: model
wiki_rank: 240
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 圣邦微
wiki_category: 磁开关
catalog_vendor: 圣邦微
catalog_type: 磁开关
catalog_form: 芯片
search_aliases:
- VCS2395
- VCS2395S
official_url: https://www.sg-micro.com/cn/product/VCS2395
document_version: 2025-09 Rev.A，8页
model_card: true
datasheet_url: https://www.sg-micro.com/rect/assets/44618042-c8aa-424d-906e-c08938df5bd7/VCS2395.pdf
datasheet_label: 原厂数据手册（PDF）
product_image: /images/wiki/sgmicro/5e862c9d90ab495f.png
product_image_caption: VCS2395 官方页使用的原厂产品页共用SOT-23-3封装示意
product_image_source: https://www.sg-micro.com/api/assets/47789a8d-5b7e-4ba1-87f7-349777e2cc09
---

## 核心参数

依据[原厂手册](https://www.sg-micro.com/rect/assets/44618042-c8aa-424d-906e-c08938df5bd7/VCS2395.pdf)（2025-09 Rev.A，8页）。典型值、最大值与适用条件分别保留。

| 参数 | 数值与适用条件 |
| --- | --- |
| 逻辑与输出 | 平面二维360°全极感应；开漏输出；输出为磁状态，不是角度编码（手册第1、5页） |
| 供电／温度 | 2.0～5.5 V；−40～125°C；推荐工作范围，典型值除特别说明外25°C（手册第1、2、4页） |
| 平均电流 | 典型0.45 µA，最大1.0 µA；VDD=3.3V，按表列条件，不当所有工作点保证（手册第4页） |
| 采样／时序 | 典型60 Hz；典型休眠16.7 ms；典型启动3.5 ms；周期数值不等于最坏响应，快速掠过事件另验（手册第4页） |
| BOP动作点 | 典型±15 Gs，表列最小±5/最大±35 Gs；TA=25°C、VDD=2.0～5.5V（手册第4页） |
| BRP释放点 | 典型±11 Gs，表列最小±2/最大±25 Gs；TA=25°C、VDD=2.0～5.5V（手册第4页） |
| 磁迟滞 | 典型4 Gs，最小1/最大15 Gs；同磁参数条件，不当全温门限范围（手册第4页） |
| 低电平／上拉 | VOL最大0.1 V；典型应用图使用10kΩ上拉；VOL条件负载10mA、VDD=3.3V；10kΩ是应用图示例，不是任意线缆的固定值（手册第1、4页） |
| 封装／订货 | SOT-23-3；VCS2395S；1=VDD，2=OUT，3=GND；按TOP VIEW连接（手册第2、3页） |

## 同为全极开关，输出驱动仍要区分

VCS2395是开漏输出，VCS2381/2382/2383为推挽。使用本型号需要为信号高电平提供合适上拉，并核对允许的输出电压、接收器门限与负载；两类器件不能只按封装相同直接换料。

## 60Hz的意义是缩短采样间隔

相比15Hz的VCS238x，60Hz对应更短的采样间隔，同时典型电流也提高。选择应围绕机构最短事件和电池预算，而不是把典型功耗或频率各自拿出来排名；脉冲捕获仍需在目标机构验证。

## 上拉和输出电容共同决定边沿

手册典型电路给出10kΩ上拉和1nF输出电容。实际板上电容、线缆及接收器输入会改变上升边沿，电阻也决定低电平时的灌电流；应在高低压、温度和最长线缆条件下记录波形。

[VCS238x系列](/models/vcs238x/)采用推挽输出，比较时应同时核对驱动方式、采样频率和磁阈值。

## 资料版本与边界

- 磁阈值最小/典型/最大表在25°C条件下，尚不能作为全温保证窗口。
- 本页没有把60Hz换算周期当作最坏响应或漏检保证。

## 官方资料

- [VCS2395产品页](https://www.sg-micro.com/cn/product/VCS2395)
- [VCS2395数据手册（2025-09 Rev.A，8页）](https://www.sg-micro.com/rect/assets/44618042-c8aa-424d-906e-c08938df5bd7/VCS2395.pdf)
