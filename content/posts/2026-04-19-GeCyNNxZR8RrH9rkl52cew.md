---
title: "AI来了以后，IC行业35岁工程师最怕的，可能不是被替代"
date: 2026-04-19T00:00:00+08:00
slug: "GeCyNNxZR8RrH9rkl52cew"
description: "工资不像刚毕业时那么低了，身体也不像刚毕业时那么扛了。下面的人更年轻，更便宜，眼睛盯波形能盯到半夜两点，第二天照样开站会。你自己也不是干不动了，只是越来越清楚：有些活不是不能干，是再这么干下去，心里会发虚。"
original: "https://mp.weixin.qq.com/s/GeCyNNxZR8RrH9rkl52cew"
---

## 芯片这行干到 35 岁，很多话其实不用明说。

工资不像刚毕业时那么低了，身体也不像刚毕业时那么扛了。下面的人更年轻，更便宜，眼睛盯波形能盯到半夜两点，第二天照样开站会。你自己也不是干不动了，只是越来越清楚：有些活不是不能干，是再这么干下去，心里会发虚。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DBrlpXS1RIUdjzqbzU0SLUG1toNHDwkG7iar9FLs4PYUWxv4qedMhYZAiaquqDgnH3jFuKfZuDVJl8JafAxoU700KNobR0JdZG1uDmEYyTDV0/640?wx_fmt=jpeg&from=appmsg)

因为你知道，自己不可能永远靠“**能熬**”“**能顶**”“**能把几百页报告啃完**”来证明价值。

而 AI 一进来，最扎心的地方就在这儿：

>

**它先吃掉的，恰恰就是很多基层中年工程师这些年最熟、也最耗命的那部分活。**

### 你不是怕 AI 太强，你是怕公司突然发现：你最值钱的，原来只是加班

这句话不好听，但很多人心里都明白。

以前项目一紧，最能证明自己的办法，就是扛活。

STA report 几百条 violation，先拉表。 CDC 几百个 warning，一个个点。 仿真 log 一页页翻。 ECO 前后网表 diff、约束 diff、波形截图、问题单整理，都是靠人肉磨出来的。

这些活不光累，还特别磨人。你明知道里面很多工作没什么技术含量，就是重复、比对、筛查、汇总，但项目就卡在这儿。谁把这些东西啃完，谁就像是“最有价值的人”。

可现在这套逻辑开始松了。

一份 timing report，加上几版历史结果、模块层级和约束摘要，AI 很快就能先把 **setup violation** 超过阈值的路径捞出来，按 **startpoint** 分组，按公共逻辑锥聚类，把多 mode、多 corner 下反复冒头的热点先拎出来。以前新人熬一晚上才能做出的第一轮整理，现在它几分钟就能给你一版像样的底稿。

![](https://mmbiz.qpic.cn/mmbiz_jpg/DBrlpXS1RIUxe4fKfDsYskwzX5qB2XfMIHicROvcUGRcmPiayMwickh3QNxuBVZtETiaEweZdXhsUTZiavyagC02glDHz4Fia1uHmKbdCICNe4mP0/640?wx_fmt=jpeg&from=appmsg)

CDC 也一样。 哪些像 **reconvergence**，哪些像 **pulse crossing**，哪些像 **async reset release**，哪些其实只是同类结构反复报，AI 很适合先做粗筛和归类。

这时候最难受的，不是“AI 懂芯片了”。

而是公司会越来越看清一件事：

>

**原来很多很贵的人，大量时间一直花在其实没那么贵的事情上。**

这对刚毕业的人是冲击。 对 35 岁上下、卡在基层技术岗的人，更是一下顶到心口。

因为你会忍不住问自己一句：

>

**如果这些活以后不值钱了，那我还剩什么？**

### 真正让人睡不着的，从来不是 report 本身，是最后那句“这条到底放不放”

芯片行业里，外行最容易看错的一点，就是以为工程师最重要的能力是分析。

其实很多时候，不是。

分析当然重要，但真正贵的，是**拍板**。

干过项目的人都知道，有些会，最安静的时候最难熬。PPA、后端、设计、验证、DFT、架构，一圈人坐着，屏幕上挂着红字，谁都能说几句道理，谁都能讲一点风险，谁都能提一个“再看看”。

可真正值钱的，从来不是这些“再看看”。

是一条 **setup violation** 摆在那儿，你到底怎么定。 是补 buffer，还是改逻辑，还是加一级 pipeline，还是回去重查 **generated clock**、**false path**、**multicycle** 有没有建偏。 每个选项背后都不只是技术，是**面积、功耗、频率、验证量、布局布线难度、ECO 成本和 tapeout 节点**。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DBrlpXS1RIXR588In669tsKZGibQ8cR7JbtFUHicJibBNxiaiaHuMGqbLKfYBGu0jdg3yriafq6BBETuU0koceVO4ReRfPlynib6KbTRU0WjklHyz4/640?wx_fmt=jpeg&from=appmsg)

CDC 更狠。

最难的从来不是工具报出来。 最难的是最后那句：

>

**这条修，还是 waiver。**

做过的人都知道，**waiver** 不是流程动作，是真签字。

你一旦放过去，等于你在说：这条 crossing 在这个架构、这个模式、这个初始化顺序、这个时钟关系下，我认为不会变成量产风险。

这句话不是说给工具听的。 是说给未来几百万、上千万成本听的。 也是说给几个月后的 **bring-up**、客户现场、返修单、甚至下一次绩效听的。

AI 可以帮你整理理由，可以把历史 pattern 找出来，可以告诉你哪类结构通常风险更高，哪类同步方式常见误报更多。

但它接不住那句最关键的话：

>

**放。**

也接不住另一句更难受的话：

>

**别省这点时间了，这条得修。**

芯片这行最贵的地方，不是“会不会分析”。

而是到了**该花钱、该延期、该背锅**的时候，谁敢把话说死。

![](https://mmbiz.qpic.cn/mmbiz_jpg/DBrlpXS1RIUqxR15f5ia03le8nZC2hD9pWibZkF4e1yTnhyYpicGUMHicNxMJsG3aIECRiaCgZWV8MDAvImEfR0bApXejYYRqYLZibwMvdQ7ibGeibE/640?wx_fmt=jpeg&from=appmsg)

### 35岁以后最疼的，不是自己不如年轻人了，是你突然发现自己一直没机会拍板

这才是很多基层中年工程师真正的痛点。

你不是没经验。 你也不是没干过活。 你甚至可能比上面的人更懂那些脏细节：哪种 reset 最容易出鬼，哪种 CDC 看着顺其实最脏，哪种 setup violation 八成不是路径问题而是约束问题，哪次 metal ECO 看着还能顶其实是在赌。

可问题是，这些年你也许一直都在“**做判断前的工作**”，却很少真的轮到你做判断。

你负责把 report 整干净。 你负责把问题梳理明白。 你负责把几种方案都列出来。 可最后拍板的人不是你。

这就是很多 35 岁工程师最憋的地方。

>

**不是不会。 是不被允许负责。**

于是年纪上来了，工资也上来了，职级却卡住了。公司嘴上说你是骨干，实际上很多最贵的决定还是轮不到你。你继续做很多活，继续加很多班，继续替项目擦边角，但你心里也清楚：

>

**只要你还停留在“把问题整理给别人拍板”的位置，你就永远有一种说不出的虚。**

而 AI 来了以后，这种虚会更明显。

因为“整理给别人拍板”这件事，本身就越来越容易被压价。 报告能自动归类，日志能自动摘要，pattern 能自动提取，初筛能自动做。 你再靠这些证明自己，分量会越来越轻。

所以 35 岁以后真正分人的，不是会不会用更多工具，不是会不会写更花的 Tcl，也不是还能不能熬夜。

而是：

>

**公司愿不愿意把贵决定交给你。**

### 真正把人打老的，不是 bug 本身，是那种“差一点就放过去了”的瞬间

这行干久了以后，人记住的从来不是自己写过多少 RTL，也不是跑过多少回归。

记住的都是那些后背发凉的瞬间。

是某条 CDC warning，工具没报得特别凶，结构也像那么回事，仿真还过了，最后上板偶发吞脉冲，查了两周才知道是慢时钟域根本采不到那个窄脉冲。

是某次 **reset release**，block level 全绿，到了 subsystem 才偶发起不来，最后发现 **isolation** 撤早了一拍，状态机在脏窗口里吃了值。

是大家狠狠干了三天 datapath，插 buffer、搬寄存器、改 mapping，最后才发现问题根本不在路径本身，而在约束模型从第一天就建歪了。

是某次 **metal ECO**，所有人都不想动 **full mask**，因为那真是钱，真是延期，真是会上要挨问责，但最后还是得承认：这一把 metal 顶不住，再赌就是把坑往客户那边推。

![](https://mmbiz.qpic.cn/mmbiz_jpg/DBrlpXS1RIXmG8DOuXj755warIZ9zdz4xZiavzYbiahDQnRMRn1icFuPYOYldqAibI7DgIRcHGmtcib4qogYvaP88Rvq506oXBeI8XuMTZ8nicKkU/640?wx_fmt=jpeg&from=appmsg)

这些事，才会把一个人真正打成熟。

所以我现在越来越觉得，AI 对基层中年 IC 工程师最残酷、也最公平的一点，就是它把一件事照得很清楚：

>

**你到底是在靠体力和耐心撑着价值， 还是已经开始能替项目承担结果。**

如果是前者，你会越来越慌。 因为你会发现，自己这些年最耗命的那部分事，正在迅速变便宜。 如果是后者，AI 反而是好东西。 因为终于有人能替你把那些低价值、但特别吃命的苦活吞掉了，你可以把精力留给真正贵的东西：**识别风险、比较代价、做决定、扛后果**。

### 说到底，35岁以后真正危险的，不是 AI，是公司认真看了一眼你这些年到底在卖什么

卖加班，危险。 卖执行，危险。 卖“我什么都能帮你整理好”，也越来越危险。

真正开始值钱的，是另一种东西：

-

项目要不要再做一轮 **ECO**

-

哪条 **CDC** 能不能 **waiver**

-

哪次 **signoff** 能不能冒这个险

-

哪种看起来能省钱的方案其实是在往后埋雷

这类事情，最后总得有人拍板。 拍错了，要有人背。 拍对了，往往也不会立刻有人夸，只是下一次更贵的决定会继续交给你。

这才是基层中年工程师真正该争的位置。

>

**不是继续证明自己多能干。 而是慢慢让自己变成那个在最贵、最难、最容易出事的时候，别人会转头问一句： “你怎么看？”**

那一下，才是真的值钱。

![](https://mmbiz.qpic.cn/mmbiz_jpg/DBrlpXS1RIWMeWewMM5ibZ2vnSPfTCvwDO9rU4cRX71RMjianrUnHGiamymxkX7ytFKygQ5D8fpFC4av6EL9ATUgSsA5n7cyCWJSwebZibibvkaE/640?wx_fmt=jpeg&from=appmsg)
