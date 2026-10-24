---
title: "MA734"
description: "标称3µs低延时的MagAlpha角度芯片，分辨率随工作配置变化。"
wiki: true
wiki_type: "model"
wiki_rank: 217
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["MPS"]
wiki_category: "数字角度"
catalog_vendor: "MPS"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["MA734"]
official_url: "https://www.monolithicpower.com/en/ma734.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 分辨率 | 8～12.5位，按工作配置 |
| 时延 | 3µs指匀速旋转条件下的指标，不能外推到所有动态过程 |
| 输出 | SPI读取角度与配置；不是ABZ增量输出型号 |
| 定位 | 速度响应与角度噪声应一起比较 |
| 推荐供电 | 3.0～3.6 V；3.3 V标称 |
| 工作温度 | −40～125°C |
| 供电电流 | 官网列11 mA |
| 磁场下限 | 30 mT |
| 滤波截止频率 | 官网列95、380、95,000 Hz；按配置选择 |
| 最高转速 | 60,000 rpm |
| 封装 | QFN-16，3 × 3 mm |
| 附加功能 | 可配置磁场阈值、角度变化中断、NVM配置保存 |

参数来源：本页所列[原厂产品资料与手册](https://www.monolithicpower.com/en/ma734.html)。

## 工作方式与型号定位

MA734面向低动态延迟的SPI角度读取，8～12.5位分辨率随配置变化。它没有MA732那类ABZ增量输出，不能作为只换型号不改接线的直接替代。

## 安装、接口与配置

3µs指标对应匀速旋转。速度快速变化时，仍需测试滤波和角度预测的响应；若用它做位置环，还要加入SPI传输、采样调度及主控使用数据的时间。

## 校准与选型验证

可配置磁场阈值和角度变化中断适合做诊断或唤醒。调试时先用易恢复的易失寄存器验证配置，再按手册保存NVM，避免每次调参都写非易失存储；写后应检查冷启动的实际配置。

## 官方资料

- [MA734 官方资料](https://www.monolithicpower.com/en/ma734.html)
