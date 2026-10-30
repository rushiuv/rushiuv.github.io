---
title: KTM1301
wiki: true
wiki_type: model
catalog_type: 磁开关
catalog_form: 芯片
wiki_rank: 128
seed_count: 1
lastmod: '2026-10-30'
description: KTM1301 是全极性TMR微功耗磁开关，采用CMOS推挽输出；50Hz、1.6kHz与连续工作档分别对应不同功耗，适合按事件速度选择状态检测方案。
official_url: https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/magnetoresistiveSwitchSeries/index.html
related_companies:
- 昆泰芯
datasheet_url: https://chat.connteck.com/downloads/KTM1301/KTM1301_Datasheet_CN.pdf
datasheet_label: 数据手册原链接
wiki_category: 磁开关与状态检测
document_version: 版本以链接文件名及原件为准；公开链接核对：2026-10-30
model_card: true
catalog_source: https://chat.connteck.com/products/switches/KTM1301/
search_aliases:
- KTM1301
product_image: /images/catalog/ktm1301-browser-original.jpg
product_image_caption: KTM1301 原厂SOT-23-3L封装图，公开手册第1页
product_image_source: https://chat.connteck.com/downloads/KTM1301/KTM1301_Datasheet_CN.pdf
---

## 核心参数

| 项目 | 内容与条件 |
| --- | --- |
| 原理与逻辑 | TMR全极性磁开关；CMOS推挽输出；首页明确，不采用来源矩阵开漏标注；有磁动作输出低，无磁释放输出高（手册第1页） |
| 供电范围 | 1.8～5.5 V；工作电压，按完整版本确认IO负载（手册第1页） |
| 低功耗工作点 | 50 Hz：160 nA；1.6 kHz：600 nA；连续：1.9 µA；均为VDD=3.0 V首页标注；最低电流与最高频率不能合并（手册第1页） |
| 动作与释放门限档 | BOP/BRP：±45/±36、±30/±21、±18/±12、±9/±6、±7/±4 Gs；首页列五组成对门限，完整公差需核电磁参数表，不将2 Gs当所有档回差（手册第1页） |
| 温度与封装 | −40～125°C；SOT-23-3L、TO-92S；首页产品声明，各封装脚序另核（手册第1页） |
| ESD | HBM 8 kV；首页器件声明，不代表整机测试（手册第1页） |


参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTM1301%20Series%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)。

## 纳安级版本测的是什么

KTM1301以TMR检测磁场门限，输出磁体是否到位。它不是连续位置编码器，不提供SPI角度。50Hz版本用低平均电流保持周期性检测，适合电池供电的低速状态事件。

## 电流与频率需成对读取

公开手册首页分别标注50Hz、1.6kHz与连续工作的电流，不将最低电流与最高频率合并。旧目录把连续版本写作5000Hz，本次尚未用完整时序表复核。50Hz和1.6kHz换算的周期约20ms和625µs，计算周期也不是最坏响应保证。

## 磁门限决定装配窗口

五档动作和释放门限形成不同磁迟滞。磁体尺寸、极性、轨迹和气隙决定机械触发距离；选择更低场门限时还应核对外部磁场及周围磁性件的影响。

## 怎样接入并验收

CMOS输出的电平和负载需与主控输入匹配，主控睡眠状态还要确认唤醒方式。测试最弱磁体、最大气隙、正负磁极以及全温动作/释放位置；快速掠过事件另测捕获率。

## 官方资料

- [KTM1301 原厂资料入口](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/magnetoresistiveSwitchSeries/index.html)
- [KTM1301 数据手册（官方 PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTM1301%20Series%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)

## 选型补充

### 事件检测模式影响电池预算

低频采样适合缓慢开合，高速经过或计数则要求更短响应窗口。平均电流不能脱离模式、供电和输出负载理解，整机电池寿命还需计入主控、无线和电池自放电。

### 全极性也要检查动作与释放

南北极均可触发不表示全部姿态下的动作距离一致。应分别测试两种磁极、接近角度和装配间距，记录动作/释放门限与机构行程的对应关系，防止临界位置重复跳变。

### 水表气表计数要验证最短磁脉冲

旋转磁体的有效触发区决定事件持续时间。最高机械速度下应把磁场波形、开关输出和主控计数同步比较，检查遗漏和重复计数；器件频率不能独自证明整机计量正确。


## 公开资料与型号核对

PDF第1页与详情概述确认CMOS推挽，来源矩阵写开漏，不能混用。五档BOP/BRP应成对读取，不将网页2Gs回差泛化到所有档位。

本次目视核对首页功能与工作点，连续版本输出频率、公差及完整时序仍以相应电参数表为准。

按完整型号、等级和版本选择手册。公开链接核对日期：2026-10-30。

- [KTM1301_Datasheet_CN.pdf](https://chat.connteck.com/downloads/KTM1301/KTM1301_Datasheet_CN.pdf)

[来源产品页](https://chat.connteck.com/products/switches/KTM1301/) · [昆泰芯型号目录](/wiki/?vendor=昆泰芯)
