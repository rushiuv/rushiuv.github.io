---
title: 用KIN52示例，把参数表改成整机验收记录
description: 23bit、重复定位和RS485分别落到可测项目，未知协议与掉电恢复保持未确认。
date: '2026-10-24'
lastmod: '2026-10-24'
layout: engineering-single
engineering_entry: true
plan_id: E11
guide_group: 环境与验收
weight: 1
related_basics:
- resolution-accuracy
- interfaces
- mounting
related_model_slugs:
- kin52
related_guides:
- first-power-interface
- cold-start-validation
- dual-encoder-difference-budget
- position-validity-state
- independent-samples
- sample-time-contract
- calibration-data-integrity
related_applications:
- robot-joint
- servo-motor
- water-meter
- pneumatic-cylinder
keywords:
- 整机验收
- KIN52
- 测试记录
aliases:
- /wiki/engineering/system-acceptance-record/
topic_method: true
---


型号表回答器件有什么规格，验收记录还必须回答：这件订货配置装到这台机器后，谁在什么条件下量过什么。下面以KIN52为例设计记录，**不是已执行的测试报告**。

## 先写清楚要验的对象

[KIN52公开产品页](https://www.reagles.cn/index/product_detail/content/10138.html)技术表列单圈23bit（兼容17bit）、5V±5%；概述给出重复定位可达±3角秒，并列RS485、SSI、BiSS等接口。先把实物订货号、图纸版本、接口配置与协议文件编号写入表头；简介中的选项不能当成同一件实物同时具备。

23bit换算出的码宽为：

\[
q=\frac{360\times3600}{2^{23}}=0.1545\ \mathrm{arcsec}
\]

码宽远小于±3角秒，并不矛盾：前者是数字刻度，后者是厂家列出的重复定位项目，两者都不能直接充当安装后整圈绝对误差限值。

## 每一行都能追到条件与原始值

| 验收项 | 本次怎么填 |
| --- | --- |
| 电气接入 | 芯片/模块端测电压，规格窗口4.75～5.25V；记录启动瞬态、电源和负载条件 |
| 读数解释 | 核实际位宽、方向、零位与圈数格式；留原始帧及协议版本，不能只存换算角度 |
| 重复定位 | 固定参考位置、接近路径与负载，多次返回；记录分布及厂家项目定义，定义未齐先不判符合±3角秒 |
| 整圈误差 | 独立角度参考、安装状态和参考不确定度；限值由项目或对应合同定义，不能填±3角秒代替 |
| 动态与时间 | 指定速度，记录采样到使用的龄期、异常计数；2.5Mbps不等于位置更新率 |
| 环境与恢复 | 温度、冷启动、首次有效位置；掉电移动、计圈保持及恢复行为须核订货资料并实测 |

[TI的RS485说明](https://www.ti.com/document-viewer/lit/html/SSZTCS4)明确其规定电气特性，不规定协议。因此“有RS485”不足以填上命令、校验、超时或圈数恢复。公开资料未明确的条目写“待原厂确认”，实测未执行写“未测”，不补想象中的PASS。

表尾保留四种结果：已测符合、已测不符合、未测、不适用。每项附判定依据、原始数据位置、配置版本和日期。某行失败时保留首次结果及处置后的复测，不能覆盖原记录；掉电行为未确认时，停止对重启后绝对位置能力作结论。

[下载整机验收空白CSV模板](/downloads/encoder-acceptance-record.csv)。填写时先保留未知项，再按[采样时间约定](/topics/guides/sample-time-contract/)、[独立样本检查](/topics/guides/independent-samples/)与[配置数据完整性](/topics/guides/calibration-data-integrity/)补齐相应证据。
