---
title: "TMR3081"
description: "双全桥TMR角度传感芯片，输出差分正余弦，不内置数字角度接口。"
wiki: true
wiki_type: "model"
wiki_rank: 228
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["多维科技"]
wiki_category: "模拟角度"
catalog_vendor: "多维科技"
catalog_type: "模拟角度"
catalog_form: "芯片"
search_aliases: ["TMR3081"]
official_url: "https://www.dowaytech.com/TMR3081-TMR-Angle-Sensors.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 输出 | SIN／COS模拟差分，360°方向测量 |
| 电源／桥阻 | 1.0～5.5V；目录5kΩ |
| 适用磁场 | 200～800Gs |
| 封装 | TSSOP-8 |
| 峰值输出 | 官网参数表300 mV/V；需结合桥路供电和负载 |
| 角度误差口径 | 官网参数表0.8°；未在摘要给出全条件定义 |

参数来源：本页所列[原厂产品资料与手册](https://www.dowaytech.com/TMR3081-TMR-Angle-Sensors.html)。

## 工作方式与型号定位

TMR3081由双全桥输出差分正余弦，后级读取四个桥臂信号并完成角度计算。360°方向测量不等于芯片内部已经提供数字绝对角度接口。

## 安装、接口与配置

目录工作磁场200～800Gs对应20～80mT。磁场必须在全圈和装配公差下满足要求；桥路1.0～5.5V供电还应和ADC的共模、摆幅及参考搭配。

## 校准与选型验证

原厂表列0.8°角度误差，未在页面统一给出全条件定义，应结合手册核对。验证需分开观察差分幅值、零偏、正交度及机械残差，不把300mV/V峰值或5kΩ桥阻直接解释成角度准确度。

## 官方资料

- [TMR3081 官方资料](https://www.dowaytech.com/TMR3081-TMR-Angle-Sensors.html)
