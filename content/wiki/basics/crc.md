---
{
  "title": "CRC：帧正确不等于角度正确",
  "description": "理解校验覆盖范围、参数与错误处理，区分数据传输完整性、测量有效性和数据新鲜度。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-24",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "接口与应用",
  "weight": 146,
  "related_basics": [
    "spi-ssi",
    "interfaces",
    "latency",
    "i2c"
  ],
  "related_topics": [
    "编码器接口"
  ],
  "related_model_slugs": [],
  "related_guides": [
    "sample-time-contract",
    "calibration-data-integrity"
  ],
  "related_applications": [
    "servo-motor"
  ]
}
---

CRC把规定比特序列按既定多项式计算成校验值，接收端重新计算并比较。它能发现所覆盖数据中的一类损坏，却不会知道磁铁有没有偏心、机械零位是否标错。一个带着系统偏差的角度，只要按协议正确发送，CRC照样通过。

## 位宽相同，算法仍可能不同

实现至少要确定多项式、初始值、输入位序、输出处理和参与计算的字段。命令、状态和位置是否全部受保护，必须看具体协议，不能把“八位CRC”直接理解成同一段程序。字节排列错误或少算状态位，也会导致所有帧不通过。

[BiSS协会AN3](https://biss-interface.com/wp-content/uploads/2025/07/BiSS_AN3_appnote_E3en.pdf)给出CRC多项式与计算方法；[TI TMAG5170](https://www.ti.com/product/TMAG5170)也提供串行通信CRC。这是两处独立定义，应分别使用各自的测试向量，不能因为都叫CRC就混用。

## 接收错误后的动作同样重要

发现错误帧后，应记录原因、计数和对应时间，再按系统要求拒绝本帧、重读或进入降级状态。若直接沿用上一帧，又把时间标成当前时刻，控制器会收到一份“格式没问题”的旧位置。重试能否赶上控制周期，必须纳入时间预算。

验证时可以在测试程序中翻转受保护位、改变字段顺序、模拟连续坏帧与超时，检查接收端是否真正拒绝错误数据。这些是通信故障注入，不代表已覆盖磁场失效、芯片内部故障或功能安全所需的全部诊断。

## 选型要问完整的数据可信链

除了CRC，还要读状态位、量程或磁场标志、更新时间与失联判据。CRC不是身份认证或加密，不能阻止知道算法的人构造另一份合法帧；有限校验长度也不表示绝无漏检。只有明确错误模型与系统响应，校验功能才从一项参数变成可验证的行为。

## 把状态位纳入真实测试向量

[BiSS AN3 Rev E3](https://biss-interface.com/wp-content/uploads/2025/07/BiSS_AN3_appnote_E3en.pdf)指出典型过程数据CRC覆盖数据通道中的传感器值、状态及生命计数，且发送前取反。只校验位置字段，会把不同的受保护消息当成相同输入。调试时先保存一帧原始比特，再分别翻转状态位与位置位，确认接收器确实拒收；不要用“收到六位校验”代替算法验证。[时间约定](/topics/guides/sample-time-contract/)还要检查重试后数据是否过旧，[配置完整性](/topics/guides/calibration-data-integrity/)则处理保存过程的另一类损坏。
