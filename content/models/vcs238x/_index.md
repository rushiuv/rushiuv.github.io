---
title: VCS238x系列
description: VCS2381、VCS2382、VCS2383为同系列平面二维全极AMR推挽开关，按25°C磁阈值窗口选择成员；三款共用一份手册。
wiki: true
wiki_type: model
wiki_rank: 239
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 圣邦微
wiki_category: 磁开关
catalog_vendor: 圣邦微
catalog_type: 磁开关
catalog_form: 芯片
search_aliases:
- VCS2381
- VCS2381S
- VCS2382
- VCS2382S
- VCS2383
- VCS2383S
official_url: https://www.sg-micro.com/cn/products/amr-sensor
document_version: 2025-09 Rev.A，8页
model_card: true
datasheet_url: https://www.sg-micro.com/rect/assets/11532fa9-9d2d-45be-9bd4-64d54249e3cb/VCS2381_VCS2382_VCS2383.pdf
datasheet_label: VCS238x系列原厂手册（PDF）
product_image: /images/wiki/sgmicro/5e862c9d90ab495f.png
product_image_caption: VCS2381／2382／2383官方页共用SOT-23-3封装示意
product_image_source: https://www.sg-micro.com/api/assets/47789a8d-5b7e-4ba1-87f7-349777e2cc09
catalog_level: 系列
merged_models:
- vcs2381
- vcs2382
- vcs2383
---

VCS238x是平面二维全极AMR磁开关系列，三款共用推挽输出和封装，核心区别在动作、释放及迟滞窗口。选型以最小／最大门限配磁体与气隙，典型值只用于说明档位。

## 三个型号的阈值比较

| 型号／订货号 | BOP动作点 | BRP释放点 | 磁迟滞 |
| --- | --- | --- | --- |
| <span id="config-vcs2381"></span>VCS2381 / VCS2381S | 典型±7 Gs；表列最小/最大±3～±22 Gs；磁参数TA=25°C、VDD=2.0～5.5V；按正负磁极对称口径读取（手册第4页） | 典型±5 Gs；表列最小/最大±1～±18 Gs；磁参数TA=25°C、VDD=2.0～5.5V；不是机械释放距离（手册第4页） | 典型2 Gs；最小1 Gs，最大10 Gs；同磁参数条件，不能仅用典型门限计算全公差窗口（手册第4页） |
| <span id="config-vcs2382"></span>VCS2382 / VCS2382S | 典型±15 Gs；表列最小/最大±5～±35 Gs；磁参数TA=25°C、VDD=2.0～5.5V；按正负磁极对称口径读取（手册第4页） | 典型±12 Gs；表列最小/最大±2～±25 Gs；磁参数TA=25°C、VDD=2.0～5.5V；不是机械释放距离（手册第4页） | 典型3 Gs；最小1 Gs，最大12 Gs；同磁参数条件，不能仅用典型门限计算全公差窗口（手册第4页） |
| <span id="config-vcs2383"></span>VCS2383 / VCS2383S | 典型±10 Gs；表列最小/最大±3～±22 Gs；磁参数TA=25°C、VDD=2.0～5.5V；按正负磁极对称口径读取（手册第4页） | 典型±8 Gs；表列最小/最大±1～±18 Gs；磁参数TA=25°C、VDD=2.0～5.5V；不是机械释放距离（手册第4页） | 典型2 Gs；最小1 Gs，最大10 Gs；同磁参数条件，不能仅用典型门限计算全公差窗口（手册第4页） |

表内磁参数条件为TA=25°C、VDD=2.0～5.5V，依据2025-09 Rev.A第4页。正负号按全极对称口径读取，不把25°C门限窗口扩展为全温保证。

## 共用电气与引脚

- **逻辑与输出**：平面二维360°磁场感应，全极性，推挽输出；360°指芯片平面内敏感方向，不是角度数值输出（手册第1、5页）
- **供电与温度**：2.0～5.5 V；−40～125°C；推荐工作条件，典型值除特别说明外25°C（手册第1、2、4页）
- **平均电流**：典型0.2 µA，最大0.7 µA；VDD=3.3V，电气表总温度条件；不把典型值作上限（手册第4页）
- **采样与时序**：典型15 Hz；典型休眠66.7 ms；典型启动3.5 ms；15Hz不等于任意短磁事件必检出，也不是最坏响应保证（手册第4页）
- **输出电平**：高电平最低VDD−0.2V；低电平最大0.1V；负载10mA、VDD=3.3V（手册第4页）

- **封装及引脚**：SOT-23-3，TOP VIEW为1 VDD、2 OUT、3 GND；三个完整订货号分别为VCS2381S、VCS2382S和VCS2383S。

## 把磁阈值落到机械触发距离

磁体公差、气隙、倾斜与温度共同决定触发位置。较低典型门限可能扩大检测距离，也改变外部磁场扰动裕量；验证要覆盖最弱磁体、最大气隙及往返释放，而不是只在标称位置测一次翻转。

平面二维360°敏感方向与全极触发仍只输出高低状态，不提供连续角度。15Hz间歇测量还需与最短磁事件比较，快速掠过时应测试实际重复捕获率。

[VCS2395](/models/vcs2395/)为开漏输出、典型60Hz与0.45µA；不能沿用本系列推挽输出的接线及功耗结论。


## 官方资料

明确型号、配置与版本后使用对应文件。


- [官方产品入口](https://www.sg-micro.com/cn/products/amr-sensor)
- [VCS238x系列原厂手册（PDF）](https://www.sg-micro.com/rect/assets/11532fa9-9d2d-45be-9bd4-64d54249e3cb/VCS2381_VCS2382_VCS2383.pdf)

- [VCS2381官方产品页](https://www.sg-micro.com/cn/product/VCS2381)
- [VCS2382官方产品页](https://www.sg-micro.com/cn/product/VCS2382)
- [VCS2383官方产品页](https://www.sg-micro.com/cn/product/VCS2383)
