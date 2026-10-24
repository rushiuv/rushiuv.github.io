---
title: "KTM1301"
wiki: true
wiki_type: "model"
catalog_type: "磁开关"
catalog_form: "芯片"
wiki_rank: 128
seed_count: 1
lastmod: "2026-10-24"
description: "KTM1301是昆泰芯全极型TMR磁开关系列，用于非接触状态感知。"
official_url: "https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/magnetoresistiveSwitchSeries/index.html"
related_companies: ["昆泰芯"]
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTM1301%20Series%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁开关与状态检测"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
---

## 核心性能

### 产品介绍

KTM1301是昆泰芯全极型TMR磁开关系列，用于非接触状态感知。TMR桥与ASIC集成，根据磁场跨越门限切换逻辑输出。 [官方资料](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/magnetoresistiveSwitchSeries/index.html)

### 核心参数

- **检测极性** 全极型磁开关
- **输出** 开关状态
- **配置选项** 低功耗与不同采样频率版本
- **磁门限及输出结构** 随完整后缀变化

### 接口与输出

KTM1301 与主控或驱动器的连接应以完整订货号、引脚表和时序章节为准。下面保留官方公开页已经确认的输出与编码信息；没有列出的接口不据系列习惯补写。

- **输出** 开关状态
- **磁门限及输出结构** 随完整后缀变化

### 工作原理

以下解释本类器件在系统中的一般工作方式，具体集成功能以本型号官方资料为准。

磁场跨过工作点时，开关输出切换；磁场回到释放点后，状态恢复。两个门限之间的回差帮助抑制边界抖动。单极、全极和锁存器件对磁极及翻转条件的定义不同，应先确认类别。

微功耗器件可能采用周期唤醒检测，通过降低测量占空比减少平均电流。这样做会引入检测等待时间，目标物运动过快时，不能只看静态磁场足够强就认定一定会触发。

### 典型应用与使用条件

开关给出的是状态，而非连续位置。把它用于门磁、盖位或转速计数时，磁体公差、气隙、方向和门限温漂共同决定触发位置；需要连续位移时应选择线性测量链。

要把产品放进实际设备，还要确认数据对应的物理位置和时刻。传感器读数、接口传输和控制器使用并非同一个环节；读数更新并不一定意味着刚完成一次新测量。协议校验可以发现部分传输错误，无法发现全部机械安装变化。

比较两个备选型号时，应在相同输入、温度、带宽和校准状态下看结果。分辨率、噪声、重复性与绝对误差各有定义；目录页的典型值也不应改写成每颗样品、所有条件下的保证值。某一功能能配置，不表示所有输出可以同时工作。

## 官方资料

- [KTM1301 原厂资料入口](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/magnetoresistiveSwitchSeries/index.html)
- [KTM1301 数据手册（官方 PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTM1301%20Series%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
