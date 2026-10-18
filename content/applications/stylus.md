---
{"title":"触控笔：测到笔尖位移，还没有测到书写压力","description":"磁传感可以读取笔内运动，但压力标定、倾斜干扰和屏幕坐标属于不同问题。","date":"2026-10-18T10:00:00+08:00","lastmod":"2026-10-18","layout":"application-single","application_entry":true,"application_group":"消费电子","weight":1,"related_basics":["magnetic-encoder","air-gap","resolution-accuracy"],"reference_topic":"触控笔"}
---

触控笔里的一颗磁传感器，可以围绕笔芯轴向移动或侧键动作建立测量链；它并不因此获得笔尖在屏幕上的二维坐标。这里讨论的是“笔内位移检测”这一候选结构，不代表任何品牌触控笔采用了以下器件。

## 先把压力变成可重复的运动

一种设计是让小磁体随笔芯移动，固定传感器读取磁场变化，再通过弹性件把接触力映射成位移。可把候选前端放在同一条“磁场—位移—力”链上比较：

| 候选 | 测量量或输出 | 适用边界 | 原厂来源 |
|---|---|---|---|
| TI TMAG5273 | 多轴磁场，I²C | 可观察侧向变化；仍需力标定 | [详情](https://www.ti.com/product/TMAG5273) |
| Melexis MLX90393 | XYZ磁场，数字输出 | 换测量模式会改变噪声与采样时间 | [详情](https://www.melexis.com/en/product/MLX90393/Triaxis-Micropower-Magnetometer) |
| 昆泰芯 KTH3105 | 比例式模拟磁场电压 | 单轴路线需外部ADC，先证明行程单调 | [KTH31型号表](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/proportionallinerhalleffectsensor/index.html) |

三者都不是已标定的笔尖力传感器。若轴向位移足够可区分，模拟单轴也值得验证；若侧向运动容易混入，则需更多观测量，而不是先按输出位数排序。

理想线性弹簧有力等于刚度乘位移的关系；实际还要扣清预紧力、摩擦和回程差。只用一次向下按压曲线换算压力，可能在抬笔时得到另一条结果。倾斜书写引起的侧向力，也可能改变笔芯导向与磁体姿态。

## 磁场变化必须能区分轴向和侧向

样机应同时保存原始磁场、位移参考及加载方向。先检查整个有效行程是否单调，再加入不同倾角、笔尖横向受力和装配偏移。如果两种机械状态给出几乎相同的磁场，增加输出位数不能解除这种歧义。

磁吸充电、笔套磁体或平板边框也可能改变局部磁场，应在接近真实使用姿态时验证，而不是只在裸板上测量。

## 选型看转换链，不只看小封装

需要比较量程、噪声、采样时间、休眠唤醒、接口和整笔功耗。快速书写时，过强平均滤波可能让笔尖已抬起、压力值还没归零。验证须覆盖轻触、连续划线、快速抬笔、温度变化及磨损后的回程；压力等级数不等于每一级都有同样的力分辨能力。

## 原厂资料

- [TI TMAG5273](https://www.ti.com/product/TMAG5273)
- [Melexis MLX90393](https://www.melexis.com/en/product/MLX90393/Triaxis-Micropower-Magnetometer)
