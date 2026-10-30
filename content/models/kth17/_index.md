---
title: KTH17系列
description: 全极霍尔开关系列，用于磁体靠近、盖合与低功耗位置事件检测。
wiki: true
wiki_type: model
wiki_rank: 203
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
wiki_category: 磁开关
catalog_vendor: 昆泰芯
catalog_type: 磁开关
catalog_form: 芯片
search_aliases:
- KTH1701
- KTH1702
- KTH17系列
official_url: https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/microPowerSeries/index.html
document_version: 官方公开产品页或目录，核对：2026-10-18
model_card: true
catalog_level: 系列
---

KTH17采用全极检测，成员的输出级、采样档和温度范围不同。频率与电流必须按同一版本配对比较。

## 型号与核心异同

| 具体型号／版本 | 输出 | 采样／电流（1.8V） | 温度 |
| --- | --- | --- | --- |
| KTH1701 | CMOS | 25/100/500Hz；0.9/2.4/10.4µA | −40～85°C |
| KTH1702 AE | 开漏 | 25Hz；0.9µA | −40～125°C |
| KTH1702 CC | 开漏 | 40kHz；2.25mA | −40～125°C |

## 共同条件与参数依据

- **共同供电**：1.8～5.5V，官网目录
- **KTH1701阈值档**：H：±48/±28Gs；L：±36/±20Gs；U：±26/±14Gs（动作/释放）
- **封装**：SOT-23-3L、TO-92S，按订货号

## 全极检测适用的任务

KTH17系列用于检测磁体出现或离开。全极表示两种磁极均可触发相应状态，不表示测量两个方向的连续磁场，更不能以一个开关输出恢复全圈绝对角度。适合盖合、到位与磁吸状态等任务。

## 1701与1702的实际差别

KTH1701目录以CMOS输出和多档低功耗采样为主，KTH1702目录同时列低频微功耗与高速版本，并采用开漏输出。外部上拉、电平以及整机待机电流需随成员重新核算，不能只替换料号。

## 选频率要看动作持续时间

25、100、500Hz分别对应约40、10、2ms的采样周期。该换算用于判断动作捕获需求，不是保证的响应上限。触发磁体在检测区域停留的时间，应覆盖所用版本的采样和输出条件。

## 怎样比较阈值

动作点与释放点共同形成磁迟滞。比较磁体大小或安装距离时，要保留磁极、封装面、环境温度和完整后缀；现场距离不是芯片本身的固定规格。量产验证应覆盖最弱磁体和最大气隙。

## 官方资料

- [KTH17系列 官方资料](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/microPowerSeries/index.html)
