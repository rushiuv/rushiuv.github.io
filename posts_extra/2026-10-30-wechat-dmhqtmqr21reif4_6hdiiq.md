---
title: 长线传输吃掉信号质量：模拟正余弦 vs 数字协议
date: '2026-10-30T11:00:00+08:00'
slug: wechat-dmhqtmqr21reif4_6hdiiq
description: 编码器装机后精度下降，问题常不在芯片在线缆：模拟正余弦怕幅值衰减与相移失配，数字协议怕边沿畸变与共模干扰，布线处方完全不同。本文分信号类型拆解线缆损伤机理，给出屏蔽、双绞、终端匹配的分类处方与验收方法。
original: https://mp.weixin.qq.com/s/dmHqTMqr21reIF4_6HdiIQ
original_from: 转载自微信公众号「方寸技研」
author: 方寸技研
tags:
- 转载
no_promo: true
---

<div class="wechat-reprint">
<img alt="长线传输与信号质量技术封面" decoding="async" loading="eager" src="/images/wx/wechat-dmhqtmqr21reif4_6hdiiq-001-dbfe4291f6f8.png"/><p>实验室台架上，这台编码器的角度重复性是 0.01°。装进设备、拉上三米线缆，抖动直接放大十倍，EMC 预测试还扫出一根超标尖峰。芯片没换、参数没动、算法没改——变的是那根线。</p>
<p>线缆是编码器系统里最便宜、也最常被低估的器件。而且模拟正余弦信号和数字协议信号，被线缆伤害的方式<strong>完全不同</strong>——用同一套布线思路对付两者，等于哪儿都防了、哪儿都没防住。</p>
<img alt="模拟与数字信号的长线损伤清单" decoding="async" loading="lazy" src="/images/wx/wechat-dmhqtmqr21reif4_6hdiiq-002-61461f0ff8ee.png"/><p>图 1｜模拟信号伤害清单 vs 数字协议伤害清单</p>
<h3>一、两类信号，两张伤害清单</h3>
<p><strong>模拟正余弦信号</strong>传输的是连续幅值，线缆的每一分损伤都直接进幅值和相位：直流压降让信号摆幅缩水；线缆电容和输出阻抗构成低通，频率越高衰减越狠；两路 Sin/Cos 线长或容抗不对称会引入相移失配，插值直接报错；外界干扰耦合进来就是实打实的角度噪声。</p>
<img alt="模拟正余弦经过长线后的波形示意" decoding="async" loading="lazy" src="/images/wx/wechat-dmhqtmqr21reif4_6hdiiq-003-946dd228431d.png"/><p>图 2｜正余弦波形经过长线后的变化</p>
<p><strong>数字协议信号</strong>传输的是边沿时序，线缆的伤害换了一副面孔：长线容抗让边沿变缓，时序余量被吃；阻抗失配在端点反射，振铃打断判决门限；共模干扰沿着屏蔽层找入口；所谓"协议抗干扰强"，前提是校验没被关掉、误码重传机制还活着。</p>
<img alt="数字发送与接收端边沿变化示意" decoding="async" loading="lazy" src="/images/wx/wechat-dmhqtmqr21reif4_6hdiiq-004-38b7dd0ea8f9.png"/><p>图 3｜发送 vs 接收端对比</p>
<p>带走一句话：<strong>模拟信号怕"幅值被偷"，数字信号怕"边沿被掰"——伤害机制不同，处方就不同。</strong></p>
<h3>二、模拟正余弦的布线处方</h3>
<p><strong>双绞是底线。</strong> Sin、Cos 各自走双绞，让耦合进两根线的干扰在差分接收里抵消。单端传输加单根线的老做法，在长线上等于给干扰开绿灯。</p>
<p><strong>屏蔽单端接地。</strong> 屏蔽层只在一端接参考地——通常在接收侧。两端都接会形成地环路，把两个设备之间的地电位差圈进信号回路，地噪声直接串进来。</p>
<img alt="模拟正余弦的四条布线处方" decoding="async" loading="lazy" src="/images/wx/wechat-dmhqtmqr21reif4_6hdiiq-005-b893b39ef0c4.png"/><p>图 4｜双绞 / 屏蔽单端接地 / 差分接收 / 激励配对</p>
<p><strong>激励与反馈配对走线。</strong> 需要激励的方案——电感式、旋变类——激励线和反馈线配对双绞，让拾取干扰在解调时被同步抵消。</p>
<p><strong>接收端差分化。</strong> 芯片端尽量用差分接收，别把宝贵的共模抑制比浪费在单端引脚上。</p>
<h3>三、数字协议的布线处方</h3>
<p><strong>终端匹配是第一件事。</strong> 先查协议手册要求的特征阻抗和终端电阻【待核对手册】，线缆特征阻抗与终端匹配上了，反射振铃才能压下去。</p>
<p><strong>共模扼流加隔离。</strong> 长线跨越设备地电位差的场合，共模扼流圈压共模电流，必要时上数字隔离器切断地环路。</p>
<img alt="数字协议的四条布线处方" decoding="async" loading="lazy" src="/images/wx/wechat-dmhqtmqr21reif4_6hdiiq-006-b51f98b5c93a.png"/><p>图 5｜终端匹配 / 共模扼流 / 隔离 / 校验开启</p>
<p><strong>协议校验别关。</strong> CRC、重传机制是协议抗干扰的底气，为了"省几个字节"把校验关掉，长线上的误码就直接变成位置错误。</p>
<p><strong>边沿余量要验收。</strong> 用示波器在接收端看边沿，上升时间不能吃掉判决窗口的时序余量。</p>
<img alt="屏蔽层单端与两端接地对照示意" decoding="async" loading="lazy" src="/images/wx/wechat-dmhqtmqr21reif4_6hdiiq-007-40f8964b160d.png"/><p>图 6｜图6 屏蔽层两端接地形成地环路 vs 单端接地的对比</p>
<h3>四、验收两步法</h3>
<p><strong>静态重复性验收：</strong> 装好线缆后，固定轴不动，连续采集位置数据看散布——散布比实验室数据明显变大，说明干扰已进来，先解决再谈精度。</p>
<p><strong>动态波形验收：</strong> 示波器看接收端波形——模拟信号看摆幅是否缩水、两路相位是否对称；数字信号看边沿是否陡峭、有无振铃过门限。波形干净，数据才可信。</p>
<img alt="静态重复性与动态波形两步验收流程" decoding="async" loading="lazy" src="/images/wx/wechat-dmhqtmqr21reif4_6hdiiq-008-7bca40cf88d6.png"/><p>图 7｜图7 静态重复性 + 动态波形两步验收流程</p>
<h3>对照卡：两类信号的长线处方</h3>
<img alt="模拟与数字长线处方对照卡" decoding="async" loading="lazy" src="/images/wx/wechat-dmhqtmqr21reif4_6hdiiq-009-39ac6923500b.png"/><p>图 8｜图8 模拟 vs 数字五维对照卡表格图形化</p>
<table><tbody><tr><td>维度</td><td>模拟正余弦</td><td>数字协议</td></tr><tr><td>最怕什么</td><td>幅值衰减、相移失配</td><td>边沿畸变、反射振铃</td></tr><tr><td>第一处方</td><td>双绞 + 屏蔽单端接地</td><td>特征阻抗 + 终端匹配</td></tr><tr><td>干扰入口</td><td>耦合直接进幅值</td><td>共模沿屏蔽层进地</td></tr><tr><td>接收端</td><td>差分接收</td><td>隔离 + 共模扼流</td></tr><tr><td>验收动作</td><td>静态散布 + 摆幅/相位检查</td><td>边沿余量 + 校验开启确认</td></tr></tbody></table>
<h3>总结</h3>
<p>· 线缆伤害分两套机制：模拟怕幅值被偷，数字怕边沿被掰，处方不能混用；</p>
<p>· 模拟靠双绞、屏蔽单端接地、差分接收；数字靠终端匹配、隔离、校验别关；</p>
<p>· 长线装好后先做静态重复性和动态波形两步验收，波形干净再谈精度。</p>
<br/>
</div>
