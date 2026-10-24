---
{
  "title": "伺服电机：换向角与负载位置不能混成一个指标",
  "description": "轴端磁编码器和旋变解码是不同反馈路线，选型要同时看时间、机械误差和故障行为。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-24",
  "layout": "application-single",
  "application_entry": true,
  "application_group": "工业与运动",
  "weight": 207,
  "related_basics": [
    "latency",
    "resolution-accuracy",
    "interfaces"
  ],
  "reference_topic": "伺服电机",
  "related_guides": [
    "sample-time-contract",
    "dynamic-latency-test"
  ],
  "related_model_slugs": [
    "as5047p",
    "ktm5200",
    "ktm5900"
  ]
}
---

伺服电机的角度首先服务转子换向和速度控制；机器最终工作点的位置，还会经过减速器、丝杆或皮带。电机端反馈准确，并不自动保证负载端同样准确。选型前先确定闭环测点，才能解释一颗传感器究竟负责什么。

## 两条路线，连输入信号都不同

同样输出角度，前面的感应对象和安装条件可能完全不同：

| 候选 | 测量量或输出 | 适用边界 | 原厂来源 |
|---|---|---|---|
| ams AS5047P | 轴端磁绝对角度 | 需要匹配轴端磁体与接口 | [手册](https://look.ams-osram.com/m/d05ee39221f9857/original/AS5047P-DS000324.pdf) |
| ADI AD2S1210 | 旋变信号解码，角度与速度 | 需要旋变、激励及模拟输入链 | [详情](https://www.analog.com/en/products/ad2s1210.html) |
| 昆泰芯 KTM5200 | 在轴AMR绝对角度，ABZ/UVW等 | 饱和磁场、校准与时序须匹配 | [详情](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/KTM52XX/index.html) |
| 昆泰芯 KTM5900 | TMR磁角度，SPI等输出 | 需核对具体磁路、校准和动态配置 | [具体型号表](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrTMPMagnrticEncoderChip/index.html) |

KTM5200与KTM5900增加了AMR、TMR两类磁反馈候选，不是仅按标称位数替换AS5047P，更不能直接替代旋变解码输入。比较精度时需同时固定温度、校准与安装条件；脉冲线数和四倍频计数也不能混用。

若电机有7对极，1°机械角对应7°电角度。这是坐标换算，不代表1°机械误差总能接受；应把误差放回电流矢量、转矩波动与实际控制要求中判断。

## 位数没有说明数据来自哪个时刻

动态误差还包括传感链、通信、控制任务和执行更新的时间。滤波能减小读数噪声，也可能改变带宽与相位。串口速率高，只说明比特搬得快，不能单独证明样本新鲜。

由角度差分估速度时，还要使用真实样本间隔。重复读取同一帧，再突然读到新帧，可能被误算成速度先归零、再出现尖峰；总线读取时间不能替代角度采样时间。

## 比较在轴精度之外的条件

验证应保留转子零位定义、方向、磁极对数、采样触发、状态字与报警行为，再检查低速、反转、加减速、温度和电机通电后的干扰。丢数据不能当成转子不动，复位后的第一帧也须确认有效。原厂分辨率、车规资格或诊断能力，不等于驱动系统已通过安全认证，更不能代替负载端精度验收。

## 原厂资料

- [ams AS5047P数据手册](https://look.ams-osram.com/m/d05ee39221f9857/original/AS5047P-DS000324.pdf)
- [ADI AD2S1210](https://www.analog.com/en/products/ad2s1210.html)


## 末端不到位，先比较两处测点

[欧姆龙日文技术解说](https://www.fa.omron.co.jp/guide/technicalguide/14/186/index.html)按检测器安装位置区分半闭环与全闭环。排查“驱动器显示到位，工件却未到位”时，同时记录电机反馈和末端独立量具，先分清[分辨率与准确度](/wiki/basics/resolution-accuracy/)及[数据延迟](/wiki/basics/latency/)。

设丝杆导程5mm/圈，电机端剩余偏差0.002圈，理想对应10µm；这是自设换算，不包含丝杆、联轴器与安装误差。若末端偏差超过项目预算而电机端已收敛，先检查两测点间的传动关系；运动中偏差随速度增大，再按[采样时间约定](/topics/guides/sample-time-contract/)与[动态延迟测试](/topics/guides/dynamic-latency-test/)分离时间项。判据须以末端任务及参考不确定度制定，不能用驱动器到位位代替。
