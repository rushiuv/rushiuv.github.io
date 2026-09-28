---
title: "Radivoje Popović教授（EPFL）与霍尔传感器帝国：从一间瑞士实验室，铺到整个全球产业链"
date: 2025-10-04T00:00:00+08:00
slug: "2Xn99HBw_PeVcr8eoTc5jA"
description: "霍尔效应一八七九年就被发现了；问题从来不在“有没有效应”，而在“能不能把它做成稳定、便宜、能上车上机的器件”。早年的器件多数用 InSb、GaAs 等 III-V 材料，灵敏度好却难以规模化。Popović 在九十年代做了几件决定性的事。"
original: "https://mp.weixin.qq.com/s/2Xn99HBw_PeVcr8eoTc5jA"
models: ["MLX90316"]
companies: ["英飞凌", "Melexis", "Allegro", "TDK", "MPS", "AKM", "Apple", "特斯拉", "EPFL"]
tags: ["霍尔", "车规", "瑞士"]
---

## 你打开手机地图，小箭头乖乖跟着你的身体旋转；你踩下油门，汽车控制器立刻捕捉踏板角度；在粒子加速器的隧道里，工程师用一支看似普通的“笔”去量几特斯拉强磁场里的细微波动。看不见的磁场在这一刻都被“翻译”成了可读的电压，这个翻译官就是霍尔传感器。

## 而把“好玩的小电压”变成“好用的大产业”的那条骨架线路，清清楚楚落在瑞士洛桑联邦理工学院（EPFL）**Radivoje Popović**教授和他带出的学生队伍身上：垂直霍尔、三轴探头、spinning current 偏移抑制、与 CMOS 的深度耦合——从原理到工艺到系统，他把一套能量产、可标定、可扩展的框架钉死在了行业底层，后面的公司与巨头几乎都在这张“设计图”上走路。

![](/images/wx/a6bd66f4e3a12e57c5a5949af2ac994c.webp)

##

### 技术框架为什么绕不开他

霍尔效应一八七九年就被发现了；问题从来不在“有没有效应”，而在“能不能把它做成稳定、便宜、能上车上机的器件”。早年的器件多数用 InSb、GaAs 等 III-V 材料，灵敏度好却难以规模化。Popović 在九十年代做了几件决定性的事。

第一，他把只能盯着垂直磁场的平面霍尔翻转成了**垂直霍尔器件**，让芯片对平行于硅片表面的磁场也能高效感知；

第二，他把平面与垂直单元在同一颗芯片上正交排布，做成**三轴集成探头**，让一个硅片同时读出 (B_x,B_y,B_z)。这是后来所有 3D 霍尔芯片的雏形，而且更关键的是，他证明了这事儿**可以在标准 CMOS 流程里完成**，不是只能靠特种工艺的小作坊。早期论文把“在 CMOS 高压工艺里实现高灵敏度垂直霍尔”的方法讲得非常清楚，发明人与单位一栏里，EPFL-DMT-IMS 和 SENTRON 并排站着。

![](/images/wx/2554c50fcdb50d5cf8a44038ddcb9ce1.webp)

第三个“卡脖子”点叫偏移与漂移：没有磁场也会有输出，温度一变就乱飘。Popović 学派把**spinning current**（电流旋转法）用成了行业基操——通过在多电极霍尔片上快速轮换激励/取样方向，让固定偏移在一轮轮采样中互相抵消，再配合斩波/锁相等读出链，1/f 低频噪声和零点飘移被压进了角落。今天你随手打开一篇高速霍尔读出论文，仍能看到“随机化四相 spinning current”这样的现代化迭代，祖法不变。

![](/images/wx/5b5cbc12acfe3ea9d45133481042f5bc.webp)

(US6064202A United States Patent)

第四步，是把这些“物理+读出”的方案变成**商品级的硅系统**。他既写了成体系的专著《Hall Effect Devices》，把材料、几何、电路、噪声与校准连成书，又在产业侧推进把霍尔元件、低漂移前端、温度/应力补偿、ADC 和接口放到一颗芯片里，**成本线和良率线**终于同时过线，这才有了后来汽车与消费电子的爆发。

![](/images/wx/b3a765529c23a29fdbf42c180f6b29f0.webp)

这四步铺完，霍尔从“实验室奇趣”跃迁为“产业地基”。为什么说“绕不开他”？因为在“能测三轴、能压偏移、能用 CMOS、能进量产”这四个考题上，行业至今用的仍是他定下的解题套路。EPFL 的官方页面把他在“垂直霍尔器件、首个三轴集成探头、Tissot T-Touch 电子罗盘”等节点上的发明与早期开发写得明明白白，这不是自我阐述，是一条能被公司与产品相互印证的技术脉络。

### 学生为什么能把论文做成公司、公司为什么会被并购

有了“框架”，创业就不再是“玄学碰运气”，而是把图纸拆成拼图去落地。九十年代，**Sentron AG** 拿着 IMC-Hall（集成磁通集中器 + 霍尔）与垂直/平面组合方案，先是在科研和表计类场景试水，随后把**2D-VH-11** 这样的器件塞进 **Tissot T-Touch** 腕表做电子罗盘——这是三轴磁传感第一次走入大众消费。公司报表里写得直白：2003 年营收超 200 万瑞郎；

![](/images/wx/af321c1ca1cd54e7fba2f855ceec1494.webp)

2004 年二月，传感器业务及“Sentron”品牌整体被**Melexis N.V.** 收购，一纸新闻稿把“IMC-Hall 的量产化价值”盖了章。

![](/images/wx/772a38c59b8bd234ca0efa11ecc8ea5c.png)

收购之后发生了什么？你在媒体与数据手册上能看到非常清楚的对应关系：**Melexis MLX90316** 挂上了“Triaxis™”标签，这是一颗**非接触 360°** 角度传感的**单芯片霍尔 SoC**，用廉价永磁体就能做车规角度；它既是 Melexis 自家 CMOS 平台的延续，也是 Sentron 技术栈的产业化承接——IMC 结构把平行场“折”成垂直等效场喂给硅里那组霍尔单元，后端再用数字链去校正。从当年的行业报道到后来的数据手册，能清楚读到它的技术与应用位置：节气门、踏板、方向盘角度，全部指向量产车的真实工况。

![](/images/wx/f9db09fb90b7ad53beffc3c033c929de.webp)

同一时期，**Senis AG** 从 Sentron 的体系里分拆出来，Popović 亲自挂 **CTO**，目标不是手机或车，而是**科研级 teslameter 与三轴探头**：分辨率下探到**微特斯拉**量级，带宽从 **DC 到 300 kHz**，量程从几十毫特斯拉一直拉到几特斯拉，空间分辨率做到百微米量级，给同步辐射装置、加速器磁铁校准、磁场扫描提供“行业标尺”。一支手持探头能在几特斯拉背景下盯住细小波动，靠的就是三轴正交结构、低漂移读出与可追溯校准的组合拳。Senis 的公开资料和 3D Hall 传感器手册把这些“硬指标”写得清清楚楚。

![](/images/wx/33a3a116391e6960c363928db71dbf87.webp)

再往后，**学生公司被北美巨头买走**的桥段也出现了。2014 年，**Monolithic Power Systems (MPS)** 发布新闻：以 **1170 万美元现金 + 最高 890 万美元绩效**收购瑞士 **Sensima Technology SA**。MPS 的表述毫不遮掩——这家“小而硬”的公司手里握着**角度测量与三维磁场感知的 CMOS 集成磁传感技术**，并且会被直接并入电源管理与电机控制的产品路线。那份新闻通稿今天仍在。

![](/images/wx/c0c5c397bde28c2bf5cb0a9c27cb690c.png)

这套“论文→公司→并购”的逻辑为什么顺畅？因为教授提供的不是一两个“点子”，而是一套“体系”。体系意味着可复制、可验证、可叠代，意味着**专利+工艺+算法+标定+封装**的协同闭环。

Sentron 被 Melexis 吃掉之后，Triaxis 成了车规角度领域的一根柱子；Sensima 进入 MPS 之后，角度磁感与功率/电机控制的系统级耦合被进一步做实。到了 2025 年，连“老牌的 Sentron”本体也进入了下一轮整合：**Millar** 宣布完成对 Sentron 的并入，公开新闻称之为“把 pH、电导率、压力与磁传感制造能力纳入纵向一体化的 CDMO 版图”。产业的棋局一直在走，但每次落子都沿着同一条主干。

![](/images/wx/f7811ee5bc171ea7de1ea774115c2f0c.png)

### 巨头为什么都在他的“图纸”上走路

把车型号、芯片型号、新闻通稿摆在桌面上看，你会发现竞争者们的方法论惊人一致。**Melexis** 把 IMC-Hall 写进自家的技术白皮书，把“如何把**水平磁场**通过集成磁通集中器**等效成垂直场**喂给霍尔单元”讲成了标准教材；**Infineon** 的 TLE 家族在电流与角度传感上同样倚重**垂直霍尔 + 数字补偿**；**Allegro MicroSystems** 在 A1335、A1369 上把**全数字链路**与偏移校正推到新能源车逆变器侧；**AKM/TDK/Asahi Kasei** 长期把**三轴磁传感**打进移动设备，SENIS 的行业报告甚至直接点名“ASAHI 在 iPhone 罗盘里使用了 IMC 技术的某种版本”，这类说法至少从“结构路线”上与 Popović 铺下的主干握手，尽管不同公司在具体材料与读出电路上会做各自的取舍。

![](/images/wx/62f1ab62b05aed71313823767cfbf93d.webp)

“图纸”的力量还体现在**性能指标如何被一代代刷新**。以 Senis 的 3D Hall 为例，“**1 µT 级分辨率 + DC–300 kHz 带宽 + 40 mT–4 T 量程**”这种参数组合既能下地磁、又能上强场，意味着从地球物理到加速器磁铁一网打尽；而在车规与工业侧，**线性误差 < 0.1%**、偏移等效磁场（OEMF）从毫特斯拉压到几十微特斯拉以下、**温漂**通过片上热敏和数字 LUT 去消解，这些“看不见的指标”才是工程现场能不能“白天热车、晚上严寒”都稳稳工作的关键。SENIS 的讲稿把 3D 测量的频段、空间分辨率与可追溯校准写得很细，datasheet 又把 DC–300 kHz 这类硬参数给了“数”，这正是“科研标尺—工业规格”交叉验证的意义。

![](/images/wx/a49d5e4d5d745fb718caa75632992325.webp)

从更宏观的层面看，Popović的贡献像是替行业**定义了三条铁律**：其一，**结构**必须三维正交（平面+垂直），否则你永远在“丢量纲”；其二，**读出**必须抑偏移/抑 1/f/可标定（spinning current + 斩波 + 数字校正），否则你永远在“读幻觉”；其三，**工艺**必须与 CMOS 深度耦合，否则你永远在“玩昂贵的手工艺”。只要产品面向车、机、电、研这四大场景，这三条铁律就一条都躲不开。

### 这一条脉络对“未来”意味着什么

把今天的热点逐一往这张图纸上投射，会发现它们都不是“另起炉灶”，而是**在既有骨架上的加注解**。

-

**AI/ML 补偿**正在把“温漂/非线性/应力耦合”的表征学到模型里，让偏移校正从固定系数变成在线自适应，学术界对 spinning current 的现代化演绎正在以更高采样率、更强随机化进一步榨干低频噪声；

-

**二维材料/石墨烯霍尔**把迁移率、噪声本底与柔性封装带来的新自由度推向前台，但依旧要回答“正交几何+读出补偿+校准可追溯”这些老问题；

-

**新能源电驱**把**带宽/延迟**推上台前，从几千赫兹的电机，到数十上百千赫兹的功率电子开关，都需要“高带宽+低相位延迟”的磁测通道，Senis 那种 DC–300 kHz 的三轴器件之所以能横跨科研与工业，恰恰说明“结构—读出—工艺”的老三件仍然起决定性作用。

说到底，这条从 EPFL 出发的“教授—学生—公司—并购—巨头量产”的链路，已经把霍尔从物理课本搬进了人类的工程肌肉记忆：**Sentron** 把 IMC-Hall 卖进了 **Tissot T-Touch** 并在 **2004 年被 Melexis 收购**；**Senis** 把科研标尺立到了**1 µT 分辨率、DC–300 kHz 带宽**的三轴探头上；**Sensima** 把 CMOS 角度磁感做成了可并入**MPS 电源/电机控制**的大拼图；**Sentron** 本体在 **2025 年又被 Millar** 纳入纵向整合；这每一环都有可核对的新闻与数据手册作证。

等你再回头看那句最简单的提法——“现代霍尔产业的骨架来自 Popović教授”——你会发现，这不是溢美，而是把一堆硬事实串成一句最省话的结论。

### 参考文献

1.

EPFL – Radivoje Popović 教授个人主页
https://people.epfl.ch/radivoje.popovic

2.

SENIS 公司 – Popović 教授关于垂直霍尔、Sentron、Tissot T-Touch 等历史资料 (PDF)
https://www.senis.swiss/wp-content/uploads/2023/02/iemc04_popovic.pdf

3.

EE Times – Melexis 旋转位置传感器 (MLX90316) 提供非接触 360° 检测
https://www.eetimes.com/melexis-rotary-position-sensor-provides-non-contacting-360-degree-detection/

4.

PR Newswire – Monolithic Power Systems 收购瑞士 Sensima Technology SA
https://www.prnewswire.com/news-releases/monolithic-power-systems-inc-acquires-sensima-technology-sa-a-developer-of-magnetic-sensors-268500462.html

5.

Fierce Electronics – MPS 收购 Sensima 新闻报道
https://www.fierceelectronics.com/components/monolithic-power-systems-inc-acquires-sensima-technology-sa-a-developer-magnetic-sensors

6.

PR Newswire – Millar 收购 Sentron, 整合传感器业务
https://www.prnewswire.com/news-releases/millar-solidifies-its-position-as-a-leading-contract-design-and-manufacturing-partner-in-sensor-technology-with-sentron-acquisition-302380606.html

7.

Millar 官方博客 – 关于收购 Sentron 的说明
https://millar.com/Blog/Millars-Acquisition-of-Sentron/

8.

ResearchGate – Popović 教授关于垂直霍尔器件的论文 (示例)
https://www.researchgate.net/publication/242666848_The_vertical_Hall-effect_device

9.

Semantic Scholar – Spinning Current 技术综述
https://www.semanticscholar.org/paper/Spinning-current-method-for-offset-reduction-in-Hall-Popovic/

10.

SENIS 官方产品页面 – 3D Hall Probes, Teslameter 技术指标
https://www.senis.swiss/products/3d-hall-probes/

![](/images/wx/88029d0e022db03effe122b36e9950ac.webp)
