---
{
  "title": "机器人关节：电机角与输出角各管哪一段",
  "description": "区分换相反馈、关节定位和传动链观测，从测点、同步与断电状态确定编码器方案。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-18",
  "layout": "application-single",
  "application_entry": true,
  "application_group": "工业与运动",
  "weight": 209,
  "related_basics": ["singleturn-multiturn", "latency", "inl"],
  "reference_topic": "机器人关节"
}
---

关节里至少有两个不同的位置问题：转子到了哪里，决定电流怎样换相；减速器输出到了哪里，决定连杆姿态。传感器放在电机尾轴，只能直接看到该测点，无法自动消除减速器回差、弹性变形或输出轴安装误差。

## 先画出反馈路径

电机侧可以由轴端磁铁和角度芯片形成换相、速度与位置反馈。输出侧则要在法兰或输出轴另设测量路径；中空结构还要为走线、磁环和读头留空间。把电机角除以减速比得到的是理想运动关系，不等于在受力时直接测到了输出角。

器件按“测量量→输出→集成边界”并列，而不是只排名位数：

- [MPS MA730](https://www.monolithicpower.com/en/ma730.html)：轴端磁角→角度与ABZ；仍只观察安装轴。
- [Infineon TLE5012B](https://www.infineon.com/part/TLE5012B-E1000)：GMR磁角→SSC等接口；磁路与控制器接入需要匹配。
- [昆泰芯KTM5300](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/KTM53XX/index.html)：离轴AMR角→SPI、ABZ等；离轴结构与校准条件仍要验证。
- [昆泰芯KTM5800](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/absoluteangledivider/index.html)：外部正余弦→角度与增量输出；它是细分器，不能省掉读头和磁环或码盘。

这些是芯片路线，不证明某关节已采用，也不构成直接替换或整机精度保证。

## 首先约束的是测点与时间

电机磁路、相电流和钢制结构会改变传感器附近的场。必须用实际通电工况验证，不能只在电机未上电时转动磁铁。两端角度用于差分时，应统一方向、减速比、累计圈数和有效测量时刻；不同滤波延迟会产生随速度变化的假角差。

角差能提供传动链状态线索，却不自动等于外界扭矩。刚度、迟滞、重力与摩擦背景都要有模型和独立参照。高位数也不等于达到关节所需的绝对精度或功能安全等级。

## 验证要覆盖一次完整动作

在独立参考下检查上电姿态、缓慢跨零、正反转、负载保持及温升后的误差。记录两路原始角度和状态，而不只保存控制器最终位置。若关节断电后能被外力转过多圈，应单独验证多圈保持；单圈绝对值芯片不能凭软件记忆保证断电期间的位置。
