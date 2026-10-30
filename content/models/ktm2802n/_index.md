---
title: KTM2802N
wiki: true
wiki_type: model
catalog_form: 芯片
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
model_card: true
description: KTM2802N 是面向气缸磁性端位检测的 AMR 开关型号，二线/三线接法和输出类型应按本型号电路确定，不能仅凭系列名称替换簧片开关。
wiki_rank: 318
catalog_type: 磁开关
wiki_category: 磁开关
official_url: https://chat.connteck.com/products/
catalog_source: https://chat.connteck.com/products/
search_aliases:
- KTM2802N
---

## 目录信息与参数条件

以下为[来源产品矩阵](https://chat.connteck.com/products/)的目录标注，用于初步检索；尚未用对应手册正文逐项复核，冲突项见下文，不能直接用作设计保证值。

| 项目 | 内容与条件 |
| --- | --- |
| 器件定位 | AMR 高压气缸开关·SIP |
| 目录所列接口 | 两线 / 三线 |
| 目录所列温度 | -40 ~ 105°C |
| 目录所列封装 | HFBP2*3-6L |

## 气缸到位是一个磁事件

活塞磁环经过传感器时形成动作窗口，输出表示是否达到对应磁状态，不直接给出活塞毫米位置。缸体材料、槽口、磁环和敏感轴都会改变动作区，应在目标气缸上测往返触发点。

## 二线与三线对负载要求不同

二线传感器的供电与负载共用回路，需要检查残余电流和导通压降；三线则有独立供电和输出。接 PLC 输入前，应确认 NPN/PNP、负载位置和输入门限，不能只对线色接线。

## 最快活塞运动决定漏检风险

气缸速度越高，磁环停留在有效区的时间越短。应同步记录机械动作和输出脉冲，检查高低压、不同负载与温度下的动作稳定性，避免慢速调试正常而高速生产漏检。


## 公开资料与型号核对

分类页写SIP，矩阵写HFBP2×3-6L；系列供电另有30V/32V口径差异，不能合并成单一配置。

来源无独立详情页及本型号PDF直链，不能把KTM2802P或KTM28系列的输出条件直接赋给N型号。

目前未取得可确认属于本型号的产品照片或技术图，保留文字资料；不以相邻型号的封装图代替。

来源未提供可读取的 KTM2802N 本型号 PDF；旧 KTM2802 系列公开链接返回空文件，暂停下载入口，不将其作为 N 后缀手册。


[来源产品页](https://chat.connteck.com/products/) · [昆泰芯型号目录](/wiki/?vendor=昆泰芯)

