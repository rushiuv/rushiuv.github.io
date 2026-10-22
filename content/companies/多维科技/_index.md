---
title: "多维科技"
description: "多维科技 Dowaytech（MDT）：江苏 TMR/AMR 磁传感器 IDM，TMR3081 车规角度芯片全温区误差小于 0.8 度，机器人关节对轴方案给到 0.05 度。"
wiki: true
wiki_type: "company"
wiki_rank: 18
seed_count: 12
lastmod: "2026-10-22"
official_url: "https://www.dowaytech.com/"
related_models: []
related_companies: []
---

多维科技站在磁阻敏感元件这一层：它做 TMR、AMR 的感应电桥，也做把电桥信号变成角度或阈值的芯片，另外还卖磁传感器晶圆代工。对做编码器的人，它最有用的公开材料不是分辨率数字，而是它把“对轴一颗数字角度芯片”和“离轴四颗线性芯片加一颗解算芯片”这两条关节编码器路线连同各自精度口径一起写了出来。

## 公司与品牌

中文名 江苏多维科技股份有限公司，英文 MultiDimension Technology，简称 MDT，现行品牌写作 Dowaytech。官网版权行为 2011–2026，备案主体在江苏（苏ICP备18053872号）。目录分两段：芯片侧是 TMR 开关、角度、线性、齿轮，AMR 开关、角度、线性、磁栅，以及薄膜型温度传感器；模组侧是磁图像检测、电流传感器、齿轮编码器、AGV 磁导航、低噪声线性、流量与 USB 磁强计。[官网](https://www.dowaytech.com/)

公司自述做的是“磁传感器晶圆 IDM 模式制造平台”，对外也提供晶圆代工，公开口径是“经过十多年”的积累。这一点决定了它在链上不是纯设计公司：工艺与器件是它自己的资产，客户买到的既是芯片也是定制片的制造能力。

## 编码器相关产品线与公开规格

| 系列 | 类型 | 公开精度口径 | 其他公开参数 |
| --- | --- | --- | --- |
| [TMR3081](https://www.dowaytech.com/TMR3081-TMR-Angle-Sensors-Automotive-Electronics.html) | 车规 TMR 角度，模拟 sin/cos 差分 | 全温区角度误差 < 0.8°（−40…+150 °C） | 工作磁场 200–800 Gs、TSSOP8、对轴与离轴、AEC-Q100 与 NEVC 认证、上电即输出有效角度 |
| [TMR3015](https://www.dowaytech.com/TMR3015-TMR-Angle-Sensors-High-Precision.html) | 高精度 TMR 角度，模拟单端 sin/cos | 官方表述为配合磁路与闭环可做到微米级重复定位 | 双半桥四元件、3–5.5 V、−40…+85 °C、DFN4L 0.8×0.4×0.23 mm 与 1.6×1.6×0.5 mm、SOT23-5 三种封装 |
| TMR3110／TMR3111 | 数字角度，用于对轴关节编码器方案 | 自校准配合单对极磁铁 0.05° | 40000 rpm、SPI／ABZ／PWM、TMR3111D 封装 DFN10L 3×3×0.75 mm |
| TMR2615 + MDT3259 | 线性 TMR 四颗按 90° 排布，加角度运算芯片 | 离轴方案 ±0.15° | 3000 rpm 以上、TMR2615 为 DFN3L 1.6×1.6×0.5 mm、MDT3259 为 DFN24L 4×4×0.75 mm、带多阶谐波校准 |

三条要分开读。TMR3081 与 TMR3015 是芯片级口径，0.8° 是“全温区最大角度误差”，TMR3015 干脆没有给度数。0.05° 与 ±0.15° 是方案级口径，含磁铁、气隙、排布与校准，不能当成裸芯片精度去和别人的单颗数字直接比。[关节编码器方案](https://www.dowaytech.com/Dowaytech-Magnetic-Encoder-Solution-for-Robot-Goints.html)

离轴方案值得单独看一眼：四颗 TMR2615 在磁环外圈按 90° 排布，靠四路互相补偿压掉轴向与径向抖动，再由 MDT3259 做自校准、出绝对角。这条路线的取舍是拿器件数量和布板面积换安装容差，和一颗芯片贴轴端的做法不是一个成本结构。

官网给的是芯片级典型值与最大值，以及方案级的合成精度。要拿它的数和霍尔、AMR 对比，先对齐口径——全温区最大误差、25 °C 典型误差、含磁铁校准后的方案误差是三个不同的量。

## 在编码器链上的位置

多维在链上属于“自己有磁阻工艺线”的那一类。往上它买衬底、镀膜靶材与封测产能，往下它卖芯片、方案与代工服务。因此对整机编码器厂，它是可选的磁阻敏感元件与角度解算来源；对芯片同行，它同时是工艺与产能的参照物。

能推断的是它在 TMR 材料与工艺上的投入深度——车规认证、全温区误差、多种超小封装都是公开的。**不能推断**的是某家编码器整机厂内部用了谁的裸片：官网不公布客户名单，也不公布 BOM。看到“某整机用 TMR”时，只能反推它对温度与精度的取舍。

## 官方资料

- [多维科技官网](https://www.dowaytech.com/)
- [TMR3081 车规角度传感器芯片发布](https://www.dowaytech.com/TMR3081-TMR-Angle-Sensors-Automotive-Electronics.html)
- [TMR3015 高精度角度传感器芯片发布](https://www.dowaytech.com/TMR3015-TMR-Angle-Sensors-High-Precision.html)
- [机器人关节磁编码器方案（对轴、离轴、双对轴）](https://www.dowaytech.com/Dowaytech-Magnetic-Encoder-Solution-for-Robot-Goints.html)
- [磁性器件晶圆定制及代工](https://www.dowaytech.com/foundry.html)
