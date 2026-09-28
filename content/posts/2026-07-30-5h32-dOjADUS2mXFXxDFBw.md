---
title: "磁编码器的 AGC 等信号削波了才降增益，就已经晚了屹晶微专利CN122306120A，让它在撞上 ADC 满量程之前就预判"
date: 2026-07-30T00:00:00+08:00
slug: "5h32-dOjADUS2mXFXxDFBw"
description: "屹晶微专利CN122306120A，让它在撞上 ADC 满量程之前就预判"
original: "https://mp.weixin.qq.com/s/5h32-dOjADUS2mXFXxDFBw"
---

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIW8qyibxicCa9mh6Kl6kU7KgL0qsoDtD1M0294U3ctwvcX3ufkVX9SCcg4vLE5pne0avHJ2lZw71IDpBzo4QtdiazQ50VmrhnnbGU/640?wx_fmt=png&from=appmsg)

编码器 · 位置反馈 · 芯片

## 磁编码器的 AGC 等信号削波了才降增益，就已经晚了

屹晶微专利CN122306120A，让它在撞上 ADC 满量程之前就预判

磁编码器真正怕的，不是信号幅值小一点，而是 sin/cos 信号碰到 ADC 满量程后被削平。传统 AGC 往往等“超标”才降增益，但对高速伺服来说，这时坏角度已经流出去了。

### 一个“反应慢半拍”的老毛病

磁编码器的角度，是从一对正交的 sin/cos 信号里用 **atan2**解出来的。

这对信号的幅值，取决于传感器和磁铁之间那点气隙处的磁通密度。而气隙并不是恒定的：装配公差、磁铁温漂、结构振动，都会让信号幅值慢慢偏离出厂标定值。

幅值小一点，通常还能通过归一化继续算角度；但幅值一旦大到超过 ADC 满量程，峰顶就会被削平。sin/cos 不再是同步缩放，而是被非线性砍掉一块，最终让 atan2 的比值失真，角度里冒出明显的谐波和尖刺。

AGC 的真正目的，不是把幅值调得漂亮，而是绝不让信号碰到 ADC 的轨。

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIVVsYXECKroGKhrpNxpt8d4datcw8wQkgicsEw9icAia9PICnkWmV82VOcvZ1eiamPxEp2JhYrzKNFvJPaaFmUdEgwjdicR2GBwYz4A/640?wx_fmt=png&from=appmsg)

### 传统 AGC 的病：它是“事后诸葛亮”

传统 AGC 的逻辑很直接：检测到幅值超标，就降增益。问题出在“检测到”这三个字。

等芯片确认幅值已经越过阈值，甚至已经削波时，那几个坏采样点早就送进 atan2，算成了错误角度。普通低速系统可能只看到一两个小毛刺，但高速伺服里，几个采样周期的角度跳变就可能带来换相错误、电流冲击，甚至触发过流保护。

现场表现往往是电机突然报故障、停机，但坏数据只持续几十微秒，普通示波器触发未必能抓住。于是故障看起来像“偶发”，实际上是 AGC 动手得太晚。

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIXibOW4TIG5mkwQoiciaRYuuguLw0rLknzzhUVUUDIX6YqM3lqiahwiaqmxDEoWVSqbj3cSTLXtrAnhOGyJICI7SweR6B2kubLTg6fY/640?wx_fmt=png&from=appmsg)

### 屹晶微的做法：预测 + 稳定区间

#### 第一层：前瞻评估

这套思路不只看当前幅值，还持续跟踪幅值变化趋势和历史极值。当信号同时满足“接近历史极值”和“还在继续上涨”两个条件时，就提前判断它正在冲向饱和，于是先把 PGA 增益降下来。

关键不在于“幅值大”，而在于“幅值大，而且还在涨”。稳态下信号长期处在量程 80%，并不一定需要降增益；只有它继续朝满量程逼近，才真正需要动作。

#### 第二层：稳定区间

AGC 如果只盯着一个目标值，信号在目标附近稍微波动，增益档就容易反复上跳下跳。每一次增益切换，都会给 sin/cos 信号链带来瞬态，最终在角度输出上留下尖刺。

因此再设置一个上下阈值区间：幅值只要留在区间内，增益就保持不动；只有真正冲出区间，才重新调节。

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIVeVrib8icbxhibbqgcnjc716x8ibVrcnvXl5FeDaBljfggEcOcVdvSArEfL0SgtdLpg87raPv4C5Xjiceic7sRCur0wgL69gkqNBRrs/640?wx_fmt=png&from=appmsg)

### 翻译成信号链语言

atan2 本质上看的是 sin 和 cos 的比例关系。只要两路信号被同一个增益同步放大或缩小，比例不变，角度理论上也不变。

真正破坏角度的，是削波。削波不是“幅值变大”，而是波形的一部分被硬生生截掉，导致比例关系被破坏，误差不再能靠归一化消除。

预测层解决“动作太晚”，死区解决“动作太频繁”。两者缺一不可。

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIWZ9X0U7asTw6VibZVjyE9NTSxgcwQXtLW07TnSuFicSvWG02y4devjnKE1pLvaBk9iakoibibN2XFBNibqBKKA1IVvy1FJ37lPn2joY/640?wx_fmt=png&from=appmsg)

### 代价与边界

**历史极值需要建立。**上电初期或工况突变时，历史记忆还不充分，预测能力会打折。

**趋势判断存在窗口权衡。**采样点太少，趋势判断容易受噪声干扰；采样点太多，又会引入额外延迟。

**它只解决幅值饱和。**偏心、温漂、磁场谐波、结构误差，仍需其它校准机制处理。

**死区宽度需要取舍。**太窄会抖，太宽会迟钝，本质上是在跟踪速度与稳定性之间做交换。

### 给做编码器的人的启发

快系统里，事后反应和事前预判不是“优化一点”，而是本质差别。任何阈值保护都应该追问：等检测到越界时，坏数据是不是已经流出去了？

如果答案是“是”，触发条件就应该从“已经越界”提前到“正在冲向越界”，也就是趋势判断加安全裕量。

同时，任何自动调节环只要在目标值附近频繁动作，就应该考虑加死区。它牺牲一点跟踪精度，却往往能换来更干净、更稳定的控制输出。

**边界说明**

CN122306120A 为公开申请，尚未授权。本文讨论的是公开申请中的技术思路与磁编码器信号链机理，不构成法律意见。

文中关于削波、同步缩放、atan2 比值失真、死区防抖等内容，属于磁编码器信号链的通用工程解释。
