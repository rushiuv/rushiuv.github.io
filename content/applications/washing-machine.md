---
{"title":"洗衣机：转子脉冲正常，不代表滚筒状态正常","description":"霍尔锁存与双通道磁检测可以提供转速或换向信息，机械传动、失衡与门锁仍是其他测量链。","date":"2026-10-18T10:00:00+08:00","lastmod":"2026-10-18","layout":"application-single","application_entry":true,"application_group":"消费电子","weight":4,"related_basics":["pole-pairs","abz","latency"],"reference_topic":"洗衣机"}
---

洗衣机低速翻转与高速脱水的工况相差很大。若用磁检测读取电机转子或专用磁环，首先要明确脉冲属于哪个轴：直驱结构与皮带传动的换算不同，电机在转也不必然说明滚筒按预期运动。

## 霍尔信号可以承担不同任务

磁极事件与连续角度可以分别进入设计，但不能混用计数和控制接口：

| 候选 | 测量量或输出 | 适用边界 | 原厂来源 |
|---|---|---|---|
| TI TMAG5115 | 霍尔锁存数字状态 | 需匹配磁极与换向布局 | [详情](https://www.ti.com/product/TMAG5115) |
| Allegro A1233 | 双通道速度、方向路线 | 核对封装对应的输出配置 | [详情](https://www.allegromicro.com/en/products/sense/switches-and-latches/latches/a1233) |
| 昆泰芯 KTH4622 | 二维磁检测，速度与方向输出 | 按后缀核查采样档是否覆盖最高转速 | [KTH462N详情](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/highsensitive2Dhallswitch/index.html) |
| 昆泰芯 KTH7101 | 磁绝对角度，SPI等路线 | 连续角度不是原锁存信号的直接替换 | [型号详情](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/magneticencoder/index.html) |

这些是可评估前端，不表示某台洗衣机已采用，也不构成完整电机控制方案。尤其不能用低功耗采样档的平均电流，替代高速脱水时对最窄磁极事件的检验。

用于换向时，还要定义传感器相对转子磁极的安装位置与相序；用于测速时，则应明确每转脉冲数和使用哪些边沿。同一个“脉冲数”如果在一处数完整周期、另一处数双边沿，就可能得到成倍的转速偏差。

## 慢速和高速分别暴露不同问题

低速正反转应检查停在阈值附近的状态、首次启动和方向切换；高速应检查最窄脉冲、输入滤波、计时器捕获与丢边沿。高转速下仍能输出方波，不足以证明它与控制器采样时刻保持合适的相位关系。

## 不把测速链扩写成整机安全链

线束受潮、磁环位移、振动、温度及电机通电干扰都应在验证范围。还要区分传感器断线和转子静止，不能把“没有脉冲”无条件解释为已经停稳。滚筒失衡、门是否可靠锁住以及是否允许开门，需要对应的检测和控制证据，不能仅由一个转速读数推断。涉及市电和旋转部件的测试，应由具备条件的人员在安全防护下进行。

## 原厂资料

- [TI TMAG5115](https://www.ti.com/product/TMAG5115)
- [Allegro A1233](https://www.allegromicro.com/en/products/sense/switches-and-latches/latches/a1233)
