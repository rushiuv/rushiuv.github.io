---
title: "KTH78系列"
linkTitle: "KTH78"
catalog_vendor: "昆泰芯"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["KTH7801", "KTH7803", "KTH7812", "KTH7813", "KTH7814", "KTH7815", "KTH7816", "KTH7823"]
description: "KTH78 是 KTH78xx 霍尔角度编码器系列简称，覆盖 KTH7801、KTH7812、KTH7813、KTH7814、KTH7815、KTH7816、KTH7823 等成员。下列具体数值仅标注其对应型号。"
wiki: true
wiki_type: "model"
wiki_rank: 9
seed_count: 16
lastmod: "2026-10-24"
related_companies: ["昆泰芯"]
official_url: "https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html"
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7812%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
datasheet_label: "KTH7812 数据手册（系列代表型号）"
document_version: "KTH7812 官方公开手册，32 个 PDF 页面；其他成员以系列页同名手册为准"
model_card: true
product_image: "/images/wiki/kth78-diagram.webp"
product_image_caption: "图片来源：KTH7812 官方数据手册，第 5 个 PDF 页面，功能框图局部。本图仅代表 KTH7812。"
product_image_source: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7812%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
---

## 核心性能

### 产品介绍

KTH78 是博客现有标签使用的系列简称，对应昆泰芯 KTH78xx 霍尔绝对角度编码器。它包含面向不同应用和输出配置的多个型号，不能把“KTH78”直接当作一个完整订货料号。官网列有 KTH7801、KTH7812、KTH7813、KTH7814、KTH7815、KTH7816、KTH7823 等成员。[系列资料](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html)

系列共同的用途，是读取旋转磁场并生成数字位置或增量信号。各成员的接口组合、CRC 版本、噪声表现及温度等级存在差异。本页先解释共同架构，再以公开手册较完整的 KTH7812 说明如何阅读，具体设计应进入完整型号的手册。

![KTH7812 官方功能框图](/images/wiki/kth78-diagram.webp)

*图片来源：KTH7812 官方数据手册，第 5 个 PDF 页面，功能框图局部。本图仅代表 KTH7812。*

### 核心参数

- **系列类型** 霍尔磁角度编码器
- **角度编码** 系列以 16 位绝对角度为主要特征；CRC 版本可能使用不同帧格式
- **代表型号** KTH7812，工业用途
- **代表型号接口** 四线 SPI、ABZ、UVW，依配置使用
- **KTH7812 增量输出** ABZ 4～4096 步／圈；UVW 1～8 对极
- **KTH7812 温度** −40～125°C
- **KTH7812 封装** QFN-16L
- **状态功能** 磁场诊断、阈值配置与 MTP，按型号确认
- **接口版本** KTH7815公开资料存在不同接口口径，单独记录于其型号页；不把系列全部接口当作每个型号共有
- **KTH7812 数据更新** 1 µs，依对应手册条件
- **KTH7812 INL** ±0.35°，依对应校准及测试条件

### 接口与输出

KTH78系列 与主控或驱动器的连接应以完整订货号、引脚表和时序章节为准。下面保留官方公开页已经确认的输出与编码信息；没有列出的接口不据系列习惯补写。

- **系列类型** 霍尔磁角度编码器
- **角度编码** 系列以 16 位绝对角度为主要特征；CRC 版本可能使用不同帧格式
- **代表型号接口** 四线 SPI、ABZ、UVW，依配置使用
- **KTH7812 增量输出** ABZ 4～4096 步／圈；UVW 1～8 对极
- **接口版本** KTH7815公开资料存在不同接口口径，单独记录于其型号页；不把系列全部接口当作每个型号共有

### 工作原理

霍尔感应结构测量磁场分量，模拟前端与 ADC 把信号转换成数字量，角度计算电路据此生成位置。随后经过零点、方向与滤波配置，位置可以通过串行接口读取，也可以转换为 ABZ 或 UVW 脉冲。手册还列有 MTP 存储和磁场强度诊断，供系统配置与状态检测使用。

这一结构使同一系列能适配不同控制端。有的控制器希望直接得到绝对角度，有的使用定时器累计 AB 脉冲，还有的需要 UVW 换向信号。接口是否存在，要看完整料号、封装与引脚复用，不能把系列页列出的所有接口相加，视作每颗芯片都能同时输出。

在轴安装常见于轴端磁饼，离轴安装则将传感器移到中心之外。系列资料列出对离轴和多对极磁体的支持，这说明存在可设计的应用空间；具体角度映射、参考位置及安装公差仍应按对应型号和磁路核对。

### 典型应用与使用条件

选型时可先确定接口，再确定性能与环境要求。需要 SPI 与 ABZ 的工业电机、需要 SSI 的位置采集系统、希望用少量引脚读取 PWM 的装置，可能对应不同的后缀。先锁定信号接收方式，通常比从系列名称猜型号更有效。

噪声应连同滤波和带宽阅读。系列页面列有不同噪声与截止频率组合，说明低噪声或快速响应需要结合具体配置比较。评估时可同时观察静止位置散布、低速爬行和快速换向，避免只根据某一个静态读数判断动态能力。

机械上需要核对磁体极性、尺寸、气隙和敏感中心；电气上需要核对工作电压范围，而不是将“兼容 3.3 V／5 V”简单理解成任何中间电压均满足同一规格。CRC 校验可以帮助发现通信数据错误，不能单独证明整个位置传感系统达到某一安全等级。

本系列适合绝对位置检测、闭环步进、无刷电机与门控机构等应用。这里提供的 PDF 是 KTH7812 的代表手册，其他成员请从系列官网选择同名文档，避免拿一颗芯片的引脚表去接另一颗。

系列选型可以形成一个简短但有效的记录：完整料号、封装、接口、角度帧格式、供电模式和目标温度。读者以后再次看到 KTH78 标签，就可以从系列介绍快速进入适合自己的具体文档，而不必重复猜测每个后缀的作用。

对 CRC 版本，通信帧长度里的一部分可能用于校验。不能仅按总位数推导角度分辨率，而应检查位置字段到底占多少位。同样，增量口的可编程步数与绝对口的数据位数分别受各自配置控制，规格表应将它们列为两个字段。

更换系列成员时，尤其需要复核上电后的默认输出状态和配置保存方式。即便封装尺寸和感应原理相同，接收器所见的接口、电平或帧格式也可能不同。先通过明确的一圈位置和计数实验确认映射关系，再进入闭环控制，有助于减少调试中的相互干扰。

## 官方资料

- [官方产品介绍](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html)
- [下载KTH7812 数据手册（系列代表型号）（官方 PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7812%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
- 资料版本：KTH7812 官方公开手册，32 个 PDF 页面；其他成员以系列页同名手册为准
