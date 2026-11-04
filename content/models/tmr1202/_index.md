---
title: TMR1202系列
description: 连续感测的TMR锁存开关，不同后缀对应轴向和阈值选项。
wiki: true
wiki_type: model
wiki_rank: 236
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 多维科技
wiki_category: 磁开关
catalog_vendor: 多维科技
catalog_type: 磁开关
catalog_form: 芯片
search_aliases:
- TMR1202
- TMR1202D
- TMR1202H
- TMR1202HT
- TMR1202系列
official_url: https://www.dowaytech.com/sensor/switch_sensors.html
document_version: 官方公开产品页或目录，核对：2026-10-18
model_card: true
catalog_level: 系列
---

TMR1202系列采用双极锁存逻辑。选择成员时先确定磁场敏感轴，再按完整后缀核对门限与温度。

## 型号与核心异同

| 具体型号 | 敏感轴 | 共同逻辑 | 后缀差异 |
| --- | --- | --- | --- |
| TMR1202 | X轴 | 双极锁存 | H／HT的阈值与温度需按手册 |
| TMR1202D | Y轴 | 双极锁存 | 具体订货选件需按手册 |

## 共同条件与参数依据

- **输出／电流**：目录推挽，典型1.5µA

## 接入电路与配置

1202与1202D分别对应X轴和Y轴敏感方向。封装摆放相同而敏感轴不同会改变可检测磁场，因此PCB旋转方向、磁体极性和运动路径需一起确认。

## 标定与应用验证

推挽输出应检查控制器电平和上电状态。H、HT等后缀的阈值与温度应按完整型号选择；台架测试需包含正反磁场、静止边界及快速磁极切换，不把典型电流当成所有条件最大值。

## 官方资料

- [TMR1202系列 官方资料](https://www.dowaytech.com/sensor/switch_sensors.html)
