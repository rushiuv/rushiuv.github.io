---
title: "Embotech"
wiki: true
wiki_type: "company"
wiki_rank: 209
lastmod: "2026-10-22"
description: "做 L4 工业车辆自主驾驶的公司，AVM 把智能放在厂房而不是车上：基础设施激光雷达做厘米级定位，轨迹每秒 10 次、每包约 150 字节发给车辆，最高 30 km/h。"
wiki_category: "工业车辆自主驾驶"
official_url: "https://embotech.ai/"
---

Embotech 站在"工业车辆自主驾驶"这一层，而且选的是一条与车上装传感器完全相反的路：**智能放在厂房里，车上不加任何传感器与自驾硬件**。基础设施上的激光雷达负责定位，算好的轨迹以每秒 10 次、每包约 150 字节无线发给车辆。对做角度测量的人，它的意义不在"用不用编码器"，而在时间预算的写法——这条链上的指标不是延时小，而是延时可申报、行为确定。

## 公司与品牌

两个方案都在工业物流里：Automated Vehicle Marshalling（AVM）面向汽车主机厂与整车物流中心，官方称是全球唯一通过 TÜV SÜD 安全认证的 AVM 方案，2022 年起在 7×24 产线运行；Autonomous Tractor Solution（ATS）面向港口与堆场的牵引车，强调混合交通与全天候。[首页](https://embotech.ai/)；[AVM](https://embotech.ai/automated-vehicle-marshalling-solution)；[ATS](https://embotech.ai/autonomous-tractor-solution)

支撑产品是 FORCES Pro——一个把模型预测控制（MPC）问题自动编译成可嵌入代码的自动代码生成器，官方放在技术页里，说明算法栈自研且要跑在嵌入式目标上。[技术页](https://embotech.ai/technology)

## 公开指标：厘米级定位，10 Hz 下发，30 km/h

| 项目 | 官方口径 |
| --- | --- |
| 定位方式 | 厂房基础设施上的激光雷达，官方称厘米级 |
| 车上要求 | 不需要任何传感器或在车自驾系统 |
| 轨迹下发 | 无线，每秒 10 次，每包约 150 字节 |
| 速度 | 最高 30 km/h，且已做安全认证 |
| 运营量 | 每天 3,500 台以上车辆自主移动，7×24 生产，系统可用率 99.9% |
| 成本 | 官方称直接司机成本下降约 50% |
| 认证 | TÜV SÜD 认证，双路径架构：AI 路径加确定性安全路径 |

以上取自 AVM 页与技术页。[AVM](https://embotech.ai/automated-vehicle-marshalling-solution)；[技术页](https://embotech.ai/technology)

## 在编码器链上的位置

它不碰任何车上的转轴：定位靠厂房里的激光雷达，规划在后台，车辆只接收轨迹。**所以这条链上不存在"角度传感器→控制器"的闭环**，也就没有编码器的位置。这是它的架构决定的，不是它在省成本。

值得记下来的是它的时间预算写法：轨迹每秒更新 10 次，意味着上层位姿修正的周期是 100 ms 量级；真正被认证约束的是**安全路径的确定性**——每个动作都要被验证、系统健康要监控、异常要有受控退出。任何要进这条链的传感件，指标书里第一页写的不会是"延时多少微秒"，而是"最坏情况延时能不能被证明、采样时刻能不能被申报"。

不能推的部分：车辆侧到底怎么执行轨迹（是否用机械司机转方向盘踩踏板、是否走整车总线）、车辆侧有没有角度反馈、以及任何编码器品牌——官方页面全都没写。ATS 的牵引车改装方式同样没有公开。

## 公开资料的边界

公开页面给的是定位方式、下发频率与包大小、速度、运营量、可用率、认证与成本口径。**没有公开**：车辆侧执行机构与控制接口、传感器型号、算力平台、最坏情况延时、功能安全等级的具体条款、单站部署价格。这些要商务接触或看认证文件，本页不填没有来源的数字。

## 官方资料

- [Embotech 首页](https://embotech.ai/)
- [Automated Vehicle Marshalling（AVM）](https://embotech.ai/automated-vehicle-marshalling-solution)
- [Autonomous Tractor Solution（ATS）](https://embotech.ai/autonomous-tractor-solution)
- [技术页（双路径架构与 FORCES Pro）](https://embotech.ai/technology)
- [关于我们](https://embotech.ai/about-us)
