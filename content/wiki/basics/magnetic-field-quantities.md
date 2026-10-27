---
{
  "title": "磁场、磁通与敏感轴：先把量和方向对齐",
  "description": "分清B、H、磁通和器件敏感分量，避免把磁体表面值当作芯片工作点。",
  "date": "2026-10-27T00:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "磁场与信号基础",
  "weight": 200,
  "related_basics": [
    "magnetic-sensor-types",
    "magnets",
    "3d-hall"
  ],
  "related_applications": [
    "current-sensing",
    "electronic-compass"
  ]
}
---
“磁场是20 mT”还缺一个条件：在哪里、沿哪个方向测得。磁体表面的读数、芯片敏感中心的读数与整个线圈穿过的磁通，不能互相代替。

## B、H与磁通回答三个问题

磁通密度 \(B\) 的SI单位是特斯拉T；磁场强度 \(H\) 的单位是A/m；磁通 \(\Phi\) 的单位是韦伯Wb。磁通是对面元的积分：\(\Phi=\int_A\mathbf B\cdot\mathbf n\,dA\)。只有磁场均匀、方向与面积法线夹角已知时，才可简化为 \(BA\cos\alpha\)。

空气中常可近似 \(B=\mu_0H\)。磁性材料内更一般的关系是 \(\mathbf B=\mu_0(\mathbf H+\mathbf M)\)，\(M\) 为磁化强度；若有非线性或[磁滞](/wiki/basics/magnetic-hysteresis/)，就不能用一个固定磁导率处理所有工作点。1 mT=10 G=1000 µT，单位换算不会改变测量位置。

## 芯片一般读取一个分量或方向

理想单轴读头响应 \(B_s=\mathbf B\cdot\hat{\mathbf s}\)，\(\hat{\mathbf s}\) 是敏感轴单位向量。自设 \(B_x=3\)、\(B_y=4\)、\(B_z=0\) mT：总幅值为5 mT，Z轴霍尔却看到0 mT。磁铁很强仍读不到，可能是方向错了；继续加大磁铁不一定有效。

[三轴霍尔](/wiki/basics/3d-hall/)可以给多个分量；饱和角度模式的[AMR](/wiki/basics/amr/)关注磁化方向。输出对象必须由器件原理和框图确定，不能都叫“场强”。

## 工作点要写成一组条件

记录磁敏中心坐标、检测轴、磁体姿态、气隙、温度和附近铁磁件，再给B的范围。[电流检测](/applications/current-sensing/)还要控制回流导体与外场；[电子罗盘](/applications/electronic-compass/)则需要辨认设备自身磁偏置。采购磁铁的剩磁或吸力都不能替代这些条件。

来源：[BIPM SI手册：单位定义](https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf/2d2b50bf-f2b4-9661-f402-5f9d66e4b507)、[TI TMAG5170：坐标与多轴测量](https://www.ti.com/lit/ds/symlink/tmag5170.pdf)。分量例为本站自设几何算例。
