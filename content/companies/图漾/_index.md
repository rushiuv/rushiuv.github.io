---
title: "图漾"
wiki: true
wiki_type: "company"
wiki_rank: 155
seed_count: 1
lastmod: "2026-10-22"
description: "图漾科技（Percipio）：江苏的工业 3D 相机厂，T 系列 dToF 出图延迟 55ms、G 系列双目散斑 70ms、V 系列条纹结构光约 1.7~2.4s 且仅 1.14FPS，产品无转轴，靠 RVS 平台读取机械臂位姿。"
official_url: "https://www.percipio.xyz/"
wiki_category: "光学感知与空间测量"
related_models: []
---

图漾科技做的是**工业 3D 相机加手眼协同软件**，处在"外部测量"这一层。它自己的产品没有任何转轴，不采购关节编码器；但 RVS 平台要把点云换算到机器人坐标，就必须读机械臂末端位姿，而那个位姿来自本体编码器——它是编码器数据的**下游使用者**，不是采购方。读它的资料最该看出图延迟与帧率，这两个数直接决定这套视觉能不能进闭环。

## 公司与品牌

中文名图漾科技，英文 Percipio，备案为苏 ICP，官网列北京、南京、上海、深圳与韩国、日本服务点，称业务覆盖 40 多个国家及地区、100 多个应用场景、累计出货 10 万台以上、服务客户 1000 家以上（截至 2026 年 5 月的已签约及交付与内部产销统计），已授权及申请专利 100 项以上。[关于图漾](https://www.percipio.xyz//about/about-percipio)

官网没有公开成立年份、注册资本、股权结构与创始团队，本页留空、不做推测。线体自述覆盖双目散斑、条纹结构光、ToF 多路线，按近距／中距／远距分段选型，配套 RVS（Robot Vision Suite）低代码平台，含 2D/3D 算法库、深度学习模块、手眼标定与机器人运动模拟。[官网首页](https://www.percipio.xyz/)

## 产品线：按出图延迟分成"能进节拍"和"只能静态测"两档

下表取自各族参数表，同族内型号差异大，属"视型号"口径。

| 系列 | 类型 | 公开深度规格 | 出图延迟与其他 |
| --- | --- | --- | --- |
| [T 系列 TM262-E1](https://www.percipio.xyz//product/hardware/tof-camera/t-series) | dToF，入门级工业相机 | 25 fps@240×96，Z 精度 6 mm@1000 mm、15 mm@2500 mm，FOV 120°×50°，量程 300–3000 mm | 延迟 55 ms，M12 A-Code 8 孔，24 V±20%，IP65，0–45 ℃ |
| [G 系列 GM461-E1](https://www.percipio.xyz//product/hardware/dot-pattern-structured-light-camera/g-series) | 双目散斑结构光 940 nm | 30 fps@640×400，Z 精度 0.9 mm@1000 mm、2.5 mm@1500 mm，FOV 72°×49° | 延迟 70 ms，基线 66 mm，Global shutter，支持 ROS |
| [G 系列 GM465-E1](https://www.percipio.xyz//product/hardware/dot-pattern-structured-light-camera/g-series) | 双目散斑，双激光器 | 30 fps@640×480，Z 精度 0.8 mm@1000 mm、2.3 mm@1500 mm | 延迟 137 ms，基线 66 mm，量程 150–3000 mm |
| [V 系列 VMD02-4070](https://www.percipio.xyz//product/hardware/fringe-pattern-structured-light-camera/v-series) | 双目 + 条纹结构光 635 nm | 最高 1.14 FPS@2048×1536（可降至 1024×768、512×384） | 延迟约 1.7–2.4 s，分 Fast/Standard/Quality 三档 |

这张表最要紧的是**延迟跨了三个数量级**：T 型 55 ms、G 型 70~137 ms、V 型 1.7~2.4 s。T 与 G 的节拍 25~30 fps，能挂移动底盘做避障跟随；V 型 1.14 FPS、延迟近 2 秒，只能用于静态工位测量与抓取前拍照。官网对延迟的口径写得很具体：软件触发模式下从主机发触发信号到收到深度图的时间，且是用户设置保持默认标准、仅改变分辨率时测得——所以它不能当实时预算里的固定值。[T 系列参数表](https://www.percipio.xyz//product/hardware/tof-camera/t-series)

官网公开到相机级的 Z 精度（带具体距离点）、XY 精度、FOV、基线、帧率、出图延迟、尺寸重量、防护等级与工作温度；工业型号还给了 SDK（Vcamera SDK 支持 C++/C#/Python，Camport4 支持 C++）和 1 路下降沿触发。做误差预算要下对应型号的相机规格书与手眼标定报告，官网在服务与支持栏只给相机规格书、用户手册、线束规格书三个入口。

## 在编码器链上的位置

位置信息有两条来源：本体关节角（编码器）与外部测量（相机）。图漾只做后者，给的是目标物相对相机的位姿，不是关节角。RVS 做手眼标定与运动模拟要机器人位姿输入，数据来自机械臂控制器、也就是最终的编码器读数，但图漾既不采购那颗编码器，也不决定它的精度。

**能推的**：客户群是工业自动化、物流、移动机器人，这类项目对角度反馈的要求落在机械臂本体自带那套上，视觉供应商不参与。**不能推的**：不能从"某客户用了图漾相机"推出该客户关节用哪家编码器，也不能推出图漾内部用哪家图像传感器与激光器——官网只给相机级参数，不公布 BOM。

两者的口径差在于延迟：相机给的是绝对位置但延迟在毫秒到秒级、精度随距离衰减；编码器是微秒级延迟、精度与距离无关。它们不是替代关系，是**环路带宽不同的两层**，混进一张精度表比较没有意义。

## 官方资料

- [图漾科技官网](https://www.percipio.xyz/)
- [关于图漾（服务网络、专利与出货口径）](https://www.percipio.xyz//about/about-percipio)
- [T 系列 ToF 3D 相机参数表](https://www.percipio.xyz//product/hardware/tof-camera/t-series)
- [G 系列双目散斑结构光相机参数表](https://www.percipio.xyz//product/hardware/dot-pattern-structured-light-camera/g-series)
- [V 系列双目条纹结构光相机参数表](https://www.percipio.xyz//product/hardware/fringe-pattern-structured-light-camera/v-series)
- [相机规格书下载入口](https://www.percipio.xyz//services-support/technical-document/related-to-cameras/camera-specifications)
