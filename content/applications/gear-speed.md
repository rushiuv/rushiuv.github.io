---
{
  "title": "齿轮转速检测：齿轮改变磁路，脉冲才变成转速",
  "description": "区分背偏置铁磁齿轮与交替磁极轮，按齿距、气隙、事件定义和低速行为解释速度与方向。",
  "date": "2026-10-27T00:00:00+08:00",
  "layout": "application-single",
  "application_entry": true,
  "application_group": "工业与运动",
  "weight": 232,
  "related_basics": [
    "hall-effect",
    "latch",
    "air-gap",
    "sensor-noise-bandwidth",
    "abz"
  ],
  "reference_topic": "齿轮与磁极轮测速",
  "related_guides": [
    "rate-budget",
    "position-validity-state"
  ],
  "lastmod": "2026-10-27"
}
---

没有在每个齿上贴磁铁，也可以用磁传感器测铁磁齿轮：固定磁体提供背偏置磁场，齿和齿槽经过时改变局部磁路，再由霍尔或磁阻元件读出变化。它与交替磁极轮是两种目标结构，不能共用一套未经验证的阈值。

## 先确认谁在产生磁场

[TI SBAA632](https://www.ti.com/lit/an/sbaa632/sbaa632.pdf)介绍背偏置三维霍尔与铁磁齿轮的相互作用。[Infineon TLE5555说明](https://community.infineon.com/t5/Knowledge-Base-Articles/Overview-of-XENSIV-TLE5555-TMR-speed-sensor-protocols/ta-p/1065738)则区分磁极轮、需外配背偏置磁体的齿轮版本和带磁体版本。选型首先核对目标与磁路，而不是只比较“霍尔还是TMR”。

齿高、齿槽、齿距、轴向偏移与[气隙](/wiki/basics/air-gap/)都会改变敏感位置的场形。某个参考齿轮下的最大气隙，不能直接当成所有模数齿轮的保证值。普通非铁磁金属齿轮也不能直接沿用这套铁磁磁路方案。

## 每齿脉冲定义清楚，转速公式才有意义

若Z个等距齿、每齿产生一个被计数脉冲，脉冲频率f与转速n满足n=60f/Z。自设Z=60、f=500Hz，则n=500rpm。若固件改数上升沿和下降沿，必须同步修改每圈事件数，否则同一根轴会被算成两倍速度。

低速时测两个边沿的间隔更容易获得细时间信息，但等待时间变长；高速时固定窗口计数有更多事件，却必须检查最短脉宽、带宽和定时器输入。参见[速率预算](/topics/guides/rate-budget/)，不能仅凭平均频率低于采样率判断不会漏齿。

## 没有新边沿不等于已经确认静止

单路等距脉冲通常不含方向，换向和往复摆动需额外相位信息或专用协议，原理可接到[AB方向判别](/wiki/basics/abz/)。单路没有边沿也可能来自断线、磁体异常或信号过弱，速度超时与[数据有效性](/topics/guides/position-validity-state/)应分别报告。

台架在极低速、反转、最大转速及最差偏摆下同步留原始磁场或脉冲与独立转速参考。它可以为电机和传动提供速度证据，却不自动成为上电绝对角编码器；与[无刷电机换相](/applications/brushless-dc-motor/)结合时还需另对齐电零位。
