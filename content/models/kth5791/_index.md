---
title: KTH5791
wiki: true
wiki_type: model
catalog_form: 芯片
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
model_card: true
description: KTH5791AQ3QNS 是鼠标滚轮专用3D Hall芯片，公开旧说明书提供正交AB输出、I²C通信，以及标准24格到可编程128格的滚轮配置。
wiki_rank: 308
catalog_type: 线性磁场
wiki_category: 线性磁场
official_url: https://chat.connteck.com/products/3d-hall/KTH5791/
catalog_source: https://chat.connteck.com/products/3d-hall/KTH5791/
search_aliases:
- KTH5791
datasheet_url: https://conntek.github.io/files/KTH5791AQ3QNS%20%E4%BA%A7%E5%93%81%E8%AF%B4%E6%98%8E%E4%B9%A6.pdf
datasheet_label: 数据手册原链接
document_version: 版本以链接文件名及原件为准；公开链接核对：2026-10-30
product_image: /images/catalog/kth5791-original-figure.png
product_image_caption: KTH5791 AQ3QNS滚轮应用与功能框图，2024-05旧公开稿（原手册第1页）
product_image_source: https://conntek.github.io/files/KTH5791AQ3QNS%20%E4%BA%A7%E5%93%81%E8%AF%B4%E6%98%8E%E4%B9%A6.pdf#page=1
---

## 核心参数

| 项目 | 内容与条件 |
| --- | --- |
| 输出 | 正交AB；支持I²C通信；该说明书未列UART或Z相引脚（手册第1、2页） |
| 滚轮格数 | 标准24格，可编程至128格；手册“格”原始口径；不改写为1024CPR，不与主控四倍频计数混同（手册第1页） |
| 模拟电源AVDD | 2.8～5.5 V；典型3.3 V；推荐工作条件（手册第3页） |
| 数字电源DVDD | 1.8 V～AVDD；独立数字电源；不代表主模拟电源可用1.8V（手册第3页） |
| IO电源VDDIO | 1.8 V～AVDD；数字IO电源；上拉与接收器电平按此核对（手册第3页） |
| 工作温度 | −40～85 °C；AQ3QNS消费级订货条目（手册第3、6页） |
| I²C | 快速模式400 kHz；第1页主要特性；不借用其他器件1MHz能力（手册第1页） |
| 封装 | QFN3×3-16L；裸露焊盘TAP为AVSS；16个引脚加热焊盘；第2页引脚表17行不表示17信号脚（手册第2、6页） |
| 复位与测试脚 | NRST外部拉高；TEST1/TEST2接地；TEST3浮空；MS睡眠未启用可浮空；只按该旧说明书；TEN测试使能定义未给用户固定接法，不自行补造（手册第2页） |

## 滚轮格数与AB计数分开核对

2024年5月公开说明书列标准24格，可编程至128格。主控的每周期计数、边沿计数和四倍频计数另有定义，不能把“格”直接换成CPR。应一圈慢转比对机械齿位、AB周期及累计计数，再验证快速滚动和反向运动。

## AB承担滚动输入，I²C配置另核

该说明书支持正交AB和I²C400kHz，没有UART或Z相引脚依据。A/B输出应在主控端按相序判断方向，尤其测试停在临界边沿、轻微往返和快速反转，避免滤波把有效边沿吞掉。

## 三路电源不能混写为1.8V工作

AVDD主模拟电源为2.8～5.5V，DVDD和VDDIO才可从1.8V起工作且不高于AVDD。低压主控接入时需分别安排电源、上拉和复位；公开旧说明书还要求NRST外部拉高，并区分应接地和应浮空的测试脚。

## 自适应感应仍需机构验收

芯片为在轴和离轴鼠标磁滚轮提供感知路径，磁体、轴承和齿位机构仍决定装配裕量与手感。应在目标机构上验证整圈稳定性、不同速度的计数和回转行为，不从非接触原理直接推出整机寿命。


## 公开资料与型号核对

参数限2024-05公开旧说明书KTH5791AQ3QNS；第1页Rev1.0、后页页眉Rev0，保留版本差异，不声称最新规格。

网页16～1024CPR、UART/Z、1.8V主电源和0.8mA等说法未获该手册支持；本页采用原手册24～128格、AB/I²C及分电源条件。

按完整型号、等级和版本选择手册。公开链接核对日期：2026-10-30。

- [KTH5791AQ3QNS 产品说明书.pdf](https://conntek.github.io/files/KTH5791AQ3QNS%20%E4%BA%A7%E5%93%81%E8%AF%B4%E6%98%8E%E4%B9%A6.pdf)
- [KTH5791_DS_CN_V2.0.pdf](https://chat.connteck.com/downloads/KTH5791/KTH5791_DS_CN_V2.0.pdf)
- [KTH5791_AN001_PowerTradeoff_CN_V1.0.pdf](https://chat.connteck.com/downloads/KTH5791/KTH5791_AN001_PowerTradeoff_CN_V1.0.pdf)
- [KTH5791_AN002_UART_Example_CN_V1.0.pdf](https://chat.connteck.com/downloads/KTH5791/KTH5791_AN002_UART_Example_CN_V1.0.pdf)
- [KTH5791_FAQ_CN_V1.0.pdf](https://chat.connteck.com/downloads/KTH5791/KTH5791_FAQ_CN_V1.0.pdf)
- [KTH5791_Schematic_V1.0.pdf](https://chat.connteck.com/downloads/KTH5791/KTH5791_Schematic_V1.0.pdf)
- [KTH5791_DS_EN_V2.0.pdf](https://chat.connteck.com/downloads/KTH5791/KTH5791_DS_EN_V2.0.pdf)

[来源产品页](https://chat.connteck.com/products/3d-hall/KTH5791/) · [昆泰芯型号目录](/wiki/?vendor=昆泰芯)

