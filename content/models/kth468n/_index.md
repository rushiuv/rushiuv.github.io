---
title: KTH468N
wiki: true
wiki_type: model
catalog_form: 芯片
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
model_card: true
description: KTH468N 是来源矩阵中的三维全极性微功耗霍尔开关，适合在确认各轴判决关系和阈值配置后评估多方向磁体接近检测。
wiki_rank: 316
catalog_type: 磁开关
wiki_category: 磁开关
official_url: https://chat.connteck.com/products/
catalog_source: https://chat.connteck.com/products/
search_aliases:
- KTH468N
---

## 目录信息与参数条件

以下为[来源产品矩阵](https://chat.connteck.com/products/)的目录标注，用于初步检索；尚未用对应手册正文逐项复核，冲突项见下文，不能直接用作设计保证值。

| 项目 | 内容与条件 |
| --- | --- |
| 器件定位 | 3D 全极性霍尔开关·微功耗 |
| 目录所列接口 | NMOS 开漏 |
| 目录所列采样率 / 转速 | 多频可选 |
| 目录所列温度 | -40 ~ 125°C |
| 目录所列封装 | SOT-23-5L |

## 三维检测不等于输出三维坐标

三维开关用于判断磁场状态，不能据此获得连续 XYZ 数值或空间位置。机构设计需要明确由哪一个轴、哪些轴组合触发，以及正反极性是否具有相同门限和释放行为。

## 检查不同接近方向的有效窗口

磁体从正面、侧面或倾斜方向靠近时，各轴分量不同。应在机构允许姿态内测动作与释放位置，特别检查临界角度是否形成漏检区域；不能只在一种摆放方向上验证。

## 微功耗模式要覆盖短事件

状态检测若采用间歇采样，需要确认磁体经过有效区的最短时间。对快速插拔或滑动机构，主控应同时记录输入时序和目标事件，检查是否遗漏，而不是只观察静止时高低电平。


## 公开资料与型号核对

来源只有矩阵，无对应详情页、引脚图或PDF直链；具体轴组合逻辑、门限与后缀配置缺少可核对资料。

目前未取得可确认属于本型号的产品照片或技术图，保留文字资料；不以相邻型号的封装图代替。

来源未提供可核验的本型号 PDF。请通过[资料入口](https://chat.connteck.com/products/)索取，未生成下载地址。


[来源产品页](https://chat.connteck.com/products/) · [昆泰芯型号目录](/wiki/?vendor=昆泰芯)

