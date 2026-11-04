---
{
  "title": "TMR：隧道结的高响应不等于整机高精度",
  "description": "理解参考层、自由层与绝缘势垒，分清方向测量、线性磁场测量和系统角度误差。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "磁敏机理与器件",
  "weight": 309,
  "related_basics": [
    "amr",
    "gmr",
    "magnetic-hysteresis",
    "resolution-accuracy"
  ],
  "related_applications": [
    "robot-joint",
    "servo-motor"
  ],
  "related_guides": [
    "amplitude-temperature-error",
    "magnetic-field-coordinates"
  ]
}
---
TMR（隧道磁阻）使用两个磁性层之间的薄绝缘势垒。电子通过量子隧穿越过势垒，两层磁化方向的相对关系改变，隧穿电阻随之变化。与[GMR](/wiki/basics/gmr/)相比，中间层由金属换成了绝缘势垒，不能把两种图画成同一种导电连接。[TDK原理说明](https://www.micronas.tdk.com/de/produkte/tmr-angle-sensors)

## 能测方向的桥路仍有工作磁场范围

角度结构让自由层在规定磁场中跟随目标方向，参考层提供方向基准；组合桥路可形成正交信号，再计算角度。TAD2141手册公开了双桥方向检测与数字处理框图，是具体实现的例子，不代表所有TMR产品均有相同功能。[TAD2141手册§3.2.1](https://product.tdk.com/info/en/documents/datasheet/tmr-angle/ds_sensor_tmr-angle_tad2141_en.pdf)

完整一圈方向可观测，也不等于机械整圈绝对位置天然可观测。多极磁环产生重复周期时，仍需[极对数](/wiki/basics/pole-pairs/)与判区信息。线性磁场TMR、磁开关和饱和方向TMR则有不同工作区，磁场范围必须按具体型号确认。

## 大输出降低某项相对误差，不会抹去磁路错误

自设正交两路峰值100mV、单通道残余偏置1mV。在小扰动近似下，最大角误差约为 \(1/100=0.01\)rad，即0.573°。若幅度加倍、偏置保持不变，这一项约减半；这是本站理想算例，不是任何TMR产品的保证精度。

磁铁偏心造成的方向畸变、外场叠加和采样延迟并未被这个比例消除。比较[AMR](/wiki/basics/amr/)与TMR时，要对齐磁路、带宽、校准和温度，而不是只比较“输出多少毫伏”。

## 先拆误差，再决定校准能修哪一项

台架保存每通道偏置、幅度、相位和参考角，按[幅值与温度误差](/topics/guides/amplitude-temperature-error/)分别判断。桥路漂移可能需要电路或校准处理；[机器人关节](/applications/robot-joint/)电流带来的附加磁场，则要改变安装、场分布或采用规定的抑制结构。即便芯片有补偿功能，也须核对它抑制的外场方向和空间分布。
