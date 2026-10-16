---
title: "EtherCAT"
description: "运动控制网络中的位置数据需要一致的时间关系，通信周期与传感器采样分别核对。"
topic_guide: true
lastmod: "2026-10-16"
related_topics: ["编码器接口", "机器人关节", "FOC"]
---

EtherCAT用于工业实时通信，连接控制器、驱动器和I/O等设备。在运动控制中，位置反馈的网络传输与设备内部采样是不同环节，需一起安排时间关系。

## 从网络同步看到实际测量

分布式时钟提供设备间的时间同步机制，但某个产品如何触发位置采样、怎样映射状态与过程数据，仍要查设备说明和配置。网络周期短，不能直接推导传感器内部延迟小。

下方文章讨论接口生态与运动系统。具体接入以设备描述、固件版本和主站配置为准。

参考：[EtherCAT技术概览](https://www.ethercat.org/en/technology.html)、[ETG技术资料汇编](https://www.ethercat.org/en/compendium.htm)。
