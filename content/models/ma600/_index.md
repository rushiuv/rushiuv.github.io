---
title: "MA600"
product_status: "不推荐新设计（NRFND）"
catalog_vendor: "MPS"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki: true
wiki_type: "model"
wiki_rank: 87
seed_count: 2
lastmod: "2026-10-24"
description: "MA600是MPS集成TMR元件的高带宽磁角度传感器，支持在轴及离轴安装。"
official_url: "https://www.monolithicpower.com/en/products/ma600.html"
related_companies: ["MPS"]
datasheet_url: "https://www.monolithicpower.com/en/documentview/productdocument/index/version/2/document_type/Datasheet/lang/en/sku/MA600GQ/"
datasheet_label: "官网文档入口"
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 生命周期 | 官方标注NRFND；继续服务既有设计，新设计建议核对MA600A，而非理解为已经停产 |
| 角度分辨率 | 12～15 位可配置 |
| 输出 | SPI、SSI、ABZ、UVW、PWM |
| 校准 | 32 点校准表 |
| INL | 出厂小于 0.6°；用户校准后可小于 0.1°，两者条件不同 |
| 供电／封装 | 3.3 V，QFN-16 |

参数来源：本页所列[原厂产品资料与手册](https://www.monolithicpower.com/en/documentview/productdocument/index/version/2/document_type/Datasheet/lang/en/sku/MA600GQ/)。

## 工作方式与型号定位

MA600集成TMR敏感元件和角度处理，输出分辨率可配置，并有32点用户校准表。出厂INL与最终系统校准后的INL属于两个阶段，使用时应保留各自条件。

## 安装、接口与配置

磁体装好后测量误差曲线，再利用用户表补偿装配相关残差。该表并不自动提供外部角度真值；换磁体、重新装配或改变温度范围后，应复查原校准是否仍适用。

## 校准与选型验证

原厂对新设计给出MA600A后续选择，但这不等于MA600已停产。两个料号的电气、寄存器和预配置仍需分别核对。多器件或多输出组合也应计算报文时间和引脚复用，不能只看接口名称数量。

## 官方资料

- [MA600 生命周期与后续型号说明](https://www.monolithicpower.com/en/products/sensors/angular-position-sensors/ma600gqe-0000-z.html)
- [MA600A 资料卡](/models/ma600a/)
- [MA600 原厂资料入口](https://www.monolithicpower.com/en/products/ma600.html)
- [官网文档入口（官方入口）](https://www.monolithicpower.com/en/documentview/productdocument/index/version/2/document_type/Datasheet/lang/en/sku/MA600GQ/)
