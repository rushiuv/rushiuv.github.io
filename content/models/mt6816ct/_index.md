---
title: MT6816CT
wiki: true
wiki_type: model
model_card: true
wiki_rank: 405
lastmod: '2026-10-30'
catalog_type: 数字角度
catalog_form: 芯片
wiki_category: 数字角度
description: MT6816CT 是SOP8封装的AMR旋转角度编码器，可按预设采用SPI、ABZ、UVW或PWM路径；目录与详情的位宽口径需分别保留。
official_url: https://www.novosns.com/product/MT6816CT-A100-R
related_companies:
- 纳芯微
- 麦歌恩
search_aliases:
- MT6816
- MT6816CT
- MT6816CT-A100-R
- MT6816CT-A200-R
- MT6816CT-A30-R
- MT6816CT-A360-R
- MT6816CT-A400-R
- MT6816CT-A500-R
- MT6816CT-A600-R
- MT6816CT-A6D-R
- MT6816CT-A780-R
- MT6816CT-A9D-R
- MT6816CT-AAH-R
- MT6816CT-AAL-R
- MT6816CT-ABD-R
- MT6816CT-ACD-R
- MT6816CT-ACE-R
- MT6816CT-ACG-R
- MT6816CT-ACH-R
- MT6816CT-ACL-R
- MT6816CT-ACP-R
- MT6816CT-ACS-R
- MT6816CT-ACT-R
- MT6816CT-ACV-R
- MT6816CT-ADS-R
- MT6816CT-AED-R
- MT6816CT-AKD-R
- MT6816CT-AKH-R
- MT6816CT-AKK-R
- MT6816CT-H600-R
- MT6816CT-STD-R
- MT6816CT-STH-R
- MT6816CT-STT-R
- MT6816CT-U5D-R
- MT6816CT-U7D-R
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/b48c45076127e433.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/XXBSbBZIOoqVo2x1VAhcWmfcnrg.png
series_parent: mt6816
---

## 核心参数与配置

以下为官网目录中 **MT6816CT-A100-R** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | AMR磁角度编码器 |
| 目录类别 | 工业编码器 |
| 封装 | SOP8 |
| 目录等级 | Automotive |
| 数字接口 | 3-wire SPI/4-wire SPI；官网目录标注，适用于上述订货配置 |
| 核心分辨率 | 12bit；官网目录标注，适用于上述订货配置 |
| PWM输出 | 12bit；官网目录标注，适用于上述订货配置 |
| UVW增量输出 | 1~16pole pairs programmable；官网目录标注，适用于上述订货配置 |
| ABZ增量输出 | 1~1024lines programmable；官网目录标注，适用于上述订货配置 |
| 目录最高转速 | <25,000RPM；官网目录标注，适用于上述订货配置 |
| 匀速传播延迟 | <2μs；官网目录标注，适用于上述订货配置 |
| 温度范围 | -40~125；官网目录标注，适用于上述订货配置 |
| 目录供电 | 3.3~5.0；官网目录标注，适用于上述订货配置 |

## 先解决位宽口径再比较精度

官网详情标题使用14位，而代表OPN的Core Resolution目录字段为12bit，PWM另有自己的位宽。它们可能对应不同输出或配置，在核对手册前应并列标明来源，不能任选较高数字作为所有接口的分辨率。

## ABZ与UVW承担不同任务

ABZ用于位置计数，UVW对应电机换向极对关系。接控制器时分别核对线数、极对数和相序，并在机械零点与电角零点之间建立对应，不能只做一次SPI角度回读就认为换向接入完成。

## 相同CT前缀下也有生命周期区别

官网的部分完整OPN已不推荐新设计，其他仍标Active。新项目应先选定具体预设，再评估是否需要重新编程和验证，不把一个预设的状态当成MT6816CT整体状态。

## 订货版本之间的差别

### 生命周期状态

| 目录标注 | 适用完整订货号 |
| --- | --- |
| Not Recomended for New Designs | MT6816CT-A100-R、MT6816CT-A400-R、MT6816CT-A600-R、MT6816CT-A9D-R、MT6816CT-ACT-R、MT6816CT-AKH-R、MT6816CT-STH-R |
| Active | MT6816CT-A200-R、MT6816CT-A30-R、MT6816CT-A360-R、MT6816CT-A500-R、MT6816CT-A6D-R、MT6816CT-A780-R、MT6816CT-AAH-R、MT6816CT-AAL-R、MT6816CT-ABD-R、MT6816CT-ACD-R、MT6816CT-ACE-R、MT6816CT-ACG-R、MT6816CT-ACH-R、MT6816CT-ACL-R、MT6816CT-ACP-R、MT6816CT-ACS-R、MT6816CT-ACV-R、MT6816CT-ADS-R、MT6816CT-AED-R、MT6816CT-AKD-R、MT6816CT-AKK-R、MT6816CT-H600-R、MT6816CT-STD-R、MT6816CT-STT-R、MT6816CT-U5D-R、MT6816CT-U7D-R |

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [MT6816CT-A100-R](https://www.novosns.com/product/MT6816CT-A100-R) | SOP8；Automotive；Not Recomended for New Designs；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-A200-R](https://www.novosns.com/product/MT6816CT-A200-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-A30-R](https://www.novosns.com/product/MT6816CT-A30-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-A360-R](https://www.novosns.com/product/MT6816CT-A360-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-A400-R](https://www.novosns.com/product/MT6816CT-A400-R) | SOP8；Automotive；Not Recomended for New Designs；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-A500-R](https://www.novosns.com/product/MT6816CT-A500-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-A600-R](https://www.novosns.com/product/MT6816CT-A600-R) | SOP8；Automotive；Not Recomended for New Designs；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-A6D-R](https://www.novosns.com/product/MT6816CT-A6D-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-A780-R](https://www.novosns.com/product/MT6816CT-A780-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-A9D-R](https://www.novosns.com/product/MT6816CT-A9D-R) | SOP8；Automotive；Not Recomended for New Designs；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-AAH-R](https://www.novosns.com/product/MT6816CT-AAH-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-AAL-R](https://www.novosns.com/product/MT6816CT-AAL-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-ABD-R](https://www.novosns.com/product/MT6816CT-ABD-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-ACD-R](https://www.novosns.com/product/MT6816CT-ACD-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-ACE-R](https://www.novosns.com/product/MT6816CT-ACE-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-ACG-R](https://www.novosns.com/product/MT6816CT-ACG-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-ACH-R](https://www.novosns.com/product/MT6816CT-ACH-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-ACL-R](https://www.novosns.com/product/MT6816CT-ACL-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-ACP-R](https://www.novosns.com/product/MT6816CT-ACP-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-ACS-R](https://www.novosns.com/product/MT6816CT-ACS-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-ACT-R](https://www.novosns.com/product/MT6816CT-ACT-R) | SOP8；Automotive；Not Recomended for New Designs；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-ACV-R](https://www.novosns.com/product/MT6816CT-ACV-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-ADS-R](https://www.novosns.com/product/MT6816CT-ADS-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-AED-R](https://www.novosns.com/product/MT6816CT-AED-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-AKD-R](https://www.novosns.com/product/MT6816CT-AKD-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-AKH-R](https://www.novosns.com/product/MT6816CT-AKH-R) | SOP8；Automotive；Not Recomended for New Designs；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-AKK-R](https://www.novosns.com/product/MT6816CT-AKK-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-H600-R](https://www.novosns.com/product/MT6816CT-H600-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-STD-R](https://www.novosns.com/product/MT6816CT-STD-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-STH-R](https://www.novosns.com/product/MT6816CT-STH-R) | SOP8；Automotive；Not Recomended for New Designs；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-STT-R](https://www.novosns.com/product/MT6816CT-STT-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-U5D-R](https://www.novosns.com/product/MT6816CT-U5D-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |
| [MT6816CT-U7D-R](https://www.novosns.com/product/MT6816CT-U7D-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf) |

“Not Recommended for New Designs”表示该完整订货号不推荐用于新设计，不代表全部预设停产。请结合表内仍为Active的版本核对供应与配置。

## 版本与适用条件

完整订货号区分预设配置与供货形式；CT、QT、GT、SGT、SJT等型号字母还对应不同成员或封装。

同型号不同预设的生命周期可能不同，供货与新设计适用性按具体OPN查询。

## 原厂资料

- [产品详情](https://www.novosns.com/product/MT6816CT-A100-R)
- [DatasheetCN)MT6816_Rev.2.1.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/ZAe9bnX7ToO8zcxT5P5cXsednXe.pdf)
- [MT6816_Rev.2.1.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/FyBlbe4GQoeeAbx6X2Rc2pMQnGe.pdf)
- [工业编码器目录](https://www.novosns.com/industrial-encoder)
