---
title: "KTH7101"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 40
seed_count: 5
lastmod: "2026-10-24"
description: "KTH7101是昆泰芯带自动非线性校准功能的磁编码器。"
official_url: "https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/magneticencoder/index.html"
related_companies: ["昆泰芯"]
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7101%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 角度编码 | 16位，360°；理想码距约0.005493°，计算值不是精度 |
| 安装 | 在轴及离轴，ANLC自动非线性校准 |
| 工作供电 | 关键表3.0～5.0V，典型3.3V；特性介绍3.3～5V |
| 磁场条件 | 30～150mT，典型60mT；关键指标表 |
| 典型电流 | 16mA@3.3V，关键指标表 |
| 典型启动 | 20ms；实际启动配置需核对 |
| 表列非线性误差 | ±0.1°；不同安装与校准状态分别验收 |
| 数据更新 | 1µs，不能直接当成任意运动下完整链路延时 |
| 噪声 | 0.015°（1σ），关键指标表 |
| 最高转速 | 120000rpm，按手册工作条件 |
| 温度 | −40～125°C |
| 主要输出 | 三线SPI、SSI与ABZ；SOP8具体引脚/模式按手册 |
| 配置保存 | MTP，校准计算完成与保存完成需分开检查 |
| 封装 | SOP-8，手册引脚表为8脚 |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7101%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)。

## 小封装的接口取舍

KTH7101把霍尔检测、角度计算与ANLC集成在SOP8中。八脚封装的接口由实际引脚和复用配置约束，不能把KTH7111/7112的PWM、UVW等全部功能简单移到本型号上。

## 绝对角度和ABZ怎样使用

16位绝对角度用于上电位置读取，ABZ提供边沿计数。增量计数器需要独立配置线数、方向和Z相。三线SPI使用双向数据线，主控必须按手册处理发送与接收换向，不能沿用任意四线SPI接法。

## ANLC与安装误差

校准要按该型号规定的磁路和运动条件进行。置零只改变角度起点，ANLC针对非线性补偿，二者不能互相替代。校准后应独立测整圈残差，而不是以完成标志替代准确度判定。

## 启动与非易失保存

典型20ms反映给定配置下的启动，控制器还需等待有效数据。参数修改后要核对MTP保存、重新上电加载和输出一致性。回读寄存器暂时改变，只证明当前运行配置改变，不证明断电后仍保存。

## 官方资料

- [KTH7101 原厂资料入口](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/magneticencoder/index.html)
- [KTH7101 数据手册（官方 PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7101%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
