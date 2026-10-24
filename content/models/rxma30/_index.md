---
title: "RXMA30"
wiki: true
wiki_type: "model"
catalog_type: "线性编码"
catalog_form: "编码模块"
wiki_rank: 140
seed_count: 1
lastmod: "2026-10-24"
description: "RXMA30是雷尼绍的1.5D绝对式多自由度光栅栅尺，具有相互正交的刻线方向，配合RESOLUTE读数头构成位置测量系统。"
official_url: "https://www.renishaw.com/en/renishaw-introduces-true-absolute-multi-dof-encoder-system-featuring-new-rxma30-15d-scale--50008"
related_companies: ["雷尼绍"]
datasheet_url: "https://www.renishaw.com/resourcecentre/download/rxma30-15d--146447?userLanguage=zh"
datasheet_label: "官方数据手册"
wiki_category: "光栅与多自由度观测"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/rxma30-datasheet-figure.jpg"
product_image_caption: "rxma30 原厂手册插图（PDF 第 1 页）"
product_image_source: "https://www.renishaw.com/resourcecentre/download/rxma30-15d--146447?userLanguage=zh"
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 产品类别 | 1.5D 绝对式多自由度光栅栅尺 |
| 刻线 | 相互正交方向 |
| 配套读头 | RESOLUTE |
| 系统能力 | 特定多栅尺／读头布局最多观测六自由度 |

参数依据：[原厂产品页或对应资料](https://www.renishaw.com/en/renishaw-introduces-true-absolute-multi-dof-encoder-system-featuring-new-rxma30-15d-scale--50008)。

## 产品功能与测量链

RXMA30的1.5D栅尺具有相互正交的刻线方向，配合RESOLUTE读头获取多自由度位置信息。它不是单只读头直接测出任意空间六轴位姿。

## 接入与配置

系统最多观测六自由度的能力来自特定多读头、多栅尺几何和解算布局。评估时需明确各自由度的测量轴、基线长度、有效行程和坐标定义。

## 使用与验证

机械基准、读头姿态、热膨胀及阿贝臂长会进入系统误差。安装后应分别做轴向位移、横向扰动和姿态变化测试，不能只验证主运动方向就声明所有自由度均达到同一精度。

## 版本与待核项目

原厂公告说明多自由度测量结构，不给本页假定统一的六自由度精度。完整系统还需对应RESOLUTE读头、接口选件及安装设计资料；线性分辨率与姿态角误差应分别给单位。

## 官方资料

- [RXMA30 原厂资料入口](https://www.renishaw.com/en/renishaw-introduces-true-absolute-multi-dof-encoder-system-featuring-new-rxma30-15d-scale--50008)
- [RXMA30 数据手册（官方 PDF）](https://www.renishaw.com/resourcecentre/download/rxma30-15d--146447?userLanguage=zh)
