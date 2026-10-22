---
title: "奥比中光"
wiki: true
wiki_type: "company"
wiki_rank: 156
seed_count: 1
lastmod: "2026-10-22"
description: "奥比中光（Orbbec）：自研 MX6800 深度引擎 ASIC 的 3D 视觉厂，Gemini 335 双目相机 1280×800@30fps、2 米处空间精度≤1.5%，产品无转轴、不输出关节角。"
official_url: "https://www.orbbec.com/"
wiki_category: "光学感知与空间测量"
related_models: ["MX6800"]
---

奥比中光是这条链上少见的**自己做感知计算芯片的模组厂**：它把深度计算的 ASIC（[MX6800](/models/mx6800/)）和光学系统一起做成相机，卖的是"深度图 + 点云"。但要注意区分——MX6800 是深度引擎，处理的是双目/结构光的视差解算，不是磁或光学的角度测量芯片；这家公司没有一根转轴，也不输出关节角。读它资料的正确姿势是看芯片与光学怎么分工、以及精度指标在什么距离与 ROI 下成立。

## 公司与品牌

全称奥比中光，英文 Orbbec，中文站 orbbec.com.cn、国际站 orbbec.com，自述"机器人视觉及 AI 视觉科技公司"。产品线按双目 3D 相机、ToF 相机、单目结构光、智能相机、激光雷达、无本体数据采集平台分栏，各栏都有在售型号与参数页。[奥比中光中文站](https://www.orbbec.com.cn/)

客户口径写在中文字站案例栏："为全球超 7000 家客户提供优质产品和服务"。案例栏有一条可核对的具体用法：韩国 Twinny 的 NarGo 订单拣选机器人每台装两台 Gemini 335，用于自主定位、路径规划、避障与交互，官网称该项目物流运营成本降低 64.4%。[奥比中光中文站](https://www.orbbec.com.cn/)；[Twinny 案例](https://www.orbbec.com/case-studies/logistics-costs-reduced-by-64-4-twinny-launches-latest-logistics-robot-product-equipped-with-orbbec-cameras/)

英文站的新闻区还挂着一条技术来源信息：奥比中光发布基于微软 iToF 深度技术的产品族。这条只说明 iToF 这一支有对外授权关系，不涉及其他系列。[iToF 产品族新闻](https://www.orbbec.com/news/orbbec-announces-family-of-products-based-on-microsoft-itof-depth-technology/)

## 产品线与公开规格

下表数值取自官方产品页，同一系列型号间差异大，属"视型号"口径。

| 系列 | 类型 | 公开深度规格 | 其他公开参数 |
| --- | --- | --- | --- |
| [Gemini 335](https://www.orbbec.com/products/stereo-vision-camera/gemini-335/) | 主动 + 被动双目，850 nm，50 mm 基线 | 1280×800@30 fps，量程 0.10–20 m+（最佳 0.26–3 m），2 m 处空间精度 ≤1.5%（90%×90% ROI） | MX6800 ASIC 处理，FOV H90°×V65°，RGB 1920×1080@30 fps，USB 3.0 Type-C，<3 W，−10–45 ℃，90×25×30 mm，97 g，IP5X，支持 IMU 与触发 |
| [Gemini 338Le](https://www.orbbec.com.cn/) | 双目，抗环境光，工业接口版 | 官网列抗环境光干扰与稳定深度成像 | 千兆以太网 + PoE |
| [Gemini 338Lg](https://www.orbbec.com.cn/) | 双目，车规级串行接口版 | 同上 | GMSL2 / FAKRA |
| [Gemini 335Le](https://www.orbbec.com.cn/) | 双目，加固版 | 官网标"可靠耐用" | 千兆以太网 + PoE，IP67 |
| [Femto Bolt / Femto Mega](https://www.orbbec.com/products/tof-camera/femto-mega/) | iToF 深度相机 | 系列级参数见产品页 | 面向物流、机器人、医疗与健身场景 |
| [Astra 2 / Astra Mini Pro](https://www.orbbec.com/products/structured-light-camera/astra-2/) | 单目结构光 | 系列级参数见产品页 | 近距离人脸、三维扫描与体积测量 |
| [Persee 2 / Persee N1](https://www.orbbec.com/products/camera-computer/persee-2/) | 带算力的智能相机 | 系列级参数见产品页 | 相机内嵌计算，输出点云与识别结果 |
| [Pulsar 系列 / MS 系列与 LS635](https://www.orbbec.com.cn/) | 激光雷达与相关芯片 | 中文站单列 LS635 芯片页 | 与深度相机分属不同产品线 |

两点值得单独记。**MX6800 的定位是"省掉外部处理"**：官网把"advanced MX6800 depth engine ASIC, for reduced latency … eliminating the need for external processing"写成卖点，这意味着相机内部已是完整信号链，客户拿到的是成品深度图，不是原始视差。**精度口径必须带条件**：Gemini 335 的 ≤1.5% 绑定 2 m 距离与 90%×90% ROI，换距离或换 ROI 就不是这个数。[Gemini 335 产品页](https://www.orbbec.com/products/stereo-vision-camera/gemini-335/)

官网公开到相机级：深度分辨率与帧率、量程与最佳量程、空间精度及其距离/ROI 条件、FOV、功耗、尺寸重量、防护等级、工作温度、接口与 SDK。做误差预算需要对应型号的 datasheet 与标定报告，英文站产品页给 Datasheet、SDK、Documentation 三个入口。

## 在编码器链上的位置

它卖的是**外部环境的位置**，编码器卖的是**自身关节的位置**，两条链在整机 BOM 里并存但不相交。机器人要做闭环控制，角度必须来自电机侧或输出侧编码器；相机补的是"目标在哪"，误差来自标定、基线、环境光与视差解算，与控制环的码盘误差不是同一类。

**能推的**：自研深度 ASIC 说明它把算力成本与延迟握在自己手里，这类公司对上游的诉求集中在图像传感器、激光器（VCSEL/EEL）与光学件，不在磁敏感元件。**不能推的**：不能从"某机器人用了 Gemini"推出该机器人的关节编码器品牌，官网不公布客户 BOM；也不能反推奥比中光内部图像传感器来自哪家——产品页只写"Orbbec ASIC"，其余元件不列。

## 官方资料

- [奥比中光英文站](https://www.orbbec.com/)
- [奥比中光中文站（产品分类与客户口径）](https://www.orbbec.com.cn/)
- [Gemini 335 产品页（MX6800 与精度口径）](https://www.orbbec.com/products/stereo-vision-camera/gemini-335/)
- [Femto Mega iToF 相机](https://www.orbbec.com/products/tof-camera/femto-mega/)
- [Astra 2 结构光相机](https://www.orbbec.com/products/structured-light-camera/astra-2/)
- [Persee 2 智能相机](https://www.orbbec.com/products/camera-computer/persee-2/)
- [基于微软 iToF 技术的产品族新闻](https://www.orbbec.com/news/orbbec-announces-family-of-products-based-on-microsoft-itof-depth-technology/)
- [Twinny 物流机器人案例](https://www.orbbec.com/case-studies/logistics-costs-reduced-by-64-4-twinny-launches-latest-logistics-robot-product-equipped-with-orbbec-cameras/)
