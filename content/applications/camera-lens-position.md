---
{
  "title": "相机AF与OIS：检测到镜头位置，才有闭环的依据",
  "description": "区分对焦轴向位移与防抖横向位移，解释磁反馈、双元件归一化和整条执行链的边界。",
  "date": "2026-10-27T00:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "application-single",
  "application_entry": true,
  "application_group": "消费电子",
  "weight": 31,
  "reference_topic": "相机AF与OIS位置反馈",
  "related_basics": [
    "hall-element-materials",
    "hall-temperature-drift",
    "sensor-transfer-function",
    "sensor-noise-bandwidth"
  ]
}
---
自动对焦AF与光学防抖OIS都涉及微小位移，但目标不同：AF调整光学对焦位置，OIS在需要补偿的方向移动镜组或图像传感器。驱动电流表达执行命令；位置传感器提供机构实际到了哪里的反馈，读数到位置要经过[传递关系](/wiki/basics/sensor-transfer-function/)映射。两者不能互相代替。


![磁传感与信号采集的暖纸场景插画，示意测量任务而非具体镜头结构](/images/learning/signal-quality-20261027.webp)

## 位置环要看到被控的自由度

在一种磁反馈结构中，磁体随运动件移动，固定端霍尔元件检测局部磁场，再通过标定映射成为位置。AF的轴向观测不能直接代替OIS的横向观测；多个自由度还要检查交叉耦合与可观测性。即使各通道都有读数，也要验证是否能独立分辨要求的运动。

闭环需要目标值、位置读数、控制器和执行机构。陀螺仪用于感知设备角运动，其信号并不证明镜头已执行了补偿；位置反馈与图像质量评价又属于不同层次。

## 差和比只能抵消共同的乘性变化

对两个已去零点的理想通道，设 \(v_1=A(T)g_1(x)\)、\(v_2=A(T)g_2(x)\)，则 \(r=(v_1-v_2)/(v_1+v_2)\) 可抵消共同幅度 \(A(T)\)。这需要分母远离零、两路同温且共同比例成立；不同失调、[温漂差](/wiki/basics/hall-temperature-drift/)、采样时刻或装配变化不会因此消失。

差和比在行程内仍须单调，过弱信号还会放大归一化噪声。不同磁路的毫米行程不能从一张原厂示意图直接移植；应测全行程与温度，分别保留原始通道和归一化位置。

## 验收必须同时记录命令与运动

记录驱动命令、驱动电流、原始磁读数、参考位置和时间，检查阶跃、往返、保持、温度及姿态变化。滤波过重可能使位置看起来平滑，却增加稳定时间；单点静态校准也不能证明运动时无交叉轴误差。

来源：[AKM低漂移霍尔与OIS应用](https://www.akm.com/eu/en/products/hall-sensor/tutorial/low-drift/)、[AKM高灵敏度霍尔与双元件反馈示例](https://www.akm.com/eu/en/products/hall-sensor/tutorial/high-sensitivity-hall-element/)。归一化关系为在所述条件下的本站代数推导，不对应任何具体手机或模组的实现声明。
