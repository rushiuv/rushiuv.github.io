---
title: "ams OSRAM"
description: "奥地利 Premstaetten 的光与传感器公司：2026-07-01 把非光学模拟/混合信号传感业务（含 AS5047P 类磁角度）以 5.7 亿欧元卖给英飞凌，自身只剩光发射与光感知。"
wiki: true
wiki_type: "company"
wiki_rank: 4
seed_count: 24
lastmod: "2026-10-22"
official_url: "https://ams-osram.com/"
related_models: ["AS5047P"]
related_companies: ["英飞凌"]
---

读 ams OSRAM 现在必须带一个时间点：它在 2026 年 7 月 1 日把非光学的模拟与混合信号传感业务整体卖给了英飞凌。这意味着本站保留的 AS5047P、AS5600 这类磁角度资料，法律主体与技术支持已经换了东家；而 ams OSRAM 自己退回「光」——LED、激光、光电探测器与光学传感。对做编码器的人来说，它如今是光编码器光源与接收端的候选供应方，不再是磁角度芯片的同台竞争者。

## 奥地利 Premstaetten 起家，120 年的品牌与一场主动收缩

ams-OSRAM AG，注册地与总部在奥地利 8141 Premstaetten（格拉茨附近），同时在慕尼黑设联合总部，SIX 瑞士交易所上市（ISIN AT0000A3EPA4），2025 年营收 33 亿欧元，员工约 18,500 人，专利约 12,000 项；官网提到 OSRAM 品牌 120 周年。2026 年 2 月 4 日公司宣布战略聚焦「Digital Photonics」，即把光发射与光感知数字化、像素化；2026 年 7 月 1 日完成向英飞凌出售非光学模拟/混合信号传感业务，现金对价 5.7 亿欧元，CEO Aldo Kamper 的表述是把资源集中到核心业务、同时强化资产负债表。[交割公告](https://ams-osram.com/news/press-releases/infineon-closing)；[公司地址与简介](https://ams-osram.com/company/about-ams-osram)

## 磁角度业务已经出手，剩下的目录里只有光

| 对象 | 类型 | 公开事实 | 官方入口 |
| --- | --- | --- | --- |
| 非光学模拟/混合信号传感业务 | 磁与其他非光学传感 | 2026-07-01 交割，现金对价 5.7 亿欧元，买方英飞凌 | [交割公告](https://ams-osram.com/news/press-releases/infineon-closing) |
| AS5047P | 磁角度传感器 | 现列于英飞凌官网，页面标题为 "AS5047P - Angle sensors" | [infineon.com/part/AS5047P](https://www.infineon.com/part/AS5047P) |
| Digital Photonics | 光发射 + 光感知 | 官方定义为光的发射与感知的数字化，像素化发射器与传感器加电子电路 | [公司简介](https://ams-osram.com/company/about-ams-osram) |
| 光电探测器 | 光编码器的接收端 | 产品区含 photodiodes、phototransistors、multi chips | [Photodetectors 目录](https://ams-osram.com/products/photodetectors) |
| 激光与 LED | 光编码器的光源端 | 产品区含 color/IR lasers（EEL、VCSEL）与各类 LED | [Lasers 目录](https://ams-osram.com/products/lasers) |

这张表要读成「谁现在负什么责」：磁角度那条线在英飞凌，ams OSRAM 这边只剩光源、探测器与光学传感。旧手册上的 ams 标识只反映文档来源，不等于当前供货主体。

## 在编码器链上的位置

在光编码器这条路上，ams OSRAM 的位置是光源与接收器件的供应方：光源的波长、功率稳定性、发光面积与驱动方式会改变光斑与对比度，光电探测器的响应度与暗电流决定前端信噪比。但这些器件的可用性要落到具体料号，不能由「这家公司做光」推出「某款编码器的光源就是它」——那是 BOM 层面的事，官网不公布。

在磁角度这条路上，它已经退出：AS5xxx 归英飞凌。所以看到「ams 的 AS5047P 精度多少」这类问题时，答案要去英飞凌的文档里找；本站的 [AS5047P 型号页](/models/as5047p/) 保留历史口径，但当前入口指向新东家。**不能推理的是各整机厂、编码器厂当前用谁家的 LED 或 PD**，也不能把业务交割理解为产品停产——两者是不同的事。

## 公开资料的边界

官网公开的是业务结构、财务口径、公司地址与产品区分类。**没有公开**的是：交割后各型号的料号归属清单（要靠英飞凌逐型号页确认）、光学器件在具体编码器结构里的实测对比度与温漂、以及任何整机厂的设计导入。本次核对 ams OSRAM 站点的产品区，未见磁角度传感器子类；AS5047P 的英飞凌页面只取到页面框架与标题，未取到参数表，因此本页不写它的位数、接口精度与延时。报价与交期不公开。

## 官方资料

- [ams OSRAM 官网](https://ams-osram.com/)
- [公司地址与简介](https://ams-osram.com/company/about-ams-osram)
- [2026-07-01 非光学传感业务交割公告](https://ams-osram.com/news/press-releases/infineon-closing)
- [光电探测器产品区](https://ams-osram.com/products/photodetectors)
- [激光产品区（EEL / VCSEL）](https://ams-osram.com/products/lasers)
- [产品选择器](https://ams-osram.com/products/product-selector)
- [AS5047P 当前官方页（英飞凌）](https://www.infineon.com/part/AS5047P)
