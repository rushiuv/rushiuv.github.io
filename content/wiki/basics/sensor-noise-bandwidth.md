---
{
  "title": "噪声与带宽：平滑了多少，也要问慢了多少",
  "description": "将输入等效噪声、噪声带宽、采样与延迟分开，比较同一条件下的位置分辨能力。",
  "date": "2026-10-27T00:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "磁场与信号基础",
  "weight": 204,
  "related_basics": [
    "sensor-transfer-function",
    "angle-noise",
    "latency",
    "chopper"
  ],
  "related_applications": [
    "current-sensing",
    "servo-motor"
  ]
}
---
静止时读数更稳，并不一定代表运动时测得更准。平均和低通会改变噪声，也会改变对运动的响应；比较读头时必须同时给出带宽与延迟。

## 电压噪声要折回实际测量量

输入等效磁噪声近似 \(\sigma_B=\sigma_V/|S_B|\)。如果目标是位移，还需除以工作点的磁场梯度：\(\sigma_x\approx\sigma_B/|dB_s/dx|\)。自设 \(\sigma_V=0.5\) mV、\(S_B=50\) mV/mT、梯度2 mT/mm，可得 \(\sigma_B=0.01\) mT、\(\sigma_x=5\) µm；这些是局部、小信号、同一带宽下的RMS量，不是全行程绝对精度。

ADC有多少位只说明码格。信号只占部分量程，或模拟噪声跨越多个码格时，增加输出位数不等于增加有效信息。

## 带宽与采样率不能互相替代

若白噪声密度近似恒定为 \(e_n\)，RMS约为 \(e_n\sqrt{B_N}\)，其中 \(B_N\) 为等效噪声带宽。对单极点低通，\(B_N=\pi f_c/2\)，不是直接把−3 dB截止频率代进去。低频1/f噪声、干扰尖峰和量化噪声又需要各自模型。

采样率描述多久给一个样本；模拟带宽描述哪些变化能通过。采样前若未充分限带，混叠进入低频后，简单平均不能恢复原信号。

## 用同一滤波模型同时计算稳态与动态

自设一阶低通 \(\tau=10\) ms，\(f_c=1/(2\pi\tau)\approx15.9\) Hz。阶跃在一倍时间常数达到最终变化量的63.2%，10%–90%上升时间约22 ms。这说明低噪声可以伴随明显跟随滞后；低频群延迟约为 \(\tau\)，并非所有频率都延迟同样时长。

<figure class="basic-figure technical-figure"><div class="diagram-viewport" tabindex="0" role="region" aria-label="工程示意图，可左右滑动查看"><img src="/images/learning/noise-bandwidth-20261027.svg" alt="一阶低通阶跃响应由0上升，在10毫秒到达63.2%，标出截止频率15.9赫兹和10至90百分比上升时间22毫秒" width="960" height="560" loading="lazy"></div><figcaption>解析模型计算图，τ=10 ms；没有添加虚构实测噪声或器件指标。<a href="/images/learning/noise-bandwidth-20261027.svg" target="_blank" rel="noopener">查看原图 ↗</a></figcaption></figure>

试验时固定滤波设置、样本数与测量温度，分别报告静态RMS、幅频响应及阶跃响应。[伺服反馈](/applications/servo-motor/)还要把传感延迟接回整个控制环。

来源：[TI TMAG5253：输出滤波及延迟](https://www.ti.com/lit/ds/symlink/tmag5253.pdf)、[ADI：噪声带宽基础MT-048](https://www.analog.com/media/en/training-seminars/tutorials/MT-048.pdf)。公式后的数值为本站自设模型，不是性能排名。
