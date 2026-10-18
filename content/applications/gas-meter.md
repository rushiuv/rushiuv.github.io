---
{"title":"燃气表：转得很慢，也要保住每一次计数","description":"磁计数路线需要同时核对低功耗采样、方向与机械计量关系，不能把脉冲直接当标准体积。","date":"2026-10-18T10:00:00+08:00","lastmod":"2026-10-18","layout":"application-single","application_entry":true,"application_group":"工业与运动","weight":203,"related_basics":["pole-pairs","abz","absolute-incremental"],"reference_topic":"燃气表"}
---

带机械传动的燃气表，可以把计量机构的运动转换成磁极经过传感器的事件。芯片先得到磁状态或边沿，累计体积仍要使用已确定的机械传动关系和计量系数；涉及温压补偿时，还需要额外测量与模型。

## 低功耗与最窄事件要一起算

磁极事件、转向信息和电池消耗应放在同一个转动工况下比较：

| 候选 | 测量量或输出 | 适用边界 | 原厂来源 |
|---|---|---|---|
| TI DRV5012 | 低功耗霍尔锁存状态 | 单路状态不自动提供方向 | [详情](https://www.ti.com/product/DRV5012) |
| Infineon TLI4966G | 双霍尔速度、方向路线 | 需核对系统功耗与磁极轮 | [详情](https://www.infineon.com/part/TLI4966G) |
| 昆泰芯 KTH4622 | 二维磁检测，速度与方向输出 | 采样档必须覆盖最窄磁极事件 | [KTH462N详情](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/highsensitive2Dhallswitch/index.html) |
| 昆泰芯 KTM1301 | 全极TMR开关 | 可评估单路计数；不直接提供方向 | [具体型号表](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/magnetoresistiveSwitchSeries/index.html) |

KTH4622增加方向相关信息，KTM1301提供另一种低功耗磁事件路线；二者都不是体积计量芯片。工作频率、门限与电流要按完整订货后缀配对，不能取各版本的最好数字拼成一个器件。

假设机械每转产生4个有效计数，计量系数为每转0.01立方米，则每个有效计数代表0.0025立方米。这是机械关系算例，不是通用燃气表常数。边沿数量、转向和复位恢复若错一项，累计误差就会持续留下。

## 停在阈值附近最容易暴露问题

传动轮在极低速、反向或振动中经过阈值，单路数字状态不能自动区分一次正向通过与多次往返。锁存特性、磁极间距和方向判别，需要配合真实机构确认。低功耗周期采样还要覆盖最快瞬时运动，不能以平均转速很低判定不会漏计。

## 验证计数，而非只看输出会翻转

在获准的测试设备上比较机械基准、原始边沿、方向和累计量，覆盖启动、停止、反转、断电及低电量恢复。还需核对外磁干扰与温度条件。可燃气环境与计量设备有独立安全、密封及认证要求，磁传感器选型不能代替这些验证，也不授权现场改表。

## 原厂资料

- [TI DRV5012](https://www.ti.com/product/DRV5012)
- [Infineon TLI4966G](https://www.infineon.com/part/TLI4966G)
