---
title: "同批两颗 KTM5900、共用一张温补表，一颗到 100°C 就 ＂过期＂ 了"
date: 2026-07-17T00:00:00+08:00
slug: "4Zp5zcvpo8f2D4k1rMlG-w"
description: "MAGNETIC ENCODER / CALIBRATION LABEL"
original: "https://mp.weixin.qq.com/s/4Zp5zcvpo8f2D4k1rMlG-w"
---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIX14qduyb76NHW6Kv9sf4Wy3Wh5onPmkGqZrtUKoAVBAiaPMSJOpkNvZ3Ffd3gRjYdRTulLicnwKS3ObfQoqAoT4owkYjKDbyRp8/640?wx_fmt=png&from=appmsg)

|

MAGNETIC ENCODER / CALIBRATION LABEL

 |

HANDLE WITH DATA

 |

## 同批两颗 KTM5900、共用一张温补表，一颗到 100°C 就 "过期" 了

| LOT / 批次
SAME BATCH | CAL. TABLE / 补偿表
SAME TABLE |

已过期 · CALIBRATION EXPIRED

两颗编码器，同一批次的 KTM5900，同一张温度补偿表。

一颗零下四十度照样干活；另一颗刚上到一百度，就偏了半度。

芯片一样。磁铁一样。补偿表一样。

我在测试台前盯着这两条曲线，追了三天。最后把两台拆开——差的只是 **联轴器型号**。

那一刻我才想明白：厂家给的那张温度补偿表，**少了一列**。

|

温度

 |

补偿值

 |

有效期

 |
|

−40°C

 |

CAL −0.12°

 |

缺失

 |
|

+25°C

 |

CAL +0.00°

 |

缺失

 |
|

+100°C

 |

CAL +0.48°

 |

缺失

 |

那一列，叫「保质期」

01 / TWO ACCOUNTS

### 温漂不是一种东西，
是两笔方向相反的账。

我们平时张口就说"温漂"，其实把可逆和不可逆混在一起。厂家那张补偿表，只修得了其中一笔。

|

可逆

温度回来，误差也回来
像橡皮筋，有来有回

✓ 补偿表能补

 |

不可逆

温度回来，误差却留个抬升
退磁 / 应力 / 松动，回不去

✗ 越补越乱

 |

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIWyqtrTia5PUfXib2rC0Tp3VY9TsgHHuxUHfqnqWSMp4kdwrG3nGIpb7pqw4WgXvEst8T3SOUN8DHP2poS7VU6q5ZJI11q93j1T0/640?wx_fmt=png&from=appmsg)

把一次温度循环后的残余误差拆开，大概长这样：

|

ε(T,t) = fcomp(T)
可逆 · 能补

 |

＋ Σ Δirr,k
不可逆 · 逐次累加

 |

补偿表只抵消前面那项。后面那项每超一次温就叠一点——**今天标好的表，明天磁体又老化一点，就对不上了**。

不可逆基线抬升不是唯一变量，热膨胀不同步、偏心放大、封装应力都掺一脚；但在我追的这几台里，它权重最大。

02 / MECHANICAL AMPLIFIER

### 最想不到的放大源，
藏在芯片外面。

回到开头那两台。差别在联轴器，不是玄学。联轴器受热膨胀，把编码器和轴之间的 **偏心** 顶大一点；而离轴磁编码器恰恰对偏心极其敏感。

同一台样机，**其他都不动、只换联轴器**，结果是这样：

|

83%

125°C 高温当下
平均偏移直接降这么多

 |

91%

回到 25°C 后
那条不可逆尾巴也被按住

 |

**同一颗芯片、同一张补偿表，只因为夹它的那个联轴器换了，保质期就差出一个数量级。**

03 / PRE-AGING

### 退磁预老化的温度，
直接定了保质期。

磁体的不可逆退磁，得在出厂前用高温预老化"榨干"。关键是温度选多少。我见过一个很自然的选法：工况 125°C，那拿 100°C 差不多吧。

不够。

|

+0.087°

100°C 预老化用于 125°C，
第一个温度循环就留下的不可逆抬升

 |

3.1×

是 130°C 预老化
样品的约 3.1 倍

 |

0.087° 听着小，但它是 **不可逆** 的、第一循环就冒出来的，后面每超一次温还会继续加。对一个 ±0.1° 的关节，光这一项就吃掉大半裕量。

T预老化 ≥ Tmax,work + (10~20)°C

| 1

先压不可逆

 | 2

再补可逆

 |

顺序反了，你标定得再漂亮，明天都会过期。这句话规格书不写，它藏在良率里。

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIWTYoZETeBnMhgBFfNUF4xBlXh7tIO3Hh6ZVG0KlsKscx92XdUnXS5Z3UBrXNsD1bXOX5hRFHBpicybuaTrbW1uvdSjEA6ynUuo/640?wx_fmt=png&from=appmsg)

04 / MASS PRODUCTION

### 从一百台到十万台，
这件事会变味。

试制就几十上百台，每台手工标定，一台一张表，管几个月没问题。不可逆那点账，藏在"反正每台都单独校过"里，看不出来。

|

一百台

每台手工标定

 |

→

 |

十万台

共用一张表？

 |

量产十万台，你没法给每台单独扫全温。可 **联轴器扭矩有离散、磁铁有批次差异、炉温有梯度**——每台的"不可逆底子"都不一样。共用一张补偿表，等于假设它们的保质期一样长。

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIUZqLjLECX0l30KZLBT5XqXLXlwGlBkiaRycUib2D0FS2LIp208R8rqzibGFkibiadCWUfa1DlvEOJjJpUQKic89vmseiaoE3UGyTJBKc/640?wx_fmt=png&from=appmsg)

验收要守的不是"每台都能打到 ±0.1°"——是"十万台里最差的那一台，能不能打到"。

05 / TAKEAWAY

出厂校准不是一次配置、终身有效；它是一支 **有保质期的耗材**，保质期长短，由你出厂前对不可逆温漂的处理决定。

这不是哪颗芯片精度不行——KTM5900 的静态指标很能打。是我们太习惯把"补偿曲线"当成一劳永逸，少想了"它只对可逆项有效"这一层。所以下次多做两件事：

**选型 / 来料，问一句**：这颗编码器的磁体做过多高温度的退磁预老化？够不够你最高工况再 +10~20°C？

**验收 / 量产，记一列**：除了常温精度，把"高温循环后的回温残余"单独记下来——那一列，才是你补偿表保质期的真实读数。

PRECISION HAS AN EXPIRY DATE

精度，是有保质期的

— 知识卡片 —

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIVdjyVXwNXaI7IONdTFuSgK1F9EsSuia10W9FqGqqFicBc9NNIs4XRdscichyoEpPC5Vsvr3m3mey4nyrU89PVZzPyglRYCJl0wdw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIWo3WyiaFGMIeQheMDleDxLdlkO84gJtCibT4MmnqjUaKUtF3zOt7RKFAyjwKiaWfdBGqsDpWNrthxlLULAUyl8MsHrcpVcbCuQo0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIUcQMX0pkx9VOiaenMfwuicplKz4PMqOG9PU3ibrzx4zcJDrhsWjHyTicBDheKBeX9ITgRVOKggUV010QskCHoHgibYdfb9hbtf599o/640?wx_fmt=png&from=appmsg)

微信公众号｜如是有为 · KTM5900 温度校准手记
