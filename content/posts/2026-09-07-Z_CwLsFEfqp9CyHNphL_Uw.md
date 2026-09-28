---
title: "美敦力7亿美元投康诺思腾，手术机器人最难测的不是力，是把机器自己的力扣掉"
date: 2026-09-07T11:21:00+08:00
slug: "Z_CwLsFEfqp9CyHNphL_Uw"
description: "9 月 1 日，美敦力宣布向康诺思腾战略投资约 7 亿美元，并获得 Sentire 手术机器人在美国以外部分已获批市场的分销权。"
original: "https://mp.weixin.qq.com/s/Z_CwLsFEfqp9CyHNphL_Uw"
---

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIVLUT8Zqibn0oVia2tQrprMrUUhjpQKUoqR5hNetBpPKWHZiaGXOTOUibSaIia6wlhsUO13kpILbe5EdiapeOJHyA1uuH6jZhvJdIibng/640?wx_fmt=png&from=appmsg)

## 美敦力7亿美元投康诺思腾，手术机器人最难测的不是力，是把机器自己的力扣掉

9 月 1 日，美敦力宣布向康诺思腾战略投资约 **7 亿美元**，并获得 Sentire 手术机器人在美国以外部分已获批市场的分销权。

这里先把几个容易写错的事实钉死：康诺思腾是**创立并总部位于香港**的手术机器人公司，在深圳等地设有研发和产业布局；Sentire 2024 年获得中国 NMPA 批准，2026 年 5 月又获得欧盟 CE Mark 和新加坡 HSA 批准。美敦力自己的 Hugo 已经进入全球 35 个以上国家，2025 年 12 月获得美国 FDA 泌尿外科适应证许可，美敦力预计其全球累计手术量将在**公司本财年结束前**超过 5 万例——不是“2026 年底”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIXSlJ0gdwDRkSrQpKhcd9dm0TmGNNdCf8UCxSQd5x65NydXWzDibQrWard8ACXWAp56cAPsm8WKtKwsXwWN645374icQAa3cicryw/640?wx_fmt=png&from=appmsg)

我做磁传感器和编码器，看这种新闻习惯先跳过融资数字，去找机械臂到底怎么感知。

但开始这篇文章前, 有件事必须先说清楚：

>

**目前我没有在美敦力和康诺思腾的公开材料里找到足够证据，证明 Hugo 或 Sentire 具体采用了哪一种末端力传感方案。**

所以这篇不猜 Sentire 里面装了什么，也不猜 Hugo 有没有某个隐藏算法。

真正值得挖的是另一个问题：

**一台手术机器人，到底怎样知道自己夹在组织上的那几牛顿力？**

答案比“装一颗力传感器”麻烦得多。

### 01电机电流测到的从来不是“组织力”

先看最容易想到的一条路线。

伺服电机的输出转矩，在一定工作区间里可以从电流估：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM543JMpg1RUJms43dzsgOyrmHXA73UicbXw1C3nVDOkX5dtAbsDfqmvnWHQ2Im31dA3ck2WwtQF8clRvlb6oroH1tj9KI1GYo64kHYqbVjgg8A/640?wx_fmt=svg&from=appmsg)

于是很容易产生一个想法：

电流都知道了，电机出了多大力矩也知道了，再通过机械传动关系，不就能算出钳尖用了多大力？

真正做控制的人看到这里，麻烦才刚刚开始。

因为电机输出的那一份转矩，并不是全部送到了病人的组织上。

它首先要养活整条机械传动链。

可以粗略地把这笔账写成：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4rGuDF35Eoia4pPJHfRClPn2T7B95BWOSiav3AcLyicibHKRHEN9ibRWIJOC48wDgOcRZgkRMuetXnNtG5npbWsiaCLQmt5KWfkBRPhwUmmUrzdRsw/640?wx_fmt=svg&from=appmsg)

其中真正想知道的只有第一项，也就是组织作用在器械上的那部分。

剩下的是什么？

钢丝绳、滑轮、齿轮、轴承的摩擦；传动件弹性变形；回差；惯量；重力；钢丝绳预紧；器械腕部运动产生的耦合；滞回；trocar 穿刺器与器械杆之间的接触力；甚至同一把器械使用次数增加之后机械特性的变化。

所以真正的软件并不是在做：

**电流 → 力。**

而是在做：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM728rcRkicd0QIFSyTpetf7FQNRMfubcLNickRnfibXu154ruIzeAPbTCv6X1ueVlibck0NEqsMfaiaWEFMRtdk0ml8mANbEzItialb7KpTDauyvibXQ/640?wx_fmt=svg&from=appmsg)

最后才通过机构的运动学和雅可比关系，把关节侧扰动力矩映射到器械端：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5uymiaX8wy72XIsl1vE2GNzF9qibiac078KwicPsUfZ1bmjdnXBptoNZMw4hiacrcahXYoHtiatyiaVCZat7MNchkMTGPnCVa4a2kV5gTibrwkkp3Svw/640?wx_fmt=svg&from=appmsg)

这时候问题的性质已经完全变了。

**不是“电流测得准不准”，而是你能不能把机器自己消耗掉的那部分力，从总负载里扣干净。**

一篇针对机器人辅助微创手术力感知的系统综述，把这件事情画得很直白：model-based sensorless 方案可以利用机器人本身已有的编码器、电机电流等信号，但它最严重的误差源恰恰就是 drivetrain friction、elasticity/backlash、drive-train actuation、instrument inertia/gravity 和 instrument behavior variation。论文还特别指出，工具随时间发生变化，会使最初标定出来的模型逐渐失准。

这跟做编码器有一点很像。

ADC 位数做到 18 bit，并不意味着角度就有 18 bit 精度。

同样，电机电流测得非常准，也不意味着组织力就知道得非常准。

>

**你测准的是总账，但医生想知道的是其中一笔子账。**

### 02所以最干净的办法，其实就是往钳尖走

如果能把力传感器直接放到器械最靠近组织的位置，这道减法一下会简单很多。

那篇系统综述把传感器可能摆放的位置从后往前列了一遍：instrument interface、instrument base、proximal shaft、actuation cable、trocar、distal shaft、articulated wrist，一直到 **gripper jaw**。

它给出的结论非常值得注意：

**传感器放在 gripper jaw，得到的力读数最准确。**

原因一点都不神秘。

因为这时传感器已经越过了大部分传动链。

钢丝绳前面怎么摩擦、减速机构怎么滞回、电机轴承吃掉多少转矩，都很难再混进真正的组织接触力里。

从测量学上说，这是最舒服的位置。

从产品工程上说，却几乎是最难受的位置。

### 03越接近真正要测的力，传感器活得越惨

手术钳尖不是“装不进传感器”。

这句话不能写。

研究界已经做过很多 gripper jaw、articulated wrist、distal shaft 甚至更靠近末端的力传感器。

>

真正的问题是：**越往末端走，传感信号越纯，但传感器受到的工程约束越残酷。**

首先是体积。

钳尖本身已经塞着夹持结构、腕部自由度、钢丝绳或其他传动件；如果还涉及单双极电凝，又有新的电气结构要求。力传感器不仅要放进去，还得保留足够机械强度和刚度。

其次是封装。

综述直接评价，gripper jaw 上的传感器最难 fabrication、packaging、mount 和 shielding，电子学通常还不能直接贴着换能器放，于是长距离引线又会把信噪比拉下来。

再往下才是我觉得真正让普通传感器工程师头大的东西——**灭菌。**

综述列出的典型蒸汽灭菌条件是：

**120–135°C、约 207 kPa、100% 湿度，持续 15–30 分钟。**

这不是简单做一轮高温存储实验。

换能结构、粘接剂、wire bonding、绝缘层、coating、signal conditioning electronics，都得反复经历这套环境。论文明确指出，这种环境可能破坏换能器、调理电子学、导线绝缘、粘接和涂层。

还没完。

靠近病人体内，就有湿度和液体侵入、绝缘、电磁干扰、生物相容性问题；如果是有限使用次数的器械，又多了一笔耗材经济性。

于是出现了一个非常漂亮，也非常残酷的工程矛盾：

**最适合测力的地方，恰恰最不适合放传感器。**

### 04这不是理论问题，达芬奇5已经选择往前走

所以现在再说“手术机器人的力反馈都是靠电流猜出来的”，已经明显不对。

da Vinci 5 就是现成的商业反例。

Intuitive 对它的描述非常明确：Force Feedback 使用的传感器位于**尽可能接近实际组织受力的位置，也就是器械尖端附近**；系统把器械端检测到的推、拉作用力传给医生的手控器。官方还宣称，在相关测试中，使用 Force Feedback 可使组织受到的力最多降低 43%。后一个数字应当理解成厂商公布的性能结果，而不是直接等同于独立的大规模临床终点。

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIX6poxbktmMnNTzZJjMyibogfgdEwwicpoOK7WA5AOfibFO1sgXf9u8HAZhPCcqOKpkPZB2jmYBF3jmDjF7cjuqdgp8cBVwnCzfS4/640?wx_fmt=png&from=appmsg)

真正值得看的反而是 Intuitive 自己解释“为什么拖了这么多年”。

它说得非常工程化：传感器被塞进如此小的空间以后，非常容易让各种**并不属于组织接触力的额外力**跑进传感信号。

这句话比宣传里的“Force Feedback”重要得多。

因为它说明，即便你已经把传感器移到了器械尖端附近，问题依然没有变成：

**有没有信号。**

而仍然是：

**这个信号里，到底哪部分是我真正想要的力。**

只不过相对于电机端估算，末端传感把那一大串需要补偿的传动链，砍掉了很长一截。

### 05传感器往后退一步，硬件简单了，算法的债就来了

为什么研究界仍然有那么多人研究 sensorless？

因为它实在太诱人。

机器人本来就有编码器，本来就有电流采样，本来就有电机控制器。

不增加一颗进入无菌区的传感器，理论上硬件成本几乎不变。

系统综述统计的文献里，sensorless model-based 甚至是数量非常大的一类路线。常见办法就是拿编码器位置、速度、电机电流等现成变量，建立动力学模型、扰动观测器或者数据驱动模型，再去反推外力。

这时候你真正依赖的就不是某一颗 sensor 的 datasheet，而是**模型有没有把机器自己描述准确。**

比如摩擦。

真实钢丝绳系统的摩擦很难只是：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4GDCeHQO1ictwT9icwk1vdQCDjDjZvllVL6ibwJu70iblczPv9LEjw0m3OV0pCHrrEBJZA1onCI239nbVK0AYCWqWeraO8qVBNuFJMaE4QymMnnw/640?wx_fmt=svg&from=appmsg)

换向前后可能不一样，预紧变化会影响它，弯曲状态会影响它，温度会影响它，使用次数也会影响它。

再比如滞回。

同样一个电机角度，从正方向走过来和从负方向走过来，器械末端的真实位置、钢丝绳张力和夹持力未必是同一个状态。

于是在实验台上做一套 calibration，得到一张非常漂亮的曲线，并不意味着几百次动作之后、换一把器械之后、重新装载之后，它还在那条曲线上。

综述对此说得非常直接：很多模型依赖开始时取得的 calibration 或 training set，但工具行为随时间变化，会使估算精度恶化；温度和湿度等环境参数也会改变器械特性。

这才是“用电流估力”真正难的地方。

**不是算不出来，是零点永远在动。**

### 06连反电动势也有人拿来算，但现在还远谈不上“行业主流”

还有一种很有意思的研究路径：不用额外力传感器，直接利用电机的 back-EMF 判断负载。

2025 年一篇论文就在手术机器人实验平台上做了这件事。

他们用带 StallGuard 的 TMC2209 步进驱动器，通过 back-EMF 相关量估计器械端作用力。在 2.4–8.2 N 的实验范围内，回归得到约 **0.95 的决定系数**和 **0.4 N 的均方根误差**。

数字看起来不错。

但作者同时明确指出，back-EMF 的波动限制了实时力反馈的准确性，仍需要改善电机稳定性和模型。更重要的是，这篇论文自己写得很清楚：**利用 back-EMF 监测机器人手术中的力，此前并没有被系统探索。**

所以它可以证明“这条路有人正在做”，不能证明“手术机器人普遍这样做”。

### 07“力反馈”四个字，其实没有告诉你力是怎么来的

这也是我现在看手术机器人宣传资料时最警惕的一件事。

**Force feedback 是输出功能，不等于 force sensor 是输入器件。**

前面的力，可以来自钳尖应变计，可以来自 FBG，可以来自 MEMS，可以来自器械杆的应变，也可以来自电机电流和动力学模型算出来的扰动力。

后面的 feedback，则还可以是直接通过手柄产生阻力，也可以变成视觉、振动甚至声音提示。

系统综述甚至专门把 direct force feedback 和 sensory substitution 分开讨论。

所以看到一家产品写“具有触觉反馈”，我现在不会先问：

**“用了哪颗力传感器？”**

而会先问：

**“那个反馈量到底在哪里被观测出来？”**

这是完全不同的问题。

### 08力反馈有价值，这一点倒不用争

2023 年的一篇 meta-analysis 纳入了 **56 项研究、768 名受试者、174 个观测值**。

有 haptic feedback 相比没有 haptic feedback，平均施力下降的效应量为 0.83，峰值施力下降 0.69，任务完成时间改善 0.83；论文还观察到准确性等方面的收益。

但这组数字只能说明一件事：

**给医生恢复有用的力信息，确实可能改变操作表现。**

它不能说明所有商业机器人都具有这种能力，更不能证明“用电流估算”或者“用某一种传感器”一定能获得相同效果。

这里一定要把两个问题拆开。

一个是：

**医生有没有力信息，会不会更好。**

另一个是：

**这台机器给医生的那一个力，到底测得准不准。**

后一个问题，才是传感器工程真正难的地方。

### 09如果我是医院采购，我反而不会先问“有没有力反馈”

我会要求供应商把下面这几件事说清楚：

-

**力在哪里测？** 是器械尖端、腕部、器械杆、驱动机构，还是模型估算？

-

**测的是几维？** 只有夹持力，还是轴向、横向以及多自由度力/力矩？

-

**换器械之后怎么办？** 每把器械有没有单独标定，装卸以后是否重新校准？

-

**寿命怎么处理？** 摩擦、钢丝绳预紧、滞回随使用变化以后，误差是否被监控？

-

**给的到底是什么指标？** 量程、重复性、绝对误差、带宽、漂移、灭菌后变化，至少应该分开讲。

因为一旦这些问题答不出来，“有 force feedback”这一句话的信息量其实非常低。

### 10再回头看美敦力这7亿美元，反而没必要硬扯力反馈

到这里再看这笔交易，商业逻辑已经足够解释它，不需要再人为加入“力反馈责任不好划，所以只投资不收购”这一层故事。

美敦力自己的官方说法很清楚：Sentire 将和 Hugo 形成一个**双平台组合**，针对不同临床场景、医院需求和经济模型提供更多选择；约 7 亿美元的战略投资同时包含 Sentire 在美国以外部分已获批市场的分销权。

截至 9 月 1 日的公开信息，Hugo 已进入 35 个以上国家；Sentire 已分别获得中国、欧盟和新加坡的市场准入。美敦力买的是产品组合、渠道扩张和时间，而不是公开资料里某一项已经得到确认的力传感技术。

至少目前没有证据允许我们再往前走那一步。

但这笔交易倒是让我重新注意到了手术机器人里一个很有意思的传感问题：

>

**工业机器人测外力，很多时候可以在关节里塞一颗力矩传感器；手术机器人真正关心的，却是几百毫米传动链另一头，那块软组织到底吃了多少力。**

电机知道自己出了多少力。

钳尖知道组织吃了多少力。

这两个数中间隔着钢丝绳、关节、摩擦、弹性、滞回、惯量、trocar 和一整套会老化的机械结构。

所以手术机器人力感知最困难的，从来不是：

**“力能不能测。”**

而是：

**“机器自己吃掉的那些力，能不能一项一项扣干净。”**

越靠近电机，传感器越好活，算法越难。

越靠近组织，信号越干净，传感器越难活。

da Vinci 5 已经证明，产业界开始愿意付出很高的工程成本，把传感位置重新往器械尖端推。

这可能才是手术机器人力反馈真正值得看的下一场竞争：

**不是谁先在宣传页上写出“触觉反馈”四个字，而是谁能把从组织到医生手上的这一条力链，做到可测、可标定、可灭菌、可重复、可量产，而且用了几百次以后还知道自己到底准不准。**

>

7 亿美元是新闻。 **把那几牛顿力测明白，才是工程。**

#### 参考资料

Medtronic 2026 年 9 月 1 日战略合作公告。Medtronic：Cornerstone Robotics strategic partnership 康诺思腾同期官方公告。Cornerstone Robotics：Strategic Partnership with Medtronic 手术机器人力感知系统综述。Force sensing in robot-assisted keyhole endoscopy Intuitive 对 da Vinci 5 Force Feedback 的技术介绍。Intuitive：da Vinci 5 Force Feedback 机器人手术触觉反馈 meta-analysis。The benefits of haptic feedback in robot assisted surgery 2025 年 back-EMF 力估算研究。Smart Force Sensing in Robot Surgery Utilising the Back Electromotive Force
