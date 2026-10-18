---
{
  "title": "气缸位置检测：到位开关与连续行程是两种任务",
  "description": "从活塞磁体、缸筒与外部读头建立测量路径，检查有效行程、重复位置和钢结构影响。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-18",
  "layout": "application-single",
  "application_entry": true,
  "application_group": "工业与运动",
  "weight": 221,
  "related_basics": ["magnetic-encoder", "mounting", "self-calibration"],
  "reference_topic": "气缸位置检测"
}
---

气缸上的磁性开关通常观察活塞磁体是否进入某个区域，适合到位确认；连续位置控制则要求在有效行程内区分每个位置。把一个开关换成分辨率更高的磁场芯片，并不自动得到整根气缸的毫米读数，磁场与行程关系还要建立。

## 读头看到的是经过缸筒的磁场

磁体随活塞移动，传感器可以固定在缸外。缸筒材料、壁厚、安装槽、磁体方向和旁边钢制支架都会改变读头看到的场。场强相同的两个位置若方向也不足以区分，就存在位置歧义，必须缩短工作区、增加观测维度或采用多个读头。

先按测量量、输出与覆盖范围分开比较：

- [TI TMAG5170](https://www.ti.com/product/TMAG5170)：三轴磁场→SPI；连续行程仍需映射与标定。
- [Melexis MLX90333](https://www.melexis.com/en/product/MLX90333/Triaxis-mainstream-rotary-linear-and-joystick-position-sensor-IC-Analog-PWM-SPI)：磁位置→模拟、PWM或SPI配置；有效区间由实际磁路决定。
- [昆泰芯KTM2802](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/hvcpDetectionSensor/index.html)：水平磁场进入阈值区→两线或三线开关；它是气缸到位检测路线，不是连续位移尺。

这些候选不能保证穿透任意缸筒，也不表示旧开关接线可以直接复用。

## 最先约束有效覆盖区间

磁体远离时信号变小，靠近时又可能超量程。有效行程由这两个边界以及场形是否唯一共同确定。需要长行程时，阵列拼接要校对不同读头的零点、增益和接力区，不能用单点灵敏度外推整段精度。

位置也不等于推力或速度已经可控。气压、负载、密封摩擦与压缩性会改变运动，即使位置测量准确，阀和控制系统仍需满足动态要求。用相邻位置求速度还会放大噪声，滤波延迟要进入预算。

## 验证包含伸出与缩回两条轨迹

用独立位移参考，检查全行程、两方向、不同压力负载和温度下的误差，保留磁场原始量与状态。再测磁体松动、旁边气缸动作与线路中断。到位信号只能证明规定观测成立，不能代替夹伤防护、机械锁定或设备的安全停机功能。
