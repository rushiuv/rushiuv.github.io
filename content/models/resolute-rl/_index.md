---
title: RESOLUTE RL
description: RESOLUTE RL负责沿绝对码尺读取直线位置。纳米输出格式、周期内细分误差和每米长度准确度分属不同层，不能把1nm分辨率写成整段行程1nm准确度。
wiki: true
wiki_type: model
wiki_rank: 300
seed_count: 0
lastmod: '2026-10-24'
related_companies:
- 雷尼绍
wiki_category: 光学绝对读头
catalog_vendor: 雷尼绍
catalog_type: 光学绝对读头
catalog_form: 编码器／模块
search_aliases:
- RESOLUTE RL
- resolute rl
official_url: https://www.renishaw.com/en/37823.aspx
document_version: 英文系列页与原厂RL选型帮助，核对2026-10-24
model_card: true
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 形态 | 开放式绝对光学直线读头，需配RTLA/RTLA-S/RELA/RSLA等相应码尺 |
| 分辨率 | BiSS配置可选1/5/50nm；其它协议与特殊版本分别核订货号 |
| 速度 | 原厂系列/选型页给最高100m/s；可用速度须核协议、分辨率和控制器配置 |
| 温度／防护 | 标准RL工作0～80°C、IP64；不要移用RA旋转ETR版本温区 |
| 读数间隙 | RTLA-S/RSLA/RELA：0.8±0.15mm；RTLA配FASTRACK：0.6±0.15mm |
| 外形 | 18×36×16.5mm（高×长×宽） |
| 精度层次 | 系列标注SDE±40nm、抖动<10nm RMS；码尺精度、系统长度误差与具体配置另核 |

## 产品功能与测量链

RESOLUTE RL负责沿绝对码尺读取直线位置。纳米输出格式、周期内细分误差和每米长度准确度分属不同层，不能把1nm分辨率写成整段行程1nm准确度。

## 接入与验证

先按码尺与安装方式确定间隙、热基准和长度条件，再核输出协议。原厂不同页面列出的最高速度、最低分辨率及特殊版本不能自动组合成一套同时保证值。参见[标尺热安装](/topics/guides/linear-scale-thermal/)与[直线电机](/applications/linear-motor/)。

## 官方资料

- [RESOLUTE英文系列页](https://www.renishaw.com/en/37823.aspx)
- [RL/RA原厂选型参数](https://www.renishaw.com/epc/en/42987.aspx?help=true&type=Readhead)
