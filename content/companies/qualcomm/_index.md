---
title: "Qualcomm"
wiki: true
wiki_type: "company"
wiki_rank: 64
seed_count: 3
lastmod: "2026-10-22"
description: "高通机器人平台以 IQ10、IQ-9075、QCS6490 分档，第三方控制器公开 100 TOPS 与 2 路 CAN FD，接口表里没有编码器输入。"
official_url: "https://www.qualcomm.com/internet-of-things/applications/robotics-processors"
wiki_category: "计算平台与机器人软件"
related_models: []
---

高通在这条链上的角色与 NVIDIA 类似但落点更低：它卖的是带视觉与 AI 加速的 SoC，用在 AMR、无人机与人形的控制盒里。与编码器的交界仍然是总线而不是传感器——公开的机器人控制器规格表里，能做关节反馈的接口是 CAN FD，不是编码器输入。

## 公司与品牌

机器人业务挂在物联网（IoT）产品线之下，官网 2026 年用 Dragonwing 这一品牌统称工业与机器人处理器。定位写法强调能效、内置功能安全、AI 推理与"开放的硬件、软件与 MLOps 工具"，覆盖从家用机器人到人形。[机器人与无人机页](https://www.qualcomm.com/internet-of-things/applications/robotics-processors)

## 平台按档位分，第三方控制器把接口写清楚了

官网按系列列产品，第三方合作控制器则给出可直接核对的接口清单：

| 平台 | 官网写的定位 | 公开的接口与性能 |
| --- | --- | --- |
| [Dragonwing IQ10](https://www.qualcomm.com/internet-of-things/products/iq10-series) | 机器人线的旗舰档，面向 AMR、人形与通用机器人 | 强调 AI、算力与图像处理，内置功能安全；具体数字要看单型号页 |
| [IQ-9075](https://www.qualcomm.com/internet-of-things/products/iq9-series/iq-9075) | 工业级、宽温、算力密集设备 | 研华 AFE-A503 用它做到最高 100 TOPS，带 4 路 GbE、4 路 USB、2 路 COM、2 路 CAN FD、16 位 DIO、3 个 M.2，可接 LiDAR、IMU 与可选的 GMSL 相机 |
| [QCS6490](https://www.qualcomm.com/internet-of-things/products/q6-series/qcs6490) | 连接性强、IO 扩展多的边缘设备 | 官网强调多千兆连接、可扩展算力与摄像头能力 |
| QRB5165（RB5） | 消费、企业或工业机器人 | 端侧 AI 加 5G 连接 |
| [RB3 Gen 2 开发套件](https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit) | 面向 IoT 的 AI 边缘开发套件 | 用于早期验证，不当作量产规格 |

这张表里没有任何一项是编码器或旋变输入。关节反馈在驱动器一侧采集，经 CAN FD 或 EtherCAT 上到控制器；控制器能做的只是给出目标位置与读取状态字。

## 在编码器链上的位置

一条多轴设备的信号路径是：编码器 → 驱动器（换相与闭环）→ 现场总线 → 控制器 SoC。高通站在最后一格，所以它决定的是"一台设备能跑几路视觉、能不能在端侧跑模型、控制盒做多大"，不决定角度怎么测。功能安全也一样：SoC 内置安全机制只覆盖它自己那一格，整链的等级仍按 13849 或 62061 在系统层算。

官网给系列定位与部分合作方案的接口，不给各型号的工业温度等级细表、长期供货承诺、CAN FD 实际抖动与 EtherCAT 主站支持情况；这些要查型号数据手册与合作方文档。

## 官方资料

- [高通机器人与无人机处理器](https://www.qualcomm.com/internet-of-things/applications/robotics-processors)
- [Dragonwing IQ10 系列](https://www.qualcomm.com/internet-of-things/products/iq10-series)
- [IQ-9075](https://www.qualcomm.com/internet-of-things/products/iq9-series/iq-9075)
- [QCS6490](https://www.qualcomm.com/internet-of-things/products/q6-series/qcs6490)
- [RB3 Gen 2 开发套件](https://www.qualcomm.com/developer/hardware/rb3-gen-2-development-kit)
