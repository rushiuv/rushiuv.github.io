---
title: SSx9线性霍尔系列
wiki: true
wiki_type: model
catalog_type: 线性磁场
catalog_form: 芯片
wiki_rank: 142
seed_count: 1
lastmod: '2026-10-30'
description: SS49E 在本站对应 Honeywell SS39ET／SS49E／SS59ET 系列的线性霍尔器件，以比例式模拟电压输出磁场信息。
official_url: https://automation.honeywell.com/us/en/products/sensing-solutions/sensors/magnetic-sensors/ss39et-ss49e-ss59et-linear-hall-effect-sensor-ic
wiki_category: 线性磁场与位移映射
document_version: Honeywell SS39ET/SS49E/SS59ET Issue4，005850；本次核对2026-10-24
model_card: true
datasheet_url: https://prod-edam.honeywell.com/content/dam/honeywell-edam/sps/siot/en-ca/products/sensors/magnetic-sensors/linear-and-angle-sensor-ics/common/documents/sps-siot-ss39et-ss49e-ss59et-product-sheet-005850-3-en-ciid-50359.pdf
datasheet_label: Honeywell SS39ET/SS49E/SS59ET Issue4 数据手册
catalog_level: 系列
search_aliases:
- SSx9线性霍尔系列
---

本页比较Honeywell同一原厂资料中的SS39ET、SS49E和SS59ET，先按具体成员与封装识别，再使用对应电气表。市场同名兼容料不自动继承这些规格。

## 型号与核心异同

| 具体型号／配置 | 封装或资料对应 | 选型区别 |
| --- | --- | --- |
| SS39ET | SOT-23封装路径 | 不能用作SS49E的封装依据 |
| SS49E | 扁平TO-92式 | 本页电气值按Honeywell Issue4条件 |
| SS49E-L | SS49E引脚构型选件 | 引脚形式与标准件分别核对 |
| SS49E-F | SS49E引脚构型选件 | 引脚形式与标准件分别核对 |
| SS59ET | 同一原厂文档收录 | 具体封装及保证值按本成员读取 |

## 共同条件与参数依据

- **感知方式**：线性霍尔
- **输出**：随供电成比例的模拟电压
- **工作供电**：2.7～6.5V DC，Issue4表1
- **供电电流**：5V、25°C：典型6mA，最大10mA
- **灵敏度**：5V、25°C：1.0～1.75mV/G，典型1.4mV/G
- **零磁场输出**：5V、25°C、0G：2.25～2.75V，典型2.50V
- **磁场范围**：表1最小±650G、典型±1000G；对应±65/±100mT，条件依表注
- **输出电压范围**：保证列1.05～(VS−1.05)V；典型0.95～(VS−0.95)V，5V基准条件
- **响应时间**：3µs典型，表1条件
- **工作温度**：−40～100°C；表1常规电特性默认−40～85°C，除另注明

## 接口与安装

ADC参考若与传感器供电同源，可利用比例关系减小共同电源变化带来的读数影响；但输出饱和、零偏和温漂仍需分别考虑。

## 动态与装配验证

Honeywell系列文档同时覆盖SS39ET、SS49E与SS59ET，封装和各项保证值应按具体成员读取。市场上同名替代料不能直接继承原厂规格，选型应核对制造商、包装标识及正式资料。

## 官方资料

- [SS49E 原厂资料入口](https://automation.honeywell.com/us/en/products/sensing-solutions/sensors/magnetic-sensors/ss39et-ss49e-ss59et-linear-hall-effect-sensor-ic)

- [Honeywell Issue4数据手册（官方PDF）](https://prod-edam.honeywell.com/content/dam/honeywell-edam/sps/siot/en-ca/products/sensors/magnetic-sensors/linear-and-angle-sensor-ics/common/documents/sps-siot-ss39et-ss49e-ss59et-product-sheet-005850-3-en-ciid-50359.pdf)
