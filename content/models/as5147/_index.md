---
title: "AS5147"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 56
seed_count: 3
lastmod: "2026-10-24"
description: "AS5147是面向旋转位置测量的磁角度传感器，采用在轴磁体，提供绝对角度与电机控制相关输出，历史手册保留ams产品背景。"
official_url: "https://www.infineon.com/part/AS5147"
related_companies: ["英飞凌"]
datasheet_url: "https://www.infineon.com/assets/row/public/documents/30/49/infineon-as5147-datasheet-en.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/as5147-official.jpg"
product_image_caption: "AS5147 原厂产品页所列 TSSOP-14 封装示意（封装共用图）"
product_image_source: "https://www.infineon.com/part/AS5147"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 绝对角度分辨率 | 14 位 |
| 位置接口 | SPI、ABI、UVW、PWM，组合依引脚配置 |
| 补偿功能 | 动态角度误差补偿 |
| 安装方式 | 在轴磁体 |
| 理想数字码距 | 按14位全圈换算：360°/2^14 ≈ 0.02197266°；计算值，不是准确度保证 |
| 5V工作供电 | 4.5～5.5 V |
| 3.3V常规模式 | 3.0～3.6 V，−40～125°C；扩展150°C需按手册设置对应位及电压条件 |
| 工作磁场 | 35～70 mT，芯片表面规定测量几何；低于35mT噪声性能下降 |
| ABI分辨率 | 512脉冲/圈=2048步/圈；可选256脉冲/圈=1024步/圈 |
| UVW | 1～7对极可编程 |
| 供电电流上限 | 15 mA |
| 噪声上限 | NOISESET=0：0.068° RMS；NOISESET=1：0.082° RMS，均为原表Max列，按手册磁场条件 |
| INL（最佳安装，25°C） | 最大±0.8° |
| 封装 | TSSOP-14 |

参数来源：本页所列[原厂产品资料与手册](https://www.infineon.com/assets/row/public/documents/30/49/infineon-as5147-datasheet-en.pdf)。

资料定位：AS5147 v2-00（2021-07-22）正文第1、7～8页，供电扩展温度条件不得省略。

## 工作方式与型号定位

AS5147读取在轴磁体方向，并通过绝对位置、增量和换向输出接入电机控制。14位描述位置码宽，不能直接替代手册给定条件下的INL、噪声和动态误差。

## 安装、接口与配置

SPI角度、ABI线数和UVW极对数各有配置含义。电机极对设置与真实绕组必须对应，机械零位也需与电角度对齐；否则串行角度读数正常，换向仍会出错。

## 校准与选型验证

动态角度补偿针对处理延迟，装配偏心与倾斜需要另行评价。与AS5047P比较时应核对完整料号、温度等级和手册版本，不能把相似名称当作引脚、OTP或寄存器完全兼容的证明。

## 官方资料

- [AS5147 原厂资料入口](https://www.infineon.com/part/AS5147)
- [AS5147 数据手册（官方 PDF）](https://www.infineon.com/assets/row/public/documents/30/49/infineon-as5147-datasheet-en.pdf)
