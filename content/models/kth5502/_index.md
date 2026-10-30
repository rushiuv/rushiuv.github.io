---
title: KTH5502
description: KTH5502 将三轴霍尔感知与角度计算集成在单芯片中，提供数字、增量、PWM 与模拟等输出路径，选型时需先确定实际使用的接口和安装方式。
wiki: true
wiki_type: model
wiki_rank: 201
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
wiki_category: 数字角度
catalog_vendor: 昆泰芯
catalog_type: 数字角度
catalog_form: 芯片
search_aliases:
- KTH5502
official_url: https://www.conntek.com.cn/html/web/product/magneticAngleDetectionChip/kth5502/index.html
document_version: 版本以链接文件名及原件为准；公开链接核对：2026-10-30
model_card: true
datasheet_url: https://chat.connteck.com/downloads/KTH5502/KTH5502_DS_CN_V1.3.pdf
datasheet_label: 数据手册原链接
catalog_source: https://chat.connteck.com/products/3d-hall/KTH5502/
product_image: /images/catalog/kth5502-original.png
product_image_caption: KTH5502 原厂产品与封装示意
product_image_source: https://www.conntek.com.cn/html/web/product/magneticAngleDetectionChip/kth5502/index.html
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 感应/量程 | XYZ霍尔检测；XYZ典型工作范围±100mT，官网目录 |
| 角度编码 | 16位，360°在轴角度 |
| 角度INL | 目录±1°，具体条件按手册 |
| 供电 | 1.7～3.6V |
| 平均电流 | 目录5mA，持续感应模式 |
| 采样能力 | 目录10kSPS |
| 最高转速 | 目录5000rpm |
| 输出选项 | I²C/SPI、ABZ、PWM、模拟，按引脚配置 |
| 温度/封装 | −40～125°C；SOP-8L、DFN 2×2mm-8L |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH5502%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)。

## 它同时涉及场强与角度

KTH5502集成XYZ磁检测及角度相关处理，低压供电和小封装适合紧凑旋钮或位置节点。场强范围与角度精度分别描述前端输入条件和角度输出误差，16位数字编码不是±1°误差的另一种写法。

## 先确定实际输出模式

I²C、SPI、ABZ、PWM和模拟输出属于可配置选项，不能按五种接口同时可用绘制电路。需要先确认封装引脚和模式，再确定主控使用总线读取、边沿计数还是ADC采集。

## 磁路与速度条件

官网表格按在轴360°列出应用。磁体方向和位置应使敏感点获得有效方向变化，同时避免某一分量越界。10kSPS是采样速率，5000rpm是目录转速条件，不能直接相互推导系统延时。

## 参数如何用于选型

与更高带宽编码器比较时，保留供电、滤波、输出模式和磁体条件。样机应分别检查静止噪声、整圈误差、快速反转以及输出行程映射；数字位数增加不能代替这些测试。

## 官方资料

- [KTH5502 官方资料](https://www.conntek.com.cn/html/web/product/magneticAngleDetectionChip/kth5502/index.html)

- [KTH5502 官方产品手册（PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH5502%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)

## 选型补充

### 绝对角度与增量计数怎样配合

数字角度用于读取当前磁场方向，ABZ 则把运动转换为边沿序列。主控选择绝对读取还是增量跟踪，会改变启动、零点和丢脉冲处理方式；两种输出来自同一磁路，不能据此认定为独立冗余。

### 先定接口，再核对订货型号

源页列出多类输出和多种封装，不能理解为每个订货型号都把所有信号同时引出。应按所选 SKU 的引脚、输出模式和供电条件画图，尤其避免把模拟接口、PWM 位宽和数字角度位宽混成一项性能。

### 在轴与离轴分别验收

在轴旋转、偏心旋转和离轴读头的场分量轨迹不同。来源提供普通与离轴专版文档，应按目标几何选择资料，再检查气隙、偏心、倾斜对整圈误差的影响。不能用一次静态读数代替整圈准确度验证。


## 公开资料与型号核对

按完整型号、等级和版本选择手册。公开链接核对日期：2026-10-30。

- [KTH5502_DS_CN_V1.3.pdf](https://chat.connteck.com/downloads/KTH5502/KTH5502_DS_CN_V1.3.pdf)
- [KTH5502_DS_CN_V1.3_off-axis.pdf](https://chat.connteck.com/downloads/KTH5502/KTH5502_DS_CN_V1.3_off-axis.pdf)
- [KTH5502_DS_EN_V1.3.pdf](https://chat.connteck.com/downloads/KTH5502/KTH5502_DS_EN_V1.3.pdf)

[来源产品页](https://chat.connteck.com/products/3d-hall/KTH5502/) · [昆泰芯型号目录](/wiki/?vendor=昆泰芯)
