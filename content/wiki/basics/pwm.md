---
{
  "title": "PWM角度输出：占空比、周期与故障区间",
  "description": "用输入捕获解码位置PWM，避免把角度编码波形、功率驱动PWM和磁极脉冲混为一谈。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-18",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "接口与应用",
  "weight": 148,
  "related_basics": ["interfaces", "latency", "uvw", "i2c"],
  "related_topics": ["编码器接口"],
  "related_model_slugs": []
}
---

位置传感器的PWM通常把角度编码在占空比或规定的脉宽里。它与驱动电机功率的PWM不是同一件事，也不同于转得越快、脉冲越密的测速输出。主控需要根据手册解码波形，不能仅凭看到方波就按边沿数量累计位置。

## 占空比要按有效区间换算

若器件定义占空比D从Dmin到Dmax映射一圈，理想归一化角为`u=(D−Dmin)/(Dmax−Dmin)`。例如假设10%到90%对应量程，占空比50%才是中间位置；直接把50%当半圈，在这个点恰好正确，但其它点未必正确。这个比例是解释公式的假设，不是通用芯片配置。

[Infineon TLE5012B手册](https://www.infineon.com/dgdl/Infineon-TLE5012B_Exxxx-DataSheet-v02_01-EN.pdf?fileId=db3a304334fac4c601350f31c43c433f)为PWM划分测量与诊断区间；[Melexis MLX90371](https://www.melexis.com/en/product/mlx90371/triaxis-performance-rotary-linear-position-sensor-ic-analog-pwm)提供可配置PWM输出。两者的频率、极性和故障编码应分别核对，不能共用未经验证的默认换算。

## 输入捕获比软件轮询更可控

用定时器记录上升沿、下降沿及下一个上升沿，才能得到同一周期的高电平时间和总周期。捕获频率、计数器溢出、边沿抖动与线缆波形会进入角度误差。若只测高电平、不测实际周期，还会把传感器时钟漂移误当成位置变化。

## 一根输出线也有时间代价

完整周期收齐后才能解码，不代表角度恰好在收齐时测得。低输出频率会限制新位置到达速度；提高主控计时精度也消不掉传感器本身的更新延迟。快速闭环应把测量、编码、传输和解码一起算进预算。

选型验证应覆盖零位附近、最大量程、丢边沿、固定高低电平和诊断占空比。故障值不能被截断成合法角度；重新上电时也要等待有效输出，而不是把第一个不完整周期送进控制环。
