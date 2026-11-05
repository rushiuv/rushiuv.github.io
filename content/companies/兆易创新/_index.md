---
title: "兆易创新"
wiki: true
wiki_type: "company"
wiki_rank: 615
lastmod: "2026-11-05"
description: "兆易创新（GigaDevice，603986.SH / 3986.HK）：北京存储与 MCU 公司，SPI NOR 全球第二，GD32H78E/77E 与 GD32H77R 片内原生支持 Tamagawa、BiSS-C、EnDat 2.2 等编码器协议。"
official_url: "https://www.gigadevice.com.cn/"
wiki_category: "芯片与信号链"
search_aliases:
- 兆易创新科技集团股份有限公司
- GigaDevice Semiconductor
- GD32
related_models: []
---

兆易创新是北京的一家存储与 MCU 公司，SPI NOR Flash 全球第二、Arm 通用 MCU 中国品牌第一，2025 年营收 92 亿元里八成半来自存储。对关节模组厂，这是另一条决策线——编码器选谁是一件事，谁来读它是另一件事。

## 公司与主营结构

兆易创新科技集团股份有限公司（GigaDevice），2005 年 4 月成立，总部北京，2016 年 8 月 18 日在上交所上市（603986.SH），2025 年在港交所上市（3986.HK）。核心产品线为存储器（Flash、利基型 DRAM）、32 位通用型 MCU、智能人机交互传感器、模拟产品。[公司简介](https://www.gigadevice.com.cn/about/company-profile)

官网给的市场位置是：全球排名第一的 Fabless Flash 供应商，SPI NOR Flash 市占率全球第二、累计出货超 310 亿颗；Arm 通用型 MCU 中国品牌排名第一，81 个系列、800+ 款型号、累计出货超 25 亿颗；32 位通用 MCU 全球第七；专利授权 1249 项，服务客户 20000+。公司已通过 ISO 26262:2018 ASIL D 体系认证与 IEC 61508 功能安全产品认证。

2025 年营业收入 92.03 亿元、同比增长 25.12%，归母净利润 16.48 亿元、同比增长 49.47%，研发费用 11.17 亿元。2026 年中报的产品结构是存储芯片 98.27 亿元（84.97%）、微控制器 14.30 亿元（12.36%）、模拟产品 1.91 亿元——MCU 是第二增长曲线，也是编码器系统里用得上的那部分。公司对自身的定位表述为"感存算控连"一体化芯生态，"控"指的就是 MCU。

那条叫"智能人机交互传感器"的产品线是触控与指纹识别方向，与磁场无关，不在这次讨论范围里。

## 与编码器系统相关的器件

真正相关的是 MCU 与 EtherCAT 从站控制器。价值不在算力，而在"片内原生支持哪些编码器协议"——这决定了 BOM 里能省掉几颗协议转换与调理芯片。

| 器件 | 角色 | 公开参数 | 与编码器的关系 |
| --- | --- | --- | --- |
| GD32H78E / 77E | 高性能 MCU | 片内集成 EtherCAT 从站控制器，DC 同步周期精度 62.5 µs；2 个 OSPI 支持 200 MHz 与 DTR；16/32 位 EXMC 可直连 SDRAM 与 FPGA；获 TÜV 莱茵 IEC 61508 SC3（SIL 2 / SIL 3） | 原生支持多摩川 T-format、HIPERFACE DSL、EnDat 2.2、BiSS-C、尼康 A-format，以及旋转变压器（R/D）；通信接口带 CBC 保护 |
| GD32H77R | 机器人 / 伺服专用 MCU | 片内 EtherCAT 从站 + 两路百兆 PHY；单边传输延迟最快 < 50 ns；DC 同步 62.5 µs；支持 FSoE，满足 IEC 61508 SIL 3；1.7~3.6 V | 集成 EnDat、BiSS-C、Tamagawa 等绝对式编码器接口，内置 RDCM 旋变数字转换模块 |
| GDSCN832 | EtherCAT 从站控制器（独立芯片） | 2/3 端口，集成 2 个内部 PHY + 1 个 MII 扩展；8 个 FMMU、8 个同步管理器；8 KB 双端口内存；64 位分布式时钟，精度 < 1 µs；SPI/QSPI/OSPI 从机最高 100 MHz | 编码器数据进运动控制网络的门，不参与角度解算 |
| GD25 系列 SPI NOR Flash | 存储 | 车规型号如 GD25LT 系列 | 存固件、参数表、多圈绝对值与校准数据 |

## 协议支持为什么是关键

BiSS-C、EnDat 2.2、多摩川 T-format、HIPERFACE DSL、尼康 A-format 是五套互不兼容的绝对编码器串行协议，电气层、帧结构、CRC 规则各不相同。传统做法是在 MCU 与编码器之间加一颗 FPGA 或专用接口芯片做转换，成本与开发周期都是另一档；MCU 能原生解这几套，意味着换编码器品牌时不用重做接口板。

EtherCAT 这块的背景是：从站控制器长期由倍福体系供货，兆易在拿到倍福正式授权后推出 GDSCN832，2024 年 11 月发布、2025 年二季度起量产。它把两路 PHY 与从站控制器都放进片内，官方称省去两颗外置工业级 PHY；GD32H77R 更进一步，把从站控制器与两路百兆 PHY 一起集成，单边传输延迟做到 50 ns 以内，并支持 FSoE 安全数据同网传输。

DC 同步 62.5 µs 是给多轴用的。单轴不敏感，多关节联动的时序一致性靠的就是这个数——它管"什么时候采的"，编码器精度管"采到多准"，两者各管一头。

## 在编码器链上的位置

编码器链条可以粗分四段：敏感元件 → 解算与校准 → 协议与接口 → 运动控制网络。兆易只做后两段，做得比较彻底：协议在 MCU 里解，网络在 MCU 或从站控制器里接，固件与校准参数存在自家 Flash 里。

这个位置有个副作用：它对编码器的精度没有话语权。客户抱怨角度不准，问题可能出在磁编芯片、安装偏心、码盘，也可能出在 MCU 的采样时序，而兆易只能解决最后一段。此外，GD32H78E 系列"原生支持"的实现方式是硬件协议引擎还是固件库加定时器捕获，公开页面只给协议清单不给实现细节，各协议支持的时钟上限与长线驱动能力需查对应型号的用户手册。

## 官方资料

- [兆易创新官网](https://www.gigadevice.com.cn/)
- [关于兆易创新（产品线与市场地位）](https://www.gigadevice.com.cn/about/company-profile)
- [GD32 MCU 官网](https://www.gd32mcu.com/)
- [GD32H7 系列扩容（EtherCAT 与编码器协议支持）](https://www.gd32mcu.com/cn/detail/566)
- [EtherCAT 从站控制芯片 GDSCN832 发布](https://www.gd32mcu.com/cn/detail/559)
- [2025 年年报数据](https://m.cnstock.com/commonDetail/660336)
