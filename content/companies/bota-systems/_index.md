---
title: "BOTA Systems"
wiki: true
wiki_type: "company"
wiki_rank: 205
lastmod: "2026-10-22"
description: "苏黎世 ETH 机器人系统实验室衍生公司，做 6 轴力/力矩与关节力矩传感器：MiniONE 30 克、Rokubi 120 克带 EtherCAT 菊花链，量程与采样率只在 datasheet 里。"
wiki_category: "力觉传感与机器人部件"
official_url: "https://www.botasys.com/about"
---

BOTA Systems 站在"力觉传感与机器人部件"这一层，卖的是六轴力/力矩传感器、关节力矩传感器、夹爪和定制件。它与角度测量不是竞争关系，而是**同一个关节里的另一路测量**：力/力矩靠应变敏感元件做，角度靠编码器或磁传感做，两者共用安装面、共用对外的总线与同步时钟，但器件链完全分开。对做编码器的人，它的价值在于看清"关节里第二路信号"的接口与带宽要求，以及一家 ETH 衍生公司如何在十年里把实验室件做成产品目录。

## 公司与品牌

官方自述是苏黎世联邦理工机器人系统实验室（Robotic Systems Lab, ETH Zürich）的衍生公司，创始人为 Klajd Lika、Ilias Patsiaouras、Marco Hutter。时间线值得抄下来：2013 年做出第一台用于腿式机器人的多轴力矩传感器原型，同期开发 HAKI（Rokubi 的前身）；2015 年扩到关节力矩传感器、单轴力传感器与触觉；2016 年与 ETH 机器人系统实验室合作给 ANYmal 装 Rokubi；2019 年 Rokubi 与 SensONE 首次商业化；2020 年正式成立 Bota Systems AG；2022 年推出 Medusa、LaxONE、MegaONE；2023 年扩产；2024 年推出 MiniONE 与 MiniONE Pro，并在雅典设子公司、在加州 Fremont 开客户体验中心。[About](https://www.botasys.com/about)

## 公开产品线与能核到的参数

目录分四块：六轴力/力矩传感器（MiniONE、MiniONE Pro、MimX Gen A、Rokubi、SensONE、SensONE T80、PhisX Gen A、PixONE、LaxONE、MegaONE）、按机器人型号预配的套装（UR、Franka FR3、Kinova Gen3、FANUC CRX、KUKA KR4、Stäubli、Kassow、Meca500、Unitree G1、AgileX、I2RT YAM）、夹爪 GraspX，以及关节力矩传感器与定制件。

| 系列 | 类型 | 公开的关键数值 | 其他公开参数 |
| --- | --- | --- | --- |
| [MiniONE](https://www.botasys.com/force-torque-sensors/minione) | 六轴力/力矩，微型 | 整机 30 克 | USB、UART、RS232/422/485、Modbus；可配滤波、分辨率与更新率；有 Robotiq 2F 指尖套装 |
| [Rokubi](https://www.botasys.com/force-torque-sensors/rokubi) | 六轴力/力矩，腿式与人形常用 | 整机 120 克 | EtherCAT 与工业两种通信变体；双量程（高灵敏/高量程）；供电 5~75 V；支持菊花链 |
| [SensONE](https://www.botasys.com/force-torque-sensors/sensone) | 六轴力/力矩，工业型 | 整机 240 克 | EtherCAT 与工业两种变体；双量程；ISO 法兰适配中等负载机器人；配 UR、Franka、Stäubli、Kuka、Kassow、Piper 套装 |
| [GraspX](https://www.botasys.com/grippers/graspx) | 夹爪 | 每根手指装 TactX 六轴力觉，官方称每指 12 自由度感知 | 与自家力觉配套 |

唯一能在公开页面核到的是重量、供电与接口，**量程、分辨率、采样率、过载与温漂都只在 datasheet 里**，网页不写。

## 在编码器链上的位置

关节里有两路测量：力矩与角度。BOTA 占力矩这一路，信号链是应变敏感元件加专用前端与 ADC；角度那一路由编码器或磁传感完成，两路在同一个关节壳体内、共用对外的现场总线与时序。这意味着两件事：**它是同一安装面的邻件，不是竞争对手**；但它对总线的要求（EtherCAT 同步、菊花链、低延时）会直接影响角度器件要不要跟同一条总线。

不能推的部分：BOTA 的官方页面不披露敏感元件的具体型式与前端芯片，也不提任何编码器方案；反过来说，也不能因为某台机器人用了 BOTA 的力矩传感器，就推断它关节里用了哪家的角度器件。两边是独立采购。

## 公开资料的边界

公开网页给的是形态、重量、接口、量程档位数量与供电范围。**没有公开**：各型号的力/力矩量程数值、分辨率、采样率、过载倍数、温漂、串扰、防护等级的具体等级、价格与交期。这些要下对应型号的 datasheet，或走 Sensor Config Tool 配置后询价。本页不填没有来源的数字。

## 官方资料

- [About Bota Systems](https://www.botasys.com/about)
- [产品总览](https://www.botasys.com/products)
- [六轴力/力矩传感器目录](https://www.botasys.com/force-torque-sensors)
- [MiniONE 产品页](https://www.botasys.com/force-torque-sensors/minione)
- [Rokubi 产品页](https://www.botasys.com/force-torque-sensors/rokubi)
- [SensONE 产品页](https://www.botasys.com/force-torque-sensors/sensone)
- [GraspX 夹爪](https://www.botasys.com/grippers/graspx)
