---
{
  "title": "MR比、桥路灵敏度与精度：三个数字别排成一个榜",
  "description": "说明磁阻变化率的分母、桥路电压和系统误差为何不能直接互换。",
  "date": "2026-10-27T00:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "磁场与信号基础",
  "weight": 206,
  "related_basics": [
    "magnetic-bridge",
    "amr",
    "gmr",
    "tmr"
  ],
  "related_applications": [
    "servo-motor",
    "handheld-joystick"
  ]
}
---
看到“MR比更大”，可以先问两件事：电阻相对哪个状态变化，输出经什么桥路和读出电路转换。磁阻变化率能说明材料与结构的响应，却不能直接给出一颗角度芯片的系统精度。

## 百分比需要先交代分母

常见定义是 \(MR=(R_{AP}-R_P)/R_P\)，P与AP分别表示两磁化层平行、反平行状态。若自设 \(R_P=1\) kΩ、\(R_{AP}=2\) kΩ，按此定义是100%；换成以 \(R_{AP}\) 作分母就是50%。两种报告数字不能不看定义就比较。

AMR的高低电阻则对应磁化与电流的相对方向，物理结构与P/AP自旋阀不同。摘录百分比时应连同材料、结构、磁场、温度和测试方式一起保留，不把某厂某代材料的示例值当成所有AMR/GMR/TMR的固定范围。

## 从电阻到电压还经过桥路

桥压取决于哪些桥臂随场增减、变化是否对称、激励大小及后级负载。[电桥分压式](/wiki/basics/magnetic-bridge/)可以直接计算，不能把单电阻100%的变化率照抄成输出100%电源摆幅。成品手册的mV/V、mV/mT和mV/°也分别描述不同的横轴与激励条件。

## 更大信号只改善误差链的一部分

增大信号幅度有利于降低后级固定电压噪声的相对影响；桥自身噪声、磁滞、温漂、磁化跟随、机械偏心及算法误差仍在。角度对通道误差的敏感性还与瞬时信号向量有关。做选型比较时应固定磁路、温度、带宽与校准条件，再比较角度误差和抖动，不能从MR比推出“必然更准”。

来源：[TDK-Micronas：TMR结构与MR比](https://www.micronas.tdk.com/en/technologies/tmr-angle-sensors)、[TDK：TMR角度传感原理](https://product.tdk.com/en/techlibrary/productoverview/tmr-angle-sensors.html)。电阻例及桥路推导为本站自设算例。
