---
{
  "title": "屏蔽门：电机走完行程，不等于门已关闭锁定",
  "description": "把门扇位移、驱动角度与锁闭状态分开，验证传动松弛、端点检测和故障响应。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-18",
  "layout": "application-single",
  "application_entry": true,
  "application_group": "工业与运动",
  "weight": 217,
  "related_basics": ["absolute-incremental", "mounting", "interfaces"],
  "reference_topic": "屏蔽门"
}
---

屏蔽门驱动可以通过电机角估算门扇移动量，但皮带松弛、机构打滑或连接件异常，会让电机仍在转而门没有按比例移动。因此行程、实际关到位和锁闭应作为不同观测，不能只用一个电机目标位置同时证明三件事。

## 连续位置与端点检测承担不同任务

轴端编码器适合生成开关门速度曲线和位置反馈；固定读头配门上磁体，可以检测某个到位区间。开关量只说明磁场经过阈值，并没有给出完整位移。传感器安装在锁机构时，还需确认它观察到的确是锁舌状态，而不是门扇靠近。

按测量量、输出与限制比较：

- [MPS MA730](https://www.monolithicpower.com/en/ma730.html)：电机磁角→角度与增量接口；看不到门扇脱离传动后的真实位置。
- [TI DRV5032](https://www.ti.com/product/DRV5032)：磁体到达→开关量；不能输出全行程。
- [昆泰芯KTH7816-X-N-QN16](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html)：霍尔角→SPI、SSI、PWM或ABZ；仍要建立轴角到门位的关系。
- [昆泰芯KTM1302](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/magnetoresistiveSwitchSeries/index.html)：磁体进入阈值区→开漏开关；需按后缀核对采样频率和阈值。

这些是感知候选，不是直接互换的安全元件或具体屏蔽门采用证明。

## 最先检查阈值和真实机械位置的关系

磁体气隙、门体挠曲、温度和钢结构会移动开关触发位置。需要在装配公差最差处验证进入与退出阈值，避免刚好停在迟滞边界产生状态反复。采用休眠式开关，还要核对更新间隔能否覆盖门运动期间最短的磁场事件。

连续位置链则要检查零点恢复、传动比和上电后是否需要重新寻零。堵转电流、位置停滞或关到位信号各自只有有限证据，不能直接等同于门缝无人或锁闭可靠。

## 失效试验不能省掉独立保护

按批准规程测试传动松弛、磁体偏移、线路中断和传感器固定高低电平，核对系统是否识别矛盾并进入规定状态。普通磁位置感知不等于人员防夹、防坠或列车联动安全功能。安全回路、锁闭检测、障碍物保护与整机符合性仍需专门设计和验证。
