---
{
  "title": "霍尔锁存：撤走磁铁后为什么还不释放",
  "description": "解释双极磁场触发、上电状态和边沿计数，说明锁存不保证断电记忆或50%占空比。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "开关与连续检测",
  "weight": 402,
  "related_basics": [
    "switch-polarity",
    "bop-brp",
    "pole-pairs",
    "absolute-incremental",
    "abz"
  ],
  "related_applications": [
    "brushless-dc-motor",
    "water-meter"
  ]
}
---
用一个磁极触发霍尔锁存器，再把磁铁移远，输出可以一直保持。典型双极锁存需要反方向磁场跨过另一阈值才复位，适合交替经过南北极的磁环；普通接近再离开的路径可能永远不给它复位条件。

## 保持状态不等于断电记忆

自设门限例子：正向超过+3mT置位，反向低于−3mT复位，在−3～+3mT间保持此前状态。门限与高低电平这里只作说明，不对应特定型号。零场落在保持区，所以撤走磁铁没有强制改变状态。

掉电后，上一次逻辑值是否保留是另一回事。上电磁场若处于保持区，必须查器件启动定义；不能从连续运行的漂亮方波，推出上电即可知道位置。[TI DRV5013](https://www.ti.com/product/DRV5013)是可供核对的具体锁存器例子。

## 对称门限也不单独保证一半占空比

[AKM锁存教程](https://www.akm.com/eu/en/products/hall-sensor/tutorial/hall-effect-ic-latch/)用理想磁场展示锁存与单极开关的波形差异。实际占空比还受磁极宽度、气隙、磁场谐波、失调、门限不对称和传播延迟影响。只有门限、磁场与时序满足相应对称条件，才接近50%。

对[无刷电机](/applications/brushless-dc-motor/)而言，应核边沿相对于转子电角度的位置，不能只检查平均占空比。每个磁极在最弱磁场、最大气隙下都应跨过所需门限。

## 有脉冲不等于有方向和绝对位置

单路重复脉冲可用于相对计数或测速；方向通常需要适当相位的额外通道。两路相隔四分之一磁周期，也不是永远相隔四分之一机械圈，见[磁极对数](/wiki/basics/pole-pairs/)与[ABZ](/wiki/basics/abz/)。

验证覆盖慢速、最大转速、反转、起停与断电重启；计数系统还要查漏边沿。若要求掉电后仍知道整圈位置，应按[绝对与增量](/wiki/basics/absolute-incremental/)重新定义信息来源。
