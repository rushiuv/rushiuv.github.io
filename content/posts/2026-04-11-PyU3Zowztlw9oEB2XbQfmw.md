---
title: "深度解析 ENX 22 EMT：瑞士maxon真正解决的，不是精度，而是电机旁边测得准、断电以后记得住"
date: 2026-04-11T00:01:00+08:00
slug: "PyU3Zowztlw9oEB2XbQfmw"
description: "很多人会把 ENX 22 EMT 理解成“一颗高端编码器芯片”。这其实不准。更准确的理解是：它是一套小型位置子系统。因为一套模块如果同时做到单圈 17 位、多圈 16 位、断电记圈、SSI/BiSS 差分输出，而且还能塞进 22 mm 这一…"
original: "https://mp.weixin.qq.com/s/PyU3Zowztlw9oEB2XbQfmw"
---

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIU89sWuMwBXibVTP4YSbd5mGoG7EyJacLCa5XodDJTuicPibwPicMzvcIlk8FibI2D72GgbBiak20x8FONVWJ3BDHIHzjyiaZrmkA4We4/640?wx_fmt=png&from=appmsg)

很多人会把 ENX 22 EMT 理解成“一颗高端编码器芯片”。这其实不准。更准确的理解是：它是一套小型位置子系统。因为一套模块如果同时做到单圈 17 位、多圈 16 位、断电记圈、SSI/BiSS 差分输出，而且还能塞进 22 mm 这一类小型系统里，它内部大概率不可能只靠一颗单芯片硬扛，而是至少拆成三层：第一层负责单圈测角，第二层负责 Wiegand 取能与多圈记忆，第三层负责把单圈和多圈数据封装后通过 SSI/BiSS 输出给控制器。maxon 自己对外卖的也是模块，而不是裸芯片，甚至明确写了这类传感器“只能作为组合件的一部分购买”。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DBrlpXS1RIXJ3zx22MyiaotyMmqswL4FGnP3ILlClpjeX5zsCTgp56wyYF0P705wibBCkArfTmISVWG81DdvB0tOYuq2blxO6QOywDWiclmH5Y/640?wx_fmt=jpeg)

真正关键的是第二层。因为这层决定的不是“这一刻角度精度”，而是系统掉电之后会不会失忆。iC-PMX 之所以最像 maxon 这类方案的心脏，不是因为它名字里带“encoder”，而是因为它公开给出的功能就是这套问题的标准答案：Wiegand 脉冲取能、无电池无齿轮计圈、方向检测、外接非易失存储器、还能给上层微控制器交换数据。更重要的是，iC-Haus 甚至还公开了一颗与它配套的 iC-RMF，直接写明是给 iC-PMX 这种取能式多圈计数器配套的 FRAM 存储器。也就是说，iC-PMX + iC-RMF这组组合，本身就是行业里一条非常清晰的“无电池多圈模块”技术血统。

这里面有个特别容易被忽略的技术点：iC-PMX 不是单纯的“记圈器”，它自己还带 4 路低噪声霍尔差分模拟输出。这个信息很关键，因为它说明它并不只是站在单圈角度芯片旁边打辅助，它本身就长在“磁式单圈 + 无电池多圈”的交界处。也正因为这样，我才会说它最像 ENX 22 EMT 模块里真正的核心芯片。当然，这里还是要把边界说死：公开资料只能支持“高概率像”，不能支持“百分之百就是”。

## 如果真把 maxon 模块拆开看

## 最可能不是“一颗神芯片”

## 而是“1+1+1”的系统搭法

所以我更倾向于这样理解 ENX 22 EMT：

第一块，是单圈角度前端，负责把这一圈里的绝对位置做出来；

第二块，是Wiegand 取能多圈管理芯片，负责断电记圈；

第三块，是接口和协议输出层，把单圈与多圈整合后，通过 SSI/BiSS 差分送出去。

这也是为什么我不建议把 ENX 22 EMT 简化成“某颗芯片很厉害”。它真正厉害的地方，是它把单圈精细测量和掉电不失忆这两件事拆开做，再用一个小模块把它们重新缝合起来。前者解决的是“这一刻位置对不对”，后者解决的是“掉电回来我还认不认识自己”。在机器人现场，后者往往比前者更贵，因为它直接决定维护、搬运、断电检修后的恢复时间和风险。

## 如果把 maxon 这套思路横着展开

## 哪些国产芯片最有资格塞进这种模块里

这里就要把问题分清楚。国内现在并不缺“单圈角度芯片”，真正缺的是“像 iC-PMX 这种把 Wiegand 取能、多圈计数、掉电写存储、状态同步做成一颗专用芯片”的那一层。换句话说，国产要复刻 ENX 22 EMT，不是先缺单圈，而是先缺无电池多圈架构芯片。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIUx6t4pSVaWica7dgEYyMUz3FBib4ia2vqKO3v0JWxicncH5qXxicwoJzN64EquhE8iaiah7NOkf064TgPSrS8t2eR7dW7JVsb5u4rGxc/640?wx_fmt=png&from=appmsg)

但如果只看单圈前端，其实国内已经有不少能打的芯片可以拿来做这套模块的“前半身”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIXicfdGOCmaEUhFgQfQSMfEEdHqYSyibX57Zn9Wq6tVgib9DUJtb1bRttArd7zbZibQbfH2f2OFIb0BDibFCqaFLC2xtaAmH0PZf3OE/640?wx_fmt=png&from=appmsg)

先看昆泰芯。KTH78 系列是 16 位霍尔绝对角度编码器，支持 SPI、SSI、ABZ、UVW、PWM，系统延时 1 微秒，最高转速 120000 rpm，还带磁场诊断/报警。这类芯片的优势很明显：接口齐、延时低、落地快，很适合做 maxon 这类模块里的单圈层。它欠缺的不是角度本身，而是掉电不失忆这一层目前没有公开的一体化方案。

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIUA36Jso3XvrmtFtdPRRApsntNpqYhVDToEH0rh8IRumye1HMUZ9awRWgcUGQEzwgFCvPB7pl7s88wlCCLwXXojSYPVaL6WUOM/640?wx_fmt=png&from=appmsg)

再看多维。TMR3111 这颗芯片非常值得重视。官方给的是 23 位绝对位置信息读取能力，SPI/ABZ/PWM 输出，转速到 40000 rpm，角度输出延迟小于 2 微秒，还带自校准和 EEPROM，可做对轴与离轴。它本质上已经很接近“高端单圈前端”的样子。TMR3108 也有 17 位高速绝对角度输出，带 SPI、ABZ、UVW/PWM 配置和自校准。多维这条线的特点是：前端很强，尤其适合把单圈做漂亮；但从公开资料看，它还没有把 Wiegand 取能多圈这层做成像 iC-PMX 那样的专用芯片。

![](https://mmbiz.qpic.cn/mmbiz_jpg/DBrlpXS1RIUhEd1RhNiaez8v3V1C0ic21y2wCZFiaib2KaVZDBkBX8SuDLLRIDibNpPqYnlDMzUWiajhBhxaueEiaRYsiaDdqSicAXEqrFYMOkURc6jw/640?wx_fmt=jpeg)

麦歌恩这边，要分两条看。一条是 MT6835，它官方直接定位在“通用伺服控制”“17 位绝对值伺服电机控制”这类场景，说明它瞄准的是高性能单圈绝对值编码。另一条更有意思的是 MT6701，它走的是差分霍尔思路，官方明确强调它天然抗外部磁场干扰，还给了 SSI 接口、状态位和 CRC，而且专门把直流无刷舵机、机器人关节写成应用场景。这个产品很值得注意，因为它在逻辑上跟 maxon 的 ENX MILE 有一点共鸣：不是先追求最漂亮的纸面噪声，而是先解决“电机旁边能不能测得还算干净”这个问题。不过，它依然主要停留在单圈与抗干扰层，离 ENX 22 EMT 这种无电池多圈记忆模块还有一层没补。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIUWd4PEcYVy96UyvYVQgEnhIZpYPFVAaPTcrVnHjcPXHQlgeluK40Q8ApSWcoCSuIENOHwsRUaKKn1iczFQUCqY0NUphRibv2Z9Q/640?wx_fmt=png&from=appmsg)

MPS 这边最像“可塞进 maxon 模块前半身”的，其实不是整套多圈方案，而是高性能单圈前端。比如 MAQ600 这类产品，官方给的是 TMR 传感器、高带宽、高精度、支持 SPI/SSI，系统校准后 INL 可以做到 0.1° 以内，封装 3×3 mm；如果更看重靠近电机的杂散场环境，那它 2024 目录里的 MagDiff 家族，比如 MA900、MAQ79010，更明确强调对寄生杂散磁场的鲁棒性，接口里已经给到 SPI、SSI、ABZ、UVW 等。MPS 这条线的强项是把单圈前端做成高带宽、高精度、甚至带杂散场鲁棒性；但从公开资料看，它并没有公开一颗对应 iC-PMX 这种“Wiegand 多圈管理芯片”。所以如果用 MPS 来拼 ENX 22 EMT，最现实的方式也还是“单圈 MPS + 外部 Wiegand 多圈层 + 存储/协议层”。

## 如果只看“能不能复刻 maxon 模块”

## 真正的短板不是角度芯片，而是这四层

把这些芯片横向放在一起看，你会发现一个很现实的结论：国内现在最不缺的是“把单圈角度做出来”的芯片，最缺的是把它做成“断电不失忆的系统模块”的那一层。

真正要国产化 ENX 22 EMT 这种模块，重点不是只盯单圈前端，而是要补齐下面四件事。

第一，是Wiegand 脉冲取能和稳定计圈。这不是普通 MCU 加几行代码就能替代的，因为它面对的是极短脉冲、极低能量和掉电边沿。iC-PMX 这类芯片的价值，就在于它把这些边界情况吃掉了。

第二，是低能耗、掉电脉冲友好的非易失存储链路。iC-Haus 连配套 FRAM 都给出来了，说明这不是小配角，而是架构核心。因为你不只是要“记圈”，你还要在能量极不宽裕的瞬间安全落盘，而且不能把圈数写坏。

第三，是单圈和多圈的同步状态机。这一层很少有人写，但实际上最容易出坑。因为系统不是只要知道“这圈里几度”和“总共几圈”两个数字，而是要确保两者在掉电、反转、抖动、慢速、小幅往返这些边界情况下仍然能对上。对机器人来说，这一层如果不同步，恢复位置时就会出鬼。

第四，是最后的工业接口和诊断层。ENX 22 EMT 对外不是吐一个原始角度，而是模块级 SSI/BiSS 差分输出。这说明 maxon 卖的并不是“传感器裸能力”，而是“控制器能直接接进去用”的完整接口能力。这个层面看着不像核心，其实决定了模块能不能被整机厂真正拿去量产。

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIUibrIBiaiarocsqPuQ6uDj49B683xwxdD92gYwrjVBtiamvYCM1sgxVo8BibTTmtEF2AtNsK5AkQSjfJaSqBIa1zibIErJq5s2yGLtg/640?wx_fmt=png&from=appmsg)

## 不得不说：maxon 模块的价值

## 不是“精度更高”，而是“记忆更可靠”

所以这件事最后还是要回到你最想写的那个核心点：编码器的价值，越来越不只是角度本身，而是系统在最狼狈的时候，能不能还知道自己是谁。

maxon 这套模块当然有它一贯的可靠性、集成度和工业气质，这些都可以顺带提。但真正该下刀的地方不是“瑞士做得精”，而是：它把单圈测角和掉电记忆这两个原本常常被拆开的工程问题，塞进了一个很小的模块里。这样做的后果是，维护、断电、搬运、手动旋转之后，系统不用重新“找自己”，而是马上就知道自己在第几圈、现在在哪里。

这也是国产化最该盯的方向。不是再比谁多一位分辨率，而是尽快补出一颗类似iC-PMX这种层级的“无电池多圈管理芯片”，再把昆泰芯 KTH78、多维 TMR3111/TMR3108、麦歌恩 MT6835/MT6701、MPS 的 MAQ600 或 MA900 这一类单圈前端拼进去。到那时，国内才算真正从“会做角度芯片”，走到“会做系统级编码器模块”。

如果非要把这篇压成一句最狠的话，我会这么写：

maxon 这类模块真正贵的，不是角度算得多漂亮，而是掉电以后它仍然记得你是谁。国产现在最该补的，不是再多卷一位分辨率，而是把这层“系统记忆”做成芯片。

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIVsmeYSia6wnQk4EQNZopkaQXSH8Mdd5DGQOVM211y0LDv26EAl7UIxkqQsiaZV0Nh4XLIyQ4lQEibthOW89C9oA6ias93dOSoicQ60/640?wx_fmt=png&from=appmsg)
