---
title: KTM13xx系列
wiki: true
wiki_type: model
catalog_type: 磁开关
catalog_form: 芯片
wiki_rank: 129
seed_count: 1
lastmod: '2026-10-30'
description: KTM13XX 是昆泰芯磁开关系列标签，具体成员提供不同磁门限、采样频率、输出形式及封装。
official_url: https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/magnetoresistiveSwitchSeries/index.html
related_companies:
- 昆泰芯
related_models:
- KTM1301
wiki_category: 磁开关与状态检测
document_version: 公开资料核对：2026-10-16；文件版本见下载件
model_card: true
catalog_level: 系列
search_aliases:
- KTM13xx系列
---

KTM13xx包含全极、单极与锁存器。先选择磁体极性和状态逻辑，再核对输出级、采样档与封装。

## 型号与核心异同

| 具体型号 | 逻辑 | 输出／采样区别 |
| --- | --- | --- |
| KTM1301 | 全极 | CMOS；50/1600/5000Hz对应160nA/600nA/1.9µA（3V） |
| KTM1302 | 全极 | 开漏；目录50/5000Hz版本 |
| KTM1304 | 全极 | CMOS；50Hz、160nA（3V）；DFN 2×2mm-3L |
| KTM1311 | 单S极 | 具体输出、门限及版本按手册 |
| KTM1321 | 单N极 | 具体输出、门限及版本按手册 |
| KTM1331 | 锁存 | 具体输出、门限及版本按手册 |

## 共同条件与参数依据

- **常见供电**：官网所列1301/1302等成员1.8～5.5V，不扩展到未列成员
- **1301阈值例**：A～E动作绝对值45/30/18/9/7Gs，其他成员不得照搬
- **温度口径**：上述目录成员−40～125°C
- **封装口径**：SOT-23-3L、TO-92S、DFN等，按成员

## 按逻辑选，不按同族编号选

KTM13XX包含全极、单极与锁存器。全极适合两种磁极均可出现的到位检测，单极只对指定极性动作，锁存器需要反向磁场切换。相同的电压和封装不意味着状态逻辑相同。

## 输出结构影响电路

CMOS输出可主动驱动逻辑电平，开漏版本需要外部上拉。上拉电阻既影响边沿，也影响被拉低时的系统电流。芯片目录的纳安平均电流不包含所有外部电路消耗。

## 门限字母不是跨成员通用表

A、B、C等阈值字母应与完整型号一起查询。即使系列中多数成员沿用相近门限，不同L/R或其他后缀也要独立核对，不能用1301的C档解释全部13系列。

## 选型顺序

先确定磁体运动与极性，再确定输出逻辑和主控电平，最后选择门限、采样和封装。验收保留动作点、释放点、事件持续时间、温度及磁体公差，不能用“低功耗TMR”一句话代替可复现条件。

## 官方资料

- [KTM13XX 原厂资料入口](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/magnetoresistiveSwitchSeries/index.html)
