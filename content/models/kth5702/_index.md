---
title: KTH5702
wiki: true
wiki_type: model
catalog_form: 芯片
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
model_card: true
description: KTH5702 的已核对AQ1手册将其定义为X/Y两轴Hall旋转位置传感器，集成CORDIC输出XY平面绝对角度；测量模式和转换配置决定响应与功耗。
wiki_rank: 302
catalog_type: 数字角度
wiki_category: 二维角度
official_url: https://chat.connteck.com/products/3d-hall/KTH5702/
catalog_source: https://chat.connteck.com/products/3d-hall/KTH5702/
search_aliases:
- KTH5702
datasheet_url: https://conntek.github.io/files/KTH5702AQ1_DS_CN.pdf
datasheet_label: 数据手册原链接
document_version: 版本以链接文件名及原件为准；公开链接核对：2026-10-30
product_image: /images/catalog/kth5702-original-figure.png
product_image_caption: KTH5702 AQ1产品概述与功能框图（原手册第1页）
product_image_source: https://conntek.github.io/files/KTH5702AQ1_DS_CN.pdf#page=1
---

## 核心参数

| 项目 | 内容与条件 |
| --- | --- |
| 感知轴与角度输出 | 2D：X/Y轴；16位ADC；16位XY平面绝对角度；原厂AQ1手册第1、5页；不是网页介绍的XYZ三轴输出（手册第1、5页） |
| 工作供电 | 2.8～5.5 V；典型3.3 V；推荐工作条件；第6节总说明为25°C测量，温度额定另列（手册第4页） |
| IO供电 | 1.8 V～VDD；数字IO电源，不把1.8V作为芯片主电源下限（手册第4页） |
| 工作温度/封装 | −40～125 °C；QFN3×3-16L；第26页KTH5702AQ1QNS订货表（手册第4、26页） |
| 测量峰值电流 | 典型4.89 mA；VDD=3.3 V；25°C；不是全周期平均电流（手册第4页） |
| 待机与空闲电流 | 持续模式待机典型61.7 µA；唤醒睡眠待机典型2.4 µA；空闲典型1.4 µA；VDD=3.3 V；25°C；不同状态不能相互替代（手册第4页） |
| 水平磁场线性范围 | −130～+130 mT；Gain=20；25°C；第1页建议平面磁场大于20mT（手册第1、4页） |
| 角度输出RMS噪声 | 典型0.98°/0.28°/0.128°；B=20 mT、25°C；分别magnOsr=0/1/3且digCtrl=0；不是绝对角度精度（手册第4页） |
| 角度输出RMS噪声（高过采样） | 典型0.065°；B=20 mT、25°C、magnOsr=3、digCtrl=3；须连同转换时间权衡（手册第5页） |
| 启动时间 | 典型4 ms；25°C；手册时间参数表（手册第5页） |
| 单轴转换时间 | 可编程165～33349 µs；25°C；不能把最快单轴时间当作整次XY角度输出周期（手册第5页） |
| 整次测量时间 | 持续/唤醒模式：m×TCONVM+108 µs；单次模式另加220 µs；25°C、measTime=0，手册默认m=2；108µs测量结束、220µs空闲激活均为典型表列（手册第5页） |
| SPI | Mode 3：CPOL=1、CPHA=1；最大5 MHz；25°C、VDD=3.3 V；不是源页其他型号的10MHz（手册第15页） |
| I²C | 标准模式最大100 kHz；快速模式最大400 kHz；25°C、VDD=3.3 V（手册第16页） |
| 数据就绪 | INT高时可回读；INT低表示正在测量；持续感应模式；应搭配INT读取，不以固定总线轮询假设数据有效（手册第8、17页） |

## 两轴角度先对应机构旋转平面

AQ1手册明确使用X、Y磁场分量求XY平面角度，不是三轴XYZ位置输出。机构应使目标旋转在此平面产生可用场矢量，并检查全圈幅值、偏心和倾斜的影响。数字角度位宽不能代替整圈准确度。

## 转换噪声与响应需要成组选择

手册给出不同magnOsr与digCtrl下的角度RMS噪声，同时列出可编程单轴转换时间。一次角度测量默认包含两轴转换和结束时间，不能用最快单轴时间宣称整个角度输出刷新率；应根据动作速度选择配置并验证动态滞后。

## 持续模式依INT判断何时读取

持续感应模式中，INT低表示正在测量，INT高才允许回读；若未及时读取，下一次测量开始时INT会再次拉低。唤醒睡眠模式的阈值事件则保持中断直至主机读回，主控需区分两种行为。修改配置前按手册先进入空闲模式。

## AQ1引脚与订货后缀对应

KTH5702AQ1QNS采用QFN3×3-16L封装。SPI使用Mode 3，A0/A1在SPI模式需接地；不用TRIG时也接地。VDD_IO可低于主电源，接口上拉和主控电平应按IO电源检查。


## 公开资料与型号核对

KTH5702AQ1手册适用于AQ1QNS，定义为二维XY、QFN3×3-16L和−40～125°C；网页另列三轴、TSSOP14、150°C和30KSPS，与该版本手册不一致。

该手册明确2D X/Y、QFN16、−40～125°C、SPI最高5MHz和I²C400kHz，不能把KTH5701参数或其他等级直接迁移。

按完整型号、等级和版本选择手册。

- [KTH5702AQ1_DS_CN.pdf](https://conntek.github.io/files/KTH5702AQ1_DS_CN.pdf)
- [KTH5702AQ1_DS_CN.pdf](https://chat.connteck.com/downloads/KTH5702/KTH5702AQ1_DS_CN.pdf)

[来源产品页](https://chat.connteck.com/products/3d-hall/KTH5702/) · [昆泰芯型号目录](/wiki/?vendor=昆泰芯)

