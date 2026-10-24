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

## 核心性能

### 产品介绍

RXMA30是雷尼绍的1.5D绝对式多自由度光栅栅尺，具有相互正交的刻线方向，配合RESOLUTE读数头构成位置测量系统。 [官方资料](https://www.renishaw.com/en/renishaw-introduces-true-absolute-multi-dof-encoder-system-featuring-new-rxma30-15d-scale--50008)

### 核心参数

- **产品类别** 1.5D 绝对式多自由度光栅栅尺
- **刻线** 相互正交方向
- **配套读头** RESOLUTE
- **系统能力** 特定多栅尺／读头布局最多观测六自由度

### 接口与输出

RXMA30 当前公开资料没有给出可独立核对的数字通信或脉冲接口细节。若器件提供模拟量、开关量或模块级连接，应按官方引脚／线缆定义接入；在取得型号级手册前，本页不补造协议、速率或电平。

### 工作原理

以下解释本类器件在系统中的一般工作方式，具体集成功能以本型号官方资料为准。

光栅将空间位置编码在标尺上，读头根据光学图案恢复位置。多个不同方向或不同位置的读头提供额外几何观测，可以结合已知基线区分平移和转动。

多自由度不是一个孤立位数参数。它依赖读头数量、放置方向、安装基准和计算关系；当测量点或基线变化时，可观测误差也会变化。

### 典型应用与使用条件

高分辨率有助于读取微小变化，绝对精度仍与标尺精度、热膨胀和安装误差有关。系统补偿还需要把读头坐标与机器运动坐标对应起来。

要把产品放进实际设备，还要确认数据对应的物理位置和时刻。传感器读数、接口传输和控制器使用并非同一个环节；读数更新并不一定意味着刚完成一次新测量。协议校验可以发现部分传输错误，无法发现全部机械安装变化。

比较两个备选型号时，应在相同输入、温度、带宽和校准状态下看结果。分辨率、噪声、重复性与绝对误差各有定义；目录页的典型值也不应改写成每颗样品、所有条件下的保证值。某一功能能配置，不表示所有输出可以同时工作。

## 官方资料

- [RXMA30 原厂资料入口](https://www.renishaw.com/en/renishaw-introduces-true-absolute-multi-dof-encoder-system-featuring-new-rxma30-15d-scale--50008)
- [RXMA30 数据手册（官方 PDF）](https://www.renishaw.com/resourcecentre/download/rxma30-15d--146447?userLanguage=zh)
