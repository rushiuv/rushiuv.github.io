---
title: "华虹"
wiki: true
wiki_type: "company"
wiki_rank: 100
seed_count: 2
lastmod: "2026-10-22"
description: "华虹宏力（688347/01347）做特色工艺代工，eNVM 覆盖 0.35µm~40nm，BCD 到 800V，上海三座 8 英寸、无锡两座 12 英寸。"
official_url: "https://www.huahonggrace.com/"
wiki_category: "制造工艺与产业分工"
related_models: []
---

华虹在编码器链上同样落在"芯片变成硅片"这一步，但路线与先进逻辑厂不同：它把资源压在特色工艺上，模拟与电源管理、eNVM、逻辑射频、功率分立四块公开写明覆盖的工艺段与电压段。对做角度芯片的人，这意味着它的公开资料能回答"这颗芯片该走哪个平台、电压段够不够"，而不能回答"谁在里面流片"。

## 公司与品牌

华虹宏力半导体有限公司（英文 Hua Hong Grace，简称 HHGrace），A 股代码 688347、港股代码 01347。官网自述为"全球领先的特色工艺纯晶圆代工企业"，战略写作"8 英寸 + 12 英寸"与先进"特色 IC + 功率器件"，并写明是华虹集团的一员。[中文首页](https://www.huahonggrace.com/)；[公司简介](https://www.huahonggrace.com/html/about.php)

产线：上海金桥与张江共三座 8 英寸厂、一座 12 英寸厂（HH Fab1/2/3 与 HH Fab5），无锡国家高新区两座 12 英寸厂（HH Fab7、HH Fab9A、HH Fab9B）。官网把两座无锡 12 英寸厂单独表述为专做特色工艺的 12 英寸产线。[晶圆厂清单](https://www.huahonggrace.com/html/business_fab.php)

## 四个平台各自的公开工艺段

官网每块平台都给了工艺覆盖范围，这是它比多数代工厂更可用的一点——数字是官方页面原口径，不含推断：

| 平台 | 公开工艺段 | 其他公开参数 |
| --- | --- | --- |
| [嵌入式存储 eNVM](https://www.huahonggrace.com/html/business_embedded_storage.php) | 8 英寸 0.35µm~90nm，12 英寸 90nm~40nm | eFlash、EEPROM、eOTP/eMTP；官方称同节点下光刻层次与 eFlash 擦写次数有优势 |
| [模拟与电源管理](https://www.huahonggrace.com/html/business_ap_management.php) | 8 英寸 0.35µm~0.11µm，12 英寸 90nm~65/55nm | 自研多代 BCD，器件电压 1.5V~800V，含低压、中压、高压与超高压 |
| [逻辑与射频](https://www.huahonggrace.com/html/business_logic_rf.php) | 0.35µm~40nm | RFCMOS、RFSOI、CIS 与 MEMS；CIS 用高透过率 BSI 像素，ISP 与像素 3D 堆叠，分辨率覆盖 1MP~200MP |
| [功率器件](https://www.huahonggrace.com/html/business_power_component.php) | 8 英寸与 12 英寸双线 | 低压 MOSFET 主覆盖 200V 以下，深沟槽超结 200~900V，IGBT 600~1700V；自研 DT-SJ 与 IGBT 背面工艺 |

角度芯片常用的是前两块：BCD 决定前端与驱动能否同片集成，eNVM 决定校准系数存哪。800V 那一档与角度测量无关，是给电源与电机驱动客户看的。

## 在编码器链上的位置

华虹卖的是特色工艺能力与设计服务，客户名单不公开。所以从"某颗磁传感或角度芯片在华虹流片"这件事，只能推出它选了哪个电压段与存储类型，推不出精度与温漂表现——那些由敏感元件、码盘与校准定。反过来，整机厂看它也有用：8 英寸 0.35µm 这类成熟段仍在产，老料号的工艺迁移窗口要以官网平台页为准，而不是按"先进节点替代"的直觉。

## 公开资料的边界

官网给平台级工艺段与电压段，不给单一料号的良率、产能、报价与交期，也不给 IP 成熟度清单；具体 PDK 与设计规则要签 NDA 走客户门户。另一个实测细节：站点的中文子页（`/business_*.php`）返回 404，同一批内容在英文路径 `/html/` 与繁体 `/c/` 下可读，查资料时走这两个入口更省事。

## 官方资料

- [华虹宏力中文首页](https://www.huahonggrace.com/)
- [公司简介](https://www.huahonggrace.com/html/about.php)
- [晶圆厂清单](https://www.huahonggrace.com/html/business_fab.php)
- [嵌入式存储 eNVM 平台](https://www.huahonggrace.com/html/business_embedded_storage.php)
- [模拟与电源管理（BCD）平台](https://www.huahonggrace.com/html/business_ap_management.php)
- [逻辑与射频平台](https://www.huahonggrace.com/html/business_logic_rf.php)
- [功率器件平台](https://www.huahonggrace.com/html/business_power_component.php)
