---
title: "Melexis 第一颗“中国造”芯片，真正狠的不是 250kHz，而是那根编程线"
date: 2026-10-08T10:00:00+08:00
slug: "msUOzwlgh5cloVe_544maw"
description: "SENSOR · MANUFACTURING · EOL CALIBRATION"
original: "https://mp.weixin.qq.com/s/msUOzwlgh5cloVe_544maw"
companies: ["华虹", "Melexis"]
tags: ["霍尔", "半导体产业"]
---

SENSOR · MANUFACTURING · EOL CALIBRATION

## Melexis 第一颗“中国造”芯片，真正狠的不是 250kHz，而是那根编程线

MLX91241 最值得国内传感器同行盯住的，不是带宽，也不是 3μs，而是 **1-pin EOL programmable**。因为这一行参数，决定了它是在卖一颗芯片，还是在参与客户的量产制造。

![](/images/wx/cb3b63e2102bc396cb879d6e7489cf00.jpg)

图源：Melexis 官方新闻稿，2026-09-15

9 月 15 日，Melexis 宣布 MLX91241 成为其首颗采用中国本土化制造模式生产的 IC，晶圆由华虹宏力代工。新闻里最醒目的当然是“中国制造”，产品页最醒目的则是 **250kHz、3μs**。

但如果站在量产传感器工程师的角度，我会把荧光笔画在另一行：**End-of-line programmable，offset 和 sensitivity 可以由客户在最终装配后，通过单引脚协议重新设定，而且普通 MCU 就能实现，不要求专用编程器。**

真正的问题

一颗 Hall 芯片在晶圆厂里校得再准，装进 C-Core 以后，为什么还要再校一次？

### 因为最后测量的根本不是“芯片”

MLX91241 是 conventional Hall。典型应用里，母排或电缆穿过铁磁 C-Core，传感器放进气隙。电流先变成磁场，磁芯再把磁通集中到气隙，Hall 芯片最后看到的是这个局部磁场。

Melexis 设计指南给出的近似关系

B[mT] ≈ 1.25 × I[A] / d[mm]

也就是说，在这个一阶模型里，气隙 d 直接决定磁场增益。传感器厂能把芯片本身的 offset、gain、温漂修得很漂亮，却控制不了客户最后装出来的气隙究竟是 4.9mm、5.0mm，还是 5.1mm。

|

气隙 d

 |

B/I

 |

相对 5.0mm

 |
|

4.9 mm

 |

0.2551 mT/A

 |

约 +2.04%

 |
|

5.0 mm

 |

0.2500 mT/A

 |

基准

 |
|

5.1 mm

 |

0.2451 mT/A

 |

约 -1.96%

 |

这里只用 Melexis 公开的一阶近似说明量级；真实系统还会叠加磁芯材料、位置、磁滞、饱和、频响和温漂。

![](/images/wx/14a41ecddda77ee9b7df90e6235c9e77.jpg)

Melexis conventional Hall + C-Core 开发套件。注意：此图用于说明同类 C-Core 架构，并非 MLX91241 专属开发板。图源：Melexis

### 0.1mm 的机械公差，可能比芯片参数表上的小数点更大

如果 nominal gap 是 5mm，仅仅 ±0.1mm，就已经对应大约 ±2% 的磁场增益变化。这里还没算 Hall 芯片在气隙中的偏心、母排相对位置、磁芯材料离散、装夹应力以及不同批次磁芯的磁性能变化。

所以“芯片出厂已经校准”并不能自动等于“模块装完以后也准”。芯片厂校的是 silicon；客户最后卖出去的却是 **silicon + PCB + busbar + core + holder + assembly**。

MLX91241 真正有意思的地方，是把校准边界从“芯片出厂”往后推到了“系统装配完成”。

### 所谓 EOL，不是再测一遍，而是把装配误差吃回去

MLX91241 的公开产品页明确写到：传输特性在工厂已经做温度修调，但客户仍可在 EOL 阶段重新编程 **offset 与 sensitivity**。这两个量刚好对应线性测量里最基本的两类系统误差：零点偏移和增益偏差。

如果只讨论一阶线性校准，工程上两个已知电流点就足以确定一条直线。设两点为：

(I₁, V₁) (I₂, V₂)
K = (V₂ - V₁) / (I₂ - I₁)
V₀ = V₁ - K·I₁

这是校准原理示意，不代表 MLX91241 官方披露了具体两点校准流程；完整编程细节仍以其正式 datasheet 为准。

于是量产线可以先把整个模块装好，再给它零电流和一个标准电流，测出最终系统的偏移与斜率，然后把修正量写回传感器。

这一刀切得很漂亮：**机械公差没有消失，只是从“必须加工掉”变成“只要稳定，就可以校掉”。**

![](/images/wx/b37496bbab2eeb3d304e605705de7a37.jpg)

MLX91241，SIP4-VB 封装。图源：Melexis 官方产品页

### 而“1-pin”三个字，决定它能不能真的进产线

EOL programmable 并不新鲜。真正值得盯的是后半句：**via a 1-pin protocol that can be implemented on any standard MCU without requiring a proprietary programmer。**

对实验室来说，专用编程器、多一组通信接口、多几根测试针都不是问题；对几十万、几百万件的产线来说，每多一个接触点，都意味着 fixture、更换周期、接触失效率、节拍和维护成本。

如果原有 EOL 工站那颗 MCU 就能完成编程，那么校准不再是一台“传感器专用设备”，而可以直接变成整机测试流程里的一个动作。

这才是我认为最狠的一层

Melexis 卖的已经不只是“更准的 Hall”，而是“允许你的机械件没那么准”的权利。

如果一个静态误差是稳定、可测、可重复的，那么最贵的解决方案往往不是把它加工到消失，而是测出来，再校掉。传感器里的几个可编程参数，有时比把塑胶支架、磁芯气隙和装配定位全部再提升一个机械精度等级便宜得多。

这也是为什么我现在再看 Melexis 的“中国制造”新闻，注意力反而从晶圆厂转回了产品定义：**它第一颗中国本土化 IC，就把量产终端校准做成了产品的一等公民。**

如果只记住一句话

一百万颗芯片并不难。
难的是装进一百万套不完全一样的机械结构以后，
最后还能像同一套产品。

所以 MLX91241 上我最想圈出来的，不是 **250kHz**，不是 **3μs**。

是 1-pin EOL programmable。

因为前两个参数说明它能不能测得快。最后这一行，说明 Melexis 有没有真的想清楚：**这颗传感器怎么被客户一天生产几千颗。**

资料与图片来源

1. Melexis：MLX91241 中国本土化生产新闻稿

2. Melexis：MLX91241 官方产品页

3. Melexis：Current Sensors Reference Design Guide

4. Melexis：Conventional Hall C-Core Development Kit
