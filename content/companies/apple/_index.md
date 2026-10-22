---
title: "Apple"
wiki: true
wiki_type: "company"
wiki_rank: 77
seed_count: 2
lastmod: "2026-10-22"
description: "Apple 在编码器链上属终端应用层：iPhone 18 Pro 用第二代与 3D sensor-shift 防抖，Vision Pro 靠 6 个追踪相机加 4 个眼动相机算位姿，官方从不披露角度反馈分辨率与供应商。"
official_url: "https://www.apple.com/"
wiki_category: "终端产品与感知应用"
related_models: []
---

Apple 站在链条最末端的终端应用层，而且是"只发布结果、不发布器件"那一端。它公开的每一个角度问题都有自己的解法：手机防抖是把整块图像传感器在平面内甚至三维上做闭环微位移，头显位姿靠 6 个追踪相机加 4 个眼动相机做视觉解算。对做编码器与磁传感的人，Apple 不是可直供的客户，而是"最高端消费电子如何绕开旋转测量"的对照样本：需求由它定义，器件名字从未出现在官网上。

## 三条产品线，三种角度问题的解法

Apple 官网公开的规格里能读到三套不同的技术选择。iPhone 18 Pro 的主摄与超广角是 48MP Fusion，主摄写"第二代 sensor-shift 光学图像防抖"，长焦给"3D sensor-shift 光学图像防抖与自动对焦"配 tetraprism 结构，实现 4 倍光学与 8 倍光学品质变焦，屏幕是最高 120Hz 的 ProMotion。[iPhone 18 Pro 规格](https://www.apple.com/iphone-18-pro/specs/)

Vision Pro 的规格页列出：两个主相机、6 个外向追踪相机、4 个眼动相机、TrueDepth 相机、LiDAR 扫描仪、闪烁传感器与环境光传感器；支持 90Hz、96Hz、100Hz、120Hz 四档刷新率；一般使用续航 2.5 小时、视频播放 3 小时；外接电池 353 克；芯片侧是 M5 与 R1 两颗。[Vision Pro 规格](https://www.apple.com/apple-vision-pro/specs/)

Mac 与 iPhone 的主芯片都是自研，这条在公开页面上能核实。[Mac](https://www.apple.com/mac/)；[iPhone 18 Pro](https://www.apple.com/iphone-18-pro/)

## 位移防抖是微执行器闭环，官方只给名字不给指标

"sensor-shift"这个说法在规格页上的层级只到"第几代、几轴"：主摄是第二代、长焦是 3D（三轴）。工程上这意味着把整块传感器做闭环微位移，需要有执行器、位置反馈与控制环三件套。**公开资料到此为止**——执行器行程、位置反馈方式（霍尔、磁阻、光学还是电容）、闭环带宽、控制频率，一处都没有。

对比之下，Vision Pro 的头部位姿完全不走机械测量：6 个外向相机加 IMU 解算 6DoF，眼动是 4 个相机做视线估计。这条路线对"角度测量"的启示是，消费级的高精度角度需求正在被视觉与惯性吃掉，留给旋转编码器的位置是**执行器内部的闭环**，而不是系统级位姿。

## 在编码器链上的位置

Apple 不采购"编码器"这个品类。它的角度信息来自三处：图像（位姿与眼动）、惯性（IMU）、闭路微执行器（防抖与对焦的音圈/压电结构）。选型权在 Apple 自己的硬件团队，以及它认证的模组厂；官网看不到任何一颗器件的名字、型号或供应商。

所以对器件厂，它的角色是"模组厂背后的终端定义者"：接口、尺寸、功耗、可靠性预算由它划，器件由模组厂去选。**不能推的部分必须写明**：任何 Apple 产品用哪家磁传感器或编码器芯片，官网零披露；也不能从 48MP、8 倍变焦、120Hz 这些数字反推任何反馈分辨率或延时。

## 公开资料的边界

公开页面给的是相机像素与防抖型式、屏幕刷新率、传感器数量、续航与重量、芯片型号。**没有公开**：防抖执行器的行程与闭环带宽、对焦行程、IMU 的型号与噪声密度、头显位姿解算延时、任何器件供应商与 BOM、整机报价结构。这些只能靠拆解或认证文件，本页不做这类推断，也不写"Apple 用了某家方案"。

## 官方资料

- [Apple 官网首页](https://www.apple.com/)
- [iPhone 18 Pro 规格](https://www.apple.com/iphone-18-pro/specs/)
- [iPhone 18 Pro 产品页](https://www.apple.com/iphone-18-pro/)
- [Apple Vision Pro 规格](https://www.apple.com/apple-vision-pro/specs/)
- [Apple Vision Pro 产品页](https://www.apple.com/apple-vision-pro/)
- [Mac 产品线](https://www.apple.com/mac/)
- [Apple Newsroom](https://www.apple.com/newsroom/)
