---
title: "TLE5012B"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 33
seed_count: 6
lastmod: "2026-10-18"
description: "TLE5012B 离轴安装误差排查：先核对磁场条件、完整型号、SSC 接入与自校准配置，再区分静态误差和动态延迟。附原厂资料及复现条件单。"
official_url: "https://www.infineon.com/part/TLE5012B-E5000"
related_companies: ["英飞凌"]
datasheet_url: "https://www.infineon.com/assets/row/public/documents/30/49/infineon-tle5012b-exxxx-datasheet-en.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-18；数据手册 Rev.2.1（2018-06-20）"
model_card: true
product_image: "/images/wiki/tle5012b-official.jpg"
product_image_caption: "TLE5012B 原厂产品／封装图"
product_image_source: "https://www.infineon.com/part/TLE5012B-E5000"
---

## 核心性能

- **感应技术** GMR 磁角度检测
- **数字数据** 角度与状态读取
- **通信** SSC 等功能由 E5000 等具体后缀配置
- **订货范围** 增量及其他输出组合按对应引脚表

## 离轴安装后误差大，先确认什么？

TLE5012B 利用 GMR 元件测量磁场方向。能读到角度，不等于保证任意离轴磁路的机械角精度。数据手册的精度条件采用均匀平面磁场，并限定垂直分量为零，不能直接套到任意侧向安装。[原厂数据手册，第16–17页](https://www.infineon.com/assets/row/public/documents/30/49/infineon-tle5012b-exxxx-datasheet-en.pdf#page=16)

### 先留下条件，再判断误差

- **完整后缀与配置**：记录 E5000 等完整型号并读回配置，不能只写“TLE5012”。各后缀的接口和默认功能不同。[第45–46页](https://www.infineon.com/assets/row/public/documents/30/49/infineon-tle5012b-exxxx-datasheet-en.pdf#page=45)
- **接入是否正确**：SSC 是 SPI-compatible 的双向三线接口；核对 DATA 换向、帧结构、安全字与时序，不直接套任意四线 SPI 驱动。[第26–29页](https://www.infineon.com/assets/row/public/documents/30/49/infineon-tle5012b-exxxx-datasheet-en.pdf#page=26)
- **自校准修了什么**：AUTOCAL 不等于整圈离轴非线性校准。用户手册描述其用 X/Y 极值更新偏置与幅值同步参数，并对整圈运动和温度变化设条件；剩余周期误差仍需参考角验证。[用户手册入口，正文第22–23页，需 myInfineon 登录](https://www.infineon.com/de/gated/infineon-tle5012b-usermanual-en_13801894-eee3-4707-8a78-269c36379c18)
- **静态还是动态**：静止角度误差与转动后出现的误差分开记录；滤波、接口与预测配置影响动态表现，刷新周期不能直接当固定测量延迟。[第23–24页](https://www.infineon.com/assets/row/public/documents/30/49/infineon-tle5012b-exxxx-datasheet-en.pdf#page=23)

本站的起步建议是保存一张条件单：完整型号、磁体与充磁方向、相对转轴位置、气隙、供电、温度、转速、接口和配置；保留参考角与输出角的整圈原始记录。它是复现建议，不是原厂指定验收流程，也不能单凭一个 INL 数字确定根因。

### 沿问题继续查

- [先把在轴、离轴、气隙、偏心与倾斜说清楚](/wiki/basics/mounting/)
- [校准曲线为什么还需要独立条件验证](/tags/%E9%9D%9E%E7%BA%BF%E6%80%A7%E6%A0%A1%E5%87%86/)

## 官方资料

- [TLE5012B 原厂资料入口](https://www.infineon.com/part/TLE5012B-E5000)
- [TLE5012B 数据手册（官方 PDF）](https://www.infineon.com/assets/row/public/documents/30/49/infineon-tle5012b-exxxx-datasheet-en.pdf)
