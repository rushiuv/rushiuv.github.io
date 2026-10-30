---
title: VCE2755
description: VCE2755 将AMR敏感结构和ASIC集成，提供360°绝对角度及多种输出；18位输出码宽、14位有效角度口径和ABZ的1024ppr上限需要分开读取。
wiki: true
wiki_type: model
wiki_rank: 238
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 圣邦微
wiki_category: 数字角度
catalog_vendor: 圣邦微
catalog_type: 数字角度
catalog_form: 芯片
search_aliases:
- VCE2755
- VCE2755Q079
- VCE2755Q102
- VCE2755Q104
- VCE2755Q113
- VCE2755Q134
- VCE2755Q161
- VCE2755S076
- VCE2755S087
- VCE2755S096
- VCE2755S108
- VCE2755S121
- VCE2755S124
- VCE2755S142
- VCE2755S152
- VCE2755S153
- VCE2755S159
- VCE2755S164
official_url: https://www.sg-micro.com/cn/product/VCE2755
document_version: 2026-01 Rev.A.3，30页
model_card: true
datasheet_url: https://www.sg-micro.com/rect/assets/db119b16-8eeb-40df-8fd5-74e92fd603fd/VCE2755.pdf
datasheet_label: 原厂数据手册（PDF）
product_image: /images/wiki/sgmicro/3c9d045f0e4c07d8.png
product_image_caption: VCE2755 官方页使用的原厂产品页共用SOIC-8封装示意；不是唯一可选封装
product_image_source: https://www.sg-micro.com/api/assets/7c267236-6f8a-43e4-82e1-128cee30031b
---

## 核心参数

依据[原厂手册](https://www.sg-micro.com/rect/assets/db119b16-8eeb-40df-8fd5-74e92fd603fd/VCE2755.pdf)（2026-01 Rev.A.3，30页）。典型值、最大值与适用条件分别保留。

| 参数 | 数值与适用条件 |
| --- | --- |
| 原理与输出角度 | AMR与ASIC集成，0～360°；饱和磁场下测方向；18位为数字输出字宽（手册第1、5页） |
| 有效角度口径 | 14位；典型最小分辨率0.022°；电气表明确14-bit effective angular resolution，不写18位机械精度（手册第5页） |
| 工作电源／温度 | 3.0～5.5 V；−40～125°C；推荐工作范围；典型参数除特别说明外在25°C（手册第3、5页） |
| INL | 典型±0.3°；全温范围、工作磁场>300 Gs；该数位于TYP列，不是MAX保证（手册第5页） |
| 工作电流 | 典型10 mA；电气表总条件TA=−40～125°C、VDD=3.0～5.5V，典型值25°C（手册第5页） |
| 瞬态噪声 | 典型0.01° RMS；25°C；随系统滤波带宽配置调整（手册第5页） |
| 无补偿系统延时 | 典型2 µs；电气表Actual latency without compensation；首页<2µs宣传与此分开，不写最坏值（手册第1、5页） |
| 最高跟踪速度 | 18000 rpm；单对极条件；不是ABZ任意配置均满足的整机速度（手册第5页） |
| ABZ输出 | 1～1024 ppr；按寄存器和订货配置；PPR与主控四倍频计数分开（手册第5页） |
| UVW／PWM | UVW 1～16极对；PWM典型971.1或485.6 Hz，±5%；频率由PWM_FREQ配置；不能把UVW极对数当编码器机械圈数（手册第5页） |
| 启动／存储 | 典型启动16 ms；MTP典型1000次擦写；MTP读写3.0～5.5V，按编程流程；不上升为任意工作条件寿命保证（手册第5页） |
| 封装与接口 | SOIC-8或TQFN3×3-16JL；SPI/SSI/ABZ/UVW/PWM；SOIC-8与TQFN引脚资源及3/4线SPI不同，按完整订货配置（手册第1、2、4、7页） |

## 先分清码宽、有效角度和增量脉冲

VCE2755 的18位数字角度并不等于18位有效机械精度。手册另外给出14位有效角度口径，而ABZ提供1～1024ppr；接收器若作四倍频，得到的是边沿计数。三种数值分别服务数字传输、噪声/有效分辨与增量计数，不能互换。

## 封装和出厂配置决定接入方式

SOIC-8的三线SPI与TQFN的四线SPI、UVW/PWM/ABZ引脚复用需要按订货行检查。完整Q/S配置号还包含脉冲数、方向、Z宽度、滤波与迟滞等差异；目录保留这些订货号用于检索，画图与软件初始化时仍须回到对应配置。

## 高转速要同时检查ABZ带宽与动态误差

最高18000rpm是在单对极条件下的跟踪指标。按1024ppr计算，A/B基频在该转速可达0.3072MHz，这是计算值；实际还要检查接收器、线缆和边沿能力。整机延迟应包括滤波、串行读取和控制计算，不能只填芯片典型2µs。

## 和同系列器件比较时只保留有据差异

与VCE2758相比，本型号的ABZ表列上限为1024ppr。若控制器实际只需较低脉冲数，仍应按封装、配置与整机误差选择，不能凭4096比1024大就认定整机精度更高。

[继续比较VCE2758](/models/vce2758/)。

## 资料版本与边界

- 网页概述称全温±0.3°、延迟<2µs；电气表第5页将±0.3°和2µs列在TYP列，本文按表格条件解释，不作最大保证。
- 本次核读产品页、订货表、电气/动态表及接线说明；未逐一执行寄存器配置、编程或硬件验证。
- 官网订货表的VCE2755S152未在本次PDF文字订货表中定位；保留为官网检索别名，不臆造其默认配置。

## 官方资料

- [VCE2755产品页](https://www.sg-micro.com/cn/product/VCE2755)
- [VCE2755数据手册（2026-01 Rev.A.3，30页）](https://www.sg-micro.com/rect/assets/db119b16-8eeb-40df-8fd5-74e92fd603fd/VCE2755.pdf)
