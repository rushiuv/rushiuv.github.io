---
title: "Intel"
wiki: true
wiki_type: "company"
wiki_rank: 48
seed_count: 4
lastmod: "2026-10-22"
description: "Intel 是 x86 平台厂兼代工厂，18A 用 RibbonFET 加 PowerVia、14A 再叠背面供电，另有 Intel 3 的 E 版扩展到 I/O 与模拟。"
official_url: "https://www.intel.com/"
wiki_category: "计算平台与机器人软件"
related_models: ["D435i"]
---

Intel 在编码器链上有两个不相干的位置：一是机器人控制器里的 x86 主板——角度值最终被这个控制器读走，但读的是总线帧不是传感器信号；二是晶圆代工，18A/14A 这类节点决定别人家的 SoC 能做成什么样。它的深度视觉（RealSense）是第三条线，与角度无关，容易混淆。

## 公司与品牌

官网把历史起点写在 1971 年的第一颗微处理器上，现在的自我定位横跨处理器、加速器与软件，覆盖云、企业与边缘三层；同时把 Intel Foundry 表述为"唯一总部在美国的领先节点代工厂"，业务含芯片设计、制造与先进封装。[公司概况](https://www.intel.com/content/www/us/en/company-overview/company-overview.html)

同一页给的三组数字值得记住口径：2030 年单颗器件上 1 万亿个晶体管、全球 70% 的 PC 跑在 Intel 上、全球 7 万件自有专利资产。三条都是官网自述，不是第三方统计。

## 代工节点公开到相对提升的量级

Intel Foundry 的工艺页把节点、晶体管结构与相对提升一起写，比多数代工厂具体：

| 节点 | 官网写的结构与公开数字 |
| --- | --- |
| [Intel 14A](https://www.intel.com/content/www/us/en/foundry/process.html) | RibbonFET 2 全环绕栅极 + PowerDirect 背面供电；同功耗性能提升 15~20%，或同性能功耗降 25~35%，密度较 18A 提升最多 30% |
| Intel 18A | 业界首个把 RibbonFET 与 PowerVia 背面供电组合；同功耗性能最多提升 18%、同性能功耗最多降 38%，密度较 Intel 3 提升 30%；家族含 18A-P（每瓦性能再提 9%）与面向 3DIC 的 18A-PT |
| Intel 3 | 最后一个 FinFET 节点，同功耗性能提升 18%，密度较 Intel 4 提升 8%；已量产量产但仅作设计服务节点；E 版扩展 I/O 与模拟能力，T 版提供穿透硅通孔 |
| 12nm | 与联电合作的 12nm 平台 |

"E 版扩展 I/O 与模拟"这条与传感器芯片最直接相关：角度芯片要的不是主频，而是模拟前端与 IO 的余量。官网没给该节点下模拟器件的电压档位、匹配精度与噪声数据，只有"扩展"这个描述。

## 在编码器链上的位置

多轴设备的控制柜通常是 x86 加实时系统，跑运动控制与 EtherCAT 主站；角度值以总线帧的形式进来，周期由总线决定，与传感器本身的接口无关。所以 Intel 的位置是"读角度的人"，不是"产生角度的人"。把 x86 平台换成别家，编码器的接口与精度都不变，变的只是插补周期与可达轴数。

RealSense 是另一条线：深度相机与 IMU，不含旋转测量。官网现存入口已转到独立站点，产品按 D430、D450、D555、D585 Pro、D405 等系列列；本站的 `[D435i](/models/d435i/)` 型号页属于这一族，与编码器无交集。[realsenseai.com](https://www.realsenseai.com/)

节点页给相对提升，不给晶圆价格、产能、良率与客户名单；处理器侧不给具体型号的工业温度等级与长期供货承诺，要查产品规格书。

## 官方资料

- [Intel 官网](https://www.intel.com/)
- [公司概况与关键数字](https://www.intel.com/content/www/us/en/company-overview/company-overview.html)
- [Intel Foundry 总览](https://www.intel.com/content/www/us/en/foundry/overview.html)
- [代工工艺节点（14A、18A、Intel 3）](https://www.intel.com/content/www/us/en/foundry/process.html)
- [RealSense 现站点](https://www.realsenseai.com/)
- 本站 D435i 型号页
