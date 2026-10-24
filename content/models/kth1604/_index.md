---
title: "KTH1604"
description: "双输出单极霍尔开关，用于判定磁体靠近与离开事件。"
wiki: true
wiki_type: "model"
wiki_rank: 265
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["昆泰芯"]
wiki_category: "磁开关"
catalog_vendor: "昆泰芯"
catalog_type: "磁开关"
catalog_form: "芯片"
search_aliases: ["KTH1604"]
official_url: "https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/microPowerSeries/index.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
series_parent: "kth16"
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH1604%20Series%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
datasheet_label: "KTH1604 官方产品手册"
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 感应逻辑 | 双输出单极型霍尔开关 |
| 供电 | 1.6～5.5V |
| 采样档位 | 5Hz或20Hz，按S/T等完整订货配置 |
| 平均电流 | 1.6µA@1.8V、5Hz；3.3µA@1.8V、20Hz，官网目录 |
| TH/SH动作与释放 | 场强绝对值46/34Gs；20Hz/5Hz分别对应T/S版本 |
| TL/SL动作与释放 | 场强绝对值33/23Gs |
| SU动作与释放 | 场强绝对值22/16Gs，目录5Hz |
| 输出 | CMOS双输出 |
| 工作温度 | −40～85°C，官网目录 |
| 封装 | DFN/FBP 1×1mm-4L |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH1604%20Series%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)。

## 两路输出解决什么

KTH1604将磁场事件变为两路逻辑状态，适合小型盖合、磁吸或位置事件检测。它输出的是磁极是否满足动作条件，不是连续磁场数值，也不是二维坐标。两个输出应按对应手册真值表解读。

## 阈值与采样是两项选择

H、L、U等阈值档决定需要多大的场强，S/T等采样档决定多久观察一次。不能把最敏感阈值和最快采样自动拼成实际存在的订货号。表中正负号对应磁场极性，装配图还须核对封装正反面。

## 低功耗与事件漏检

平均电流包含周期性工作方式的结果。按频率换算，5Hz版本两次采样间隔约200ms，20Hz约50ms；快速经过的磁体需要用实物确认捕获率。输出接控制器唤醒脚时，还要核对该脚的保持、边沿与上拉条件。

## 安装验证

先固定磁体方向，测接近和远离的触发位置，再加入气隙、温度和供电公差。磁迟滞可抑制临界翻转，但不能补救磁体停在动作边缘或有效场持续时间过短。两路均需做冷启动状态确认。

## 官方资料

- [KTH1604 官方资料](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/microPowerSeries/index.html)

- [KTH1604 官方产品手册（PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH1604%20Series%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
