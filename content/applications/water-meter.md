---
{
  "title": "水表：磁脉冲能记转数，体积还要靠计量关系",
  "description": "比较低功耗磁计数与超声路线，检查启动小流量、漏脉冲、反流和外磁干扰。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-24",
  "layout": "application-single",
  "application_entry": true,
  "application_group": "工业与运动",
  "weight": 219,
  "related_basics": [
    "magnetic-encoder",
    "abz",
    "mounting"
  ],
  "reference_topic": "水表",
  "related_guides": [
    "rate-budget",
    "position-validity-state"
  ],
  "related_model_slugs": [
    "ktm1301"
  ]
}
---

带旋转计量机构的水表可以把磁体固定在叶轮或传动部件上，由干区霍尔器件记录磁极经过。芯片测到的是磁场事件，不是直接测到多少升。每个脉冲对应的体积必须来自整表结构、标定和适用流量范围，不能只由磁极数量决定。

## 功耗与漏计要放在同一张账里

候选按事件量、输出与边界比较：

- [TI DRV5032](https://www.ti.com/product/DRV5032)、[Allegro A1171](https://www.allegromicro.com/en/products/sense/switches-and-latches/switches/a1171)：霍尔磁事件→开关量；均需按订货号核对更新方式、极性和阈值。
- [昆泰芯KTM1301](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/magnetoresistiveSwitchSeries/index.html)：TMR磁事件→CMOS开关；50Hz与5000Hz等版本不能混用功耗和漏计结论。
- [昆泰芯KTH4622](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/highsensitive2Dhallswitch/index.html)：二维磁场变化→速度与方向信号；需要匹配磁体轨迹和采样版本，不直接给出体积。

这些都不是完整水表芯片或整表计量等级证明。

休眠采样可降低平均电流，却可能错过短于观测间隔的磁场事件。应在最大流量、最小磁体有效宽度与最差气隙下验证，不把静止时的低功耗直接换算成动态计数可靠性。系统功耗还包括主控唤醒、上拉与通信，不能只看传感器典型值。

## 一个脉冲通常不能解释反流

单开关能计事件，但方向信息需要额外空间相位或其它观测。机械摆动在阈值附近反复经过时，也可能与真实累计流量混淆。若要求反流识别，应核对双通道的相位、时序和状态机，而不是简单把任何边沿都加一。

磁传感路径与超声飞行时间是不同的计量架构；超声方案没有旋转叶轮脉冲，不能强行套编码器每圈模型。强外磁监测也要另行定义，不能把普通开关翻转直接当成篡改证据。

## 验证用体积参照闭环

在启动小流量、最大流量、反向流动和温度变化下，同时核对原始事件与已知体积，检查停水摆动、掉电保存和电池末期表现。磁体更换或计量机构变化后需要重新验证。芯片可用只是计量链的一环，整表的法定计量检验与环境要求仍需分别满足。


## 最大流量先量磁事件持续多久

[TI DRV5032原厂资料](https://www.ti.com/product/DRV5032)提供不同采样率、阈值和输出版本，因此低功耗比较必须带订货号。先读[动作与释放阈值](/wiki/basics/bop-brp/)及[AB相方向判别](/wiki/basics/abz/)，再按[速率预算](/topics/guides/rate-budget/)检查事件宽度。

自设磁场越过动作阈值仅持续6ms，而理想周期采样间隔为50ms；即使平均脉冲频率很低，也可能整段落在两次观测之间。此例只说明漏观测可能，不推算具体芯片漏计率。最大流量台架上同步留磁场/开关边沿、时间和体积参考，分别核正流、反流与停水摆动；若边沿数偏少，先检查持续时间和气隙，不先改体积系数。按[位置数据有效性](/topics/guides/position-validity-state/)的分层思想区分事件缺失与记录冻结，未知流向不能直接计正向体积。
