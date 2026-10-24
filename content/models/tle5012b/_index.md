---
title: "TLE5012B"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 33
seed_count: 6
lastmod: "2026-10-24"
description: "TLE5012B 离轴安装误差排查：先核对磁场条件、完整型号、SSC 接入与自校准配置，再区分静态误差和动态延迟。附原厂资料及复现条件单。"
official_url: "https://www.infineon.com/part/TLE5012B-E5000"
related_companies: ["英飞凌"]
datasheet_url: "https://www.infineon.com/assets/row/public/documents/30/49/infineon-tle5012b-exxxx-datasheet-en.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-18；数据手册 Rev.2.1（2018-06-20）"
model_card: true
product_image: "/images/wiki/tle5012b-official.jpg"
product_image_caption: "TLE5012B 原厂产品／封装图"
product_image_source: "https://www.infineon.com/part/TLE5012B-E5000"
---

## 核心性能

### 产品介绍

TLE5012B是英飞凌磁角度传感器系列，利用GMR元件测量磁场方向，并将结果转换为数字角度。官网有多个后缀版本，接口与预配置须对应具体订货号。 [官方资料](https://www.infineon.com/part/TLE5012B-E5000)

### 核心参数

- **感应技术** GMR 磁角度检测
- **数字数据** 角度与状态读取
- **通信** SSC 等功能由 E5000 等具体后缀配置
- **订货范围** 增量及其他输出组合按对应引脚表

### 接口与输出

TLE5012B 与主控或驱动器的连接应以完整订货号、引脚表和时序章节为准。下面保留官方公开页已经确认的输出与编码信息；没有列出的接口不据系列习惯补写。

- **通信** SSC 等功能由 E5000 等具体后缀配置
- **订货范围** 增量及其他输出组合按对应引脚表

### 工作原理

以下解释本类器件在系统中的一般工作方式，具体集成功能以本型号官方资料为准。

旋转磁体使芯片感受到的磁场方向随轴变化。敏感元件把方向变化变成电信号，前端采样与数字电路根据两路或多路信息计算相位，最后输出绝对角度、脉冲或占空比。霍尔、AMR、GMR与TMR采用不同的敏感原理，不能只凭相同位数判断性能相同。

在轴安装通常把磁体放在轴端，离轴结构则把读头移到轴线以外，为中空走线留下空间。两种结构的场分布和误差不同，能否支持离轴必须看具体型号和磁路条件。

### 典型应用与使用条件

角度字长说明一圈分为多少个数字刻度，绝对精度说明读数离真实位置多远，噪声影响静止和低速时的波动，延迟影响运动中数据的新鲜程度。这四个量应分别阅读。

在伺服系统中，读取更快不一定得到更及时的新数据，还要确认传感器内部刷新和滤波。匀速补偿后的延迟也不能直接代表快速加减速时的跟踪误差。

要把产品放进实际设备，还要确认数据对应的物理位置和时刻。传感器读数、接口传输和控制器使用并非同一个环节；读数更新并不一定意味着刚完成一次新测量。协议校验可以发现部分传输错误，无法发现全部机械安装变化。

比较两个备选型号时，应在相同输入、温度、带宽和校准状态下看结果。分辨率、噪声、重复性与绝对误差各有定义；目录页的典型值也不应改写成每颗样品、所有条件下的保证值。某一功能能配置，不表示所有输出可以同时工作。

## 离轴安装后误差大，先确认什么？

TLE5012B 利用 GMR 元件测量磁场方向。能读到角度，不等于保证任意离轴磁路的机械角精度。数据手册的精度条件采用均匀平面磁场，并限定垂直分量为零，不能直接套到任意侧向安装。[原厂数据手册，第16–17页](https://www.infineon.com/assets/row/public/documents/30/49/infineon-tle5012b-exxxx-datasheet-en.pdf#page=16)

### 先留下条件，再判断误差

- **完整后缀与配置**：记录 E5000 等完整型号并读回配置，不能只写“TLE5012”。各后缀的接口和默认功能不同。[第45–46页](https://www.infineon.com/assets/row/public/documents/30/49/infineon-tle5012b-exxxx-datasheet-en.pdf#page=45)
- **接入是否正确**：SSC 是 SPI-compatible 的双向三线接口；核对 DATA 换向、帧结构、安全字与时序，不直接套任意四线 SPI 驱动。[第26–29页](https://www.infineon.com/assets/row/public/documents/30/49/infineon-tle5012b-exxxx-datasheet-en.pdf#page=26)
- **自校准修了什么**：AUTOCAL 不等于整圈离轴非线性校准。用户手册描述其用 X/Y 极值更新偏置与幅值同步参数，并对整圈运动和温度变化设条件；剩余周期误差仍需参考角验证。[用户手册入口，正文第22–23页，需 myInfineon 登录](https://www.infineon.com/de/gated/infineon-tle5012b-usermanual-en_13801894-eee3-4707-8a78-269c36379c18)
- **静态还是动态**：静止角度误差与转动后出现的误差分开记录；滤波、接口与预测配置影响动态表现，刷新周期不能直接当固定测量延迟。[第23–24页](https://www.infineon.com/assets/row/public/documents/30/49/infineon-tle5012b-exxxx-datasheet-en.pdf#page=23)

本站的起步建议是保存一张条件单：完整型号、磁体与充磁方向、相对转轴位置、气隙、供电、温度、转速、接口和配置；保留参考角与输出角的整圈原始记录。它是复现建议，不是原厂指定验收流程，也不能单凭一个 INL 数字确定根因。

### 沿问题继续查

- [先把在轴、离轴、气隙、偏心与倾斜说清楚](/wiki/basics/mounting/)
- [校准曲线为什么还需要独立条件验证](/tags/%E9%9D%9E%E7%BA%BF%E6%80%A7%E6%A0%A1%E5%87%86/)

## 官方资料

- [TLE5012B 原厂资料入口](https://www.infineon.com/part/TLE5012B-E5000)
- [TLE5012B 数据手册（官方 PDF）](https://www.infineon.com/assets/row/public/documents/30/49/infineon-tle5012b-exxxx-datasheet-en.pdf)
