---
title: "AS5600"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 46
seed_count: 4
lastmod: "2026-10-24"
description: "AS5600 是 12 位在轴霍尔旋转位置传感器，支持 I²C 读取及模拟量／PWM 输出，适用于非接触旋钮和电位器替代。"
official_url: "https://www.infineon.com/part/AS5600"
related_companies: ["英飞凌"]
datasheet_url: "https://www.infineon.com/assets/row/public/documents/30/49/infineon-as5600-datasheet-en.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/as5600-official.jpg"
product_image_caption: "AS5600 原厂产品页所列 SOIC-8 封装示意"
product_image_source: "https://www.infineon.com/part/AS5600"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 感应技术 | 霍尔，轴端径向充磁磁体 |
| 角度分辨率 | 12 位 |
| 接口 | I²C 读取与配置；模拟量或 PWM 位置输出 |
| 模拟输出 | 比例于 VDD，12 位 DAC |
| 可编程角度行程 | 18°～360°，起止位置可配置 |
| 供电模式 | 3.3 V 或 5 V |
| 工作磁场 | 30～90 mT |
| 工作温度 | −40～125°C；支持自动低功耗模式 |
| 理想数字码距 | 按12位全圈换算：360°/2^12 ≈ 0.08789062°；计算值，不是准确度保证 |
| PWM配置 | 115/230/460/920 Hz典型值，容差±5%；占空比2.9%～97.1% |
| 上电准备时间 | 最大10 ms |
| 慢滤波SF=00 | 2.2 ms阶跃延迟；最大0.015° RMS（1σ） |
| 慢滤波SF=01 | 1.1 ms阶跃延迟；最大0.021° RMS（1σ） |
| 慢滤波SF=10 | 0.55 ms阶跃延迟；最大0.030° RMS（1σ） |
| 慢滤波SF=11 | 0.286 ms阶跃延迟；最大0.043° RMS（1σ） |
| 系统INL | 最大±1°；最佳直线拟合、360°行程、无磁体偏移及未做零位编程，PWM/I²C条件 |
| 正常模式电流 | 典型6.5 mA，PM=00常开；60mT典型磁场，不含外部负载 |
| 低功耗LPM1 | 典型3.4 mA，PM=01，轮询5 ms |
| 低功耗LPM2 | 典型1.8 mA，PM=10，轮询20 ms |
| 低功耗LPM3 | 典型1.5 mA，PM=11，轮询100 ms |
| 5V／3.3V供电 | 5V模式4.5～5.5 V；3.3V模式3.0～3.6 V；OTP烧录另有供电条件 |

参数来源：本页所列[原厂产品资料与手册](https://www.infineon.com/assets/row/public/documents/30/49/infineon-as5600-datasheet-en.pdf)。

资料定位：AS5600 v1-06（2018-06-20）正文第7～8页和第28页滤波表；阶跃延迟与噪声逐档配对。

## 工作方式与型号定位

AS5600可替代接触式旋钮和电位器，通过I²C读角度，并选择模拟量或PWM输出。12位全圈的理想码距是360°/4096，约0.08789°；这只表示刻度，不是保证角度误差。

## 安装、接口与配置

18°～360°可编程行程用于将选定机械范围映射到输出。零点、终点和输出模式要一起配置；模拟输出与VDD成比例时，ADC参考如何取值会直接影响系统读数。

## 校准与选型验证

磁体应满足30～90mT工作场条件。低速测速会放大12位码距形成的台阶，滤波应同时评估静止噪声和响应延迟。检验应包括全行程、端点、跨零及掉电重启，不只检查旋钮中间位置。

## 官方资料

- [AS5600 原厂资料入口](https://www.infineon.com/part/AS5600)
- [AS5600 数据手册（官方 PDF）](https://www.infineon.com/assets/row/public/documents/30/49/infineon-as5600-datasheet-en.pdf)
