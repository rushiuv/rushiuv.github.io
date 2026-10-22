---
{"title":"电子棋盘：知道有棋子，不等于知道是哪一枚","description":"磁开关适合判断占位，多轴磁场可以增加信息，但棋子身份、邻格串扰和扫描时序仍需另行设计。","date":"2026-10-18T10:00:00+08:00","lastmod":"2026-10-18","layout":"application-single","application_entry":true,"application_group":"消费电子","weight":2,"related_basics":["magnetic-encoder","stray-field","interfaces"],"reference_topic":"电子棋盘"}
---

棋子底部放磁体，格子下方检测磁场，可以在没有电接点的情况下判断占位。但“一格一个磁开关”通常只回答有无棋子；把车、马、炮或不同颜色编码出来，需要更多可区分的信息，不能从一个高低电平里凭空恢复身份。

## 先确定棋盘需要识别到哪一层

按“二值占位还是保留磁场”分候选，比按品牌分更有意义：

| 候选 | 测量量或输出 | 适用边界 | 原厂来源 |
|---|---|---|---|
| TI DRV5032 | 霍尔开关状态 | 判断占位，不直接识别棋子 | [详情](https://www.ti.com/product/DRV5032) |
| Infineon TLE493D-W2B6-A1 | 三轴磁场，I²C | 保留更多信息，需算法与扫描设计 | [详情](https://www.infineon.com/part/TLE493D-W2B6-A1) |
| 昆泰芯 KTH1604 | 单极型开关，两路输出 | 核对磁体极性、门限与采样后缀 | [具体型号表](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/microPowerSeries/index.html) |
| 昆泰芯 KTH4603 | 三维全极磁开关 | 增加触发方向覆盖，不输出连续XYZ值 | [详情](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/highlysensitive3dhallswitch/index.html) |

三维开关和三轴连续磁场不是同一种信息量；两个开关脚也不能直接当成棋子身份编码。

即使用磁体强弱编码，棋子离板高度、偏放位置与制造离散也会改变读数。两个身份的磁场分布如果重叠，软件阈值就无法稳定分开。若规则允许从已知初始局面推演走棋，应明确这是规则推断，不是传感器直接识别。

## 最容易漏掉的是满盘测试

只测一个棋子不足以验证棋盘。应保留邻格放满、相邻棋子同时提起、两枚棋子交叉移动和棋子倒置等记录，检查相邻磁体的叠加是否把空格误判为有棋。棋盘厚度和面板翘曲也要纳入气隙范围。

## 扫描系统必须跟上人的动作

阵列需要核对地址数量、总线负载、复用方式与每轮扫描时间，不能假设同型号器件可以无限并接。若相邻两格不是同一时刻读取，快速移动可能短暂显示两格都有或都没有。事件判定应保留时间戳、去抖与不确定状态，再用完整落子序列验收；提高单点分辨率并不能代替这些系统检查。

## 原厂资料

- [TI DRV5032](https://www.ti.com/product/DRV5032)
- [Infineon TLE493D-W2B6-A1](https://www.infineon.com/part/TLE493D-W2B6-A1)
