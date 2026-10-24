---
title: "TMR1202系列"
description: "连续感测的TMR锁存开关，不同后缀对应轴向和阈值选项。"
wiki: true
wiki_type: "model"
wiki_rank: 236
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["多维科技"]
wiki_category: "磁开关"
catalog_vendor: "多维科技"
catalog_type: "磁开关"
catalog_form: "芯片"
search_aliases: ["TMR1202","TMR1202D","TMR1202H","TMR1202HT"]
official_url: "https://www.dowaytech.com/sensor/switch_sensors.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 检测逻辑 | 双极锁存，不是全极接近开关 |
| 敏感方向 | 1202为X轴；1202D为Y轴 |
| 输出／电流 | 目录推挽，典型1.5µA |
| 后缀区别 | H／HT需核对阈值及温度条件，不据名称假定互换 |

参数来源：本页所列[原厂产品资料与手册](https://www.dowaytech.com/sensor/switch_sensors.html)。

## 工作方式与型号定位

TMR1202是连续感测的双极锁存开关，磁体移开不必然复位，需按相反极性达到释放条件。它适合磁极交替的状态检测，不能直接替代全极接近开关。

## 安装、接口与配置

1202与1202D分别对应X轴和Y轴敏感方向。封装摆放相同而敏感轴不同会改变可检测磁场，因此PCB旋转方向、磁体极性和运动路径需一起确认。

## 校准与选型验证

推挽输出应检查控制器电平和上电状态。H、HT等后缀的阈值与温度应按完整型号选择；台架测试需包含正反磁场、静止边界及快速磁极切换，不把典型电流当成所有条件最大值。

## 官方资料

- [TMR1202系列 官方资料](https://www.dowaytech.com/sensor/switch_sensors.html)
