---
title: "KTM13XX"
wiki: true
wiki_type: "model"
catalog_type: "磁开关"
catalog_form: "芯片"
wiki_rank: 129
seed_count: 1
lastmod: "2026-10-24"
description: "KTM13XX 是昆泰芯磁开关系列标签，具体成员提供不同磁门限、采样频率、输出形式及封装。"
official_url: "https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/magnetoresistiveSwitchSeries/index.html"
related_companies: ["昆泰芯"]
related_models: ["KTM1301"]
wiki_category: "磁开关与状态检测"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 系列范围 | TMR磁开关，XX为系列占位，不是可下单完整料号 |
| 检测逻辑 | 130x全极；1311单S极；1321单N极；1331锁存，按成员 |
| 常见供电 | 官网所列1301/1302等成员1.8～5.5V，不扩展到未列成员 |
| 1301采样/电流 | 50/1600/5000Hz；160nA/600nA/1.9µA（3V） |
| 1302输出 | 开漏；目录50/5000Hz版本，按完整料号 |
| 1304配置 | 目录50Hz、160nA（3V）；CMOS；DFN 2×2mm-3L |
| 1301阈值例 | A～E动作绝对值45/30/18/9/7Gs，其他成员不得照搬 |
| 温度口径 | 上述目录成员−40～125°C |
| 封装口径 | SOT-23-3L、TO-92S、DFN等，按成员 |

参数依据：[原厂产品与型号选型表](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/magnetoresistiveSwitchSeries/index.html)。

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
