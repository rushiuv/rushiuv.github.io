---
title: "Broadcom"
wiki: true
wiki_type: "company"
wiki_rank: 47
seed_count: 4
lastmod: "2026-10-22"
description: "Broadcom（博通）：AEAT 磁编码器 IC 与 AEDR 反射光学读头，AEAT-9988M 公开 23 位绝对角与电池备份多圈。"
official_url: "https://www.broadcom.com/products/motion-control-encoders"
wiki_category: "芯片与信号链"
related_models: ["AEDR-850x"]
---

Broadcom 的运动控制编码器是一条"元件产品线"：它卖编码器 IC（AEAT 系列）和反射式光学读头（AEDR 系列），也卖码盘与线驱动 IC，但不做带壳体的整机编码器。对做整机的人，它的价值在于三条不同的封装形态——芯片级磁编、含壳体的增量套件、贴片光学读头——以及 LPI、CPR、位数三套分辨率口径同时公开。

## 公司与品牌

现 Broadcom Inc. 的前身线是 1961 年起的惠普半导体业务，2005 年独立为 Avago Technologies，2016 年收购原 Broadcom 后改用现名，总部在加州 Palo Alto（Stanford Research Park），2025 年员工约 33000 人（维基百科口径，收入规模属其半导体与基础设施软件合并口径）。运动控制编码器只是其产品组合里很小的一块。

从编码器这条线看，品牌的来源比产品参数更值得记：AEAT、AEDR、HEDS、AR 系列型号前缀混用，说明这条线经历过多次整合，同一份目录里的产品不一定是同一代工艺。[Broadcom 公司条目](https://en.wikipedia.org/wiki/Broadcom)

## 编码器产品线与公开规格

官网把编码器分成绝对值（单圈 / 多圈）、增量（磁 / 反射式 / 透射式）、码盘、线驱动 IC、旋转开关几组。下表按类目抄，分辨率一律用官网自己的口径。

| 系列 | 类型 | 公开分辨率 | 其他公开参数 |
| --- | --- | --- | --- |
| [AEAT-9966](https://www.broadcom.com/products/motion-control-encoders/absolute-encoders/single-turn-encoders/aeat-9966) | 霍尔式绝对值磁编码器 IC（双芯片冗余） | 10~18 位可编程绝对角 | ABI 1~20000 CPR、UVW 1~32 对极、2/3 线 SSI 与 4 线 SPI、PWM、QFN-32 5×5 mm、内含 INL 校正 |
| [AEAT-9988M](https://www.broadcom.com/products/motion-control-encoders/absolute-encoders/multi-turn-encoders/magnetic-aeat-9988m) | 双轨道磁编码器 IC，电池备份多圈 | 绝对 16~23 位、多圈 10~16 位 | ABI 1~65536 CPR、UVW 1~64 对极、SSI / SPI / BiSS-C / RS-485、磁环内径 20~50 mm |
| [AEAT-901B](https://www.broadcom.com/products/motion-control-encoders/incremental-encoders/magnetic-encoders/aeat-901b) | 增量磁编码器套件（含壳体） | 256~10000 CPR | 5 V、−40~125 °C、耐油污、小体积、带线缆输出 |
| [AEAT-601B-F06](https://www.broadcom.com/products/motion-control-encoders/magnetic-encoders) | 增量磁编码器套件 | 256 CPR | 6 mm 轴、数字输出 |
| [AEDR-9930E2 / EA](https://www.broadcom.com/products/motion-control-encoders/incremental-encoders/reflective-encoders) | 反射式光学增量读头 | 397 LPI | TQFN 5×5 mm、5 V、线性与旋转 |
| [AEDR-9830 / 9830DP](https://www.broadcom.com/products/motion-control-encoders/incremental-encoders/reflective-encoders) | 反射式光学增量读头 | 318 LPI | TQFN 4×4 mm、3.3 V（9830E 支持 3.3/5 V） |
| [AEDR-9940](https://www.broadcom.com/products/motion-control-encoders/incremental-encoders/reflective-encoders) | 反射式光学增量读头 | 198.4 LPI | TQFN 4×4 mm、3.3 V |
| [AEDR-9920 / 9820](https://www.broadcom.com/products/motion-control-encoders/incremental-encoders/reflective-encoders) | 反射式光学增量读头 | 225 LPI | TQFN 4×4 mm、3.3 V 或 5 V |
| [AEDR-8600](https://www.broadcom.com/products/motion-control-encoders/incremental-encoders/reflective-encoders) | 反射式光学增量读头（旋转） | 294~304 LPI | 5 V、SMT |

三条差异要点。**AEAT-9966 是芯片，AEAT-9988M 是芯片加电池备份多圈**：前者只到单圈，多圈靠外部系统；后者把多圈计数与备份电源做成内置，磁环内径 20~50 mm 说明它面向大口径空心轴而不是小电机。**AEDR 系列是读头不是编码器**：LPI 是码盘节距，最终 CPR 由码盘直径与插值决定，官网上 LPI 与 CPR 不能直接比。**AEAT-901B 是对外最"像商品"的一档**：含壳体、带线缆、−40~125 °C，客户装上就能用。[编码器产品总目录](https://www.broadcom.com/products/motion-control-encoders)

## 在编码器链上的位置

Broadcom 在这一层是元件供应商：卖贴片读头、编码器 IC 与含壳套件，码盘与磁环由客户自己配（它也单独卖码盘）。客户是自己做整机的编码器厂、电机厂与产线设备厂，很多情况下读头直接焊在客户的电机板上。

能推的是取向：AEDR 类 4×4 mm、3.3 V 的读头，意味着客户追求体积与低功耗；AEAT-9988M 走 20~50 mm 磁环与电池备份，意味着客户能接受体积换掉电记忆。不能推断的：芯片的晶圆来源（这条线经历过多次整合，官网不写代工），以及任何客户的 BOM——写进页面的只有型号与公开参数。

## 公开资料的边界

列表页给 LPI、CPR、封装与温度档，不给逐型号精度（角秒）、抖动、插值后的有效位数、气隙公差与码盘偏心容差；AEAT-9988M 的电池类型、备份寿命、多圈计数的掉电功耗要查 datasheet。AEAT-9966 的"双芯片冗余"描述的是封装内的双 die 结构，具体诊断覆盖率与安全等级要查安全手册。

另外注意官网列表里部分单元格是空的（例如部分型号的操作温度未填），本页遇到空值就不填，不替官方补。报价、MOQ、交期不公开。

## 官方资料

- [运动控制编码器总目录](https://www.broadcom.com/products/motion-control-encoders)
- [增量磁编码器类目](https://www.broadcom.com/products/motion-control-encoders/magnetic-encoders)
- [AEAT-901B 增量磁编码器套件](https://www.broadcom.com/products/motion-control-encoders/incremental-encoders/magnetic-encoders/aeat-901b)
- [绝对值编码器类目](https://www.broadcom.com/products/motion-control-encoders/absolute-encoders)
- [单圈绝对值类目](https://www.broadcom.com/products/motion-control-encoders/absolute-encoders/single-turn-encoders)
- [AEAT-9966 单圈 10~18 位磁编码器](https://www.broadcom.com/products/motion-control-encoders/absolute-encoders/single-turn-encoders/aeat-9966)
- [多圈绝对值类目](https://www.broadcom.com/products/motion-control-encoders/absolute-encoders/multi-turn-encoders)
- [AEAT-9988M 23 位多圈磁编码器](https://www.broadcom.com/products/motion-control-encoders/absolute-encoders/multi-turn-encoders/magnetic-aeat-9988m)
- [反射式光学增量读头类目](https://www.broadcom.com/products/motion-control-encoders/incremental-encoders/reflective-encoders)
- [Broadcom 公司条目（沿革与规模）](https://en.wikipedia.org/wiki/Broadcom)
