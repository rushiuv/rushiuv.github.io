---
{"title":"旋钮操控：绝对位置与无尽旋转是两种输入任务","description":"先确定掉电后要恢复位置还是只计菜单步进，再选择磁角度或增量检测路线。","date":"2026-10-18T10:00:00+08:00","lastmod":"2026-10-18","layout":"application-single","application_entry":true,"application_group":"工业与运动","weight":204,"related_basics":["absolute-incremental","magnetic-encoder","pole-pairs"],"reference_topic":"旋钮操控"}
---

工业面板上的旋钮，有的表示一个固定设定位置，有的只是让菜单每转一格加减一步。前者关心上电时旋钮在哪，后者关心转向和增量；机械外观相似，数据含义却不能互换。

## 测到磁角度，还没有得到用户动作

TI TMAG5273通过多轴磁场和片内计算提供位置测量基础；Infineon TLE5012B是集成磁场方向检测器件。[昆泰芯KTH5502](https://www.conntek.com.cn/html/web/product/magneticAngleDetectionChip/kth5502/index.html)同样可以进入在轴旋钮的绝对角度候选；若还要观察按压引起的空间磁场变化，[KTH5701](https://www.conntek.com.cn/html/web/product/magneticAngleDetectionChip/57xilie/index.html)提供XYZ磁场与I²C/SPI路线，但按压仍需另做映射。

比较这些方案时应使用同一磁体、气隙、刻度布局和采样要求。绝对角度、连续磁场与菜单步进是三层不同信息；接口、磁路和固件不能视为直接兼容。片内角度算得出来，也不意味着已经处理好无尽旋转的跨零和反向操作。

假设菜单一圈24格，每格是15°。若在分界线上直接四舍五入，读数的小幅波动就会让显示来回跳。设置进入与退出门槛能够稳定步进，但门槛过大又会让用户感觉旋钮没有响应。

## 手感与数字刻度各有来源

触觉卡点可以由机械弹簧或电机产生，不是磁芯片天生给出的。卡点中心应落在稳定的数字刻度区间；若机械卡点正好停在软件分界线上，静止时也可能不断切换菜单。轴向按压若会改变磁体气隙，也可能改变旋转测量条件。把旋转与按压功能放在同一机构，需分别验证单独操作和组合操作。

## 工业面板还要处理异常输入

测试正反转、快速跨格、慢慢停在门槛、跨零点、上电、磁体缺失与外场干扰，并核对显示和实际控制量是否一致。连续可调设定值与危险动作确认不宜共用未经验证的单一角度门槛。应保留明确限位、确认或故障状态，不能把“无接触”直接等同于安全控制。

## 原厂资料

- [TI TMAG5273](https://www.ti.com/product/TMAG5273)
- [Infineon TLE5012B-E5000](https://www.infineon.com/part/TLE5012B-E5000)
