---
title: "瑞士苏黎世26家机器人公司没有一家做芯片"
date: 2026-09-10T08:00:00+08:00
slug: "mlx2d4R84ZvSEWhB10GgzQ"
description: "苏黎世先是一座具体的城市。它在苏黎世湖北端，是瑞士最大的城市；老城、银行总部、ETH Zürich 和工业区挤在并不大的范围里。但机器人从业者说“苏黎世”，往往不只指市界。地图上的 Bubble Robotics 在 Dübendorf，更…"
original: "https://mp.weixin.qq.com/s/mlx2d4R84ZvSEWhB10GgzQ"
---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DBrlpXS1RIVcf8g1rfm2K7AzK9OsOZvoRHqtftGXjlic51hib4ib4kmTeKYv9B4dqeMcNvJtwWeNG6UT1T70CL4iaZzcz9P4XqYgoG7GD3a8e9Q/640?wx_fmt=jpeg&from=appmsg)

## 瑞士苏黎世
26家机器人公司
没有一家做芯片
我却在一只关节里追了三遍

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6DPakKZt7dQfZzDasEPVjGCEcEqRj9NiakSeZTsficuWQFSLLmDxSz5ceDxibw8hicE6iaGFSxYNdOMxggWncJRheoWK68vCNZh4xLyUNQFGwUOkA/640?wx_fmt=svg&from=appmsg)

苏黎世先是一座具体的城市。它在苏黎世湖北端，是瑞士最大的城市；老城、银行总部、ETH Zürich 和工业区挤在并不大的范围里。但机器人从业者说“苏黎世”，往往不只指市界。地图上的 Bubble Robotics 在 Dübendorf，更多团队散在机场、ETH 校区和周边城镇，实际指的是一个可以当天往返的 Greater Zurich 工程圈。

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIWGzOo5pScNEQ9e44yLdR31WJeNa1vANqDAAa0HnraXnykDLiaCK9UhRdib3XBfOglHv0Bd49Ahjb2Xy1qucib3u8KzXBD2aEVOBI/640?wx_fmt=png&from=appmsg)

我自己也在苏黎世附近。对我来说，Hagenholzstrasse 83a 和 85 不是遥远的欧洲公司地址，而是开车可以到的两个门牌；苏黎世机场旁边那些看起来普通的办公楼里，可能一层在做四足机器人，隔壁就在校六维力传感器。地图引起我的兴趣，也不是因为“欧洲机器人之都”这个称号，而是它画的正好是我所在的工程半径。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIXdaE85shzN76h3Sc4drlCrOu6juf4rHd3Esc4gFI8Fvdxjw3CRLYWzvylDNPhWOgEONJPgOwb3hj8yQic4pGrA0h6nqXMSCdEQ/640?wx_fmt=png&from=appmsg)

这个圈最硬的背景是 ETH。ETH Robotic Systems Lab 自己的 spin-off 页面把 ANYbotics、Bota Systems、Duatic、Flexion、Gravis Robotics 和 RIVR 排在同一页；Autonomous Systems Lab 的名单里又能看到 Ascento、Sevensense、Tethys、Voliro 和 Wingtra。2025 年，RAI Institute 把波士顿之外的第二个研究中心放到苏黎世，ETH 的公开说法直接把它类比为“Boston with MIT”。所以这里的密度并非一张社交媒体地图凭空画出来，它有实验室、学生项目、公司和收购退出一路相连的公开记录。

Lukas M. Ziegler 把苏黎世的机器人公司放在一张地图上：ANYbotics、Bota Systems、Gravis Robotics、Verity、RIVR、Voliro……地图下面，有人问这些公司里究竟有多少家盈利；有人说它们更像“system builders”；还有人在转发帖里 @ 中国同行，说它们似乎需要一张去深圳的邀请函。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIUUbHsoojklRgrGU5vNcZsm8PRYkLJMbQepntic7Ocxpu9qBlVoqDaCt4IJrsaJNX4wukRZBKkytvf7pJwlBwj7cOFDpq0WmW3A/640?wx_fmt=png&from=appmsg)

*图源：Lukas M. Ziegler 的 LinkedIn 原帖。原作者注明地图并不完整。*

我一开始也在地图上找芯片公司。没找到。

后来点进 ANYbotics 的关节资料，才发现这个找法不对。位置传感器没有自己的 logo，它已经缩进一个直径 80 mm、长度 93 mm 的关节里；再往里缩，最后只剩控制框图右侧的两个希腊字母。

我原本只是想确认 ANYdrive 用了几只编码器。结果在那张图上，

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5hxKibgM5W8qCHj3DbAZH60CJylF4ZMJ1A8JaXe6Xg25wBpQLibOibXIszHpUyOOwpA0oKCPlfib7XWmLlwBs6AzM4E8PDx6zzJkjeicmxuCHNic8A/640?wx_fmt=svg&from=appmsg)

 被我圈了三遍。

### ◆第二页右下角
θj 不是一根反馈线

ANYdrive 是 ETH Robotic Systems Lab 为腿式机器人做的一体化串联弹性执行器。2016 年公开技术报告里的结构很紧凑：高转矩电机、谐波减速器、旋转弹簧、功率与控制电子装在同一个单元里。报告首页给出的重量是约 0.9 kg，峰值力矩 40 N·m，峰值关节速度 12 rad/s。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIVxEuJlUhHVtGq2NvCibgzk1X6vOB9bG17kJfezMREJQ7fXTPxiaxtuhfSGgXjyZ5JvFh7BQwGv2x4uFz0e3COG5oGibFmrXB3Ljg/640?wx_fmt=png&from=appmsg)

机械照片旁边就是控制框图。

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIWRfMiaGZoellYVBWGbFF6JvEpibAM0iblx6wlfIdVKTbibuvzYu7UdTIQmibo7lu2HPPSnMib2Nd2qDUU3Yd26ojQrOB7UjVmhSqOKk/640?wx_fmt=png&from=appmsg)

*图源：ETH Robotic Systems Lab / ANYdrive ECHORD 2016 技术报告，第 2 页裁图。右图中

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5cjtXj8fYAjgEjFRnPH9Dl9lH4Ao3rPstLju3cKTFOqoE0YDZZlOcCsblZdfKt7LQSu1cFs8icv9eFxnjYvNJvo2SDQj3qQZqwRIkibIxRED6A/640?wx_fmt=svg&from=appmsg)

 为关节输出角，

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4QwdDw1CfxmiaCs9QCPauKZnILBOte5XrPdQ1FiayeebxS8naPCNzsic5IDWvibjAXuPpLDCLrYShf6DcpleYF5h3cg3xibDlQ0T6YFDXfrFhGSyw/640?wx_fmt=svg&from=appmsg)

 为减速器侧角度。
*

*https://echord.eu/public/wp-content/uploads/2018/01/D3.3-Integrated-Electronics-MODUL.pdf*

先看最右边。减速器侧角度

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4tjGHibgxCibRt7znebBWpSUfvicmicbdRsApY885Tn9LSH9W8agljibTNb6P0g2yXokZqqiaWWjiccuDoGLOqPxk4AODnYarlWZIniblvibbnzpOZTxA/640?wx_fmt=svg&from=appmsg)

 与关节输出角

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6ZnLhWXPyP2uibVganxpPKV7rXNFo75gqPMbdrT6GSLMWFNicKYMaggjhxfxambLIvziaetQn2z7BPsVjhQ9XjJ4ZVWjfluS0mbQVad7fg4b1iaw/640?wx_fmt=svg&from=appmsg)

 做差，乘旋转弹簧刚度 k，得到关节力矩估计：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5lbC7sQYs8P8gwGXnBXPg9ic7lr91eQ54HTE1VOm8J7ibXwHCoCdPoNhdoqNtwziaRtgFN8w3NqJBuQLZycMzDD29ibuSe0Lt84ohISq8icoe7wLg/640?wx_fmt=svg&from=appmsg)

这就是串联弹性关节最关键的观测量。它没有在输出端再塞一只传统力矩计，而是测弹簧两端的位置差，把扭转角换算成力矩。

如果只看这一条线，很容易得出一句正确但没用的话：编码器误差会变成力矩误差。

我沿着

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6DPakKZt7dQdKCGdrg2vu13Vic3op9lxRrnhQeLKibNI7ogON9Ww5aqQuG2YQYWNlfbymZ57j315GfNFTqqf2AkuuhGjbnv9ftB7BKF9bMQqNA/640?wx_fmt=svg&from=appmsg)

 往左追，才发现它并不只参加这次相减。

第一条路径是位置环：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7m5mGhA2ePMXaI9TWEu7M5F3WhvfXStGFSu3kP9kx0uPK3QelxjTfzDxouFe3HbZdIqsIWusSNyhf2geITyFAZbWRN0UY3hUJHMQsqmzFURg/640?wx_fmt=svg&from=appmsg)

位置 PID 根据

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5MZmJOKJGyCfjMxgiaJRKo1BmfiaShVCWGiatd7M0flbBMuBqKZwcg6HDojr1ic98TF0OGKkwHVan3AEBWiavFxQuFrzOBvNNrIcklmxvKyjevNYg/640?wx_fmt=svg&from=appmsg)

 生成期望力矩

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM66m7RJJ6dJRfdYINW4cH1xj6C4w5Iic1PhxMtG5iaKA4GywrXsQzTBTUreYZwEdjwT3OrkRK0c2vL8IicWLYdeibeD7iavEiahqNN5ejuUyaibW3NtQ/640?wx_fmt=svg&from=appmsg)

。

第二条路径才是刚才的弹簧力矩：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7qks3jr8VoPtboB4wUghibhtXKLl1Rogj5uz3jMAFLKyuDiaX0bFDfBjg7XIFJb7PvIXwyfogEqzvjdicOcnG7SzNECS4sogutKukENicDpBo9TQ/640?wx_fmt=svg&from=appmsg)

内层力矩误差为：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM58Sb1Wic5lr4Vw3j5AOCicwYe0G8L9uAvgC76XJMhSCDvQPmdH57tx5pP0S2tLjQU22BXGdxXQia4HR85GklEUd7knh2mwnfkdibr6QsfaT9R97w/640?wx_fmt=svg&from=appmsg)

第三条路径藏在框图下方。

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7wQUFUpYnsj97tO7SNDMTPXShf91ib16diaDY9VntkMpH4kUJ2eUZfM5J4VfY0dECNlMEicQQFib47cOibxe3EKMRzJ7jxurZ1zweMrydWD9EHRbg/640?wx_fmt=svg&from=appmsg)

 先经过微分得到关节速度，速度再进入摩擦补偿，最后以电流形式加到驱动命令中。报告写出的补偿形式是：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7kNcCHaWneSJ5LiaSAt1qurOkweWefld9fTepBot1ib1VsCmXA6PY2d0rbBu2rvtE3DstBajm7tpSxE4liaO5hIKB53lR2fhOefgZUc7yyPja5g/640?wx_fmt=svg&from=appmsg)

这里前一项处理低速附近的偏置/库仑摩擦，后一项近似黏性摩擦。它们与力矩 PID 输出、

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7hEgt0iaicgyHwLwUgeutPo6bFicxqUiaHZndjlymzgMFJiaLBE7OjYeEmia1IDz46ESuLicNy9nqHd1J7KAHwQml4TBY4iaRwQpJjlqL6RUlyib1ibGZg/640?wx_fmt=svg&from=appmsg)

 前馈一起汇成期望电流

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4WhEicbAWwVL5iaJ9ibfmdSqKVrCWwzBCXcu0wKfibSnQGmfUgYoVNE5INxOWYnO5oxiaJ64WVK7NaSMxwhbHjGlSicprn7Z7hMatT49ic1Q4KKEaxw/640?wx_fmt=svg&from=appmsg)

。

同一个

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7qaNb3wZM2kyT4OscJiah3vMiaWKviaW0cE51TnqwuHrkVicbQOt0PiaMpzVfjJUOianscGEHH2CJLHCPU65Rk9AY4AWic3mSZek0HY9f4gCibx69KfA/640?wx_fmt=svg&from=appmsg)

，一份送位置环，一份与

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5jzgrh4c6fYJicwSbUXfNEWRcuk59BfIicM24n8pJDNPfFkyq9lNzFGh6xqaUf8EPZ8GLNhasTAy3ceibZzwib9gLXFbQEhDZNsAjRl680KOTIDg/640?wx_fmt=svg&from=appmsg)

 相减，一份先微分再送摩擦补偿。位置传感器不是控制系统末端的一只“读数器”，它同时参与期望力矩的生成、实际力矩的估算和电流前馈的修正。

到这里，我才开始认真想：如果

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6CicB0HEk19zhPXicaxfGibYMxAtcia03p36bTiaP6Tc4HnicsVze1odU0cCVBzDLBX1883kVoGk8WOJibPzoc9UWQczYcHmBPF0gU68sEwuhfmUCzw/640?wx_fmt=svg&from=appmsg)

 只错一帧，会发生什么？

### ◆一次正向角度毛刺，会先在两条路上同向夹击，再从第三条路反打回来

假设真实关节角没有变，

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4GbOTp2LphbRoX1TW5bl6aWE15WnH10F8H9tS2mYs8no7tSLGI7YG6BLPgkGTMicibebPnIBTcLvSeN7I8uTbto9cymk5ZIsicz1hR5ia6tiaXE6g/640?wx_fmt=svg&from=appmsg)

 的测量值却突然多出一个正误差

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6FiaRiaaoUZvQo3q02X86SgwkqIHjfXHRZwkKB564muziaC3bgOaPictTxbhA2MkbymHKwicIiav7Q5HrLI5F8ibVl85ayiaxZ96yKZItAicMjVTGicwOQ/640?wx_fmt=svg&from=appmsg)

。

在外层位置环里，测得的关节位置偏大，因此位置误差少了

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4cpvZukH2KeLatgCBDeuDj9ibLXUJM9UzNTlJGcNSahaFgOqjS15oymd9uibvROKdKCf6nPjPN969R1XhDCqTeZLdm8G4ib7VxcxEviaZlxV6PWw/640?wx_fmt=svg&from=appmsg)

：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7IOM9Gp1sdOR2OGo9SIHHJzdH4ST6m0naoUK3qmFYooNEn6icxcnyTCYx7NkIDb1kqZNDWe5AYotj0aj47EZ9AejjPLsbVXl6KVViaKQ825icCA/640?wx_fmt=svg&from=appmsg)

只看比例项，位置 PID 会把期望力矩往下拉。

与此同时，力矩估计把同一个正误差当成弹簧多扭了一点：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5EWRRVSAicibcAqMuvot1vicQWwSE8lVQKP75e7M2GsJ5R5DVbLsKicq40jibcwWP56dDeuvuqLOWLORIJ84UFiaDf1OzMROYaMTX8bweazp1eCqng/640?wx_fmt=svg&from=appmsg)

于是内层的力矩误差又被压低：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4bgrR1Os14K9tKOHl2K8l8wJo8szmiacchjCBEq5HQa3riaibGcV4W69rWwibYmCn2fia77lHhq11hERMyluPhmGh7YaSrKCcGDGKpsBSG8vxh0Mg/640?wx_fmt=svg&from=appmsg)

对一个普通正增益位置环来说，

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7m5mGhA2ePMe3ibuGJ1mvicVGhogg9enyKop3XF9ETyz72SjsFyuWQBicEvnrc9D1a84DAzxQauNSHhpzDJve97iaTYD6I6TicEzbUHZW2GdLFIvA/640?wx_fmt=svg&from=appmsg)

 本身也是负的。也就是说，这个正向位置毛刺不是只沿一条线进入力矩环：外环先降低了“我想要的力矩”，差值计算又抬高了“我已经有的力矩”。两项在

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5O6wwtZIMSha3DQGibWz2csLgF3IQIcTr0s1JDFNAfWqUsscvy4wnibBMCOGxMX1xAZaZd6cDQWFzAWZQ5BjGxgfITQC66m5JRh0Fia1drd5YRQ/640?wx_fmt=svg&from=appmsg)

 里朝同一个方向叠加，力矩 PID 会更用力地减小电流。

可第三条路偏偏不是这样。

若

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6FiaRiaaoUZvQoUou5WRkmIca57RN8U6TdxrGrFgpmzWvbJbcSIMiblRo7icPjLV3icZEOF98UeZ2kZ79gSjpJfW1v041va8aicd7782ECMic4rpbfQ/640?wx_fmt=svg&from=appmsg)

 是一步跳变，微分器看到的不是一个小角度，而是一个近似

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6l4yMVrlgKrbfgfSYaRER6To3YbRmqBPGUwNicqfzHfzDAlZ6VXpiaRiblDZVjiahbWV0wicibSzaY6fKibaVk5Juuhv5KJhJIDR7Y1ge25bHnoyOfA/640?wx_fmt=svg&from=appmsg)

 的速度脉冲。

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5WeVx7PnIlVz1pATrox1OFVK398UOgLY8XLWr6XKaVc6P9gibmFU9n5xFVhNtWfa0IowpsiaIkDXMYn9MdqNBlh8F6PrVxvj1rjbWu7HNNV3Dg/640?wx_fmt=svg&from=appmsg)

 是采样周期。摩擦补偿会把这个速度脉冲变成一股电流补偿；按框图中的正号，它可能与力矩 PID 正在做的减流动作相反。下一帧若角度又跳回去，微分项的符号随之翻转。

于是示波器上可能出现一个很不像“位置错误”的波形：力矩环向下拉，摩擦补偿在同一帧向上顶，恢复帧再换一次方向。最终相电流是三条路径相加后的结果，未必长得像原始角度毛刺。

这解释了一个现场经常让人走错方向的现象：工程师先看到的可能是电流尖峰或力矩残差，回头看降采样后的角度曲线却很平。不是角度与电流无关，而是原始的一帧错误经过差值、PID 和微分后，已经换了形状。若日志只按 100 Hz 保存，而控制器在更高频率运行，那一帧甚至根本不会出现在导出的角度曲线上。

这里不能凭 ANYdrive 公开报告断言它实际用了多高控制频率、怎样滤波，也不能断言一帧毛刺一定穿过状态机。报告没有公开这些参数。能从框图确定的是误差入口有三处；能从工程上继续追问的是：三条路径用的是不是同一帧

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4GDCeHQO1ict8uHrvUOQq2Hb4a8tAaoW4ibjKGHSBnepqykmiapLZiceOmZoY25RyEystMudia5dkAibvBGwCibFvKXdjzMYticqnyFhxoia55ZLdQ5ww/640?wx_fmt=svg&from=appmsg)

，微分前有没有去毛刺，诊断无效时各环节保持上一值、降级还是立即撤力。

我把问题写到这里，突然发现两只位置传感器虽然都在力矩差值里，坏法却并不对称。

### ◆

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4xvNGSpp5WYLAdAYuxkBJUcWn3VU7gEicB9AbcAEfamnZ1C6DtU0A1AmhWtPfticHiaPTYpj8TjcHuVt1poqO5EkVfYicxyia5CzLzbfyrDPxAB1w/640?wx_fmt=svg&from=appmsg)

 错一帧，没有三条路；这反而给故障定位留了一枚指纹

把同样的正误差放到减速器侧

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4sLEJY3bVQia9ONJI3PSRricAdN5OfsibsyHFCnQuwRJ4zwwoDPvWC50axS2AOJPAUy4cyl6MAKUibzia7ZI8icjy25icoiab2TpLszVXfGCbh6JbkRA/640?wx_fmt=svg&from=appmsg)

 上：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4uR57cggQygGjbW3nAUibxKXnzs8OXVjIFHqxcNYHs7YSFbaDKJnCAA8lW11SVB30p5lyUAVnib1jlC7HNibdtnn04QibcytJ2cz9EPZajrsKTdQ/640?wx_fmt=svg&from=appmsg)

力矩估计变小，

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM42N5m97kMkiaCsk815XLcXcTYs2ibfTYosIxMByiakGVW3CIvojAkEiboIo3ibWBxzXc3JpRxGjKMghVkPb1kL6J7gh1uXnyjH2Vz2ofS0WaeyLsg/640?wx_fmt=svg&from=appmsg)

 变大，内层力矩控制器倾向于加电流。

但在公开框图中，

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6oibvn6NrB8Sic4QvOxq0gKz6AGLAQNwpNcMkAmGkkJpXQKYset4ehic76FM75zFNjbPNqVesadSKQBiclMHM4BFXJNYsDfic3bOpg4nhZeeibJEog/640?wx_fmt=svg&from=appmsg)

 不进入外层关节位置误差，也不进入以

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM60z4hWsdFI6DvnWnMBmafQf9TAXWNLicy4ejwu7oOmP8pye3xEqDaASIHic3JqFoA5QOicARmRo12v5FBVrge7o3McKPw2zxEQpanqgje9EkqNw/640?wx_fmt=svg&from=appmsg)

 为输入的摩擦补偿。它主要通过弹簧差值影响力矩估计。

所以两只编码器出现同样方向、同样幅度的一帧毛刺，电流响应不该完全一样：

-

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5cjtXj8fYAjiacHqVQg7wEWXI87wT7R1ITSOtYWO3NYicRSPibaW7q9H4ic7q23FHARxuI1EReFFeLwd2utKsG0OS4233LWbQk3eJyiaUqxXZQlOA/640?wx_fmt=svg&from=appmsg)

 毛刺同时改动

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM70uFYYzdWFfqC1sJJUEkdGkEb8EZp9QVkegWF9zXf6rKeVpJS3ecq5iauHNKxktKxoP7DqQkmXeNW8tSyFhOE0IOJcYuGVqqrwBENd2SL7nQQ/640?wx_fmt=svg&from=appmsg)

、

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4VUFM15QrdTvJVz4ibsfic1G6y7rVEic4QNPT5hynKqnzrpSeIibUuYwnn7F5H3uuTsicibmRQMAThn8DKREZ9WtHwbMCk3DLT8fVTXm7pTEsYLhWw/640?wx_fmt=svg&from=appmsg)

 和

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5YWmNicic1s34gSgPnyISUaQ2u2Cvu5Ne4z1k88rwAVEhLIS8ibq6icrV9jtP1xKkDc7BuVcdhZmT1vOXOeibetAmiaqo0Qly3SxFJXjFEW16E2ufw/640?wx_fmt=svg&from=appmsg)

；

-

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5hnBkHfP0CJLkN3RJb6aHgFD1V9X7iaib0plOLHFxEaROnXhbgLRD8TEa7sufOfa1CQPcnZ8t9q24OkIumLdVDgjZyzhEueyxIfyb10d4e3icRg/640?wx_fmt=svg&from=appmsg)

 毛刺主要改动

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4uR57cggQygPicLS6GDfzR4FHMsZPg3Sic2icewYn54no0GZxiaiaQ0xuib2sVbMPYZUW7FRPzK2w4uJ2p3a1hKmXDXPB2whgNer1UfFmJChGX6P2A/640?wx_fmt=svg&from=appmsg)

。

这不是建议客户“多录几路数据”的泛泛而谈，而是一条可以在台架上故意注错验证的预测。分别给

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5vZDNavRnRYHWFA9Vb1ib04oDDYI7dPiayfcVBzpXqlb7hby74GFtJMvAT19UCib6DziciaicAW1icNFIho7bXXM2pl5ofMHX5Tbb9H562f8tAcBEYQ/640?wx_fmt=svg&from=appmsg)

 与

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6ZWbgoTA5LQnKkm3Lhh9hu3zibynfNbgm81XS5NicLKTjRia3L1HpN7s0t3X3ibRaqj3v5k1sNicM9bjg0YwrQVNjibT4ujeUU58icNEHht8Er5kbeA/640?wx_fmt=svg&from=appmsg)

 注入一个相同的数字台阶，记录力矩误差、摩擦补偿电流和最终

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6qXDCh1WObiaxU4Z8rwOVWogBt1xOx8iajk6icoTgyDciaiajF4wahb3NAe1sfxbI2AboUZeOSUFTH4qaxibVYNI2291xDS2f6Fb58v8ISXibX6v85w/640?wx_fmt=svg&from=appmsg)

，三条通道的先后与符号应该能对上控制框图。若对不上，说明实际固件里还有公开框图没有画出的滤波、限幅、状态机或观测器。

再把时间拉长，不看一帧毛刺，看慢慢长出来的偏置，事情又变了。

设两只传感器偏置分别为

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4sLEJY3bVQia1rnSA6rmlhRLHhm0iaOcibT8YwpRKvGCCb9ibVia4A8F5mhmbqFBoian5WTfM2ibsNLcHDqVrtUGeW65KovH5n3O7AbFTwrAwbsAeYw/640?wx_fmt=svg&from=appmsg)

、

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5gBYy8b508ql82sGRqibeczjkvJN2RwjjrfBDfmicWSjetVkictXMibiajSvPibkQviaaCgX8h2TUaAgjK1yxbHO7YyEgbuCA6RJP3ODdHcgNTgAtgQ/640?wx_fmt=svg&from=appmsg)

，那么力矩零点误差是：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6icjL0YUwXu9bkYJVbEcAR5ic0FnS5Ka8gG1W1ubERiaX9ib8phLZ1mcEx1F807mCWiaZ8KIK36eVS9TmjXgTc8zjPBw01ichgUQhZS8ZhYicpU2x2w/640?wx_fmt=svg&from=appmsg)

如果两只传感器在温度上升后恰好同向漂了相同角度，即

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM728rcRkicd0QIXibbrbN2nkdswYr864GicZlHzibc0Y0Jz2knqCibG4j0ujZQ9akvB48fKzrnF62bzBEiamEAQFr7SPop2QiaNcyN7U3My3B86Ss0dw/640?wx_fmt=svg&from=appmsg)

，差值里的偏置会完全抵消，力矩估计看起来仍然为零。

但

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4MfiaTrtD0ic4wIkYtjydzY3MTvU7E1Rxh6pFzrjCqDw9s3ymOPElqMb1rEKYwtLNFhwwibGDMPbknyanHWmXIokMtY5VGZtRU1DYrfxIgJMZbQ/640?wx_fmt=svg&from=appmsg)

 本身已经偏了。外层位置环仍会把这个共同偏置当成真实关节位置。

反过来，如果两只传感器一正一负地漂，关节姿态在外部看来可能没有明显变化，

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4Nscx9kOc58lVmcFskmDMEUOfwmkZJGuR9MTsmOJ5JzVWBD0xuE3ichYzcfLzQlqUMDAEbkGVziapibWKxO3v6CialYgRFXibSzA2Lib8t1wNwW1icA/640?wx_fmt=svg&from=appmsg)

 却会凭空长出力矩。

这是差分测量里很容易被一句“共模抑制”遮住的细节：共模误差对力矩估算可能是好事，对位置控制却不是；差模误差恰好相反。只看最终力矩零点，检不出共同偏置；只拿外部量角器校

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6DPakKZt7dQVcovRDFBDtwG60L3RBj3ib1qZp5UMuIjAdYT0e8avC3koeVMm4fbbfHPzKjrPyOJC8JtlR5sH4Q9hBA5WRSdtubfKYM6VSOiaAw/640?wx_fmt=svg&from=appmsg)

，又检不出

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6icv5gNAe3wDNkKia2dZv7WprXzZ0AJu7afWVNoUDWJW8bSKPdlQ2eFG6sojVMsXEKH6wVicibQIPTiaFI2uf0ydxLIJibnxpNM7l8nquft0EJCcibQ/640?wx_fmt=svg&from=appmsg)

 单独造成的假力矩。

到这一步，器件选型已经不能只问两只传感器各自准不准。必须问它们的误差是一起走，还是分开走。

把偏置换成随机噪声，这个问题可以写得更明确。设两路角度噪声标准差为

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4GDCeHQO1ict5Y9aXzTYIicqrticicKGJhXvMdU1wlr2IS08yFaHQw0XeQ5ia3b5Br5mLJ0An7BJv5QxngoTSeaV4kgtGPu31nkuDBq5ZSZfqhPng/640?wx_fmt=svg&from=appmsg)

、

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7Fno25L19bicQSQQmicZQufxevUGxPhjnduyInj99GKPhNUibToaRBH5gibV3XmstOibLeyWv66K3WdFe3C2CJKQGm3dI1O0HVfOflpersbVFyLvA/640?wx_fmt=svg&from=appmsg)

，相关系数为 ρ，差值力矩的标准差为：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4tjGHibgxCibRqEsXDZwuD3L6QTlfocYzUuFH4ibiaIWTwaqbJaXyOVG7NAMe4OmjBpibaJ5KPVgemPEjyVfV3xnbttyUEvtNBCeRib6xl64sCibZ1w/640?wx_fmt=svg&from=appmsg)

如果两路噪声大小相同且完全同向，

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5zj3rTp1goiaP2jNl4knqKvNibbZlnkTHr2HnXjme1siaVY5fXicUibvwoU90T0XfgKiaurU8CXXS7GxLqgTcSNNu1zVarAymnS1YNKeM05IbricriaQ/640?wx_fmt=svg&from=appmsg)

，它们在差值中抵消；如果互不相关，

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6sBDEiaW9edzbVEoI2ByicWQEWMUqiceaydMyI5LLHGAXevgBFd9u5yLQpxP0MrIwB3dplfEgibLQRuiaHlibMeib3961E37OLgbyiam9snQubScKVIQ/640?wx_fmt=svg&from=appmsg)

，差值噪声是单路的

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6sBDEiaW9edzSLy9lj1XiaFv7pFMN1deQTDcmugibAuaKY6NibibWpia88ELh48loTyWjwz66ZrzbSs1a7lQFap0B5daZaBx14a6rAXRYhic9bLKx0Q/640?wx_fmt=svg&from=appmsg)

 倍；如果同幅反向，

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5FSyXScI1ETYXTvwE2RSpA5ISL5y5PCEIBErJj176ZTpaYNg6Ww37oZhlQYc0bnBjEgiaz0zQFDZA8FGpbYQ0AFzfGGAW99Ciaug1ibibhUvCUXA/640?wx_fmt=svg&from=appmsg)

，差值噪声会变成单路的 2 倍。

因此，“两只都用同型号”也没有自动答案。同一芯片、同一供电可能引入可抵消的共模扰动，也可能让两只传感器同时受电机 PWM 或地弹噪声影响；可一旦磁体偏心方向、安装相位或数字滤波不同，这些误差投影到角度后未必仍然同相。数据手册通常分别给单颗 RMS 抖动，却不会替整机给出 ρ。这个数只能在两路同时采样的真实安装条件下估。

然后我在纸边上写下了一个更麻烦的问题：如果两只都很准，只是没有在同一时刻读呢？

### ◆两只都合格，只差 100 微秒，也能凭空扭出 0.0688°

ANYdrive 把两个角度相减，默认读者很容易把它们想成同一时刻的机械状态。但公开报告没有给出两路位置采样是否由同一触发沿锁存，也没有给出采样到控制计算的相对延迟。

先不把这当作 ANYdrive 的事实，只做一笔用于审接口的情景计算。假设关节在近似稳态、弹簧变形不变的情况下转动；把两侧角度折算到同一输出尺度后，它们的角速度都近似为 ω。若两路采样时刻相差 Δt，先令两只传感器的静态误差为零，做差时仍会多出一项：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM60KY6NjgvSjkFpeukWbswBL0Tsiaa3dOTQ0yLmiciaGI0OwL2EbFf7AIgUukWWNfE8qiacqSxT24D6IN1nxJdD7vyOdYryqeZib917dsZIuk79iarw/640?wx_fmt=svg&from=appmsg)

报告公开的峰值关节速度是 12 rad/s。若相对时差取 100 μs：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM58Sb1Wic5lr4SIDXOzm6FKt21HXWG985wP0GLocZnAiaibDYgqFlKVwfJAuoqzy0aogd27bErt3HUcdUsibk9ffzmic0fw1tUqnVP2R0jRLZdDECA/640?wx_fmt=svg&from=appmsg)

同一份报告的宣传页把关节位置精度写成小于 0.025°。上面的 0.0688° 是它的约 2.75 倍。

这并不证明 ANYdrive 有 100 μs 的错位；报告根本没给这个数。它证明的是另一个更普遍、也更容易漏掉的事情：当力矩来自两个角度的差，单颗器件都满足 0.025°，并不能推出差值也满足 0.025°。相对采样时刻本身已经成为“虚拟的第三只传感器”。

这只看不见的传感器没有磁体、没有 ADC，也不在 BOM 上。它由触发方式、总线读写次序、数字滤波群延迟、时间戳位置和固件调度共同组成。

若

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6F86vku4hPIaP9JVmng7xe3aJH3Eq9nPaCH6SszakPAdquAdFia25ibic2lFTVibYhDgduAP1y5ybBRBnicIe9M7PFRKEW4esKArgKaC3Bh0b3d5g/640?wx_fmt=svg&from=appmsg)

 先经过一段滤波，

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7aukIG1S8vVBl5KCgdamOibhBAlC7kibRg9pB5MbJmfkCNUzshQYFygDBibHicy9mRo8xnaqagYvP6fobxTXYRTFKm04xIdUVdtc2SZNHyrAml6w/640?wx_fmt=svg&from=appmsg)

 走另一段滤波，即使原始采样同时，两路群延迟不同，做差后仍可能出现与速度相关的假弹簧角。静止标定时它是零，一转起来才出现；恒速时像固定偏置，加减速时又像动态力矩。这样的误差拿静态转台慢慢转一圈，很可能测不出来。

我本来想继续乘弹簧刚度 k，把 0.0688° 换算成多少 N·m，算到这里停了。公开报告没有给出可直接用于这笔换算的刚度值与两路角度归一化细节，拿别处型号的 k 补上去，只会造出一条很像技术结论的假精确数字。

但供应商必须回答的问题已经足够具体：两路是在传感器内部同步锁存，还是 MCU 顺序读取？时间戳打在采样沿、寄存器完成还是 EtherCAT/CAN 帧发出时？诊断位与角度是不是同一帧？数字滤波切档以后，两路群延迟是否仍然相同？

这几个问题，比“最高 SPI 多少 MHz”更接近这只关节真正使用位置芯片的方式。

### ◆17 bit 展开以后，0.025° 不是一个码

报告首页的规格表还放着两个很容易被销售 PPT 合并的数字：关节位置分辨率 17 bit，位置精度小于 0.025°。

17 bit 一圈有 131072 个码，理想最低位对应：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7lkwSw0icQL4wQShKNA8D04iaQc0xMbFcM4ctK8wsJWbyJdhIWRPQAaKZ01abDORuRvGj8tN5KxiaFDOyoRog9aZnqibI2MmCDPHnTiasH3eibtS7A/640?wx_fmt=svg&from=appmsg)

因此 0.025° 约等于 9.1 个 LSB。

这不矛盾。分辨率回答输出码能切多细；精度回答测得的位置离真实位置有多远。量化只是误差的一部分，磁体偏心、正交误差、增益失配、谐波、安装公差、温漂、滤波与标定残差都能让精度跨过多个 LSB。

真正值得追问的反而是报告没有说清的地方：这条 17 bit 是

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7QJC5iaA8yFYldCKiazoDt7CB2nmX7MmXEI6Zw55Y2VtvkpQBeuglskibjrlKcLeicxUhtY9KBW6ghPLiaJJljuoWtxiaX2EUZWia2lvYH78YrTraog/640?wx_fmt=svg&from=appmsg)

 的输出分辨率，还是两路传感器各自的原始分辨率？

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM698se1Dtjk1krqianbiaGaYiaw7Sq4icpsklysXNPUmTgUjmWV0vlz8vT4uxJ5rQatvOArH9Qmp73n0iapPn63jkicnRuqAXucf6CCeswWNz0dmlVQ/640?wx_fmt=svg&from=appmsg)

 经减速比折算后，有效量化怎样进入

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7DwjZxE17sYA3TcTsuDX3Dt3pgdIML0Y7FcG8xVEkbQicMKVcneSLj0cW8Moay85dO0Er17oxvBWNdAQPLcqhtlkU7SteQjRibpXvB3nnyMd1g/640?wx_fmt=svg&from=appmsg)

？两路角度是否在同一坐标系、同一零点定义下参与相减？

我又在报告里撞到一处版本不一致。

同一份 2016 技术报告，首页宣传页写“Joint output torque resolution

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4BzJAHDZD6OwZ1opr2IO87f4cFdcXDkXDJh758exIiah45DBwx9zumQb7Tliagl3oGLW8VNIdRMFmf1ZDDI9uiaSwd7Zapb6kokdaic186WQDZkA/640?wx_fmt=svg&from=appmsg)

”；正文 1.1 节的文本却写 8 mN·m。后来公开的 ANYdrive 论文常见版本写的是 0.08 N·m。8 mN·m 与 0.08 N·m 相差十倍，而

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4q5F6AMCcR3gKw1n5178U1Ozl7SdibmB5YRKELiaSu2m1fjVGiauzredEbGYAI97I13jbDdurEA4icnJibeYZbTOmmAbdap8JNo4sv3L1uau42Fiag/640?wx_fmt=svg&from=appmsg)

 又像是对后者的取整表述。

仅凭这些公开文件，我不能替作者判断 8 mN·m 是笔误、不同硬件版本，还是不同测试口径。最稳妥的做法不是挑一个最漂亮的数写进文章，而是把页码、版本和单位一起留下。

这处小冲突也提醒我：系统公司给出的“关节力矩分辨率”，不等于某颗位置芯片的数据手册分辨率。它已经穿过两只传感器、机械刚度、标定、滤波与控制实现。若供应商只拿自己的 LSB 去对齐 0.08 N·m，连比较对象都可能选错。

### ◆第三页的 70 Hz，到 10 N·m 时只剩 24 Hz

报告下一页没有继续堆静态精度，而是把关节装上单轴台架测力矩闭环。

低幅值下，实验辨识出的力矩控制带宽达到 70 Hz。随着幅值增加，报告称受电机饱和影响，10 N·m 幅值时带宽逐渐降到 24 Hz。10 N·m 阶跃达到 90% 的时间约 13 ms；40 N·m 阶跃则约 35 ms。

这四个数放在一起，比单写“70 Hz 高带宽”更有信息。

70 Hz 不是这只关节在所有载荷下不变的属性。控制器进入大幅值区域以后，电机饱和改变了闭环表现。同一处角度延迟，在低幅小信号辨识里可能只带来一点相位损失；到大力矩、限流或饱和附近，控制器能够用来纠错的余量已经不同。

也就是说，传感器延迟不能只在空载匀速转台上报一个平均值。更接近关节的问题是：延迟随滤波档位、诊断处理、总线拥塞是否变化；在电流限幅前后，角度错误会不会触发不同的控制轨迹；同一毛刺在 10 N·m 与 40 N·m 阶跃过程中，是否被不同的饱和状态放大或截断。

静态误差表到了这里，已经自然长成一张“误差 × 控制状态”的测试矩阵。报告自己的 70→24 Hz、13→35 ms 已经说明：被测对象并非一个固定线性系统。

下一页的碰撞试验，把时间尺度又往前推了一步。

### ◆碰墙以后 2 ms 开始制动，10 ms 才完全停下

研究人员在 ANYdrive 输出端装了一个摆，给执行器下零力矩命令，再让摆高速撞上硬墙，近似模拟恢复系数为零的完全非弹性碰撞。

报告写道：碰撞发生约 2 ms 后，电机已经以最大能力减速，尽量压低弹簧中的力矩；受电机和减速器惯量影响，约 10 ms 后电机才完全停止。在其最大电机速度对应的试验条件下，峰值被写为小于 7 N·m——正文这里用了“force”一词，但单位是 N·m，应按力矩理解。

2 ms 与 10 ms 中间这 8 ms，很值得位置传感器工程师盯住。

撞墙瞬间，输出端

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4n3GB5BD0djfu5HA03PjBy3aZ4KoD03N5I9MJ9WdkdrwQLibGDz6C0BY9NhSNIJrjWm6w1CaWwGibxCRqx75TECtKQVN9XMn1wnNBPBd2AJialg/640?wx_fmt=svg&from=appmsg)

 先被外界约束，电机与减速器侧

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7dZTia5V0kZOh8icTbvIfblnRolypgsDSeOYoIXswfovgWnAGYNReejmP7LrqYEJF0WzXMkxBhqnQ800Mic41ib6rviaGH94HXjkZ0AmTkXGHxjTg/640?wx_fmt=svg&from=appmsg)

 还带着惯量继续运动，

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7hqKPgQLdtHrbnvCE7UlxciaIygU1jTJaFgAR9BHZYTKOg8jg3UiauVjnILIgV9DiclgGzpYdkLK3czu9d8B10GqDypAUfvBFdpzn7SKOE1Nw9w/640?wx_fmt=svg&from=appmsg)

 快速变化。这个差值既是被测力矩，也是控制器决定如何制动的输入。传感器要记录的不是一个缓慢扫角误差，而是一段两端运动突然分叉、随后重新收敛的瞬态。

如果两路角度的滤波延迟不一致，碰撞沿到达时，差值里会同时混着真实弹簧扭转和时间错位。若诊断算法为了抗毛刺要求连续三帧一致，再决定这三帧究竟值多少微秒；它增加的不是抽象的“延迟”，而是从碰撞到最大制动那 2 ms 预算中的一部分。

但也不能反过来从这张试验图声称“ANYdrive 对编码器的要求就是 2 ms”。电机驱动、计算、传感和机械响应共同构成这 2 ms，报告没有拆分各自占用。公开数据只能把问题框到正确的时间量级，不能替代内部时序测量。

报告最后又做了一个零力矩试验：人手随机搬动输出端，运动幅度约 2 rad、主要运动频率约 4 Hz，输出力矩仍保持在 0.2 N·m 以下。

这里我也没有把“2 rad、4 Hz”硬套成一条标准正弦，再计算峰值速度。原文说的是 randomly moved by hand，图中也不是严格正弦；把两个近似描述相乘得到一个精确峰值，会越过证据边界。

真正有用的读法是：在外部持续扰动、目标力矩为零时，

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6B9TZK0cTAP5zNPdIj3Xcia26kM2xNHIIVrE9sML9AgqP1wkwm5sMCFThcqGlvheFo988ib9YZthLueib4SHjKDX9Nb97WAWxC1GfVFwMvKpicSw/640?wx_fmt=svg&from=appmsg)

 的估算与内层控制必须跟得上，不能把人手带来的运动误认成需要对抗的关节力矩。这恰好回到前面那只“虚拟的第三传感器”：两路角度若有速度相关时差，零力矩运动中就会产生与运动速度相关的力矩残差。

一张 2016 年的试验图，就这样把 17 bit、两路同步、差值力矩、闭环带宽和碰撞瞬态串成了同一个问题。

### ◆我去找日志格式，发现时间不是每路信号各记各的

沿这条线再往下找，我没有找到 ANYdrive 当年内部的原始日志，却找到了 ANYbotics 公开的 signal_logger。

这个仓库不是一张“支持数据记录”的营销图标。它公开了缓冲区、日志元素、时间处理、文件格式和 RQT 图形界面等实现与文档。time.md 里有一个很小但很关键的实现选择：每次调用 collectLoggerData() 时统一记录一次时间，保存时再把这份时间与各个日志元素配对。标准记录器用系统时钟，ROS 版本用 ros::Time::now()，以兼容仿真时间。

换句话说，它没有让每路信号在各自写入时随手读一次时钟。一次采集调用只有一个公共时间基准。这个设计不能自动保证传感器硬件同时采样，却至少避免记录器自身又给同一批数据添上一串软件取时差。

这件事与编码器芯片看似隔了一层，实际正好咬住

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7dZTia5V0kZOlCCVxEPPxnSq4eLIYdC9kVX14Z5pWj207Or5d0pyPHDMwiapicLnu87Fjxkt8aCTyGNKSgoXyPgDE6FniagvpIjicyGr9tJOBtq7A/640?wx_fmt=svg&from=appmsg)

。

若角度值有时间戳，而诊断位没有；若电流时间来自驱动周期，角度时间来自总线接收；若日志导出时把不同频率的通道重新插值，却没有保留原始采样序号，那么最后画出来的曲线即使都在“同一根时间轴”上，也未必代表同一时刻。

所以我现在看一个位置传感器接口，不会只看能否输出 17 bit。我会继续看它能不能让系统保存以下关系：

-

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4mnqqIoJ18iawwFDzkHvw7sSJwibdbsLbPwOkAbEKhbXDicosnHmKyRfTFVUyO32uEHyI4eNZ80zvb6h9GGVzllKsFedLsR8rcQf0DiaN4m3xOwg/640?wx_fmt=svg&from=appmsg)

、

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7m5mGhA2ePMY7UOico1RetTkO6err6o2SdLJ6Ck7rOrn1kJG2iaZP61qCODFcibFnLpibkMYkicaPczS7ibbC9e4VoSwqImcUSiaJ3KzC4Rm3dy9TTQ/640?wx_fmt=svg&from=appmsg)

 与各自诊断位是否原子对应；

-

两路样本是否带可比较的采样序号或硬件时间戳；

-

角度无效时，最后有效值、错误码和恢复首帧能否区分；

-

滤波配置改变后，数据延迟是否可计算，而不只是“更平滑”；

-

原始幅值、AGC 或内部状态能否与角度同帧导出，用于区分磁路、供电与通信异常。

这五行不是给系统公司开需求清单。它们都是从那张控制框图里倒推出来的：因为

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4pXqFWzJyAj3sg5b66mcibhCy0wmTr25lIGQ62Xgiak8ibVhF4Gq6iaYV28oKvRiaKpZrVicyQWFWPEuDkvyepoeQTic8B7WyQDDAgGNP4TugSWagUQ/640?wx_fmt=svg&from=appmsg)

 有三条去路，因为

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5uymiaX8wy72X7FTibVjP5hGGJ1Rq6z7IfaEqEhQ30YxR2tPgBAr7J2YelQ5vKCvKQKnMRf4qfFsdU8yI9dXmALZa2GiaQ38SvgNicENibxjh8Pag/640?wx_fmt=svg&from=appmsg)

 与它做差，因为微分会改变错误形状，因为碰撞把可用时间压到毫秒量级，所以错误的“值、时刻、状态”必须能重新对齐。

### ◆再回到地图，芯片公司消失的位置终于具体了

Bota Systems 的公开时间线写着：2013 年先为腿式机器人与研究平台做多轴力/力矩传感器原型，2016 年与 ETH Robotic Systems Lab 合作，把 Rokubi 用到 ANYmal，2020 年才正式成立公司。今天 Bota 和 ANYbotics 公布的地址分别是 Hagenholzstrasse 85 与 83a。

这个例子并不能证明苏黎世所有供应关系都靠同一栋楼，也不能证明地图外没有半导体公司。它只给出一段可核对的硬件历史：传感器先进入机器人研究平台和控制链，后来才长成一家独立公司。

ANYdrive 里的位置传感器更隐蔽。公开资料没有告诉我具体芯片型号，也没有给芯片厂商一个 logo。可只要沿

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7dZTia5V0kZOvlfalBjDibRJiaQZMIjqpVCwicnsj1aX84VBoWWrfVpIXmkVCME4dR6QtomjKvicwadktJia1WHmf34wMtSEKYO0NxprqOVOKaDKXg/640?wx_fmt=svg&from=appmsg)

 追下去，它先决定位置误差，又参与弹簧力矩，再经微分改动摩擦补偿；沿

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6z8REia3G9ibpbOFPicdfic1Gj9hcZUftHLVUpbK8zrSaNYhvWO89QX1EtBEwdk6liceqdaWJn26VHOpONd4hqdQZmhcDIsPhptXlJPE1HxqjPJqg/640?wx_fmt=svg&from=appmsg)

 追下去，它没有出现在位置环，却能单独制造假力矩；把两者放到时间轴上，即使各自静态合格，相对延迟仍能造出不存在的弹簧变形。

地图上看不见芯片，不是因为芯片离机器人很远。

恰好相反，它离控制后果太近，已经被画成了框图里的一根线。

我最后没有在纸上写“苏黎世模式”或“深圳模式”。只留下四个还不能从公开资料回答、但任何想替换这两只位置传感器的人都绕不过去的问题：

两路角度到底在哪一个时钟沿成为“同一帧”？

共同偏置、差分偏置和单帧毛刺，固件分别怎样识别？

诊断判定占用了碰撞后 2 ms 响应窗口中的多少？

当客户只发来一段电流尖峰，能不能沿

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4XfHz4BYY7OrMQicuHzMBibjL60rchkkSicsgxLQlTKeFq1g6SkD0D5HrCvMfmjPHCyms3V5M5KeXoul3lJL68s4vgKeHFzfJMk7rohDmJdVgtA/640?wx_fmt=svg&from=appmsg)

 反向走回最初那一帧？

复验结束以后，又由谁在异常记录里确认这条传播链成立，谁负责接受下一版固件的停机判据？

地图仍然没有多出一家芯片公司。

但那颗芯片该站的位置，已经比一个 logo 清楚多了。

### ◆地图上的 26 个名字，各自靠什么被记住

这 26 个名字并不都是真正意义上的机器人公司：有研究机构，有已经并入大公司的团队，也有只做软件、根本不碰电机轴的公司。下面照地图顺序，各抓一个最难被别家替换的细节。

1.

**Verity**：它的仓库无人机每天拍货架、读库存，靠自研 UWB、视觉和固定桨飞行。最有意思的命名反差是：Verity 的专利里大量出现 angle，但核心是无线电到达角，不是机械轴角；四个桨轴并不靠位置编码器闭环。

2.

**Gravis Robotics**：它不重新造挖掘机，而是在现有工程机械车顶加一套 RACK，让机器自动挖掘、整平和搬料。动臂姿态主要由贴装 IMU 与拉线位移计恢复；对老设备来说，外挂感知比拆开液压关节加编码器现实得多。

3.

**ANYbotics**：ANYmal 的辨识度不只是四条腿，而是把防水防尘、工业巡检和串联弹性关节做成同一台机器。本文拆的 ANYdrive 正来自这条线：两只绝对位置传感器测弹簧两端，位置差直接成为关节力矩反馈。

4.

**RAI Institute Zürich**：它是研究机构，不是卖整机的创业公司。苏黎世中心是 RAI 在波士顿之外的第二站，由 Marco Hutter 推动落地；其 UMV 原型把轮腿、高速运动和学习控制放在一台机器上，硬件大量采用现成执行器模块。

5.

**mimic**：M1 灵巧手最值得看的不是“像人手”，而是腱驱动之后仍把电机角与关节角分开测。21 个关节配关节侧编码器，训练用 U1 外骨骼又有一套人体动作测量；一次示教工位的角度通道数因此几乎翻倍。

6.

**Bota Systems**：Bota 把关节力矩传感器做到 7 mm 厚，BTS-T 系列可在 4 kHz 下通过 EtherCAT 输出，标称过载能力 500%。它的核心不是一颗神秘 ASIC，而是应变弹性体、逐台标定、低延迟采集与机器人总线被封成一个薄法兰。

7.

**Flexion Robotics**：Flexion 不造自己的“标准人形”，它卖跨硬件运行的自主软件 Reflect。最特别的地方是故意把本体留给第三方：同一套策略要跨不同人形平台和定制末端执行器工作，公司的产品边界停在机器人“大脑”而非关节 BOM。

8.

**ABB Robotics**：ABB 六轴机器人的位置链仍很传统：电机侧旋变进入测量板，绝对精度靠出厂整机标定模型补偿。SafeMove 的第二安全通道也不是第二只编码器，而是主计算机的指令值；这套架构把安全认证放在器件替换之前。

9.

**Duatic**：DynaArm 一个关节同时读电机、减速器与输出端三路角度，其中输出轴是 21 位绝对位置。它没有再装传统关节力矩传感器，而是从电机电流估力矩；三路角度的价值主要是把回差、弹性和真实输出位置分开。

10.

**RIVR**：它原名 Swiss-Mile，最醒目的结构是四条腿末端各带一只轮子：12 个腿关节负责跨台阶，4 个轮毂负责高效滚行。两类轴对位置反馈的要求并不相同；被 Amazon 收购后，器件本地化岗位还落到了上海。

11.

**FORGIS**：FORGIS 不卖机械臂，它让 ABB、KUKA 等现成机器人从人类示范和视频中生成可执行程序。公开研究里，机器人状态回读只有约 100 Hz；它能改变工艺编程方式，却隔着整机厂与伺服供应商两层，碰不到编码器选型。

12.

**Sevensense Robotics**：Alphasense 把多相机、IMU 和视觉 SLAM 封成一个定位盒，后来被 ABB 收购。最值得记住的是时间关系：相机与 IMU 做硬件同步，主机侧用 PTP；轮式里程计却从另一条 UDP 路径进来，1 ms 错位在 3 m/s 下就是 3 mm。

13.

**Voliro**：Voliro T 是一台会贴墙工作的三旋翼无人机，能向曲面持续施加最高约 30 N 接触力做超声或涡流检测。整机真正需要角度反馈的不是三个桨轴，而是两根独立倾转轴；早期方案甚至靠换相霍尔与高减速比推算位置。

14.

**Embotech**：Embotech 把优化求解器直接放进自动驾驶闭环，已经用于港口无人牵引车和车辆自动泊车。早期赛车论文给过一个很硬的时间账：20 ms 控制周期里，在线优化求解约占 15 ms，留给感知、通信和执行的余量只剩几毫秒。

15.

**Bubble Robotics**：它想把水面母船 BubbleDock 驻留数月，再反复布放、回收和充电水下 BubbleBot。公司公开说子机集成成熟 ROV/AUV 平台，所以最有价值的自有转轴可能不在推进器，而在跨压力壳工作的收放绞盘与对接机构。

16.

**Nautica Technologies**：HYDRA 不是偶尔下水检查的 ROV，而是常驻船体表面做清刷与检测的爬行机器人。公开视频里能辨认出一根全宽刷辊和两组驱动脚；一旦长期自主运行，轮上角度就同时参与换相、里程计和是否打滑的判断。

17.

**Flink Robotics**：Flink 用外购六轴机械臂、自研机身和真空夹爪处理尺寸形状不断变化的包裹。它最有特色的不是再造一台万能机器人，而是让多台机器人快速换任务、协同装卸；关节编码器随整臂买进来，选型权仍在机械臂厂。

18.

**Disney Research**：Disney 的目标不是把机器人做成标准工人，而是让 Olaf、BD-X 这类角色走路时仍保留动画性格。公开论文里关节常由 Unitree、Robotis 等模块拼成，仿真训练还会随机加入约 0.005～0.015 rad 回差，专门学习硬件的不完美。

19.

**Tethys Robotics**：Tethys ONE 是 35 kg 的 ROV/AUV 双模水下机器人，能在浑水和急流中工作。它的导航底座不是摄像头，而是 500 kHz DVL、IMU 与声呐；全机明确带角度反馈的机械轴，反而是外购 Reach Alpha 机械臂。

20.

**Auterion**：PX4 作者 Lorenz Meier 创办的 Auterion，把开源飞控做成 AuterionOS、Skynode 计算模块和 Nemyx 蜂群层。Skynode S 接口能接 PWM、CAN、SPI、摄像头与 PPS，却没有专用编码器口；转轴细节被留在 ESC 和云台内部。

21.

**April Robotics**：这是一家 2026 年才登记的新公司，官网目前只留下一句“Teaching robots the human way”。它瞄准的是灵巧制造中的人到机器人技能迁移：从人的示范直接学习精细操作，再把模型变成可部署技能；公开产品与硬件细节仍很少。

22.

**microagi**：microagi 的 Atlas 不绑定某一种机器人或模型，而是在工厂里记录熟练工操作，把真实示范转进仿真，再微调策略回到产线。两位创始人来自 F1 工程体系；它卖的核心是部署与数据闭环，不是又一台展示用人形机。

23.

**Loki Robotics**：Loki 选了一个很不“科幻”的难题——让机器人像人一样清洁卫生间和复杂设施。机器要换工具、控制清洁剂并与高变化表面接触；自主策略做不完时接入人工遥操作，每次介入又变成下一轮训练数据。

24.

**Hexagon Robotics**：AEON 人形机器人的差异点来自母公司 Hexagon 的测量、定位与数字孪生资产，而不只是双足结构。它把激光扫描和空间智能带进工厂任务；与 Schaeffler 公布的计划甚至指向未来至少 1000 台的训练、验证、部署闭环。

25.

**Wingtra**：WingtraOne 用尾座式垂直起降，转换飞行时翻转整个机身，因此没有倾转机构；官方称整机只有四个可动件——两个定距桨和两片襟翼。相机也固定安装，测绘精度主要交给 PPK 和后处理，而不是机械云台。

26.

**Ascento**：Ascento Guard 用两只轮子快速巡逻，遇到台阶又能靠轮腿结构跨越，载荷集成热成像、RGB 与红外相机。它不按台卖机器人，而是提供安防 RaaS；8 小时续航、自动回充和 24/7 支持比实验室里的单次越障更接近产品核心。

### ◆公开来源

-

Lukas M. Ziegler 的苏黎世机器人公司地图原帖：地图、作者补充名单与“地图不完整”的说明；评论区含盈利能力、系统构建者及苏黎世产业条件等讨论。

-

Camilla Mazzoleni 的转发帖及评论：可核对“invite to Shenzhen”评论与对机器人集群叙事的不同意见。

-

ANYdrive 2016 ECHORD 技术报告：ANYdrive 尺寸、质量、速度与力矩指标；θj、θg、弹簧力矩估算、级联位置/力矩控制和摩擦补偿框图；17 bit 与 0.025°；70/24 Hz、13/35 ms、碰撞和零力矩试验。正文对 100 μs 的计算是基于公开峰值速度的接口审查情景，不是对该设备采样时差的实测结论。

-

ANYdrive: Compact, compliant joint units for advanced interaction：后续公开论文版本，可交叉核对 0.08 N·m、关节结构与性能试验；与 2016 报告正文的 8 mN·m 存在口径或版本差异，本文不擅自消解。

-

ANYbotics signal_logger 公开仓库：可核对缓冲、日志元素、时间处理、文件格式与 RQT 界面等公开实现。

-

Bota Systems 公司时间线：2013 年腿式机器人多轴力/力矩传感器原型、2016 年 Rokubi 与 ANYmal 合作、2020 年公司成立。

-

ETH Robotic Systems Lab 的 spin-off 名单与 ETH Autonomous Systems Lab 的 spin-off/start-up 名单：核对苏黎世机器人集群与 ETH 实验室的直接来源关系。

-

ETH 2025 年知识转移报告：RAI Institute 在苏黎世设立第二中心及“Zurich with ETH / Boston with MIT”的公开背景。
