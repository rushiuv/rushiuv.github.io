---
title: "KTM5800"
description: "KTM5800 是外接正余弦信号的角度细分器，集成双通道 ADC、校准和角度计算，可连接磁阻桥或光电读头。"
wiki: true
wiki_type: "model"
catalog_type: "信号处理"
catalog_form: "芯片"
wiki_rank: 11
seed_count: 15
lastmod: "2026-10-24"
related_companies: ["昆泰芯"]
official_url: "https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/absoluteangledivider/index.html"
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTM5800%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
datasheet_label: "KTM5800 数据手册"
document_version: "官网公开下载件，核对日期 2026-10-15"
model_card: true
product_image: "/images/wiki/ktm5800-diagram.webp"
product_image_caption: "图片来源：KTM5800 官方数据手册，第 5 个 PDF 页面，功能框图局部。"
product_image_source: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTM5800%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 器件类型 | 外部正余弦角度细分器，不集成磁体/光学读头 |
| 细分/周期 | 单电周期最高18位；最多4096对极输入；30位表达不等于30位精度 |
| 采样 | 双16位SAR ADC，最高2MSPS |
| 输入幅度 | 介绍20mV～2V；差分、共模及增益按输入章节 |
| 供电 | DVDD/AVDD 3.0～5.5V；MTP烧写4.5～5.5V、典型5V |
| 典型电流/启动 | 32mA；23ms，正常参数表 |
| SPI | 最高36Mbps，支持角度及寄存器操作 |
| ABZ | 1～65536线；表列输出频率最高20MHz |
| UVW/PWM | 1～256对极；PWM典型973Hz |
| 校准/INL | 线性、非线性和误差表补偿；单对极校准后≤±0.025° |
| 噪声/延时 | 表列0.01°（6σ）；0.5µs典型延时，外接AMR条件，不含所有滤波/整机环节 |
| 温度/封装 | −40～125°C；QFN32，5×5mm |
| 存储 | MTP至少1000次擦写，按烧写电气条件 |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTM5800%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)。

## 敏感元件和细分器的分工

KTM5800接收外部AMR、TMR、光学或磁栅读头产生的正余弦信号。输入放大、ADC、校准和角度处理在芯片内，磁场或光学位置到模拟信号的转换仍取决于外部读头。手册外接AMR时的磁场条件不能当成本芯片通用输入范围。

## 18位、12位周期数与30位

每个电周期的细分与机械周期计数是不同层次。4096周期对应12位周期表达，再与18位细分组合可形成30位位置字；这只是编码结构，实际整圈准确度还受读头、周期误差和同步基准影响。

## 模拟输入先于数字参数

先核对差分幅度、共模、增益和最大频率，再谈输出分辨率。输入削波或信号失衡会产生错误相位，即使SPI与CRC都正常。双ADC采样与后续数字滤波也需在相同配置下验证延时和噪声。

## 校准与保存

线性校准处理偏置、幅值和正交度，非线性表补偿处理相应残差，置零只定义起点。保存时MTP引脚有独立电压要求，完成后须冷启动回读。0.5µs表列延时不能直接代表含滤波、接口和控制器的反馈总延迟。

## 官方资料

- [官方产品介绍](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/absoluteangledivider/index.html)
- [下载KTM5800 数据手册（官方 PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTM5800%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
- 资料版本：官网公开下载件，核对日期 2026-10-15
