---
title: "MT6901"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 32
seed_count: 6
lastmod: "2026-10-24"
description: "MT6901 是纳芯微工业控制资料中的电感位置编码器型号，采用 PCB 线圈和金属靶的感知路线。"
official_url: "https://www.novosns.com/"
related_companies: ["纳芯微"]
datasheet_url: "https://mgmt.novosns.com/Public/Uploads/uploadfile3/files/20251106/NOVOSENSE%20Industrial%20Control%20Solution_202510.pdf"
datasheet_label: "官网文档入口"
wiki_category: "电感与电涡流测角"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 公开产品归类 | 电感式位置编码器 |
| 感知结构 | PCB 线圈与金属靶 |
| 原厂应用入口 | 纳芯微工业控制方案 |
| 资料适用版本 | 归档原厂MT6901中文Rev.0.2（2025-02）；当前原厂入口未定位独立手册直链，以下不代表已核对最新版本 |
| 绝对位置 | UART可选17/23位；SPI21位；PWM12位 |
| UART速率 | 2.5或4.0 Mbit/s，依配置；MT6901QB-STD选型行列23位、2.5 Mbit/s |
| 推荐供电 | 3.0～5.5 V，典型3.3～5.0 V，第8～9页 |
| 工作电流 | 典型60 mA，第9页；不得当作最大值 |
| 定转子垂直间距 | 0.3～1 mm，第8页；精度例子气隙0.5mm |
| 最高转速 | 12,000 rpm |
| 环境温度／封装 | −40～125°C；QFN32，5 × 5 mm |
| 增量／换向 | ABZ 1～16384脉冲/圈（四倍频最多65536步）；UVW1～16对极 |
| 简洁校准INL | 典型±0.1°，32对极线圈、AG=0.5mm，第9页 |
| 匀速校准INL | 典型±0.02°，32对极线圈、AG=0.5mm，第9页 |
| 匀速延迟／阶跃 | 典型10 µs匀速延迟；BW=7典型250 µs阶跃响应 |
| 启动时间 | 典型5 ms，电源上升<100 µs |
| 校准方法 | 简洁非匀速校准、匀速自校准、外部参考NLC；三层分别执行，不把最佳精度赋予所有模式 |

参数来源：本页所列[原厂产品资料与手册](https://mgmt.novosns.com/Public/Uploads/uploadfile3/files/20251106/NOVOSENSE%20Industrial%20Control%20Solution_202510.pdf)。

资料定位：归档原厂MT6901中文Rev.0.2第1、6、8～9、36～37页；当前公开方案入口仅能复核产品方向，独立手册链接仍待原厂提供。

## 工作方式与型号定位

MT6901由定子线圈、导电转子和芯片组成电涡流游标编码系统，两路不同周期位置用于消歧。它不依赖永磁体，线圈与转子的几何必须成套设计。

## 安装、接口与配置

UART最高23位与SPI21位是接口相关的角度表达；UART波特率、报文格式和所选位数也要配套确认。ABZ每圈脉冲、四倍频步数与UVW电机极对不能混写。

## 校准与选型验证

手册的非线性校准指标依赖所用校准方式和装配条件。应分别扫描气隙、偏心、倾斜和附近金属，既检查角度残差，也检查粗细码道的绝对位置连续性；激励断线与接收幅度诊断需纳入异常处理。

## 官方资料

- [MT6901 原厂资料入口](https://www.novosns.com/)
- [官网文档入口（官方入口）](https://mgmt.novosns.com/Public/Uploads/uploadfile3/files/20251106/NOVOSENSE%20Industrial%20Control%20Solution_202510.pdf)

MT6901 独立完整手册尚未取得；精度、引脚和通信帧格式未列。
