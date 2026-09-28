---
title: "人形机器人离商业落地还有多远？"
date: 2026-09-05T08:00:00+08:00
slug: "u-pmkrKvcdLI98_nhmaDmw"
description: "我觉得这个问题问错了一个字。不是“多远”，而是“哪里”。"
original: "https://mp.weixin.qq.com/s/u-pmkrKvcdLI98_nhmaDmw"
---

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIXCEic2J8cjbM07DlZRHt1tpHcyx4uwzs5U5TyrPFlFicMgp31jnkPazdW8zpibMNnmY3MZVjhZLNexUFB8LwKhCPapicVTSUZTrcg/640?wx_fmt=png&from=appmsg)

##

## 人形机器人离商业落地还有多远？

我觉得这个问题问错了一个字。不是“**多远**”，而是“**哪里**”。

因为人形机器人并不存在一个统一的商业化时刻。一个机器人如果每天都在平整厂房里从 A 点搬到 B 点，双腿可能永远不是最优解；但如果它必须穿过人行门、上下楼梯、跨门槛、使用现成工作台、拿人设计的工具，又不允许工厂为了它重新装修，那么两条腿突然就有价值了。

所以真正应该问的是：

> “

**什么场景愿意为“人形”这件事付溢价？**

这和汽车行业很像。不是 SUV 技术成熟以后轿车就消失了，而是不同机械拓扑开始占据不同任务空间。

那条高赞回答说，家庭里用扫地机器人式底盘，工厂里轮式比双足便宜，野外四足比双足稳。这些判断背后的核心逻辑我基本赞同：**如果地面条件已经为轮子准备好了，就不要轻易跟轮子比效率。**

但这里有一个经常被忽略的反面问题：**我们今天整个世界，其实是按照“人”设计的。**

门把手高度、楼梯尺寸、工作台高度、货架、工具、汽车驾驶位、消防通道、工厂维修空间，全都默认操作对象有人的尺度和活动范围。如果为了部署机器人，要重新修电梯、重新改线体、重新设计工装、重新布置仓库，那么原本便宜的轮式机器人，未必真的便宜。

因此人形机器人的第一笔商业账不是：

“腿贵还是轮子贵？”

而是：

**双足增加的机器成本，和为了非人形机器人改造环境的成本，谁更大。**

假设双足方案比轮式方案多出来的生命周期成本为一个量，环境改造以及获得更大任务覆盖带来的价值分别是另外两个量，那么真正的决策边界其实很简单：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7JChLu9QXwPX6vxzoYU6McWGZg0PQTt9ereC26zvfjrbOTbuicLP0k3986ic2m9O5zOHXVhX6DhVMcrRWR0VK6jQNoJNKJiayXDmpdYD0zLIbQA/640?wx_fmt=svg&from=appmsg)

左边是“坚持做人形”要多花的钱；右边则是“不做人形”以后，为场地改造和任务受限付出的代价。

**只要右边长期大于左边，双足就有商业意义。**

所以我不会说“双足不可能”。我会说：

> “

**双足不应该出现在所有地方。它只有在“人类环境本身很贵，改不起”时才真正值钱。**

这可能也是人形机器人商业化过程中最重要的一次筛选。

### ◆但双足真正贵的，并不是多了十个电机

高赞回答里有一句特别容易传播：100 台机器人，双腿比轮式多出上千个电机，这笔钱还不如装电梯。

方向没错，但如果只算电机数量，实际上还低估了双足的代价。

双足最大的成本不是静态 BOM，而是**动态系统复杂度**。

轮式移动时，在平整地面上，基本任务是克服滚动阻力和加减速。机器人停下来以后，通常也不需要持续消耗很大的电机功率来维持姿态。

双足完全不同。

走路意味着质心不断加速、减速，左右支撑脚不断切换，地面反作用力不断重新分配。某些关节周期性地经历正功、负功和冲击负载。

最基本的机械功率关系只是：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5VmtgKOhVcpjHXb5SA92bOTCUXfrFpYG9VZCoqWfcdwo0Eq9FoqSCSsE9iajyWvYfoD8lxotLgCqtK7WQsJDDAibRgNiaum8iczrXaswKTslGT5A/640?wx_fmt=svg&from=appmsg)

看起来非常普通，但放到腿上以后，麻烦在于扭矩和转速都不是平缓的。

比如机器人刚落脚的时候，膝关节、髋关节可能瞬间承担很大的地面反作用力矩；下一段动作中又可能进入反拖发电状态。真正决定电机、驱动器和减速器尺寸的，往往不是平均功率，而是**峰值扭矩、峰值电流和热循环**。

于是同样一个“500 W 电机”，装在轮子上和装在膝盖里，不是一个使用难度。

腿部驱动还要额外付出：

减速器寿命、轴承冲击、编码器抗振、线束弯折、结构刚度、散热以及跌倒后的机械冲击。

所以人形机器人的双足税，真正应该叫：

**动态机械复杂度税。**

这也是为什么我现在看到一台人形机器人跑得很漂亮，首先不会想到“它走得真像人”，而会想到：

**这套关节连续跑 3000 小时以后什么样？**

这个问题比后空翻难得多。

### ◆还有第二笔更隐蔽的账：
12 个腿部关节不是 12 个独立零件，而是一条串联系统

这件事情在商业化阶段尤其残酷。

假设一个关键关节在一个给定任务周期内可靠工作的概率是：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7qks3jr8VoPr9nzALibRzNXUvpFojNQbg2APETx0DyLmOg95bk3icLEgG1H8cbBa5fFc1hIJppcyR2XJPjibMbLOfWpymebrGia9q3MMv96EKusQ/640?wx_fmt=svg&from=appmsg)

如果一条运动链里有多个关键关节，而且先用最简单的独立近似，那么整条链的可靠度会近似变成：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5hKwWPuovPSk27HSOKicicJdQsewWnJlPvpHVlIDiaAPLP6yNBtjsD9BtUNcmmHeIKOqp2jm6H3NrpsaklGhf74sM8BaibA81JahtiaEebyic6hMvA/640?wx_fmt=svg&from=appmsg)

假设单个环节已经漂亮到：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6GXVpk5nDhYYjibBzo9dLFmY0aVuup9ic33WBbaCSmmhpza1LLMUZ5BwAMxBfibBbHffDpccQQgQhF8DX47zetfp2F54TSvkGicLnwianRAUZjN3A/640?wx_fmt=svg&from=appmsg)

12 个关键环节组合起来：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM58Sb1Wic5lr4Zj3sXqM0j7tDkQXvQjR26SqOx9styay74kBptQg8RUxIevibTnpBzoicJGU8ZuBSH3Z9M6BmdxCWa3DYpYWibMBD40WkyibwicrBRQ/640?wx_fmt=svg&from=appmsg)

这个模型当然非常粗糙，真实机器人还有共因失效、软件容错、冗余和降级运行，但它说明了一个很重要的工程事实：

> “

**机器人的复杂度不会按照零部件数量线性增长。**

你加一个关节，不只是多一台电机。

它同时增加一个：

电机、驱动器、减速器、轴承、编码器、线束、连接器、控制节点、热源和潜在失效点。

更麻烦的是，轮式机器人某一个驱动轮异常，很多情况下还能刹停。

双足机器人某个膝关节位置环突然异常，后果可能不是“停止工作”，而是：

**摔。**

而摔倒又是人形机器人特有的一笔经济账。

一台几十公斤的机器人，质心距离地面一米左右，仅仅重力势能的量级就是：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4sLEJY3bVQia9kvcZUgcYseZdMrxJvroojYOia2nnicgrtkB2D4MdRQia5s4COa0QTV0xQ71A6tqQLeJbCU003LLPp3PCFTwKiaFwUS6DTBSLRXyw/640?wx_fmt=svg&from=appmsg)

60 kg 的机器人，从 1 m 的质心高度跌落，理论势能接近 600 J。真正碰撞还会因为局部接触、姿态和运动速度产生更高的瞬态载荷。

所以家庭场景为什么特别苛刻？

不是因为机器人“走得不好看”。

而是**双足天然把一个移动系统变成了跌倒系统**。

在老人、小孩、宠物和家具周围，这个问题比“能不能端水”严重得多。

这也是高赞回答里“轮子具有被动安全”的那句话，我认为最值得继续往下挖的地方。

### ◆但做到这里，我反而开始看编码器了

因为双足越复杂，关节状态就越不能含糊。

一台轮式机器人在平地上定位，可以把不少事情交给激光雷达、视觉和轮速计。

但一台双足机器人单脚站立时，髋、膝、踝每一个关节的角度都会进入整机质心和足端位置估计。

一个很小的关节误差，经过连杆长度映射以后，会变成足端位置误差。

最简单的二维连杆关系已经能看出来：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM56p2yZk0OxOFK92ovs1BNtCjHHVsFXAAFteHKPc4hyBKXz5C8uCPqW9sdX7SdXeU0TDPECCM0CSRsR9qaiadHlUIlvEEILj4go6JISicEIFjhA/640?wx_fmt=svg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5QzUTKYQozFMicp5awklgUck7VBHhXMD7ibXavrUXDXvTunn6FicPq2cVxCTib6kroliafqUrwy5R4AZIiaHl7vUSQpmXI804RNGllibm8gia4yh827w/640?wx_fmt=svg&from=appmsg)

角度误差进入足端以后，本质上服从雅可比关系：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5YWmNicic1s34hIhYj0GYSR0ia8j9lFc4MNvhClsf4hrPw35vBoZ8cZPL4vkTmZEsZdB6vUGBuBUFPiaRt8iaCYyQhqbwoeNY1Ds20wThiaCFVTdhw/640?wx_fmt=svg&from=appmsg)

所以机器人关节多以后，“每颗编码器差一点点”并不会简单地停留在每颗编码器里面。

它会变成：

足端位置偏差、质心估计偏差、接触力分配偏差，最后再被控制器补偿。

这也是为什么我一直觉得，**真正大规模的人形机器人不可能每个关节都堆最贵的编码器，但也不可能随便放一颗能输出角度的芯片就结束。**

产业最后一定会分层。

电机端更关注高速、低延迟、低抖动和可靠换相；减速器输出端更关注绝对精度、温漂、安装偏心以及传动误差。

这正是编码器 IC 厂商比较有意思的位置。

比如昆泰芯现在做 Hall、AMR、TMR，再延伸到光学编码器 IC，我反而不会把这理解成“哪条技术路线都想做”。

更合理的理解是：

**机器人自己就不可能只需要一种编码器。**

手指、电机高速端、普通关节输出端、高精度关节，它们面对的是完全不同的成本函数。

机器人真正做到十万台以后，最值钱的未必是把所有位置传感器都做到 ±0.01°。

而是知道：

> “

**哪个关节允许我用 10 元解决，哪个必须花 50 元，哪个地方再省 5 元就会把整机性能毁掉。**

这才是量产工程。

### ◆所以人形机器人离商业落地还有多远？

我现在的答案反而比以前保守一点：

**“人形机器人”已经开始商业化，但“双足”还没有证明自己在大多数场景里值得那笔额外的钱。**

轮式能干的活，轮式大概率会赢。

四足更适合的地形，没有必要硬塞两条腿。

固定机械臂能够覆盖的工位，也没有必要为了“像人”增加一个移动底盘。

真正属于人形机器人的市场，是剩下那部分：

**环境已经按照人建好了，任务种类又多到不值得为了机器人重新改造环境。**

维修、巡检、柔性制造、复杂仓储、部分家庭服务，我认为都会属于这一类候选场景。

因此我不太相信一种叙事：

“未来所有机器人都会长成人。”

但我也不相信另一种极端：

“双腿永远没有商业价值。”

更可能的结果是，人形机器人最后证明自己的方式，非常不像今天的发布会。

没有后空翻。

没有跑步比赛。

甚至不需要特别像人。

它只需要证明一件极其无聊的事情：

> “

**这间厂房本来是给人建的，而我不改厂房，也能连续三年在这里挣钱。**

到了那一天，人形机器人才真正落地。

而那个时候，电机、减速器、编码器这些今天发布会上没人愿意拍特写的小东西，反而会变成真正决定利润率的地方。
