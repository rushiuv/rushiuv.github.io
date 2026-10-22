---
{"title":"断路器：电流检测快，不等于整机分断快","description":"区分电流传感、故障判断与执行机构，避免把芯片响应时间写成保护链总延迟。","date":"2026-10-18T10:00:00+08:00","lastmod":"2026-10-18","layout":"application-single","application_entry":true,"application_group":"工业与运动","weight":202,"related_basics":["latency","stray-field","angle-noise"],"reference_topic":"断路器"}
---

电子保护链先测电流，再决定是否触发，最后由执行结构切断回路。霍尔电流传感器测的是导体电流产生的磁场，不是直接测触头是否分开；即使传感器已经报警，执行链仍需要自己的供电、驱动和状态确认。

## 两类器件只负责链路的一部分

必须先区分完整电流传感器和仅测磁场的前端：

| 候选 | 测量量或输出 | 适用边界 | 原厂来源 |
|---|---|---|---|
| TI TMCS1123 | 隔离电流测量与过流检测 | 隔离、量程与门限按料号核对 | [详情](https://www.ti.com/product/TMCS1123) |
| Allegro ACS724 | 隔离霍尔电流测量 | 电流路径、温漂与带宽需验算 | [手册](https://www.allegromicro.com/~/media/files/datasheets/acs724-datasheet.ashx) |
| 昆泰芯 KTH3105 | 比例式磁场模拟电压 | 若研究分立磁路，需另建电流映射、ADC和隔离 | [KTH31型号表](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/proportionallinerhalleffectsensor/index.html) |

KTH3105不是带隔离导体的电流模块，不能套用前两者的安培量程或隔离额定值。它只是在定制磁路研究中可评估的磁场元件；磁芯、母排、绝缘与完整保护动作均未由该型号证明。这里不声称三者能直接组成某一额定分断能力的断路器。

假设传感与判断合计20微秒、执行机构又耗时2毫秒，则总链已超过2毫秒；不能只拿传感器的微秒级参数作为“断电速度”。这些是假设时间，用来说明串联时序，不是上述器件指标。

## 故障电流不一定留在测量范围内

正常工作时漂亮的波形，不代表短路瞬态也不饱和。应分别确认测量范围、输出限幅、过流门槛、恢复时间及断线表现。大电流自热、附近母排磁场和供电跌落，又会同时作用到前端。

## 验收看完整保护动作

验证不仅记录电流波形与报警沿，还要记录驱动、触头或半导体开关实际关断事件。隔离额定值对应特定器件和试验条件，不等于整机爬电距离、温升与开断能力已合格。高压短路试验应交由具备资质和防护条件的团队，不能按本页制作或改装保护设备。

## 原厂资料

- [TI TMCS1123](https://www.ti.com/product/TMCS1123)
- [Allegro ACS724数据手册](https://www.allegromicro.com/~/media/files/datasheets/acs724-datasheet.ashx)
