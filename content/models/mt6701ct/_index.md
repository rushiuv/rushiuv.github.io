---
title: MT6701CT
wiki: true
wiki_type: model
model_card: true
wiki_rank: 401
lastmod: '2026-10-30'
catalog_type: 数字角度
catalog_form: 芯片
wiki_category: 数字角度
description: MT6701CT 是MT6701差分Hall角度系列的SOP8型号，适合在较少引脚下读取旋转角度或接入增量控制器；完整预设配置与生命周期见订货表。
official_url: https://www.novosns.com/product/MT6701CT-A200-R
related_companies:
- 纳芯微
- 麦歌恩
search_aliases:
- MT6701
- MT6701CT
- MT6701CT-A200-R
- MT6701CT-A32-R
- MT6701CT-A360-R
- MT6701CT-A360T-R
- MT6701CT-A400-R
- MT6701CT-A400T-R
- MT6701CT-A457-R
- MT6701CT-A48-R
- MT6701CT-A50-R
- MT6701CT-A520-R
- MT6701CT-A600-R
- MT6701CT-A64-R
- MT6701CT-A682-R
- MT6701CT-A697-R
- MT6701CT-A700-R
- MT6701CT-A720-R
- MT6701CT-A722-R
- MT6701CT-A800-R
- MT6701CT-AAD-R
- MT6701CT-ABD-R
- MT6701CT-ACD-R
- MT6701CT-ACV-R
- MT6701CT-AKD-R
- MT6701CT-AKE-R
- MT6701CT-LAA-R
- MT6701CT-LAV-R
- MT6701CT-P500-R
- MT6701CT-SHC-R
- MT6701CT-ST8-R
- MT6701CT-STD-R
- MT6701CT-STF-R
- MT6701CT-STG-R
- MT6701CT-STV-R
- MT6701CT-U3D-R
- MT6701CT-U4D-R
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/b48c45076127e433.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/XXBSbBZIOoqVo2x1VAhcWmfcnrg.png
series_parent: mt6701
---

## 核心参数与配置

以下为官网目录中 **MT6701CT-A200-R** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | 霍尔角度/位置编码器 |
| 目录类别 | 工业编码器 |
| 封装 | SOP8 |
| 目录等级 | Industrial |
| 数字接口 | I²C;SSI；官网目录标注，适用于上述订货配置 |
| 核心分辨率 | 14bit；官网目录标注，适用于上述订货配置 |
| PWM输出 | 12bit；官网目录标注，适用于上述订货配置 |
| UVW增量输出 | 1~16pole pairs programmable；官网目录标注，适用于上述订货配置 |
| ABZ增量输出 | 1~1024lines programmable；官网目录标注，适用于上述订货配置 |
| 目录最高转速 | <55,000RPM；官网目录标注，适用于上述订货配置 |
| 匀速传播延迟 | <5μs；官网目录标注，适用于上述订货配置 |
| 温度范围 | -40~125；官网目录标注，适用于上述订货配置 |
| 目录供电 | 3.3~5.0；官网目录标注，适用于上述订货配置 |

## 八脚封装先做接口选择

目录同时列I²C、SSI以及增量/PWM能力，八脚资源意味着必须按引脚复用和订货配置选择实际路径。原理图应先明确绝对读取、ABZ计数还是PWM采样，不能把系列全部功能默认同时引出。

## SSI与I²C不能共用一套读取假设

SSI按时钟移出角度，I²C则使用寻址与寄存器读写，主控驱动、总线占用和有效数据判断不同。接入前检查所选预设及协议时序，再用正反转验证方向与零点。

## CT封装与预设配置

MT6701CT采用SOP8，预设配置由完整OPN确定。官网对部分预设标不推荐新设计、其他预设仍Active，不能把一个旧预设的状态扩展为整个系列停产。

## 订货版本之间的差别

### 生命周期状态

| 目录标注 | 适用完整订货号 |
| --- | --- |
| Not Recomended for New Designs | MT6701CT-A200-R、MT6701CT-A400T-R、MT6701CT-A48-R、MT6701CT-A64-R、MT6701CT-A697-R、MT6701CT-SHC-R、MT6701CT-STG-R |
| Active | MT6701CT-A32-R、MT6701CT-A360-R、MT6701CT-A360T-R、MT6701CT-A400-R、MT6701CT-A457-R、MT6701CT-A50-R、MT6701CT-A520-R、MT6701CT-A600-R、MT6701CT-A682-R、MT6701CT-A700-R、MT6701CT-A720-R、MT6701CT-A722-R、MT6701CT-A800-R、MT6701CT-AAD-R、MT6701CT-ABD-R、MT6701CT-ACD-R、MT6701CT-ACV-R、MT6701CT-AKD-R、MT6701CT-AKE-R、MT6701CT-LAA-R、MT6701CT-LAV-R、MT6701CT-P500-R、MT6701CT-ST8-R、MT6701CT-STD-R、MT6701CT-STF-R、MT6701CT-STV-R、MT6701CT-U3D-R、MT6701CT-U4D-R |

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [MT6701CT-A200-R](https://www.novosns.com/product/MT6701CT-A200-R) | SOP8；Industrial；Not Recomended for New Designs；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-A32-R](https://www.novosns.com/product/MT6701CT-A32-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-A360-R](https://www.novosns.com/product/MT6701CT-A360-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-A360T-R](https://www.novosns.com/product/MT6701CT-A360T-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-A400-R](https://www.novosns.com/product/MT6701CT-A400-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-A400T-R](https://www.novosns.com/product/MT6701CT-A400T-R) | SOP8；Industrial；Not Recomended for New Designs；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-A457-R](https://www.novosns.com/product/MT6701CT-A457-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-A48-R](https://www.novosns.com/product/MT6701CT-A48-R) | SOP8；Industrial；Not Recomended for New Designs；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-A50-R](https://www.novosns.com/product/MT6701CT-A50-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-A520-R](https://www.novosns.com/product/MT6701CT-A520-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-A600-R](https://www.novosns.com/product/MT6701CT-A600-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-A64-R](https://www.novosns.com/product/MT6701CT-A64-R) | SOP8；Industrial；Not Recomended for New Designs；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-A682-R](https://www.novosns.com/product/MT6701CT-A682-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-A697-R](https://www.novosns.com/product/MT6701CT-A697-R) | SOP8；Industrial；Not Recomended for New Designs；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-A700-R](https://www.novosns.com/product/MT6701CT-A700-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-A720-R](https://www.novosns.com/product/MT6701CT-A720-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-A722-R](https://www.novosns.com/product/MT6701CT-A722-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-A800-R](https://www.novosns.com/product/MT6701CT-A800-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-AAD-R](https://www.novosns.com/product/MT6701CT-AAD-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-ABD-R](https://www.novosns.com/product/MT6701CT-ABD-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-ACD-R](https://www.novosns.com/product/MT6701CT-ACD-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-ACV-R](https://www.novosns.com/product/MT6701CT-ACV-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-AKD-R](https://www.novosns.com/product/MT6701CT-AKD-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-AKE-R](https://www.novosns.com/product/MT6701CT-AKE-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-LAA-R](https://www.novosns.com/product/MT6701CT-LAA-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-LAV-R](https://www.novosns.com/product/MT6701CT-LAV-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-P500-R](https://www.novosns.com/product/MT6701CT-P500-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-SHC-R](https://www.novosns.com/product/MT6701CT-SHC-R) | SOP8；Industrial；Not Recomended for New Designs；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-ST8-R](https://www.novosns.com/product/MT6701CT-ST8-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-STD-R](https://www.novosns.com/product/MT6701CT-STD-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-STF-R](https://www.novosns.com/product/MT6701CT-STF-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-STG-R](https://www.novosns.com/product/MT6701CT-STG-R) | SOP8；Industrial；Not Recomended for New Designs；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-STV-R](https://www.novosns.com/product/MT6701CT-STV-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-U3D-R](https://www.novosns.com/product/MT6701CT-U3D-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701CT-U4D-R](https://www.novosns.com/product/MT6701CT-U4D-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |

“Not Recommended for New Designs”表示该完整订货号不推荐用于新设计，不代表全部预设停产。请结合表内仍为Active的版本核对供应与配置。

## 版本与适用条件

完整订货号区分预设配置与供货形式；CT、QT、GT、SGT、SJT等型号字母还对应不同成员或封装。

同型号不同预设的生命周期可能不同，供货与新设计适用性按具体OPN查询。

## 原厂资料

- [产品详情](https://www.novosns.com/product/MT6701CT-A200-R)
- [MT6701_Datasheet_Rev.1.9.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf)
- [MT6701_Datasheet_Rev.1.9_中文版.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf)
- [工业编码器目录](https://www.novosns.com/industrial-encoder)
