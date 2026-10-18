---
{
  "title": "夹爪：测到开度，还没有测到夹持力",
  "description": "比较电机角、连杆角与直线磁位置反馈，检验反向间隙、目标物接触和安全边界。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-18",
  "layout": "application-single",
  "application_entry": true,
  "application_group": "工业与运动",
  "weight": 210,
  "related_basics": ["magnetic-encoder", "mounting", "angle-noise"],
  "reference_topic": "夹爪"
}
---

夹爪反馈首先要回答测的是电机、丝杆、连杆还是指尖。电机已经停止转动，手指仍可能因齿隙、柔性指垫和目标物压缩而继续变化。要求“开度分辨率”之前，应先确定需要闭环控制哪一个实际尺寸。

## 传感器可以放在不同运动环节

旋转关节可读连杆角，再按机构关系换算指尖距离；直线滑块可带磁铁从固定读头旁经过。后者读取的是磁场随位置的变化，必须标定有效行程，不能把三轴磁场数据直接按固定比例当毫米。

按测量量、输出与边界比较：

- [TI TMAG5273](https://www.ti.com/product/TMAG5273)：三轴磁场→I²C；滑块行程仍需磁路映射。
- [Melexis MLX90333](https://www.melexis.com/en/product/MLX90333/Triaxis-mainstream-rotary-linear-and-joystick-position-sensor-IC-Analog-PWM-SPI)：磁位置处理→模拟、PWM或SPI配置；应按所选模式设计机构。
- [昆泰芯KTH7111](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html)：旋转角→SPI、ABZ等；适合比较转动环节，不能把单个角度码直接当全行程毫米值。

它们都是传感链候选，不是成套夹爪或互换料清单。

## 最先检查的是行程内是否存在歧义

磁铁在不同位置产生相近读数，或靠近端点时信号变化过小，都会使位置反演失去可靠性。金属工件靠近、另一根手指上的磁铁移动，也可能改变场。需要在整段行程和工件材料变化下检查，不只在空爪中央位置校准。

开度也不能直接换成夹持力。不同物体刚度、指垫温度、机构摩擦会改变力与位移关系。若任务需要精确力控，应另建受力测量与标定路径，不能拿电机堵转或“位置没变”作为已知夹持力。

## 让验证落到抓取过程

记录张开、闭合、接触后保持和释放的重复轨迹，用独立量具核对指尖距离与左右不对称。再测掉电、线缆断开、磁体移位和受阻时的响应。普通位置反馈不等于人员防夹保护；是否允许与人接触，要由整机风险评估、保护结构和安全功能共同决定。
