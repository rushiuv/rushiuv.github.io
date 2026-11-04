---
title: "TSMC：Chiplets和3D封装技术"
date: "2026-10-29T09:09:00+08:00"
slug: "wechat-l9zqeh1zg0etdqykbi_gtq"
description: "3DFabric 是台积电先进封装技术，包括 CoWoS、InFO、SoIC，分为前端 3D（芯片堆叠 SoIC）与后端 3D 先进封装（InFO、CoWoS）两大体系，三者可以互相组合，实现「3D×3D」的混合异构集成。"
original: "https://mp.weixin.qq.com/s/L9zqeh1ZG0ETdQyKBi_gTQ"
original_from: "首发于公众号「智能计算芯世界」"
companies:
- 台积电
tags:
- AI
---

![TSMC 3DFabric：Frontend 3D（SoIC）与 Backend 3D（InFO、CoWoS）](images/001-a82106c31b.png)

**3DFabric** 是台积电先进封装技术，包括 **CoWoS**、**InFO**、**SoIC**，分为前端 3D（芯片堆叠 SoIC）与后端 3D 先进封装（InFO、CoWoS）两大体系，三者可以互相组合，实现「3D×3D」的混合异构集成。

技术主线围绕单芯片摩尔缩放放缓，依靠异构芯粒集成突破算力、带宽、内存墙；两大前沿方向是**散热**（高算力堆叠最大痛点）与**硅光 COUPE**（共封装光学 CPO 路线）。

本文将对《TSMC Packaging Technologies for Chiplets and 3D》进行分析，详细介绍 CoWoS、InFO、SoIC。

![TSMC Packaging Technologies for Chiplets and 3D 讲义插图 1](images/002-b8ad1e04d7.png)

![TSMC Packaging Technologies for Chiplets and 3D 讲义插图 2](images/003-741dcb45b1.png)

![TSMC Packaging Technologies for Chiplets and 3D 讲义插图 3](images/004-b275a583cd.png)

![TSMC Packaging Technologies for Chiplets and 3D 讲义插图 4](images/005-c6db49ff08.png)

![TSMC Packaging Technologies for Chiplets and 3D 讲义插图 5](images/006-66c2e874f5.png)

![TSMC Packaging Technologies for Chiplets and 3D 讲义插图 6](images/007-72588db689.png)

![TSMC Packaging Technologies for Chiplets and 3D 讲义插图 7](images/008-533c754534.png)

## 二、InFO（Integrated Fan-Out）

RDL 重布线层为核心的扇出封装家族，衍生版本多：InFO-R、InFO-L、InFO_B、InFO_oS、InFO_SoIS、InFO_SoW。

### 核心技术特点

1. 以 **RDL 重布线层**做互连，不需要昂贵硅中介层，成本相比 CoWoS-S 更低；InFO-L 额外集成 LSI 局部硅互连提升局部带宽。
2. **InFO-B**：面向移动端 PoP 封装，支持 LPDDR 堆叠，寄生参数低，搭配 DTC 深沟槽电容改善供电。
3. **InFO-oS**：面向 HPC，可扩展到 1.5X、2X、2.5X 光罩尺寸；最小 2/2μm RDL 布线，支持大尺寸多 chiplet 横向集成。
4. **InFO-SoIS**：集成式有机基板，高频下插入损耗比传统有机基板低 25–30%，91/110mm² 大尺寸，高良率。
5. **InFO-SoW（晶圆级系统）**：整片晶圆做系统集成；带宽密度为传统 MCM 的 2 倍，PDN 电源阻抗仅为传统 MCM 的 3%，可集成电源模块、散热模块，面向超大规模 AI 计算。

### 适用场景

1. 移动消费电子：InFO-B / InFO PoP，手机应用处理器 AP，搭配 LPDDR 内存堆叠（如苹果 A 系列）；
2. 网络交换机芯片：InFO-oS，支持超高交换带宽（51.2Tbps 级别）；
3. 中大型 HPC 小芯片：对成本敏感、不需要 HBM 的多 chiplet 横向集成；
4. 晶圆级超大规模 AI 系统：InFO-SoW，类 Cerebras 晶圆级引擎；
5. 高频 SerDes 系统：InFO-SoIS，射频 / 高速信号，降低插入损耗。

![InFO 相关讲义插图 1](images/009-dd69d7042c.png)

![InFO 相关讲义插图 2](images/010-3259405301.png)

![InFO 相关讲义插图 3](images/011-e13f9e6dc9.png)

![InFO 相关讲义插图 4](images/012-cd0ed1ed82.png)

![InFO 相关讲义插图 5](images/013-9b00eb7b57.png)

![InFO 相关讲义插图 6](images/014-08ac3e0daa.png)

![InFO 相关讲义插图 7](images/015-65c46fd01f.png)

![InFO 相关讲义插图 8](images/016-0fd1be578a.png)

![InFO 相关讲义插图 9](images/017-2e374e5ab2.png)

![InFO 相关讲义插图 10](images/018-0e89fc3b49.png)

![InFO 相关讲义插图 11](images/019-ee4cb9967c.png)

![InFO 相关讲义插图 12](images/020-cc80388937.png)

![InFO 相关讲义插图 13](images/021-5e4f44f982.png)

![InFO 相关讲义插图 14](images/022-a2f068dc43.png)

## 三、CoWoS（Chip-on-Wafer-on-Substrate）

经典 2.5D 封装，芯片横向排布在中介层上，三大子类：CoWoS-S（硅中介层）、CoWoS-R（RDL 中介层）、CoWoS-L（LSI+RDL 复合中介层），2011 年开始量产，拥有多代演进。

### 核心技术特点

1. **CoWoS-S**：采用硅中介层 + TSV，是 HBM 标配；可集成 eDTC 嵌入式深沟槽电容；中介层持续迭代，支持 3-reticle 超大尺寸，最多可搭载 8 颗 HBM2E/HBM3；硅中介层还可以降低大芯片 CPI（芯片-封装交互应力），相比普通倒装芯片应力下降 60%。
2. **CoWoS-R**：RDL 有机中介层，替代部分硅中介层，平衡成本与规模。
3. **CoWoS-L**：集成 LSI 局部硅互连桥，兼顾高密度局部互连与大封装尺寸，适配超大规模异构 chiplet。
4. **STAR 标准架构**：标准化 HBM 布局，缩短客户设计周期，加速上市。
5. 擅长逻辑芯片 + HBM 高速内存的并排集成，横向带宽极高；散热条件优于 SoIC 垂直堆叠。

### 适用场景

1. AI 训练、HPC、GPU：CoWoS-S，逻辑芯片搭配多颗 HBM，追求巨大内存带宽（当前主流场景）；
2. 高端服务器、数据中心加速卡；
3. 超大规模异构 chiplet：多颗大芯片 + 多 HBM，使用 CoWoS-L；
4. 需要标准架构快速流片的项目，选用 CoWoS STAR。

![CoWoS 相关讲义插图 1](images/023-f44614497b.png)

![CoWoS 相关讲义插图 2](images/024-08a8bf1291.png)

![CoWoS 相关讲义插图 3](images/025-1a7a3fbd32.png)

![CoWoS 相关讲义插图 4](images/026-847ef342b7.png)

![CoWoS 相关讲义插图 5](images/027-736e35db30.png)

![CoWoS 相关讲义插图 6](images/028-d1ea3fb746.png)

![CoWoS 相关讲义插图 7](images/029-47329a3ecc.png)

## 一、SoIC（System on Integrated Chips）

真正的 3D 垂直堆叠，属于晶圆厂前端工艺，分为 CoW（芯片对晶圆）、WoW（晶圆对晶圆）两种堆叠模式，采用混合键合（Hybrid Bonding）+ TSV 硅穿孔实现芯片垂直互连。

### 核心技术特点

1. **超高密度垂直互连**：键合间距可做到 0.9μm 亚微米级别，互连密度远高于传统微凸点；支持多层芯片垂直堆叠（演示到 12 层堆叠），信号路径极短、延迟低、带宽极高。
2. **支持同/异质裸片堆叠**：可堆叠不同工艺节点、不同功能良率裸片 KGD（逻辑、存储、电容等），例如 N7-on-N7、N5-on-N5，Logic-on-DTC 深沟槽电容，可降低电压跌落（power droop）。
3. **可与 InFO/CoWoS 组合**：SoIC 完成芯片垂直堆叠后，可以再放到 InFO 或者 CoWoS 封装中，形成「3D 堆叠 + 2.5D 封装」复合方案。
4. **挑战**：垂直堆叠带来热管理压力大，需要配套高级散热方案。

### 适用场景

1. HPC/AI：计算芯片与高速缓存垂直堆叠，追求极致片间带宽、极低访存延迟；
2. 异构小芯片：把拆分后的同/异质 chiplet 做垂直堆叠，减小整体封装面积；
3. 硅光 COUPE 引擎：用于光子引擎 EIC-PIC 高密度低寄生互连；
4. 高端移动：需要紧凑体积、高电源完整性的堆叠方案。

![SoIC 与组合封装讲义插图 1](images/030-47eeeeb68b.png)

![SoIC 与组合封装讲义插图 2](images/031-598aa3874d.png)

![SoIC 与组合封装讲义插图 3](images/032-339a27bd5e.png)

![SoIC 与组合封装讲义插图 4](images/033-f81bfcd848.png)

![SoIC 与组合封装讲义插图 5](images/034-5738d9a37e.png)

![SoIC 与组合封装讲义插图 6](images/035-b874261364.png)

![SoIC 与组合封装讲义插图 7](images/036-d669398ed1.png)

![SoIC 与组合封装讲义插图 8](images/037-17bd8d99f6.png)

![SoIC 与组合封装讲义插图 9](images/038-26d00d7731.png)

![SoIC 与组合封装讲义插图 10](images/039-387aa08fc1.png)

![SoIC 与组合封装讲义插图 11](images/040-965826abab.png)

![SoIC 与组合封装讲义插图 12](images/041-285d6fb685.png)

![SoIC 与组合封装讲义插图 13](images/042-ec7c98127b.png)

![SoIC 与组合封装讲义插图 14](images/043-4090acea8d.png)

![SoIC 与组合封装讲义插图 15](images/044-7881a084ca.png)

![SoIC 与组合封装讲义插图 16](images/045-a2769155c6.png)

![SoIC 与组合封装讲义插图 17](images/046-228085f188.png)

三者可以组合，例如 SoIC 做垂直堆叠，再把堆叠完成的裸片放到 CoWoS/InFO 里，实现垂直 + 横向混合集成，充分发挥各自优势。
