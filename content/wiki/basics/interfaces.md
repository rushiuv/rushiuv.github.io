---
{
  "title": "SPI、SSI与BiSS：角度如何交给控制器",
  "description": "把协议、帧格式和电气层分开，读懂时钟、锁存、状态位与CRC的关系。",
  "date": "2026-10-16T10:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "接口与读数",
  "weight": 800,
  "related_basics": [
    "abz",
    "latency",
    "absolute-incremental"
  ],
  "related_topics": [
    "编码器接口"
  ],
  "related_model_slugs": [
    "as5047p",
    "mlx90382"
  ],
  "related_guides": [
    "sample-time-contract",
    "spi-data-age"
  ],
  "related_applications": [
    "robot-joint"
  ]
}
---
“支持串行绝对值输出”还不足以决定两端能否连接。协议定义怎样交换数据，电气层决定信号怎样沿引脚或线缆传输；相同数量的线不代表兼容。

<figure><img src="/images/editorial/chromeos-signals-20261018.webp" alt="工程师比较控制器、芯片和信号的概念插画" width="1536" height="1024" loading="lazy"></figure>

## 三种接口先看什么

| 接口 | 常见读取方式 | 接入前必须确认 |
|---|---|---|
| SPI | 主控用片选和时钟交换器件定义的帧 | 时钟模式、命令、帧长、流水返回与校验 |
| SSI | 主控提供时钟，读出位置码 | 锁存时刻、码长、二进制/格雷码及帧间隔 |
| BiSS C | 主站时钟驱动周期数据帧 | ACK、Start、位置字段、状态位、CRC与超时 |

SPI是通用接口，不同角度芯片的寄存器和命令通常不同。SSI也不能仅按名字就假定帧长、错误位和时序完全一致。BiSS应对照协会协议与相应器件的Profile和配置。

## 长线差分，与帧格式分别判断

工业编码器常用差分驱动器传输时钟和数据；板上芯片则常提供单端逻辑信号。需要核对电平、接收器、终端电阻和供电地关系。一个板上SPI引脚不能直接当作满足工业长线条件的接口。

## CRC能证明什么

CRC检查规定比特范围内的数据是否满足校验关系，用于发现一类传输或数据损坏。它不能证明磁体没有偏心、零点标定正确，也不能自动保证测量值足够新。

实现时要逐项对齐多项式、初值、位序、取反规则和参与校验的字段。不同协议或不同帧的“6位CRC”不能只凭位宽共用一套默认参数。

## 读数可信，还要有时间与状态

先确认数据在哪一刻锁存，再确认状态位是否有效，最后校验帧。若接口读得比内部更新更快，重复结果不等于每次都发生了新采样。控制器需要能区分正常静止、旧数据和故障帧。

[BiSS协会：协议、Profile 3与CRC应用说明](https://biss-interface.com/downloads/)；[POSITAL SSI Kit手册](https://dms.posital.com/pdf/manual-kit-ktd-s1.pdf)提供了一个具体SSI实现，不能代替其他器件的手册。

## 连接成功后，还要配对采样事件

串行帧能解码，不代表两路位置属于同一刻。[MLX90382原厂手册](https://www.melexis.com/-/media/files/documents/datasheets/mlx90382-datasheet-melexis.pdf)单独提供多器件同步读取能力，不能由“都支持SPI”推断同步。合成设两路有效时刻差3µs，在50圈/秒下便混入0.00015圈，即0.054°运动量。接入[机器人关节](/applications/robot-joint/)前，应把锁存、返回与使用时刻逐一标注，再用[采样时间约定](/topics/guides/sample-time-contract/)判定该角差是否可用。

建议在逻辑分析仪记录中给两路锁存事件分别编号，避免只凭接收缓冲区顺序配对。
