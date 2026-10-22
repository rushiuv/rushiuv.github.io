---
{"title":"闸机：翼门位置反馈不能代替防夹检测","description":"角度用于确认门翼状态，通道占用与夹持风险仍需要独立感知和保护逻辑。","date":"2026-10-18T10:00:00+08:00","lastmod":"2026-10-18","layout":"application-single","application_entry":true,"application_group":"工业与运动","weight":205,"related_basics":["absolute-incremental","mounting","latency"],"reference_topic":"闸机"}
---

摆闸或翼闸需要知道门翼已经开到哪里、关到哪里，以及运动是否按计划进行。磁角度反馈可以读轴的位置，但不能仅凭一条角度判断通道是否有人，也不能确认门翼与传动轴之间没有松脱。

## 安装位置决定看见哪段运动

传感器若装在电机轴上，中间的减速器回差、联轴器松动和门翼变形不一定都进入反馈。装到输出端更接近门翼角度，却要重新考虑轴心空间、线束和机械固定。不能把电机转过规定角度直接写成翼门已经到位。

轴心空间是否可用，应先于品牌和位数决定候选范围：

| 候选 | 测量量或输出 | 适用边界 | 原厂来源 |
|---|---|---|---|
| TI TMAG5170 | 多轴磁场与角度计算 | 磁体路径、选轴和映射需验证 | [详情](https://www.ti.com/product/TMAG5170) |
| Infineon TLE5012B | 磁场方向角度 | 按感应轴与原厂磁路安装 | [详情](https://www.infineon.com/part/TLE5012B-E5000) |
| 昆泰芯 KTH7101 | 霍尔磁绝对角度 | 校准与动态条件须按型号核对 | [详情](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/magneticencoder/index.html) |
| 昆泰芯 KTM5300 | 离轴AMR角度 | 让出轴心仍需匹配磁体与校准过程 | [详情](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/KTM53XX/index.html) |

KTM5300的离轴路线可以进入中空结构评估，不代表任意侧置磁体都能测准。四者都只是反馈候选，门翼承重与安全功能仍需整机设计，本文不表示某家闸机已采用这些料号。

## 到位与运动受阻需要不同证据

假设目标位置为90°，容许区间由机构先行定义。读数进入区间只证明反馈值到位；若门翼撞到物体后轴系扭转，单个角度读数无法自动区分正常停止与受阻。速度、电流、独立通道检测及机械保护各提供不同证据。

## 验证要覆盖重启和异常动作

在安全测试条件下检查断电重启、手动推门、反向回弹、磁体松动、传感器断线与通信失效。状态机应区分未知位置与关门到位，不能把无新数据默认为安全位置。防夹、紧急疏散和门翼力限制需要独立风险分析及适用标准验证，不能由芯片的精度或诊断功能替代。

## 原厂资料

- [TI TMAG5170](https://www.ti.com/product/TMAG5170)
- [Infineon TLE5012B-E5000](https://www.infineon.com/part/TLE5012B-E5000)
