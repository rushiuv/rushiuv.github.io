---
title: "MT6521"
description: "汽车角度传感器，支持选择XYZ中的感应平面，并可用于相应直线位移磁路。"
wiki: true
wiki_type: "model"
wiki_rank: 242
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["麦歌恩","纳芯微"]
wiki_category: "数字角度"
catalog_vendor: "麦歌恩"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["MT6521"]
official_url: "https://www.magntek.com.cn/upload/pdf/202406/MT652x_Datasheet_Rev.1.0_%E4%B8%AD%E6%96%87%E7%89%88.pdf"
document_version: "官方公开PDF，核对：2026-10-18；版本见下文"
model_card: true
datasheet_url: "https://www.magntek.com.cn/upload/pdf/202406/MT652x_Datasheet_Rev.1.0_%E4%B8%AD%E6%96%87%E7%89%88.pdf"
datasheet_label: "官方公开PDF"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 感应配置 | 可选择XY、XZ、YZ平面 |
| 输出 | Analog、PWM、SENT及SPI，具体模式和引脚复用见手册 |
| 编程 | 官网说明输出曲线可8点或17点编程 |
| 通道边界 | 单路与双路封装能力须分别核对，两个输出不自动等于系统冗余 |

参数来源：本页所列[原厂产品资料与手册](https://www.magntek.com.cn/upload/pdf/202406/MT652x_Datasheet_Rev.1.0_%E4%B8%AD%E6%96%87%E7%89%88.pdf)。

## 工作方式与型号定位

MT6521通过选择XY、XZ或YZ磁场平面适配旋转或相应直线磁路，输出曲线可编程。传感芯片测得的是场方向，机械行程到输出还取决于磁体安装与配置。

## 安装、接口与配置

Analog、PWM、SENT和SPI是不同输出模式，应按具体封装和引脚复用选择。8点或17点输出编程用于修正传输曲线，写入前需确定机械基准及目标电气范围。

## 校准与选型验证

双通道封装的感应中心和机械方向要分别核对，不能默认两路角度天然相同。检验应记录输出模式、编程点、温度和气隙，并检查限幅、诊断区及掉电后参数保持。

## 官方资料

- [MT6521 官方资料](https://www.magntek.com.cn/upload/pdf/202406/MT652x_Datasheet_Rev.1.0_%E4%B8%AD%E6%96%87%E7%89%88.pdf)
