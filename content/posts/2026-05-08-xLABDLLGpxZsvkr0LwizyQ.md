---
title: "人形机器人真正该怀疑的，可能不是算法和电池，而是那套默认正确了几十年的伺服逻辑"
date: 2026-05-08T00:00:00+08:00
slug: "xLABDLLGpxZsvkr0LwizyQ"
description: "5月7日，北京日报发了一篇《机器人“狂奔”仍需迈关卡》。这话我认。只是站在一个做编码器的基层工程师位置上，我现在越来越觉得，很多人把“关卡”想浅了。"
original: "https://mp.weixin.qq.com/s/xLABDLLGpxZsvkr0LwizyQ"
---

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIW2qAMTBzRwJcm3CLyfAACV2VeyI6nFslcLra6M6ibibVpotgX5cgEX21Mw0zQmxuIawIvJATZeEBUV8HPDle1z5WbeiaPBl6vbAc/640?wx_fmt=png&from=appmsg)

##

### 先别急着怪算法，身体这一层已经开始不对劲了

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIWNWxI7zcaJZEj9wxhuhu02POF8Cz6zic6KA3Q0vFP4fnsiao65so5vTnwV7qJsRykfuzQXKR53fN8rZ7ljxBQmW6DnibRSm4CoH4/640?wx_fmt=png&from=appmsg)

5月7日，北京日报发了一篇《机器人“狂奔”仍需迈关卡》。这话我认。**只是站在一个做编码器的基层工程师位置上，我现在越来越觉得，很多人把“关卡”想浅了**。

大家张口就是大模型、训练数据、算力、电池、触觉分辨率，可真正先在现场露出不对劲的，往往不是这些，而是更底下一层：**机器人外面越来越像身体，里面却还在按工业伺服的方式被切开、编号、同步、闭环**。北京日报那篇讲的是产业从实验室走向工厂的关键一跃，但我看到的另一层是：它越想进入真实世界，越会碰到“**身体和控制哲学不匹配**”这个更硬的坎。 (Sina Finance[1])

这件事不是抽象的哲学争论，而是产品细节自己在说话。4月26日**超维动力**发布的**KAI**，115 个全身自由度，单手 36 个自由度，全身 18000 个触点，可感知约 0.1N 的轻微触碰，双臂负载接近 20kg。 (Sina Finance[2])

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIUu9cHbgciaPEHQ9Uh4KKeHto9iawYGCIkJD5rXdbNcNFaGe4YibkkEiarmM3rYaaRicRVNchcUN3wGPddotpzS4pcSibFniczYc1bYUo/640?wx_fmt=png&from=appmsg)

单看这组数字，很多人会觉得这是“更复杂、更高级、更接近人”。可我盯得最久的不是 115，也不是 18000，而是它那只手里明确分成了 22 个主控自由度和 14 个柔顺自由度。

这个细节很要命，因为它其实在承认：**当机器人真的开始接触世界、贴近人、抓取不规则物体时，光靠“主动关节更听话”不够，身体内部必须预留一部分不用先算清楚、也能自己缓冲、自己顺着物体走、自己吞掉误差的能力**。

### 工业伺服为什么会成为今天所有人的默认答案

传统伺服架构之所以几乎成了整个机器人行业的母语，不是因为谁保守，而是因为它过去太成功了。机床、工业机械臂、包装设备、输送线，这些系统面对的是一个被整理得很干净的世界：边界清楚，动作固定，接触可预测，误差来源也大多能拆开。于是最自然的办法就是：每个轴都定义清楚、测量清楚、控制清楚，最后靠总线、时钟和控制器把整机拼起来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIVMdomGhBqqSVleNbSfLFu3rVwFBib468g6CPvtsmaAnWRCRKZCiburUmRdksJJs1cicarTgJrdmCrNXIPly3WP7QbFcsYHL3kiaPc/640?wx_fmt=png&from=appmsg)

这套逻辑在工业里几乎无敌。因为**工业系统最值钱的是确定性，是可追责，是重复性**，是一个问题出现以后能很快定位到“哪根轴、哪个编码器、哪段线、哪项参数”。工业伺服擅长的，正好就是把世界切成很多段确定关系，然后一段一段压误差。

问题在于，身体不是这样工作的。**身体里最重要的能力，很多时候不是“每个局部都绝对正确”，而是“整机别僵、别慢、别脆、别顶着干”**。你走路的时候脚底一滑，身体最先需要的不是某个关节再精准 0.02∘，而是整条链能不能先把你从摔倒边缘拉回来。你抓杯子的时候，真正决定动作自然不自然的，很多时候也不是某个指节角度值更准，而是手指、皮肤、肌腱、腕部顺应能不能把接触先接住。

所以问题不是伺服“不够强”，而是它强在了一个不完全对路的方向上。工业伺服擅长的是确定关系，身体擅长的却是容纳不确定关系。

### 可一旦自由度、触觉和接触一起上来，这套答案就开始顶不住了

这个矛盾，用一个很朴素的式子就能看出来：

Δp≈∑iLiΔθi

这里 Δp 是末端位置误差，Li 是各段等效长度，Δθi 是各关节的等效角误差。

这式子不复杂，但很残忍。因为它告诉你：**只要你还把整机主要理解成一串串关节角，局部小误差就会沿着身体一层一层往末端放大**。

假设某段有效长度是 0.4m，某个关节动态误差只有 0.5∘，放到末端已经是毫米级偏差。工业机械臂在很多场景里能吃下这个量，因为工位和接触都被规训过；可人形机器人不是在空中比划，它要落脚、避让、贴身交互、抓软物体、接受碰撞、承受重心转移。到了这些场景，问题往往不是“这几毫米大不大”，而是为了继续把这几毫米硬压下去，系统会不会把整具身体调得越来越紧、越来越硬、越来越怕接触。

这也是为什么**人形机器人一旦真开始追求“像身体”，传统伺服的代价就不再是线性增长**。自由度一多，接触一复杂，你会发现越来越多本该被结构吸掉、被顺应吞掉、被局部耦合抹平的误差，被硬生生推给了控制器、标定链、反馈链和售后链。它最后不是不能工作，而是越来越像一台被极限压缩的自动化设备，而不像一个有身体感的系统。

### 行业其实已经在偷偷换路，只是嘴上还没承认

真正说明问题的，不是那些口号，而是公开产品和论文里已经长出来的那些“看起来不那么伺服”的东西。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DBrlpXS1RIU3cY65rAYw4VZ53y9dxyJYyFCZRxMoStSpHicA5C9oXeia8hNemqd4YCORgGPibUglfhcnQGmONYDQNXKEb5cbpVxUeXGcTOZsWg/640?wx_fmt=jpeg&from=appmsg)

1X 的 NEO 和 NEO Gamma，官方反复强调的是 Tendon Drive、soft body、pinch proof、low-energy movements。它不是先讲高刚性，而是先讲外部包覆、被动安全、低能量动作和避免夹伤。这个语言系统本身就已经偏离了工业伺服的老词典：**它不再默认“更硬更稳”，而是默认“先别伤人、先别顶硬、先别让接触变成危险”**。 (1X[3])

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIWMfanrnDyxqiaicu7ibH5IsicJpk0ZxXdg4oTJg6dray4yIFbDLIbZdmS6ibSch6KTe6KWRB2wjW9hnTHhBNRialSiclDiamBQDibd8Vrg/640?wx_fmt=png&from=appmsg)

DLR 的 neoDavid 走得更直接。公开资料里写得很明白：它的关节采用可变刚度执行器(variable stiffness actuators)，传动链里机械弹性可调；同时还有连续体弹性颈部、带过载耦合的重力补偿躯干。更关键的是，它在操作里不是只靠位置环，而是把 proprioception 和 vision 融合起来做 grasp state estimation，再做 compliant positioning。翻成人话就是：**它已经不再把“刚性轴 + 角度闭环”当唯一中心，而是把弹性、顺应、抓握状态一起放进主回路**。 (DLR[4])

![](https://mmbiz.qpic.cn/mmbiz_jpg/DBrlpXS1RIUBEgW1JnRcO4FjPpmNTV5GUfoicEtZl3SDcIicTlezbjqcVCezWF2Q0TZbHicsxxP0y0glQVERhbfMSicvDTdibgnUq91bibYMCFn4Q/640?wx_fmt=jpeg&from=appmsg)

手部路线更说明问题。EPFL 的 ADAPT Hand 做得很漂亮，但它漂亮的地方不在于“给每个手指再多配几个电机”，而在于它把顺应性分布在皮肤、手指和手腕里，**让抓型在接触中自己组织起来**。公开结果是：面对 24 类不同物体，它实现了约 93% 的抓取成功率，在 800 多次压力测试里表现稳定，而且抓型和自然人手有 68% 的直接相似性。这里真正刺眼的一句不是 93%，而是“由被动适应驱动的自组织行为支撑了这种鲁棒性”。这等于在说，**有些智能本来就不该全堆在控制器里，而应该先长在身体上**。 (EPFL News[5])

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIW0mAfqDeXA4Qo7G1w48GnfTfoHibV8j8hD86co1icWmsKWDDIbWibseFib07TpceUnrDgHa0rKOcKpkT5BqW4qrSpnSRX6M0xibs8A/640?wx_fmt=png&from=appmsg)

触觉这条线也是同一个方向。Melexis 和 OYMotion 正在把 Tactaxis 往下一代机器人手里推，目标是更像人手的灵巧操作；Nature Machine Intelligence 2025 的 F-TAC Hand 则把**高分辨率触觉铺到了约 70% 的手部表面**，空间分辨率达到 0.1 mm，并在 600 次真实试验中显著优于非触觉方案。 (Nature[6])

你把这些东西摆在一起看，会发现行业真正往前拱的方向，不是“更纯的伺服”，而是“**更像身体的结构 + 更分布式的感觉**”。

### 人体里面根本没有“每个关节一颗高精度编码器”

很多人下意识会把人体想成：它只是有一套比机器人更高级的伺服，关节里藏着更好的“编码器”，大脑再把这些精确状态统一调度。这个比喻很顺口，但其实很误导。

关于**本体感觉**的学术综述已经讲得很清楚：肌梭、腱器官、皮肤机械感受器和关节受体都会贡献身体位置、运动和力的信息；其中肌梭通常被看作最主要的来源之一，而关节受体在经典观点里更多像接近关节极限时的“限位提醒”。 (ScienceDirect[7])

这意味着人体并不是“每个关节一颗绝对角度传感器”，而是在肌肉、肌腱、皮肤和关节周围铺了**一张分布式感觉网**。它感知的不是一个单一、统一、线性的角度真值，而是长度变化、速度、张力、皮肤拉伸、接触状态这些彼此重叠的量。

更关键的是，肌梭还不是一个固定灵敏度的被动器件。**人类肌梭更像“可控的信号处理器”，而不只是老老实实报数的传感器**。它们会被脊髓的  运动神经元调节，也就是说，身体会主动改“传感器”的灵敏度。 (PubMed[8])

把这个意思写得直白一点，人体里的感觉更像这样：

长度变化速度张力皮肤拉伸接触事件运动状态

它不是“先测一个最干净的真值”，而是“拼一个够用的身体状态”。所以**人体不是不讲究准确，而是不迷信工业伺服意义上的那种绝对准确**。身体讲究的是“够用而且活”，不是“每个时刻都把每个关节说死”。

### 身体真正厉害的，不是统一调度，而是局部先活下来

生物运动控制还有一个特别关键的特征：**它不迷信统一调度**。有研究论文说得很直：**去中心化是 biological motor control 的核心特征之一**，它允许系统依赖局部感觉信息做快速反应；相比之下，完全中心化的单控制器反而要先把整个输入空间拆明白。 (ScienceDirect[9])

翻成人话就是：脚底一滑，先救你的不一定是一个“总控大脑”重新求全身最优，而是局部环路先把你从摔倒边缘拽回来；手指一碰到物体，先变的也不一定是世界模型，而可能是局部张力、局部顺应、局部反射。身体之所以像身体，很多时候靠的不是所有部位都统一听命，而是很多局部在没等到全局命令之前，就已经知道先别死、先别断、先别顶硬。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIVTYMKSX8tKWB9zjJMaGoOd81SDQAwibmmsvcCDmvsjZIIDLVAU3IVdoqrocaLfiaXt39ysC12rKMfiaB6NjSn49icFr8HDdTHjBiaU/640?wx_fmt=png&from=appmsg)

这一点跟今天很多机器人底层仍然偏爱的思路，几乎是反着来的。我们今天的系统很喜欢“全身统一时钟、统一总线、统一控制框架、统一解释”。这当然有工程价值，但它也很容易把“身体”做成一台系统架构很整齐的机器。问题是，**身体真正宝贵的地方，很多恰恰来自不整齐，来自局部先行，来自一些关系先模糊着，只要最后别出大错就行**。

### 对编码器行业来说，最危险的不是被替代，而是继续当旧时代的零件

这也是我作为做编码器的人，最近最强烈的不安。

编码器不会消失。电机、减速器、位置反馈、总线、驱动器，这些都不会突然退场。未来很多年，人形机器人里仍然会大量使用它们。真正会变的，是它们在系统里的地位。

过去的默认前提是：**角度是核心真值，其他感觉都是辅助**。

以后的前提更可能变成：**角度只是身体状态里的一个通道，张力、顺应、接触、热状态、可信度，同样重要**。

把这个意思写成一个很粗糙的状态量，大概像这样：

这里  是角度， 是角速度， 是力或张力， 是等效刚度， 是热状态， 是这一次测量到底有多可信。

这套思路下，客户最想问的就不再只是“你多少 bit”。他更想知道：

-

这个关节现在是在顺着任务做，还是在顶着结构干？

-

这个动作发僵，是角度环的问题，还是张力、回差、温升、接触的问题？

-

这一次测得很准，但这一刻这个值还值不值得信？

**对编码器行业来说，真正危险的不是被某个新传感器一脚踢走，而是继续把自己理解成“报角度的器件”**。谁先把编码器从“角度真值源”做成“身体状态理解器件”的一部分，谁才真正踩进下一轮门槛。

### 真正的分水岭，不是谁先把模型做大，而是谁先承认“身体不是设备”

所以我现在看人形机器人，已经不太愿意先谈算法和电池了。那两件事当然重要，但它们更像表层短板。更深的一层，是我们到底愿不愿意承认：**传统伺服在人形里不是“不够强”，而是“很可能不再适合继续当总逻辑”**。

KAI 的柔顺自由度、1X 的 Tendon Drive、DLR 的可变刚度、ADAPT Hand 的分布式顺应、F-TAC Hand 的高分辨率触觉、肌梭的可调灵敏度、生物控制的去中心化，这些东西摆在一起，已经不是零散现象了。它们共同指向一句话：

>

**传统伺服在人形机器人里也许不会消失，但很可能会从“身体的主逻辑”退成“身体里的局部器官”。真正往上爬成新主轴的，是更仿生的结构、更分布式的感觉，以及不再迷信“每个关节都必须先被完全说清楚”的控制哲学。** (Eastmoney Finance[10])

这才是我现在最在意的那个“关卡”。

不是机器人还不够像人。
而是我们可能还在用一套太像工业设备的脑子，去造一具本来不该那样长出来的身体。

#### 参考资料

[1] Sina Finance

https://finance.sina.com.cn/jjxw/2026-05-07/doc-inhwzmmr2898617.shtml

[2] Sina Finance

https://finance.sina.com.cn/tech/digi/2026-05-03/doc-inhwrhfa8774697.shtml

[3] 1X

https://www.1x.tech/neo

[4] DLR

https://www.dlr.de/en/rm/media/videos/video-neodavid-a-humanoid-robot-with-variable-stiffness-actuation-and-dexterous-manipulation-skills

[5] EPFL News

https://actu.epfl.ch/news/robotic-hand-moves-objects-with-human-like-grasps/

[6] Nature

https://www.nature.com/articles/s42256-025-01053-3

[7] ScienceDirect

https://www.sciencedirect.com/science/article/abs/pii/S2468867321000389

[8] PubMed

https://pubmed.ncbi.nlm.nih.gov/35829705/

[9] ScienceDirect

https://www.sciencedirect.com/science/article/pii/S0893608021003671

[10] Eastmoney Finance

https://finance.eastmoney.com/a/202604283721481625.html
