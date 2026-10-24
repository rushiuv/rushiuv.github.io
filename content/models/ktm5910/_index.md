---
title: "KTM5910"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 42
seed_count: 5
lastmod: "2026-10-24"
description: "KTM5910属于昆泰芯KTM59系列，官网将其列为在轴应用的高分辨率TMR磁编码器。"
official_url: "https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrTMPMagnrticEncoderChip/index.html"
related_companies: ["昆泰芯"]
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTM5910%2024bit%E7%BB%9D%E5%AF%B9%E8%A7%92%E5%BA%A6%E7%A3%81%E6%80%A7%E7%BC%96%E7%A0%81%E5%99%A8.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/ktm5910-official.png"
product_image_caption: "KTM5910 原厂产品／封装图"
product_image_source: "https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrTMPMagnrticEncoderChip/index.html"
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 感应/编码 | 集成TMR；单对极最高24位，码宽不等于有效精度 |
| ADC | 双16位SAR ADC，最高2MSPS |
| 供电 | AVDD/DVDD 3.0～5.5V；典型3.3～5V |
| MTP烧写 | VDDMTP 4.5～5.5V，典型5V |
| SPI | 最高36Mbps，角度读取带8位CRC，按对应帧结构 |
| ABZ | 1～65536线，可编程；电气表输出频率最高20MHz |
| UVW/PWM | 1～256对极；PWM典型973Hz |
| 工作电流 | 下载PDF典型32mA；官网目录40mA，来源口径不同 |
| 启动/延时 | 典型23ms/0.5µs，正常表；不代表含滤波/通信的总时延 |
| 噪声 | 电气表0.01°（6σ），不能与1σ数字直接比较 |
| 最高转速 | 180000rpm，需同时满足输出频率和所选配置 |
| 温度/封装 | −40～125°C；QFN32，5×5mm |
| MTP耐久 | 至少1000次，按手册烧写条件 |
| 安装范围 | 下载PDF仅支持在轴，不沿用KTM5900离轴能力 |
| 磁场 | 下载PDF10～150mT，典型30mT；官网目录30～150mT |
| 校准INL | 下载PDF特点页写单对极校准后≤±0.025°，电气表将±0.025°置于典型列；官网目录±0.02°，不合成全温最大保证 |
| 校准 | 自动线性、自动非线性及256点补偿表 |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTM5910%2024bit%E7%BB%9D%E5%AF%B9%E8%A7%92%E5%BA%A6%E7%A3%81%E6%80%A7%E7%BC%96%E7%A0%81%E5%99%A8.pdf)。

## 与5900的关键边界

KTM5910的公开手册明确限制在轴安装，不能因为同属KTM59系列，就沿用5900的离轴安装说明和误差数字。使用轴端磁体时也应按5910的磁感中心、磁体尺寸及气隙设计。

## 把采样、编码与接口分开

双16位ADC说明模拟采样路径，24位说明角度表达，36Mbps说明SPI通信速度。三者不是同一个“速度/精度”指标。主控还需考虑读数时刻、滤波和传输，不能只按总线最高速度设定控制周期。

## 高线数输出的限制

ABZ可配置到65536线，但20MHz输出上限与主控输入能力限制可用转速。反相输出、UVW和其他并行功能还受引脚配置约束，不能把目录全部接口视为所有引脚同时输出。

## 校准与MTP验收

先固定磁体和装配，再执行对应校准与零点设置。MTP编程电压必须达到手册规定范围；写完后冷启动回读系数并复测整圈。0.5µs典型延时与0.01°六倍标准差噪声均有条件，不能作为全温整机保证。

## 官方资料

- [KTM5910 原厂资料入口](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrTMPMagnrticEncoderChip/index.html)
- [KTM5910 数据手册（官方 PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTM5910%2024bit%E7%BB%9D%E5%AF%B9%E8%A7%92%E5%BA%A6%E7%A3%81%E6%80%A7%E7%BC%96%E7%A0%81%E5%99%A8.pdf)
