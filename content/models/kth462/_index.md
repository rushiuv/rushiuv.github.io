---
title: KTH462系列
description: KTH462N 是二维锁存霍尔开关系列，KTH4621 输出两个轴的独立状态，KTH4622 输出速度与方向；A/B/C 版本对应 XY/XZ/YZ
  敏感平面。
wiki: true
wiki_type: model
wiki_rank: 208
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
wiki_category: 磁开关
catalog_vendor: 昆泰芯
catalog_type: 磁开关
catalog_form: 芯片
search_aliases:
- KTH4621
- KTH4622
- KTH462N
official_url: https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/highsensitive2Dhallswitch/index.html
document_version: 版本以链接文件名及原件为准；公开链接核对：2026-10-30
model_card: true
catalog_source: https://chat.connteck.com/products/
datasheet_url: https://conntek.github.io/files/KTH462N%20Series%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf
datasheet_label: 数据手册原链接
product_image: /images/catalog/kth462n-package.jpg
product_image_caption: KTH462N 系列 SOT-23-6L，原手册第1页
product_image_source: https://conntek.github.io/files/KTH462N%20Series%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf
catalog_level: 系列
aliases:
- /models/kth462n/
---

KTH462系列提供双输出磁状态检测。选型首先区分两路输出的含义，再选敏感平面与采样档；两根信号线相同不代表主控可以沿用同一解释。

## 型号与核心异同

| 基础型号 | OUT1／OUT2功能 | 敏感平面选项 | 采样版本选项 |
| --- | --- | --- | --- |
| KTH4621 | 两个敏感轴独立锁存状态 | A=XY；B=XZ；C=YZ | XAM或XAT，按完整订货号 |
| KTH4622 | 速度／方向输出 | A=XY；B=XZ；C=YZ | XAM或XAT，按完整订货号 |

## 采样、电气与接线条件

- **供电**：2.5～5.5 V；典型3.3 V；工作状态；电参数表TA=25°C，VDD=3.3 V，除特别说明外（手册第8页）
- **工作温度**：−40～125 °C；参考工作条件（手册第8页）
- **XAM 平均电流/采样频率**：典型32.3 µA；典型30 Hz；电流条件TA=25°C、VDD=2.5 V；30 Hz属于XAM工作模式（手册第8页）
- **XAM 唤醒时间**：典型945 µs；XAM系列工作状态，TA=25°C、VDD=3.3 V，除特别说明外（手册第8页）
- **XAT 平均电流/采样频率**：典型1.9 mA；典型1.7 kHz；电流条件TA=25°C、VDD=2.5 V；XAT为连续工作版本（手册第1、8、12页）
- **输出低电平**：典型0.01 V，最大0.05 V；IOUT=1 mA；XAM/XAT表；TA=25°C、VDD=3.3 V，除特别说明外（手册第8页）
- **动作场 BOP**：典型25 Gs，最大40 Gs；最小列未给值；OUT1/OUT2；TA=25°C、VDD=3.3 V；南极方向按图14-1，不把符号脱离敏感方向（手册第9页）
- **释放场 BRP**：最小−40 Gs，典型−25 Gs；最大列未给值；OUT1/OUT2；TA=25°C、VDD=3.3 V；磁体方向按图14-1（手册第9页）
- **磁滞 BHY**：典型50 Gs；BHY=\|BOP−BRP\|；OUT1/OUT2；同磁参数表条件（手册第9页）
- **引脚**：1 VDD；2 TEST接地；3 NC接地；4 OUT1；5 GND；6 OUT2；KTH462NXXX-ST6；注意名称NC但本手册仍要求接地（手册第3页）
- **电源去耦**：1 µF，靠近VDD；手册应用电路建议，不是电气极限（手册第1页）

## 先画磁场轨迹，再验证速度和方向

锁存状态需要相反磁极完成切换，磁体远离不一定释放。按所选XY、XZ或YZ平面画出正负场轨迹，再用目标磁体检查完整往返是否越过两路门限。

机械转速要结合每圈磁极数换成事件频率，再核算采样、主控滤波和最短驻留时间。XAM的低电流与XAT的高采样率属于不同工作点，不能合成单一性能。

KTH4622在有磁环境上电时的初始输出取决于当时磁场。主控应区分初始电平和真实运动事件，在正转、反转、临界停留和重新上电下核对两路波形。

## 资料版本

本页依据公开KTH462N系列手册。首页HBM 4kV与绝对最大额定表±6kV口径不一致，可靠性条件需按适用正式版本确认。


## 官方资料

明确型号、配置与版本后使用对应文件。


- [官方产品入口](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/highsensitive2Dhallswitch/index.html)
- [数据手册原链接](https://conntek.github.io/files/KTH462N%20Series%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
