---
title: "NSM3011／3012／3013"
description: "带片内增益与零位配置的霍尔角度器件组，按成员选择输出功能。"
wiki: true
wiki_type: "model"
wiki_rank: 247
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["纳芯微"]
wiki_category: "数字角度"
catalog_vendor: "纳芯微"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["NSM3011","NSM3012","NSM3013"]
official_url: "https://www.novosns.com/Public/Uploads/uploadfile3/files/20220726/NSM3011_3012_3013_DatasheetV1.0EN.pdf"
document_version: "官方公开PDF，核对：2026-10-18；版本见下文"
model_card: true
datasheet_url: "https://www.novosns.com/Public/Uploads/uploadfile3/files/20220726/NSM3011_3012_3013_DatasheetV1.0EN.pdf"
datasheet_label: "官方公开PDF"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 角度读数 | 手册列14位有效分辨率及SPI通信 |
| 配置 | 自动增益、旋转方向和零位可设置 |
| NSM3013 | SON可用于Z向场强阈值检测；使用SON时需按手册关闭AGC |
| 资料边界 | 依据官方EN1.0历史手册；不据此保证当前交期及新版本配置 |

参数来源：本页所列[原厂产品资料与手册](https://www.novosns.com/Public/Uploads/uploadfile3/files/20220726/NSM3011_3012_3013_DatasheetV1.0EN.pdf)。

## 工作方式与型号定位

NSM301x包含带片内增益和零位配置的霍尔角度成员，SPI用于角度与配置访问。系列页列14位有效分辨率，不应与内部帧长度或其他系列的输出位数混淆。

## 安装、接口与配置

NSM3013的SON用途涉及Z向场强阈值，使用时需按手册关闭AGC。AGC维持幅度与场强阈值测量的目标不同，不能不改配置就同时宣称兼顾。

## 校准与选型验证

按具体成员检查引脚、旋转方向及非易失保存。当前依据EN1.0历史手册，正式设计需核对现行版本；验证应包含磁体轴向移动、角度变化及温度对阈值与角度的共同影响。

## 官方资料

- [NSM3011／3012／3013 官方资料](https://www.novosns.com/Public/Uploads/uploadfile3/files/20220726/NSM3011_3012_3013_DatasheetV1.0EN.pdf)
