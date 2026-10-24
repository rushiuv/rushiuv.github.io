---
title: "MX6800"
wiki: true
wiki_type: "model"
catalog_type: "其他既有型号"
catalog_form: "芯片"
wiki_rank: 134
seed_count: 1
lastmod: "2026-10-24"
description: "MX6800是奥比中光公开用于Gemini 330系列的深度计算ASIC名称。"
official_url: "https://www.orbbec.com/products/stereo-vision-camera/gemini-330-series/"
related_companies: ["奥比中光"]
wiki_category: "深度ASIC与相机系统"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 器件类别 | 深度计算 ASIC |
| 公开配套 | Orbbec Gemini 330 系列相机 |
| 系统角色 | 相机端深度计算 |

参数依据：[原厂产品页或对应资料](https://www.orbbec.com/products/stereo-vision-camera/gemini-330-series/)。

## 产品功能与测量链

MX6800是Gemini 330系列深度相机中的深度计算ASIC，负责相机端的深度处理。相机的双目基线、镜头、投射器和图像传感器共同影响成像结果，不能把整机距离规格当作裸芯片规格。

## 接入与配置

评估该芯片时应区分购买现成相机与开发自有相机两条路径。前者关注SDK、供电、USB数据流及标定，后者还涉及光学匹配、固件和生产标定资源。

## 使用与验证

当前公开资料以配套相机能力为主，缺少可直接用于裸芯片设计的完整引脚、电气与接口表。本页不将Gemini不同机型的分辨率、帧率与视场拼成MX6800的单一保证值。

## 版本与待核项目

待补的裸芯片资料包括供电轨、封装引脚、图像输入带宽、外部存储、同步接口和公开软件支持。配套相机成品的SDK可用，不表示裸芯片参考设计或全部内部接口已公开。

多相机方案还应核对相机间同步和运动延迟；更高计算吞吐不会自动恢复由反光、遮挡或低纹理造成的缺失观测。

## 官方资料

- [MX6800 原厂资料入口](https://www.orbbec.com/products/stereo-vision-camera/gemini-330-series/)

公开资料对应 Gemini 330 相机系统，尚无 MX6800 芯片级完整手册。
