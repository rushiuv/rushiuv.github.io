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
| 温度 | −40～125°C |
| 封装差异 | 下载PDF为HFBP 5×5mm-32L；官网目录QFN32-5×5，封装图与焊盘按订货资料确认 |
| MTP耐久 | 至少1000次，按手册烧写条件 |
| 安装 | 官网在轴/离轴；按各磁体与校准条件 |
| 磁场口径 | 下载PDF典型30mT、最大80mT；官网目录30～150mT，未统一 |
| 校准INL | 下载PDF特点页写单对极校准后≤±0.025°，电气表将±0.025°置于典型列；官网在轴±0.02°/离轴±0.05°，不合成全温最大保证 |
| 校准方法 | 自动线性、自动非线性与256点误差表，按手册流程 |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTM5900%2024bit%E7%BB%9D%E5%AF%B9%E8%A7%92%E5%BA%A6%E7%A3%81%E6%80%A7%E7%BC%96%E7%A0%81%E5%99%A8.pdf)。

## 24位输出的工程含义

24位全圈理想码距约0.00002146°，这是编码换算；噪声、电气非线性及安装误差仍按各自条件读取。手册6σ噪声与其他器件的RMS或1σ不能直接并排排名，统计口径必须先统一。

## 在轴、离轴和磁场范围

KTM5900支持对应在轴与离轴应用，但官网和下载PDF在场强上限、电流及校准INL上存在差异。本页同时保留两份数值，不从每份资料挑最好项目拼成一个工作点。磁环读头半径和气隙需按具体方案确定。

## 输出频率与转速

最高180000rpm等于3000圈/秒。若选65536线ABZ，则A/B基础频率约196.6MHz，已经超过电气表20MHz；这是按数值计算的约束，说明最大线数与最大转速不能同时使用。还需计入主控计数与线缆能力。

## 校准、报警与保存

自动线性校准、非线性补偿与256点表作用不同，置零也不是精度校准。MTP写入有专用供电要求，成功后应重新上电复核。输入幅值异常、欠压和CRC错误分别处理，不能用某一种报警覆盖整个反馈链。

## 官方资料

- [官方产品介绍](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrTMPMagnrticEncoderChip/index.html)
- [下载KTM5900 数据手册（官方 PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTM5900%2024bit%E7%BB%9D%E5%AF%B9%E8%A7%92%E5%BA%A6%E7%A3%81%E6%80%A7%E7%BC%96%E7%A0%81%E5%99%A8.pdf)
- 资料版本：官网公开下载件，核对日期 2026-10-15
