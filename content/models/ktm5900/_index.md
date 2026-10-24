---
title: "KTM5900"
description: "KTM5900 是集成 TMR 磁敏元件的绝对角度编码器，单对极角度最高 24 位，支持数字位置、增量及换向输出。"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 2
seed_count: 34
lastmod: "2026-10-24"
related_companies: ["昆泰芯"]
official_url: "https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrTMPMagnrticEncoderChip/index.html"
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTM5900%2024bit%E7%BB%9D%E5%AF%B9%E8%A7%92%E5%BA%A6%E7%A3%81%E6%80%A7%E7%BC%96%E7%A0%81%E5%99%A8.pdf"
datasheet_label: "KTM5900 数据手册"
document_version: "官网公开下载件，核对日期 2026-10-15"
model_card: true
product_image: "/images/wiki/ktm5900-diagram.webp"
product_image_caption: "图片来源：KTM5900 官方数据手册，第 5 个 PDF 页面，功能框图局部。"
product_image_source: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTM5900%2024bit%E7%BB%9D%E5%AF%B9%E8%A7%92%E5%BA%A6%E7%A3%81%E6%80%A7%E7%BC%96%E7%A0%81%E5%99%A8.pdf"
---

## 核心性能

### 产品介绍

KTM5900 是昆泰芯的绝对角度磁编码器，内部集成 TMR 磁敏元件、模拟信号处理和数字角度解算。它配合外部磁铁或磁环，将旋转位置转换成控制器可以读取的角度或脉冲，官方列出的应用包括伺服电机、直驱电机、直线电机和机器人关节。[产品资料](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrTMPMagnrticEncoderChip/index.html)

理解这个型号，可以抓住两个特征：它已经集成磁敏元件，板上不必再单独放置一颗模拟磁阻角度传感器；它又保留了丰富的输出和校准配置，能够适配不同控制器与机械结构。具体的电气连接仍须按数据手册设计。

![KTM5900 官方功能框图](/images/wiki/ktm5900-diagram.webp)

*图片来源：KTM5900 官方数据手册，第 5 个 PDF 页面，功能框图局部。*

### 核心参数

- **感应原理** 集成 TMR 磁敏元件
- **角度输出** 单对极最高 24 位
- **模拟采样** 双 16 位 SAR ADC，最高 2 MSPS
- **接口** SPI、ABZ、UVW、PWM；组合受引脚配置约束
- **增量设置** ABZ 1～65,536 线，UVW 1～256 对极
- **校准指标** 单对极校准后 INL ≤ ±0.025°，保留手册条件
- **工作温度** −40～125°C
- **封装** HFBP 5 × 5 mm，32 引脚

### 接口与输出

KTM5900 与主控或驱动器的连接应以完整订货号、引脚表和时序章节为准。下面保留官方公开页已经确认的输出与编码信息；没有列出的接口不据系列习惯补写。

- **角度输出** 单对极最高 24 位
- **接口** SPI、ABZ、UVW、PWM；组合受引脚配置约束
- **增量设置** ABZ 1～65,536 线，UVW 1～256 对极

### 工作原理

磁铁随轴转动，芯片里的 TMR 敏感元件产生与磁场方向相关的正弦、余弦信号。两路模拟信号经过放大和模数转换后，数字电路计算相位，再根据零点、方向、校准和滤波设置得到输出位置。官方手册公开了双 16 位、最高 2 MSPS 的 SAR ADC，以及 SPI、ABZ、UVW、PWM 等功能模块。

SPI 适合主控制器主动读取绝对角度；ABZ 将运动转换为正交脉冲，适合已有编码器计数输入的驱动器；UVW 提供电机换向相关信号；PWM 通过占空比传递位置。这些输出来自同一条测量链，不能当作相互独立的多套传感器。并行输出引脚存在复用，实际能同时使用哪些组合，要查看手册的引脚配置表。

手册还介绍了线性校准、非线性自校准以及参考编码器对拖标定。校准的作用是补偿可识别、可重复的误差，并不能替代磁路设计。磁体松动、装配状态变化或动态振动带来的误差，仍须在整机上验证。

### 典型应用与使用条件

在轴安装将磁体放在转轴端部，离轴安装则允许传感器位于旋转中心之外。后者有利于给线缆或其他机械零件保留中空通道，同时也会改变传感器看到的磁场轨迹。可安装与达到某个精度是两个条件，应按手册推荐的磁体、气隙和敏感中心位置设计。

数据手册专门指出，封装的几何中心与传感器敏感中心并不重合，安装时应对准敏感中心。这会直接影响 PCB 与机械定位基准的选择。供电方面，模拟／数字供电和 MTP 编程供电有各自要求，不能只按一个“支持 3.3 V”描述给所有引脚供电。

用于伺服反馈时，还要结合最高转速核算脉冲频率，并确认接收端的电平、输入带宽和布线条件。内部采样很快，并不表示外部控制器能以相同速度获得一帧完整角度。量产流程中应保留配置回读、断电重启和校准结果复核，确认装配后的器件实际按预期运行。

对接口规格，ABZ 的线数与接收端计数值需要换算到同一口径。一条 A 相信号完成一个周期，正交解码器可以在 A、B 两相的四个边沿计数，因此同样的机械一圈会出现“线数”和“四倍频计数”两个数。接线调通后，应让轴完整转一圈，比较计数增量与配置值，并核对正反转方向和 Z 信号位置。

绝对位置和增量计数也各有启动条件。SPI 可以表达一圈内的位置，接收器对 AB 脉冲的累计却取决于它何时开始计数以及如何建立参考点。若系统同时使用两种输出，应明确启动时刻、零点和方向的对应关系，避免每路单独看似正确，合在控制器中却出现固定偏移。

配置记录宜保存完整料号、手册版本、磁体与安装参数、输出方式和校准结果。以后更换 PCB 或机械件时，能据此判断哪些条件发生变化，而不只是保留一张“测过合格”的曲线。

## 官方资料

- [官方产品介绍](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrTMPMagnrticEncoderChip/index.html)
- [下载KTM5900 数据手册（官方 PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTM5900%2024bit%E7%BB%9D%E5%AF%B9%E8%A7%92%E5%BA%A6%E7%A3%81%E6%80%A7%E7%BC%96%E7%A0%81%E5%99%A8.pdf)
- 资料版本：官网公开下载件，核对日期 2026-10-15
