---
title: "KTH7815"
series_parent: "kth78"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 127
seed_count: 1
lastmod: "2026-10-24"
description: "KTH7815是KTH78系列的16位工业霍尔角度器件。公开资料存在不同接口口径，须以具体订货号和适用手册确认。"
official_url: "https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html"
related_companies: ["昆泰芯"]
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7815%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/kth7815-datasheet-figure.jpg"
product_image_caption: "KTH7815 手册中的 KTH78 系列磁体布置示意，输出与精度依具体型号"
product_image_source: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7815%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
---

## 核心性能

### 产品介绍

KTH7815是KTH78系列的工业类霍尔角度型号，官网选型表将其与其他带不同带宽及噪声配置的产品并列。 [官方资料](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html)

### 核心参数

- **角度分辨率** 16 位
- **官网选型表** KTH7815-X-N-QN16及SOP8行列PWM、SPI
- **版本差异** 其他公开系列资料也出现SPI、ABZ及反相ABZ口径；不能并列成同一订货版本同时具备
- **订货依据** KTH7815 独立手册中的磁场、温度与带宽条件

### 接口与输出

KTH7815 与主控或驱动器的连接应以完整订货号、引脚表和时序章节为准。下面保留官方公开页已经确认的输出与编码信息；没有列出的接口不据系列习惯补写。

- **官网选型表** KTH7815-X-N-QN16及SOP8行列PWM、SPI
- **版本差异** 其他公开系列资料也出现SPI、ABZ及反相ABZ口径；不能并列成同一订货版本同时具备

### 工作原理

以下解释本类器件在系统中的一般工作方式，具体集成功能以本型号官方资料为准。

旋转磁体使芯片感受到的磁场方向随轴变化。敏感元件把方向变化变成电信号，前端采样与数字电路根据两路或多路信息计算相位，最后输出绝对角度、脉冲或占空比。霍尔、AMR、GMR与TMR采用不同的敏感原理，不能只凭相同位数判断性能相同。

在轴安装通常把磁体放在轴端，离轴结构则把读头移到轴线以外，为中空走线留下空间。两种结构的场分布和误差不同，能否支持离轴必须看具体型号和磁路条件。

### 典型应用与使用条件

角度字长说明一圈分为多少个数字刻度，绝对精度说明读数离真实位置多远，噪声影响静止和低速时的波动，延迟影响运动中数据的新鲜程度。这四个量应分别阅读。

在伺服系统中，读取更快不一定得到更及时的新数据，还要确认传感器内部刷新和滤波。匀速补偿后的延迟也不能直接代表快速加减速时的跟踪误差。

要把产品放进实际设备，还要确认数据对应的物理位置和时刻。传感器读数、接口传输和控制器使用并非同一个环节；读数更新并不一定意味着刚完成一次新测量。协议校验可以发现部分传输错误，无法发现全部机械安装变化。

比较两个备选型号时，应在相同输入、温度、带宽和校准状态下看结果。分辨率、噪声、重复性与绝对误差各有定义；目录页的典型值也不应改写成每颗样品、所有条件下的保证值。某一功能能配置，不表示所有输出可以同时工作。

## 官方资料

- [KTH7815 原厂资料入口](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html)
- [KTH7815 数据手册（官方 PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7815%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
- [系列资料中的接口版本提示](https://conntek.github.io/products/encoder/kth78)
