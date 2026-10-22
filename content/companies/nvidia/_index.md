---
title: "NVIDIA"
wiki: true
wiki_type: "company"
wiki_rank: 29
seed_count: 7
lastmod: "2026-10-22"
description: "NVIDIA 在机器人里卖 Jetson 与 Isaac：Thor 顶配 T5000 达 2070 TFLOPS 稀疏 FP4，相机走 16 通道 CSI 或 HSB，角度不经它。"
official_url: "https://www.nvidia.com/en-us/industries/robotics/"
wiki_category: "计算平台与机器人软件"
related_models: []
---

NVIDIA 不在编码器链上，它站在编码器的下游两步：关节角度经驱动器与现场总线上到控制器，Jetson 只负责感知、规划与推理。所以读它的资料要盯的是输入侧接口——相机走多少路 CSI、几路 HSB、功耗预算多少瓦，这些决定一台机器人能装几只眼，而不是决定它能测多准的角度。

## 公司与品牌

官网的机器人入口把业务写成三层：边缘计算（Jetson 系列与 IGX 工业平台）、开发框架（Isaac）、以及云端训练与仿真。Jetson 统一用 JetPack SDK，官网强调同一套软件覆盖全部模块，做实时传感器处理、视觉 AI 与机器人功能。[机器人业务页](https://www.nvidia.com/en-us/industries/robotics/)

## 平台按算力与功耗分档，接口清单比 TOPS 更有用

官网嵌入式页把各代模块的算力、功耗与相机接口并列，下面只抄它写了的数字：

| 系列 | 公开算力 | 公开功耗与接口 |
| --- | --- | --- |
| [Jetson AGX Thor / T5000](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/) | 最高 2070 TFLOPS 稀疏 FP4 | 40~130W；16 通道 MIPI CSI-2（D-PHY 2.1 最高 40Gbps、C-PHY 2.0），另有 HSB 相机经 QSFP 插槽，最多 20 路 |
| Jetson AGX Orin | 最高 275 TOPS | 15~60W；16 通道 MIPI CSI-2 连接器，最多 6 路相机（虚拟通道可到 16 路） |
| Jetson Orin NX | 最高 157 TOPS | 10~25W |
| Jetson Orin Nano Super | 67 TOPS | 入门级生成式 AI 边缘计算机 |
| IGX 平台 | 官网未给统一数字 | 工业边缘 AI 平台，基于 Blackwell 时代的 Thor 系统 |

软件侧，Isaac 提供仿真与机器人学习框架、CUDA 加速库、模型与参考工作流，面向 AMR、机械臂与人形；Isaac ROS 是面向 ROS 2 的开源基础，Isaac Manipulator 建在其上。[Isaac](https://developer.nvidia.com/isaac)；[Isaac ROS](https://developer.nvidia.com/isaac/ros)

## 在编码器链上的位置

Jetson 的输入清单里没有编码器这一类：相机走 CSI 或 HSB，IMU 与力传感器走 SPI/I2C 或以太网，关节反馈留在驱动器与实时总线那一层。所以"这台机器人用了 Jetson"只能推出它在视觉与推理上的投入，推不出角度反馈的方案、位数或颗数。反过来，做角度芯片的人看这套平台，需要的是它的时间预算：Thor 级模块把感知与规划压进同一块板，控制器留给总线周期与插补的余量会被重新分配。

官网给模块级算力、功耗与相机路数，不给整机 BOM、不给各接口的实际延时与抖动，也不给工业温度等级与长期供货年限——要查具体模块的数据手册与产品寿命声明。

## 官方资料

- [NVIDIA 机器人业务](https://www.nvidia.com/en-us/industries/robotics/)
- [Jetson 嵌入式平台与模块对比](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/)
- [Isaac 机器人开发平台](https://developer.nvidia.com/isaac)
- [Isaac ROS](https://developer.nvidia.com/isaac/ros)
- [Isaac Sim 仿真](https://developer.nvidia.com/isaac/sim)
