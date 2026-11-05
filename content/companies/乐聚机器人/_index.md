---
title: "乐聚机器人"
wiki: true
wiki_type: "company"
wiki_rank: 651
lastmod: "2026-11-05"
description: "深圳乐聚机器人（Leju）：从 Aelos、Roban 教育双足起家，现主力是全尺寸夸父 KUAVO 5——1.73 m、41 自由度、整机负载 20 kg，2026 上半年出货 650 台。"
official_url: "https://www.lejurobot.com/"
wiki_category: "人形机器人与关节"
search_aliases:
- 乐聚智能（深圳）股份有限公司
- 乐聚（深圳）机器人技术有限公司
- Leju Robotics
related_models: []
---

乐聚是少数把三档尺寸都做齐的整机厂：桌面级的 Aelos、中尺寸的 Roban、全尺寸的夸父 KUAVO。这三档对应三套完全不同的东西——Aelos 用舵机，Roban 用 22 个关节跑 ROS，夸父用的是自研关节模组和 400 N·m 级电机。把它们混在一起谈"乐聚的自由度"没有意义。

## 公司与产品沿革

2016 年 3 月由哈尔滨工业大学团队在深圳创立，原名乐聚（深圳）机器人技术有限公司，2025 年 9 月完成股份制改造，更名为乐聚智能（深圳）股份有限公司，品牌与产品线仍用"乐聚机器人"。国家级专精特新"小巨人"。官网把方案按科研、商服、工业、训练场四类组织，产品列 KUAVO 4Pro 与 KUAVO 5 / 5-W。[官网](https://www.lejurobot.com/)

几个时间点值得记：2018 年 Aelos 出现在平昌冬奥会闭幕式"北京 8 分钟"；2025 年 2 月夸父在亚冬会火炬传递现场出现，同年 11 月又以 5G-A 人形机器人火炬手身份出现在十五运会；2026 年 5 月创业板 IPO 申请获深交所受理，媒体口径拟募资 26 亿元，具体数字以招股书披露为准。制造端是与东方精工在佛山合建的万台级产线，加上深圳龙华的中试线，形成"深圳研发中试 + 佛山量产"的布局。

<figure class="company-photo company-photo--wide">
<div class="company-photo__frame"><a href="/images/companies/public-20261105/leju-1.webp"><img src="/images/companies/public-20261105/leju-1.webp" alt="夸父（Kuavo）人形机器人" width="936" height="670" loading="lazy" decoding="async"></a></div>
<figcaption>夸父（Kuavo）人形机器人 · 图：<a href="https://www.lejurobot.com/">乐聚机器人官网</a></figcaption>
</figure>

## 机型与公开规格

下表前两行取自公司披露与展会现场口径，后三行来自官方手册与产品资料。乐聚没有把参数集中放在一个规格页上，同一型号在不同渠道的口径会略有出入。

| 机型 | 形态 | 公开规格 | 定位 |
| --- | --- | --- | --- |
| KUAVO 5（夸父 5） | 全尺寸双足 | 1.73 m / 63.5 kg；总自由度 41（含 6 自由度灵巧手，本体 29）；电机最大扭矩 400 N·m；单臂 5 kg、整机 20 kg；腰部 ±180°；续航 ≥2 h，支持快换电；算力 100–2070 TOPS；4×深度相机 + 3D 激光雷达 | 工业规模化，纸箱拆垛、小件上料、料箱搬运 |
| KUAVO 5-W | 轮式双臂 | 官网单列型号；媒体口径续航 8 h、腰部 180° 旋转、作业范围 0–2600 mm | 产线内长时段作业 |
| KUAVO 4Pro | 全尺寸双足 | 1.66 m / 55 kg；官方手册标准版 22 自由度（臂 7×2、腿 6×2），展会版含灵巧手时更高；臂展 2.148 m | 高校与科研开发平台 |
| KUAVO 4Pro 轮臂 | 轮式 + 升降 | 官方手册：699×573×1407 mm、自重 120 kg、升降 600 mm、单臂 3 kg、续航 ≥10 h、四轮万向、原地转弯 | 导览与服务场景 |
| Roban | 小型双足 | 68.68 cm / 6.6 kg / 22 关节；ROS + Linux，树莓派级主控 | 中高职与高校教学、算法验证 |
| Aelos | 桌面双足 | 30 cm 级，舵机关节（不同资料对自由度口径不一，未取信单一数字） | K12 编程与竞赛 |

有两条容易看错。第一，41 个自由度里含 6 自由度的灵巧手，本体只有 29 个，谈关节数量时要先说明含不含末端。

## 产业链角色

自研的是整机结构、运控与"大脑—小脑"软件栈，官方表述为全栈自研。对外公开的系统层合作有三条：系统跑开源鸿蒙（KaihongOS 体系），接入华为云 CloudRobo 与盘古大模型；与中国移动合作做 5G-A 联网能力，火炬手那台就是这条线的展示。

招股书里可能有供应商集中度一类的披露，但那是财报口径，不会给出具体型号。

对下游的意义是：夸父是一条明确按工业场景设计的链，减速器与电机要经得起两班倒；对上游器件厂，这意味着认证周期比教育机器人长得多，而 Aelos 那条舵机链的成本逻辑完全不能套用。

出货口径上，2026 年中博会的现场说法是"今年上半年出货 650 台"，并称已获一汽红旗、蔚来、哈金森、海晨、中国物流、东方精工等十多家企业采购。这些是公司与展会侧口径，第三方尚无独立统计。

## 官方资料

- [乐聚机器人官网](https://www.lejurobot.com/)
- [KUAVO 4Pro 轮臂产品介绍（官方手册）](https://kuavo.lejurobot.com/beta_manual/basic_usage/kuavo-ros-control/docs/1%E4%BA%A7%E5%93%81%E4%BB%8B%E7%BB%8D/%E8%BD%AE%E8%87%82%E4%BA%A7%E5%93%81%E4%BB%8B%E7%BB%8D/)
- [科研场景方案](https://www.lejurobot.com/zh/solutions/research)
- [工业场景方案](https://www.lejurobot.com/zh/solutions/industrial)
- [OpenLET 具身智能开源社区](https://openlet.openatom.tech/)
