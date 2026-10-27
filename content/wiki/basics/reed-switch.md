---
{
  "title": "干簧管与固态磁开关：无待机电流不等于无系统代价",
  "description": "区分机械触点、电子阈值与整个唤醒电路的耗电，按真实负载和动作窗口比较。",
  "date": "2026-10-27T00:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "磁敏机理与器件",
  "weight": 311,
  "related_basics": [
    "switch-polarity",
    "bop-brp",
    "amr"
  ],
  "related_applications": [
    "laptop-lid",
    "water-meter"
  ]
}
---
干簧管利用磁场使封在玻璃管内的铁磁簧片吸合，是有实际触点的磁开关。霍尔或AMR开关则用敏感元件与电子电路产生状态。选型时，两者都先看动作窗口和输出负载，不能只比“有没有接触”。

## 簧片不需偏置，读取电路仍可能耗电

干簧管本体可以不加传感偏置；MCU上拉、分压、扫描和唤醒电路仍会耗电。自设3 V通过100 kΩ上拉、闭合触点接地，闭合期间就有30 µA电流。把元件的零待机宣传直接写成整机零功耗，会漏掉这一项。

固态磁开关需要供电，低功耗版本常用周期采样减少平均电流。其检测周期与启动等待可能影响快速动作捕获；必须把本体、读取电路与待机占空一起计算。

## 触点额定值与回差要按工况核对

干簧管有接触电阻、触点负载、弹跳和寿命条件；感性负载与浪涌不能只按稳态电流判断。玻璃封装也需要考虑装配应力。固态开关没有簧片触点磨损，但仍有输出电流、ESD和供电范围的限制。

两种路线都可能具有动作与释放窗口。干簧管常见的AT灵敏度是在规定线圈测试条件下取得，不能不看测试几何直接换成任意磁体的毫米距离。磁开关的B阈值也需要通过磁路映射到机构位置。

## 替换时沿整条故障链验证

[表计计数](/applications/water-meter/)要检查最短脉冲与读取功耗，[合盖检测](/applications/laptop-lid/)要检查附件误触发。沿真实磁体轨迹测试接近、远离、振动、最快动作和线路故障；输出形式不同还要核输入电平与上拉，不能仅按同样“ON/OFF”换料。

来源：[Littelfuse：干簧开关技术](https://www.littelfuse.com/products/magnetic-sensors-and-reed-switches/reed-switches)、[村田：AMR与干簧开关区别](https://www.murata.com/en-global/products/sensor/amr/overview/basic/difference-reed-switch)。功耗算例为本站自设读取电路。
