---
{
  "title": "角度噪声：静止读数为何还在跳",
  "description": "理解RMS、带宽、平均与速度差分；避免把读数稳定误认成准确。",
  "date": "2026-10-16T10:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "参数与误差",
  "weight": 502,
  "related_basics": [
    "resolution-accuracy",
    "latency",
    "abz"
  ],
  "related_topics": [
    "ADC",
    "非线性校准"
  ],
  "related_model_slugs": [],
  "related_guides": [
    "noise-statistics",
    "independent-samples",
    "velocity-noise"
  ],
  "related_applications": [
    "closed-loop-stepper"
  ]
}
---
轴固定不动，角度读数仍会波动。传感器前端、电源干扰、量化和机械微振动都能进入结果。要比较两颗器件的噪声，先让它们处在相同的采样、滤波和机械条件下。

## 一个噪声数字，至少配三项条件

| 条件 | 为什么需要 |
|---|---|
| 统计量 | 标准差、RMS和峰峰值不是同一个数 |
| 带宽与滤波设置 | 限制带宽会改变读数波动，也会影响动态响应 |
| 采样率与记录长度 | 决定观测频率范围；峰峰值尤其受样本数量影响 |

对于已经去掉均值的静止序列，RMS可与标准差接近；含固定角度均值的原始读数RMS则没有这个含义。存在漂移或周期扰动时，也不能直接按高斯白噪声解释。

## 为什么平均会更稳

对N个独立、等方差、零均值噪声样本，均值的标准差为 \(\sigma/\sqrt{N}\)。这是模型结论。固定偏差不会被平均消掉，相关样本也不能照搬该比例。

用移动平均压小显示抖动时，还需要接受滤波带来的时间响应变化。看起来平滑的读数，不一定适合直接送入高速控制环。

## 位置的小跳动怎样变成速度噪声

以相邻位置求速度：\(\hat\omega=(\theta_k-\theta_{k-1})/T_s\)。若两次角度噪声独立且标准差同为σ，速度噪声标准差为 \(\sqrt{2}\sigma/T_s\)。采样间隔缩小而单次噪声不变时，直接差分的速度噪声反而增大。

角度跨过0°时，先做圆周求差。例如359.9°到0.1°是正向0.2°，不能按普通减法得到−359.8°。滤波、速度估计与过圈处理都要使用一致的角度约定。

[雷尼绍编码器术语：Jitter与Filtering](https://www.renishaw.com/en/optical-and-inductive-encoders-glossary--27382)。上述平均和差分关系由列明的独立噪声模型推导。

## 先排除重复读取制造的样本量

合成设100个独立新样本的标准差为0.0001圈，平均后为0.00001圈，即0.0036°；把每点复制100遍，文件虽有一万行，却不再改善十倍。[海德汉ATS德文手册](https://product.heidenhain.de/JPBC/image/HWP.EN/hlr-system/ATS_539862-xx_BHB_543734_Ver19_01_de.pdf)也将采样率与每信号周期的采样点数分别检查。测试时保存新数据标志及时间，再按[独立样本](/topics/guides/independent-samples/)核算；若还要差分求速度，应另看[速度噪声](/topics/guides/velocity-noise/)，而非只追求显示稳定。

固定数值不跳也可能来自量化台阶；须把静止时间统计与整圈误差记录分开保存。
