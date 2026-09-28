---
title: "12万转、1μs、16位：读完 KTH7815 对比 AS5047P，几个规格表之外的现场问题"
date: 2026-09-12T08:29:00+08:00
slug: "_7IfYuHvJFSpoQPfkBSqOQ"
description: "刚看完满度科技这篇《12万转、1μs延时、16位输出，昆泰芯 KTH7815 对比 AS5047P 优势在哪》。"
original: "https://mp.weixin.qq.com/s/_7IfYuHvJFSpoQPfkBSqOQ"
---

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIWNUic8MpxVsW7HdSIAcZ1M3AVHXYLrDpjSwVP6nWnUxmqbDJSpbWKCtHXoh40wQmiaxCDI54icxLsn9aS7zZDVjcU8vXAUV7OJEg/640?wx_fmt=png&from=appmsg)

## 12万转、1μs、16位：读完 KTH7815 对比 AS5047P，几个规格表之外的现场问题

刚看完满度科技这篇《[12万转、1μs延时、16位输出，昆泰芯 KTH7815 对比 AS5047P 优势在哪](http://mp.weixin.qq.com/s?__biz=MzkzODk0NDQ2Mw==&mid=2247485043&idx=1&sn=d4ef5decf9a8c267a051295dc3d60f71&chksm=c3288b8a2f05882c405fdac38d3663c98e37fc2a4321cea42151188bd14243e3195f047929bb&scene=21&xtrack=1＃wechat_redirect)》。

|

参数

 |

昆泰芯 KTH7815

 |

ams AS5047P

 |
|

核心分辨率

 |

16 位（65536 点/圈）

 |

14 位（16384 点/圈）

 |
|

非线性误差 INL

 |

±0.35°（典型）

 |

±0.8°（25°C 最佳摆放），全温区最高 ±1.2°

 |
|

数据刷新/延时

 |

1μs

 |

SPI 读取路径 90–110μs（ABI/UVW 经 DAEC 后 1.5–1.9μs）

 |
|

最高转速

 |

120000rpm

 |

28000rpm

 |
|

工作磁场

 |

30–150mT

 |

35–70mT（低于 35mT 噪声变差）

 |
|

输出噪声（1σ）

 |

0.24°

 |

0.068°

 |
|

ABZ 分辨率

 |

4–4096 步/圈，任意整数可编程

 |

固定档位（25–1000 ppr 及 1024/512/256）

 |
|

ABZ 输出形式

 |

差分 A/~A、B/~B、Z/~Z

 |

单端

 |
|

配置存储

 |

MTP，125℃ 下 1000 次写入

 |

OTP，仅一次

 |
|

磁场诊断

 |

MGH/MGL 独立报警引脚，阈值可编程

 |

需经 SPI 读取诊断标志

 |
|

启动时间

 |

1ms（典型）

 |

最长 10ms

 |
|

ESD（HBM）

 |

±5kV

 |

±2kV

 |
|

封装

 |

QFN-16L 3×3mm / SOP-8

 |

TSSOP-14（本体约 5×4.4mm）

 |

原文已经把 16 位对 14 位、120000 rpm 对 28000 rpm、MTP 对 OTP、差分 ABZ 对单端 ABI 这些规格拆得很清楚了。下面不重复这些参数，只顺着其中几个数字，补一点规格表之外的工程语义。

这里先把边界说清楚：下面不是替 KTH7815 或 AS5047P 判定整体优劣。KTH7815 的 1μs、MTP 和差分 ABZ，按原文给出的规格来解释它们在工程上意味着什么；能不能在真实系统里形成优势，还要看两款器件是否使用同一延时定义、同一动态工况和同一线束条件测试。

因为参数表里一行字，到了现场，可能就是一次返工、一轮重新布线，或者一整晚查不出原因。

### 1μs真正要追的是测量时刻

120000 rpm 时，一圈机械角只有 500μs。因此 1μs 对应的机械角位移是：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM41d1kW0icLEbqoeEYEUdG9zW6E8RAbD306eLicicKyRrWuvRfuSkwWwvsdTlXciaZrIgjF8cJeNcEhoEiaW5Fh1SjflfYmY5SXFquMmY8VVAqdqVw/640?wx_fmt=svg&from=appmsg)

而 16 位输出的一个码值只有：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5GTfpRdIpTcO3yuLHvG5VmgnaQoH8u7ciczXQMUpGbwibjCpeuib6iajmrPiatepYemsj8As8iczmZVvGibWibfQp1gUP49rRMxIvYJ5bOib3YRsvrBqQ/640?wx_fmt=svg&from=appmsg)

两者相除：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4weUHwh47ySHedibWoVXG7yPEmpRzJnheZKYV8qibXB0tyuOgBFmtON8f1aWLK0oniaBaqu2Vu0VRzPBc7kZ21hJN9R0JMrU5PsqN0iaWIOk81rg/640?wx_fmt=svg&from=appmsg)

转子在这 1μs 里已经走过了大约 131 个 16 位 LSB。

所以“16 位”和“1μs”不能只放在同一张参数表里并排看。16 位回答的是角度被切得多细，1μs回答的是这个角度还新不新。

但这里还缺一个限定：这 1μs 的起点和终点是什么？是磁场变化到内部角度计算完成，是角度寄存器锁存到输出有效，还是芯片完成计算到 ABZ 边沿产生？如果还要经过 SPI、DMA 和 RTOS，主控真正拿到数据的时间又是另一件事。

没有边界定义的延时数字，不能直接拿去和另一颗芯片的内部传播延迟比较。

### AS5047P 的 90–110μs，不能直接和 1μs做100倍对比

AS5047P 公开资料里的 90–110μs，首先要看它描述的是哪一段。它更接近芯片内部的 core propagation delay，不等于主控从发出 SPI 命令到拿到数据的全部年龄。

AS5047P 的 DAEC 又是另一层含义。DAEC 会根据速度，对固定延时造成的角度滞后进行补偿。公开资料给出的补偿后延时是微秒级，但这个数字不能不加条件地套到所有输出链路，更不能直接当成 SPI 数据从采样到主控读取的总延时。

这也是 DAEC 最容易变成“障眼法”的地方：只做恒速角度误差测试时，补偿后的曲线可能漂亮得足以让人忽略原始延时；一旦进入速度闭环，问题就会从角度误差里露出来。速度环关心的是角度变化的相位和时间间隔，补偿器的速度估计带宽、加减速残差、处理延时抖动，都会重新进入环路。

这里至少要拆成三段：磁场变化到内部完成解算的时间，角度寄存器被锁存的时间，以及主控拿到完整数据的时间。

如果只拿 AS5047P 的 90–110μs 去除以另一颗芯片的 1μs，很容易得到一个漂亮的“100倍”结论，但这个比较未必处在同一个测量边界上。更合理的比较方式，是给每颗芯片画出同一条时间链：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5QzUTKYQozFGWq6kHqYJdPftbyfp9O6hQtS9KdRPImhDKiaDGghmCcOv81kVV1g0NJ79KJBia20EDkuhQYASZN4fBzqFkM31iawpR9MAIh1UbdA/640?wx_fmt=svg&from=appmsg)

真正进入控制环的，是这段数据年龄，而不是宣传页上孤立的一个 delay 数字。

### 恒速时补得漂亮，加减速时还要看残差

对于一个延时为 τ 的角度测量，真实位置差可以近似写成：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5O6wwtZIMShVyZCDZ3wjlaTrp3DtyeSwQbmWtJKtaia1mN2MkNqdk7wLPrBuDkpKmfUZVAGibichYiaq5Ih9LF3bAc8veXicib7DkJoicPlZVkvkgQg/640?wx_fmt=svg&from=appmsg)

第一项是速度造成的角度滞后，第二项就是加速度带来的动态残差。如果补偿器只使用当前速度，而速度估计本身又有误差，残差还会增加：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7H7FhcZzuM2pqXP9Re0yMwl30mhicHtIphrpy3qj5icSzT8PbcKPc7HeGiaIhW29XArbkAfibibIKO92sIyWB1HxibYoLgR4vNzicrsjlic6hm6HUoHg/640?wx_fmt=svg&from=appmsg)

这解释了一个现场里很常见的现象：匀速测试看起来很漂亮，启停、换向、加减速时角度却开始抖。

这不一定是磁铁突然变差，也不一定是 INL 在动态工况下突然变大。静态误差、固定延时、速度估计误差和加速度残差，本来就是不同的误差来源。

如果延时没有被补偿，高速下它直接变成角度：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4GDCeHQO1ictibiaYrzExkOF6XibhD5zGdXQNz5VBVvrx1dic5qDfPgqVYh4Z5mu6icHuQfhI0ibK9DM7QeAqGjYlXibnrVYJF6z3O1IOCZibHHFKoUqA/640?wx_fmt=svg&from=appmsg)

如果转子还有较高极对数，换算到电角度以后还要继续放大：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7z45gpuicvL3lMHLTq899iclPUHibAR5GjGLOFYjv0DjWiaH15Ekq0lvnibSw3BGjCCYxINMbc5Wia4GC9eeTnr7v8ibj6hyGhVYeV4n87tRvMkICqg/640?wx_fmt=svg&from=appmsg)

机械角看起来不到一度，到了换相和电流环里，可能已经是更大的电角滞后。

### ABZ 的 PPR、四倍频和 16 位，根本不是一回事

ABZ 是接口形式，PPR 是每转输出多少个周期，四倍频是接收端如何利用 A、B 两路边沿计数，16 位则是绝对角度编码的码值数量。

如果 A、B 每转输出 N 个周期，理想四倍频后的计数是：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5dnpFkhIaNt2bibG0Pw3JW9fRUibwVJnspYyVj3KVmMgzgL5hPzvbFZhBic3lycZN1EK1zJ8t40cAFCBIbAbLEI6vE5Gc2ic3oFecZLtRl2OOhNw/640?wx_fmt=svg&from=appmsg)

每个计数对应的机械角为：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5q5uWo2faSM2ticOhk7ydIGicv91dbvYibHDFHiayweR3NQdF1Y2rNYSzoYdUMJA2Y9JlE3MZXalq4CY9mwAiaM1sgaZpNtz38iaibQvG7sk0z2G9tQ/640?wx_fmt=svg&from=appmsg)

Z 相通常是一转一个索引脉冲，用于回零、校准或建立机械参考。它不是把 AB 两路再增加一个角度分辨率位。

所以不能写成“ABZ 也是 16 位”，也不能看到四倍频就把它等同于芯片内部的 16 位绝对角度。

ABZ 输出的是位置变化事件，绝对式接口输出的是某个测量时刻的角度状态。系统选择哪一种，取决于控制器需要边沿累计、同步锁存，还是直接读取绝对位置。

### 差分 ABZ 的价值，在线束和 PWM 旁边才真正显出来

在实验室里，一根短线接到示波器，单端 ABI 往往已经够用。但真实电机系统不是这样。编码器线束可能和 PWM、栅极驱动、电机制动线、母线电流采样线并行走线。

这时干扰往往不是干净的高频正弦，而是快速共模跳变、地电位差和边沿串扰叠在一起。差分 A、B 信号的价值，是让接收端可以利用两根线的相反变化，抵消一部分共模干扰。

但差分输出也不是自动免疫 EMI。现场仍然要看差分对是否成对走线、终端电阻是否匹配、接收端共模范围是否足够、屏蔽层接在哪一端，以及 PWM 回路和编码器回路是否形成大面积环路。

如果是 AB 相本身被干扰，通常表现为多边沿、少边沿或相位关系错误。如果是计数器、DMA 或软件读取时序出问题，波形可能完全正常，但最终位置已经错了。

### MTP 的真实价值，是给产线留一条返工路径

MTP 和 OTP 的差别，不能只写成“一个能改，一个不能改”。对磁编码器来说，磁体、气隙、芯片偏置、封装应力和装配误差叠在一起，最终参数往往要在接近成品状态下才能确定。

具备 MTP 的器件，可以把部分校准参数写入非易失存储，让芯片和具体磁体、具体装配状态匹配起来。它对量产的价值，是校准可以更靠近最终装配状态进行，返工时不必把整颗器件直接判废，校准结果也可以留下记录。

但是 MTP 不是无限修改的内存。量产要管写入次数、写入时序、掉电风险、数据锁定、读回校验和重新上电后的保持状态。

尤其不能把“写入动作完成”当成“参数已经可靠生效”。至少要做：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6qOceglOMSRvloQl9qiavnNnBibJOgWrW2JZYqkFlf8X8n2XDA5N9XokLhznzE9jGuRh2TfZKF4ibNc1icq9Oko3icwVo7XLpQWES6kW2FGtXHceg/640?wx_fmt=svg&from=appmsg)

如果校准表写错，芯片可能不会报通信错误，输出仍然是合法的角度数据，只是角度已经不属于真实转子位置。这类故障最难查，因为 CRC 可以全过，状态字也可以正常。

### 离轴不是打开几个 XY 参数就结束了

离轴安装时，传感器看到的 X、Y 信号通常会同时受到偏置、幅值不一致、正交误差、相位误差和磁场非线性的影响。

理想信号可以写成：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7p0aGulTfiaEGupYuArZlDzYKvtMhXVicPELOtG0gzvglQW0KZMzbfcib4s7CxFBWuMvsfQrCUtFZgyKCDfSIq8DbzehuTOXgEumrY6WbibHib2Cw/640?wx_fmt=svg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6sBDEiaW9edzQ7gC1SQ3VnRBWN8heCAMYx765ZGDvcEqR1GiaowMKhb9xqIcHcmLudE7orxk05dfWp9PoGSnMwh3IicVUH6fKhekk0bbJoa5ZPg/640?wx_fmt=svg&from=appmsg)

实际信号更接近：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIX8sEhNQL0AR5lHhfNiaGjicYKkHtHRwK8J6O6sNPavZdKXge0ZkTQ0GfsxCn9xRmc11REAWlXoahWV3xNrthLkKI16rFHGBoxDU/640?wx_fmt=png&from=appmsg)

圆心偏移、X/Y 增益不一致和正交误差，通常还能通过 offset、gain、phase 这类线性校准处理。画出来的 Lissajous 图可能是偏心、椭圆或倾斜椭圆。

但如果图形已经出现“蛋形”，就说明增益随输入幅度变化，问题进入了非线性区域。此时继续拧几个线性参数，往往只是把误差从一个角度区间推到另一个角度区间，需要多点校准、谐波补偿，或者从磁路、前端和 ADC 重新查误差来源。

离轴样机上调通一次，不代表换一批磁体、气隙变一点、芯片装偏一点以后，误差仍然能收回来。台架上看着还行，量产后却出现少数角度段突然变差，很多编码器项目就是在这里开始返工的。
