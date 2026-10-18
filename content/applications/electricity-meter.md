---
{"title":"电表：磁检测先分清计量与异常外场","description":"电能积分与磁干扰告警是不同链路，三轴磁传感器不能直接代替计量芯片。","date":"2026-10-18T10:00:00+08:00","lastmod":"2026-10-18","layout":"application-single","application_entry":true,"application_group":"工业与运动","weight":201,"related_basics":["magnetic-encoder","stray-field","angle-noise"],"reference_topic":"电表"}
---

电子电表没有必须旋转的码盘。电能计量需要电压、电流及其时间关系；增加磁传感器，常见任务是观察外部磁场是否异常，而不是把磁场幅值直接换成用电量。把两个任务画成独立链路，才不会为防干扰器件套用计量精度指标。

## 磁检测报告的是外场，不是偷电结论

异常外场检测可以保留连续磁场，也可以只记录阈值事件。候选应按同一施加方向、采样周期和告警目标比较：

| 候选 | 测量量或输出 | 适用边界 | 原厂来源 |
|---|---|---|---|
| TI TMAG5273 | 连续三轴磁场 | 能保留向量，需主控定义判据 | [详情](https://www.ti.com/product/TMAG5273) |
| Allegro A1266 | 三维磁开关 | 记录触发，不直接给外场幅值 | [详情](https://www.allegromicro.com/en/products/sense/switches-and-latches/switches/a1266) |
| 昆泰芯 KTH4603 | XYZ全极霍尔开关 | 核对采样档与输出组合 | [详情](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/highlysensitive3dhallswitch/index.html) |
| 昆泰芯 KTM1301 | 全极TMR开关 | 核对平面内敏感方向及布局盲区 | [具体型号表](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/magnetoresistiveSwitchSeries/index.html) |

KTM1301的低功耗磁事件路线和KTH4603的多方向检测各有适用条件，都不能凭单颗器件宣称整表抗磁覆盖。上述型号也不是指定电表实际采用或通过计量认证的证明。

外场告警只能说明测点满足触发条件，不能单独证明计量已经失准，也不能证明用户行为。系统需要保留触发时刻、持续时间、电源状态及计量侧独立诊断，再按既定流程处理。

## 盲区由装在哪里决定

只测一个方向，另一方向的外场可能未达到敏感轴阈值。改用三维检测也不保证整只表壳都被覆盖；外场在空间中变化，局部磁屏蔽和内部大电流路径都会影响测点。强场使器件超量程时，饱和码也不再代表真实场强。

## 验证覆盖，不靠一次靠近演示

比较候选芯片应核对磁场范围、恢复行为、低功耗采样周期、工作温度与上电默认状态。整机试验需由合格人员按计量及电气安全要求完成，覆盖不同施加方向、位置和电流工况。不能以“磁告警正常”替代整表误差、绝缘或计量认证，也不能擅自拆表改线。

## 原厂资料

- [TI TMAG5273：低功耗三轴磁测量](https://www.ti.com/product/TMAG5273)
- [Allegro A1266：三维磁开关](https://www.allegromicro.com/en/products/sense/switches-and-latches/switches/a1266)
