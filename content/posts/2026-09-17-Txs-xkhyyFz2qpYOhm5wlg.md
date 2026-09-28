---
title: "双磁环编码器 两个码道 之间隔了一块＂软磁"
date: 2026-09-17T17:17:00+08:00
slug: "Txs-xkhyyFz2qpYOhm5wlg"
description: "珠海楠欣半导体公开了件专利，双磁环编码器中间硬塞了一圈软磁材料。"
original: "https://mp.weixin.qq.com/s/Txs-xkhyyFz2qpYOhm5wlg"
---

珠海楠欣半导体公开了件专利，双磁环编码器中间硬塞了一圈软磁材料。

内圈单极对给个粗角，外圈多极对把角度切细。两只磁环靠得近，磁场就互相串门。外圈芯片读到的细角信号直接被带偏，算法补偿都只是在给变形的信号记账。

解法是在中间加一圈软磁隔离环。它不是屏蔽板，而是给漏磁修条低磁阻回路。磁通优先顺着它绕回去，不再漫进隔壁码道。

软磁环先导走大串扰，芯片再收掉小残差。去偏置、归一化、扶正坐标轴，最后才追波形褶皱。这套顺序不能乱。

外环是4对极，粗角一旦认错段，机械角直接跳90度。所以误差从4.8降到0.6，不是算法把数字除小了。是软磁环先救回输入，两路角度才没认错段。

两颗芯片通过接口互传，由其中一颗给出最终绝对角。转得越快，采样时刻和传输延迟越会吃进误差预算。

一只软磁环的价值，就是卡在磁场还没变成信号的门槛上。先别让两只永磁环互相捣乱，再谈算法怎样把角度算得更好。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DBrlpXS1RIUvswicFwWia5vDNTlItsT1Aq7dyM7aj9nHY5ictUYtaVq0rdlBibnOUgIzibMqcXicz1tdKJZn2TooxBxUWsU4tJXmqNmpmSSBCb3DU/0?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DBrlpXS1RIVdGupvjbKkRNPMI0NpibL0xbhpWu3ApM1yeKCBUVJYGrE25oibneK4kwRMeJjd9RKhQibicQWbeQiboxZCfib3w3e38rRSoAvmCShUQ/0?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/DBrlpXS1RIUvkRyPg9QTsmic8iaiahmU8OzeacwnVLfOwptfHEMHWnQcx9Ozrmze81fXqbgBwicw0ZxyMxBAGxHGE5Rm7cu3WuUnbXGn531ORKo/0?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/DBrlpXS1RIVQNykO6Cqj04Kdj6VQA2pHPMa2Y2mkfX3yWialNrlboibpXIJI0VQtDYWrO0nhzZV3A043ib8CSicwuFpfGmkokRyE3WaIV7buwnI/0?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DBrlpXS1RIUiayqibBPYdBiaU1G7uASYC8NibnnVx2YO4F2RRlg6PYXLiaLhzZ1pHNTJ33KEibRP7FcPQm2BZjASlYARdUnlxXW81RweD585Lib8Jg/0?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DBrlpXS1RIWKYZBWzlCHQZAsgALIAydcXHIPLEtKx9xLibINJX6g8OAzHIA97hXLDHTFDzLdnMWvmZ4xZmooVchTWJgu6ZCvv35XGTUIkchg/0?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/DBrlpXS1RIUkhSmibLUa6ej2ibDppZf7fWWrFvDWNBn2EFpymFKj89oH8gtvznia3p7CchYXicULPHMJhIwEibN3vfO4P6nrPF9vlguY2EicPW26Y/0?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/DBrlpXS1RIU4MS4YjrLKzljCeTH8NHM0HUOqLYcewSibEzwXqTOIfjAbrB3NgbgU9uKOrMSiawzdvEwicqEOeQbY4fdj5rVlABC4RmYJPpichnw/0?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIXueeCY8uMymcyqfzicSfVOfqx87iaqpcDOjAsh6D2wlZAjiblkD1FuhecOUAJx6DFkiaeumAnEyUiazSRliaE2ogJDF47rkMofEV4rA/0?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIWMYVvN6LuOYUzGgIFhuIH3pWUkBPX0lVF8muo6AJqfqX7B2yIFaIBJGVnKDsfpHg7ohY9PYjAT54zGDpoNSA3LuW5RiaDoPAyc/0?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DBrlpXS1RIXu1VO6Isd1apxuUxIiciciboPu42g44jiaCAnn09D3ZksRLtuXzOE1p8HXpDic3MLrYXKJS7gdwIyrlCjQUIP21bm90WicUgW0zKFuk/0?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/DBrlpXS1RIWOiaQMFY0uGkmdhz3Fm8rRNlRttBRzsvZuO2L5cXGcktzVJJmppfOGc2qmCG9K9oyA8tqOBTyL10JicfJ2J3UGupGNG6cwEQib48/0?wx_fmt=jpeg)
