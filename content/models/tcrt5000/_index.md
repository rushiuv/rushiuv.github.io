---
title: "TCRT5000"
wiki: true
wiki_type: "model"
wiki_rank: 143
seed_count: 1
lastmod: "2026-10-24"
description: "TCRT5000是Vishay反射式光学传感器，集成红外发射器和光电晶体管，适用于反射变化和标记检测。"
official_url: "https://www.vishay.com/zh/product/83760/"
datasheet_url: "https://www.vishay.com/docs/83760/tcrt5000.pdf"
datasheet_label: "官方数据手册"
wiki_category: "反射检测与条纹读取"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/tcrt5000-datasheet-figure.jpg"
product_image_caption: "tcrt5000 原厂手册插图（PDF 第 1 页）"
product_image_source: "https://www.vishay.com/docs/83760/tcrt5000.pdf"
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 结构 | 红外发射器与光电晶体管 |
| 检测方式 | 反射式光学检测 |
| 输出 | 光电晶体管信号 |
| 版本 | TCRT5000 与 TCRT5000L 的机械引脚形式不同 |
| 峰值工作距离 | 2.5mm，依手册反射测试条件 |
| 相对接收电流范围 | 0.2～15mm对应相对输出>20%；不是绝对测距精度范围 |
| 发射波长 | 特性页列950nm |
| 器件外形 | 10.2×5.8×7mm，长×宽×高 |
| 引脚版本 | TCRT5000：3.5mm引脚；TCRT5000L：15mm引脚 |
| 温度范围 | −25～85°C，所附Rev.1.7手册环境温度额定值 |

参数依据：[原厂产品页或对应资料](https://www.vishay.com/docs/83760/tcrt5000.pdf)。

## 产品功能与测量链

TCRT5000将红外发射器与光电晶体管装在带可见光抑制滤光的封装中，用反射光变化检测条纹或物体。裸器件没有数字比较器，常见模块的DO输出来自板上电路。

## 接入与配置

手册的峰值工作距离2.5mm以及0.2～15mm范围，均与反射测试条件有关。后者是相对接收电流大于20%的区间，不是15mm内都能精确测距的保证。

## 使用与验证

LED限流、接收负载和比较阈值应按目标材料选择。用于编码盘时要验证光斑覆盖、转速与黑白边沿，避免晶体管深饱和造成恢复变慢；L版主要区别是加长引脚，不代表更远探测距离。

黑白图案需在器件红外波段具有足够反差；人眼判断的墨色不能替代实际发射、反射和接收链路测试。

## 官方资料

- [TCRT5000 原厂资料入口](https://www.vishay.com/zh/product/83760/)
- [TCRT5000 数据手册（官方 PDF）](https://www.vishay.com/docs/83760/tcrt5000.pdf)
