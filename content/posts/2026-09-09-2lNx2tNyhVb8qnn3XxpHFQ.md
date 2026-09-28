---
title: "机器转得越快反而越找不到家，回零信号被转速压薄了，Z_WIDTH 没变，Z 脉冲却缩了 8 倍：高速回零失败，我最后查的是这 2.44 µs"
date: 2026-09-09T10:20:00+08:00
slug: "2lNx2tNyhVb8qnn3XxpHFQ"
description: "九月初，实验室。小推车把一台伺服转台送进来，电机壳还留着点温度——跑了一整天才返修的。工单上客户只写了一行字："
original: "https://mp.weixin.qq.com/s/2lNx2tNyhVb8qnn3XxpHFQ"
---

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIWzgCgpsm4GgQBLDuicia2nFNZS2QUE4eBWAw3GZibz8M6q5lia0qOHr0buRHeAXiaJQeZoxhKRQZerrteeKzE9mjD9eX4aX9YpX6jI/640?wx_fmt=png&from=appmsg)

##

## 机器转得越快反而越找不到家，回零信号被转速压薄了，Z_WIDTH 没变，Z 脉冲却缩了 8 倍：高速回零失败，我最后查的是这 2.44 µs

九月初，实验室。小推车把一台伺服转台送进来，电机壳还留着点温度——跑了一整天才返修的。工单上客户只写了一行字：

**低速找零正常，3000 转偶尔找不到 Z。**

做位置传感芯片的，第一眼看这种字，手已经习惯往磁铁方向伸了。Z 点抖动、磁铁偏心、气隙、线缆、接地……这种"找 Z 偶发失败"的案子，我查出来过不止一桩。

但这次，客户在工单下面多跟了一句：

**"以前好的，换了高分辨率以后才开始。"**

就是这句话，让我把伸向磁铁的手收了回来，把上面那台转台上那颗昆泰芯 KTM5200 的配置读了出来。

读回来第一格：Z_WIDTH = 0x2。

干净，正常。

可我眼睛没停在这格上，滑到旁边——AB 分辨率，已经从 **1000 PPR 改成了 8192 PPR**。

心口一紧。

这种"值没变、底下的东西却变了"的坑，我踩过不止一次。寄存器只是个代号，它背后那个物理量，是跟着别的参数走的。配置 dump 一模一样，不代表它对应的世界一模一样。

我把这两个配置代进去，算了一遍。

同样的 0x2，同样 3000 转——原来 Z 有 **20 微秒**。

改成 8192 PPR 以后，只剩 **2.44 微秒**。

寄存器一个 bit 都没动。

窄了 **8.2 倍**。

我盯着屏幕上那个数，客户那句话又浮上来：**"以前好的，换了高分辨率以后才开始。"**

这一下，全对上了。

### 第一笔账就很容易算错：1000 PPR 不是一圈 1000 个 count

这类问题最容易踩坑的地方，不是公式。

是单位。

增量编码器里经常同时出现：

**PPR、line、pulse、count、step、LSB。**

这些词工程师天天说，但不同 datasheet 未必在说同一个东西。

KTM5200 的公开资料里，ABZ 支持最高 65,536 脉冲/圈；标准 AB 正交如果按四边沿计数，对应的 position count 是脉冲数的 4 倍。官方产品页也明确把 ABZ 能力写成 1～65,536 脉冲/圈。

也就是说，1000 PPR 的 A/B 信号，不是每圈只有 1000 个 quadrature count，而是：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIVlrtn43IY9u8sYlt2fOIm9Vgkg6e0m83iaKsNJSynu8kiagQ1PWCfcPByfOPhTfdI3Qib3kktmyialA50nTvicSlSrgjleRKibecianc/640?wx_fmt=png&from=appmsg)

所以 1000 PPR 对应：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6jR8hYVsyCIetyBQp8mcENnrW3OoqiamqD4QE9Mlo3cBuRDBCdnW4YkkrSpeB7LORaIGDCCGnUboQpTyl9nxHQo2YUpkdjhqpQz3cwfN7ePIA/640?wx_fmt=svg&from=appmsg)

如果 Z_WIDTH=0x2 对应 4 个 AB 计数 LSB，那么这个 Z 占的机械角不是：

"4 除以 1000"。

而是：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4Wdw79TdKXxKkkBlVB4nBuhSwUKKwA6W88DIq7hemq2FwxYU31DaYvOibTVJXBr1Qx4zZrcS84K0wadzqrzKdibKcgvNj7nEvu344ZQArnUqbQ/640?wx_fmt=svg&from=appmsg)

得到：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6720O4ia4Jtq47f1JibvM85Ce6DkRlfSGN6jVrWDP7TSeauZYtnOWKiabA3lYRJBm6KujCWgwwHmxLBrO0aBo8NBicrgcGGHWMxtgPxMEHsGKwNA/640?wx_fmt=svg&from=appmsg)

3000 rpm 时，一圈只要 20 ms。

于是 Z 在时间轴上的宽度就是：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5hxKibgM5W8qKl1mAd1YesMKDyemX71p2fictFnuiaTHrBx6iadPMeejb2MF1n0fpHE66DaRP0jU3AN0bXEBHuuK2GeIqptnssPD6vaxghh6MmVQ/640?wx_fmt=svg&from=appmsg)

这里时间单位是 ms。

结果：

**20 µs。**

这一笔如果把 PPR 直接当 count，会算成 80 µs。

差整整 4 倍。

所以看到 datasheet 里的"1 LSB"，我现在第一反应已经不是代公式，而是先问一句：

**这个 LSB，到底是哪一级的 LSB？**

### 然后把 1000 PPR 改成 8192 PPR

真正有意思的事情从这里开始。

客户提高反馈分辨率以后：

Z_WIDTH

没动。

还是：

0x2

只看 register dump，这一项甚至可以直接打勾：

**一致。**

但 8192 PPR 已经意味着：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4QdbtKHI3LMwCKqvqCxU3w1LntwJWQy3fthLZWeEXDSHWOD7dD7LHTXicUVudN0Is1WyeVphiaib5t1Zu430j1VqSsD1kjhzJZGElN4Zdfw1Dibg/640?wx_fmt=svg&from=appmsg)

所以：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6OBPpNBN5yrbMdjLJxN02RB4IQYSbcJYiadCsYuY2YE3R6shEDGWnRHPQGdsxxUZyYnTuP6UgGDJOgvRyhj0dHQOW8bDs9ffIMbibxqu9Fibv7Q/640?wx_fmt=svg&from=appmsg)

同样 4 个 count 的 Z，现在只占：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7H7FhcZzuM2sGGd8Q3FeRjvUFuDFdibHXy0YZuYNQHHahklqjicMwTXbGxY656zUgjehqRFibB6EADcNbcGuj8vVO3DrmaZTxNRXaE9ian6UetibA/640?wx_fmt=svg&from=appmsg)

得到大约：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6YcDIewgn1JnVQSSxoiaGs76bialB86ic9ujIehn1FWRB3ZU9zw27rWW42Ytiaf90fuvLs8OjlECVrM05ZJvourqyWmh9CKN9j9lwRIr1TjibX3WQ/640?wx_fmt=svg&from=appmsg)

转速仍然是 3000 rpm。

一圈仍然 20 ms。

所以：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5q5GhibPFqFtiaec03ACP3M7sJ131YtfToyZOXkdjIv5o1XL1U0QT7bibo0M2EVViaHt9D7k7tibibfiaBR9ic5ZFzibqWt4CBOypk66TldQXz5QLEf4A/640?wx_fmt=svg&from=appmsg)

结果只剩：

**2.44 µs。**

于是同一个：

Z_WIDTH = 0x2

在机器里经历了这么一个变化：

**20 µs → 2.44 µs**

差了 8.2 倍。

这才是我觉得这种故障最值得写的地方。

不是"参数设错了"。

参数根本没错。

**错的是把寄存器值当成了物理量。**

### 2.44 µs 到了驱动器输入端，问题就不再属于"编码器精度"

如果驱动器 Z 输入要求有效脉宽至少 10 µs，那么事情已经很简单了。

20 µs 还有余量。

2.44 µs 连门槛都够不到。

但这里有一句现场上经常听到的话，我觉得值得单独纠正：

>

光耦有几微秒延迟，所以 Z 被吃掉了。

不完全对。

如果一个器件对上升沿和下降沿施加完全相同的传播延迟，那么一个 2.44 µs 的脉冲进去，出来理论上仍然是 2.44 µs。

只是整体往后挪了。

**纯延迟不等于脉宽损失。**

真正会杀死这种窄脉冲的是接收链。

比如：

输入 RC；

光耦或者数字隔离器的带宽；

上升沿和下降沿传播时间不对称；

施密特输入阈值；

数字滤波；

FPGA 输入 qualification；

MCU 输入滤波；

控制器 minimum pulse width 判定。

所以我查这种问题，不会只拿示波器夹在编码器 Z 输出上。

我要看三层：

**编码器 Z 输出 → 隔离/输入电路后 → 控制器真正识别到的 Z。**

很可能第一层还有一个漂亮的 2.44 µs 方波。

到了最后一层：

什么都没有。

这时候再去调磁铁，没有意义。

### 为什么低速永远像是好的

这一点也可以直接从公式里看出来。

只要 Z_WIDTH 和 PPR 不变，Z 对应的机械角就是固定的。

转得越慢，它在时间轴上自然越宽。

把前面的式子合起来。

如果：

-

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5q5uWo2faSMibOrmxyznU2siaT8uX9nibfY6ddDCRAHCcob68cmDxX4aDjzdFyxicN9X69wT41ibQUZviaia3wJFY3ewq2yA1mLJHqfH9A8BILRVBGQ/640?wx_fmt=svg&from=appmsg)

 是 PPR；

-

k 是 Z 占的 quadrature count；

-

n 是 rpm；

那么 Z 脉宽为：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7jFDxrYlJGuTvLlko2nlYicAibZrLboiaoiauFKib7fe951zC5ibqjBW0b6yag8aoQ6dCMtZZn0wUjdxjicODqv5tn7tFx7V2g7YZic4ibUATtxptLAjw/640?wx_fmt=svg&from=appmsg)

结果单位是 µs。

对于 8192 PPR、4 count：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4Wdw79TdKXxBBEAySSpnvlmf0XT5fpAv7EfRCvM09QkynAxrDvNnkpM0Is8gCxeVlqzmcqZyH5HnL59BnibuIf5w7pyicM3vCpgIVyjlibS1BKA/640?wx_fmt=svg&from=appmsg)

如果接收端最低要求是 10 µs，那么临界转速约为：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6erialA0bCAibJ1LU7VhJaahL6bEMxhazq7QDtAcxbia1yzNM3Z7tBH3yBLHQ1xRLT1JFVfLktwZAtBE7IBrYic6Vo4ux04DDMJhkm8WVun69shg/640?wx_fmt=svg&from=appmsg)

这一下就把客户的现象解释通了。

300 rpm 调。

正常。

500 rpm 调。

还是正常。

七八百转以后开始进入边缘区。

3000 rpm：

**2.44 µs。**

所以所谓：

**"低速百分之百正常，高速偶发找不到零。"**

并不神秘。

它甚至未必是一个真正意义上的"偶发故障"。

只是某个本来按**角度格数**定义的东西，经过转速以后变成了一个**时间脉冲**。

而你的接收电路只认后者。

### 我现在看 Z_WIDTH，已经不会只看 0x2

以前核配置可能是这样的：

Z_WIDTH = 0x2

对。

下一项。

现在我会继续往下翻译。

0x2

是多少个 count？

当前是多少 PPR？

一个 count 对应多少机械角？

现在是多少 rpm？

最终 Z 到了接口上还有多少 µs？

驱动器允许的 minimum pulse width 又是多少？

做到最后，0x2 这个数字本身反而最不重要。

因为芯片里存的是：

**配置。**

机械系统运动的是：

**角度。**

驱动器输入端接收到的是：

**时间。**

这中间隔了两次单位变换。

很多配置坑，就藏在这两次变换里面。

### 还有一种特别容易误读的"180°"

KTM52 这类器件的 Z 宽度配置里，还会看到 60°、120°、180° 这样的值。

这种地方我现在不会直接看到"180°"就理解成：

**机械半圈。**

一定先看 waveform definition。

因为编码器资料里的"360°"至少可能指两种东西。

一种是机械一圈：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6Dqssclat6xUAgmDgDiac0jxrMcic9NftjhLWLzib4DHUib2eX13zGUktUxcrDEF3RkYZg5pe8NA8ooBFFG165yy7AroJRMwvibXkQIG4VSJmVXsQ/640?wx_fmt=svg&from=appmsg)

另一种是一个 A/B 电周期：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5EWRRVSAicibcJH1djtZjsrJKXpeBS2tOsRtOvjSpPcicITO10dJm8aEgv403dKhZiaNmdoQZia3MCPKYvynoiaOmD7mtET0VUsQgG5iap9013BmXRQ/640?wx_fmt=svg&from=appmsg)

符号完全一样。

物理意义差得非常远。

如果是后者，那么所谓 180° 只是一个 AB 周期的一半。

PPR 一提高，它对应的机械角一样会缩。

KTM5800 官方资料明确支持 1～65,536 线可编程 ABZ 输出，其产品定位本身就是多极输入细分器，因此看这类 Z 定义时，必须先确定"角度"处于机械域还是 AB 周期域。

所以碰到这种寄存器，我现在会先问一句：

**这个 360°，到底是哪一个 360°？**

这句话比直接背寄存器表有用。

### 所以高速找不到 Z，我现在先算 µs，再拆磁铁

以后再遇到：

低速回零正常；

高速偶尔丢 Z；

或者机器原来正常，提高 PPR 以后突然开始找不到零点——

我不会第一时间怀疑磁铁。

先拿三个东西：

Z_WIDTH

PPR

rpm

把它们一直换算到最后一个单位：

**µs。**

然后跟驱动器 minimum pulse width 比。

如果已经只有两三微秒，而接收端要求十微秒，这时候继续查 INL、磁铁偏心、气隙和滤波算法，方向已经错了。

这次真正把问题暴露出来的，不是一个写错的寄存器。

恰恰是一个：

**从头到尾都没有变过的 0x2。**

它没变。

PPR 变了。

rpm 一上去。

最后到驱动器眼里的那个 Z，已经完全不是原来的东西了。

### 公开来源

-

昆泰芯 KTM5200 公开产品页 / datasheet：ABZ 支持最高 65,536 脉冲/圈；标准 AB 正交按四边沿计数时，position count = 脉冲数 × 4（官方同时给出 65,536 脉冲/圈对应 262,144 步/圈）。

-

昆泰芯 KTM5800 公开手册 ABZ 章节：Z 的位置、宽度与 A/B 波形直接相关；ABZ 支持 1～65,536 线可编程，产品定位为多极输入细分器——Z 定义须结合 AB 输出周期（AB 周期域）理解，不能只看寄存器数值。
