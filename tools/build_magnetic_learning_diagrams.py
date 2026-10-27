from pathlib import Path
import math,json,html
r=Path(__file__).resolve().parents[1]
d=r/'static/images/learning';d.mkdir(exist_ok=True,parents=True)
N='#203647';T='#367b7c';G='#b68b43';C='#d27e64';BG='#f7f3e9';LINE='#cbd4c9'
checks=[]
def text(x,y,s,size=24,fill=N,anchor='start'):
 return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}">{html.escape(s)}</text>'
def line(x1,y1,x2,y2,color=N,arrow=False,dash=False):
 return f'<path d="M{x1},{y1} L{x2},{y2}" fill="none" stroke="{color}" stroke-width="3"'+(' marker-end="url(#arrow)"' if arrow else '')+(' stroke-dasharray="9 7"' if dash else '')+'/>'
def rect(x,y,w,h,fill='#fffdf7',stroke=LINE,rx=14):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
def path(points,color=T,width=4,dash=False):
 return '<path d="'+' '.join(('M' if i==0 else 'L')+f'{x:.3f},{y:.3f}' for i,(x,y) in enumerate(points))+f'" stroke="{color}" stroke-width="{width}" fill="none"'+(' stroke-dasharray="8 6"' if dash else '')+'/>'
def save(name,title,desc,body,h=560):
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{h}" viewBox="0 0 960 {h}" role="img" aria-labelledby="title desc"><title id="title">{html.escape(title)}</title><desc id="desc">{html.escape(desc)}</desc><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M1 1 L9 5 L1 9" fill="none" stroke="context-stroke" stroke-width="1.5"/></marker></defs><rect width="960" height="{h}" rx="24" fill="{BG}"/><g font-family="PingFang SC,Microsoft YaHei,Noto Sans CJK SC,sans-serif">{text(38,48,title,27)}{body}</g></svg>'''
 (d/f'{name}-20261027.svg').write_text(svg)
# 1 Hall top view, no unsupported polarity
b=rect(195,125,465,260,'#dfebe4')+line(80,255,755,255,N,True)+text(94,228,'偏置电流 I：+x')
for x,y in [(280,185),(390,185),(500,185),(280,325),(390,325),(500,325)]:
 b+=f'<circle cx="{x}" cy="{y}" r="15" fill="none" stroke="{T}" stroke-width="2"/><circle cx="{x}" cy="{y}" r="4" fill="{T}"/>'
b+=line(428,125,428,85)+line(428,385,428,435)+rect(400,113,56,24,G,G,3)+rect(400,373,56,24,G,G,3)
b+=text(455,104,'差分测量端 A')+text(455,430,'差分测量端 B')+text(710,165,'⊙ Bz：出纸面',23,T)+line(815,350,895,350,N,True)+text(897,358,'x',20)+line(815,350,815,275,N,True)+text(804,266,'y',20)
b+=text(38,486,'VH = VB − VA；只读取横向端间电压，极性按载流子与接线定义。',23)+text(38,526,'图为平面霍尔俯视；薄片厚度沿 z，非具体封装引脚图。',22,T)
save('hall-axes','霍尔元件：电流、磁场与横向测量端','电流正向向右，B沿z出纸面，测量上下两端电位差。未指定载流子和RH符号，故不标正负。',b)
# 2 bridge
b=''
for x in [285,675]:
 b+=line(x,130,x,500)+rect(x-41,175,82,90,'#e3ece3',T,5)+rect(x-41,350,82,90,'#e3ece3',T,5)
for y in [130,500]:b+=line(285,y,675,y)
b+=line(480,90,480,130)+text(480,84,'VE 激励',24,N,'middle')+line(480,500,480,525)+text(480,553,'0 V',22,N,'middle')
for x,y,s in [(285,230,'R1'),(285,407,'R2'),(675,230,'R3'),(675,407,'R4')]:b+=text(x,y,s,26,N,'middle')
for x,s,tx in [(285,'A',218),(675,'B',701)]:
 b+=f'<circle cx="{x}" cy="305" r="6" fill="{N}"/>'+text(tx,313,s,25)
b+=line(285,305,380,305,T)+line(675,305,580,305,T)+text(480,313,'VA − VB',25,T,'middle')
b+=text(38,593,'VA = VE·R2/(R1+R2)       VB = VE·R4/(R3+R4)',23)+text(38,629,'VD = VA − VB；理想读出端输入阻抗无限大。',23,T)
save('magnetic-bridge','磁阻电桥：先定义节点，再推导输出','R1R2为左分支，R3R4为右分支，两中点差分。公式与图中编号一致。',b,650)
# 3 active low single polarity switch
x=lambda v:140+v*90
yh,yl=160,355
b=line(95,415,850,415,N,True)+line(95,415,95,105,N,True)+text(35,167,'H')+text(35,362,'L')+text(840,455,'B / mT',22)+text(36,92,'OUT',22)
b+=path([(x(-.2),yh),(x(4),yh),(x(4),yl),(x(7),yl)],T,5)+path([(x(7),yl),(x(2),yl),(x(2),yh),(x(-.2),yh)],G,4,True)
for v,s in [(0,'0'),(2,'BRP = 2'),(4,'BOP = 4')]:b+=line(x(v),105,x(v),415,LINE,False,True)+text(x(v),452,s,22,N,'middle')
b+=line(x(.5),yh,x(1.5),yh,T,True)+line(x(6.5),yl,x(5.4),yl,G,True)
b+=text(40,500,'实线：B 增大，到 4 mT 后输出变 L。',23,T)+text(40,536,'虚线：B 减小，到 2 mT 后输出变 H。',23,G)+text(40,575,'本站自设正阈值、低有效开关；回差 2 mT，不代表锁存器。',22)
save('switch-hysteresis','磁开关回差：同一个磁场值，还要知道运动历史','自设正极性低有效开关BOP4mT BRP2mT。箭头分别表示磁场增大和减小。',b,600)
# 4 exact RC response
pts=[(110+14*t,410-280*(1-math.exp(-t/10))) for t in [i/5 for i in range(251)]]
b=line(110,410,865,410,N,True)+line(110,410,110,110,N,True)+text(38,128,'1.0',21)+text(50,416,'0',21)+text(845,451,'t / ms',22)+text(60,96,'归一化输出',22)
b+=line(110,130,810,130,LINE,False,True)+path(pts,T,5)
t10=-10*math.log(.9);t90=-10*math.log(.1)
for t,label in [(10,'τ = 10 ms'),(t90,'90%')]:
 xp=110+14*t;yp=410-280*(1-math.exp(-t/10));b+=line(xp,yp,xp,410,LINE,False,True)+f'<circle cx="{xp}" cy="{yp}" r="6" fill="{G}"/>'+text(xp+10,yp-12,label,22)
b+=text(42,489,'y(t) = 1 − exp(−t/τ)     fc = 1/(2π τ) ≈ 15.9 Hz',24)+text(42,535,'y(τ) ≈ 0.632；10%–90% 上升时间 ≈ 2.197τ ≈ 22 ms',22,T)
save('noise-bandwidth','一阶低通：更平滑，也会更慢','解析阶跃响应，时间常数10毫秒。不是实测或具体器件保证值。',b)
checks.extend([{'name':'RC 1 tau','actual':1-math.exp(-1),'expected':0.6321205588285577},{'name':'RC rise ms','actual':t90-t10,'expected':21.972245773362193}])
# 5 chain two rows
b=''
for x,top,bot in [(40,'机械位置 x','机构与充磁条件'),(345,'磁场分量 Bs(x)','气隙、温度、铁件'),(650,'传感输出 V(Bs)','零点、增益、饱和')]:
 b+=rect(x,110,270,130)+text(x+135,160,top,25,N,'middle')+text(x+135,201,bot,20,T,'middle')
for xx in [310,615]:b+=line(xx,175,xx+30,175,N,True)
b+=line(785,240,785,285,N,True)+rect(650,290,270,120)+text(785,340,'采样 / ADC / 接口',23,N,'middle')+text(785,378,'量化、噪声与时间戳',20,T,'middle')
b+=line(650,350,615,350,N,True)+rect(345,290,270,120)+text(480,340,'位置估计 x̂',25,N,'middle')+text(480,378,'映射需单值且可校验',20,T,'middle')
b+=text(40,470,'V(B) 线性，不代表 V(x) 线性；数字接口也不代表位置已被唯一解算。',22)
save('sensor-chain','从位置到读数：每一段都有自己的条件','机械位置影响磁场，磁场经传感链转电压后采样，再通过映射估计位置。',b,520)
# 6 AMR normalized angle independent sinus
b=text(40,95,'理想饱和双桥：x = cos(4πu)，y = sin(4πu)',24)
for offset,fun,col,label in [(220,math.cos,T,'x'),(405,math.sin,G,'y')]:
 b+=line(110,offset,850,offset,LINE)+text(55,offset+8,label,25,col)
 pts=[(110+700*i/280,offset-65*fun(4*math.pi*i/280)) for i in range(281)];b+=path(pts,col,4)
 for u in [.1,.6]:
  xp=110+700*u;yp=offset-65*fun(4*math.pi*u);b+=line(xp,120,xp,485,LINE,False,True)+f'<circle cx="{xp}" cy="{yp}" r="6" fill="{C}"/>'
for u in [0,.1,.5,.6,1]:b+=text(110+700*u,515,str(u),21,N,'middle')
b+=text(842,515,'u',24)+text(40,564,'u=0.1 与 0.6 的两路输出相同；单靠此双桥只能区分半圈。',23)+text(40,604,'u 为机械转数；此图不包含额外极性或粗码判别通道。',22,T)
save('amr-angle','AMR双桥的半圈歧义：两路都重复，软件不能凭空补信息','数学生成的两个正交二倍频响应，u0.1与0.6有相同sin cos输出。',b,630)
checks.append({'name':'AMR half turn equal','actual':abs(math.cos(4*math.pi*.1)-math.cos(4*math.pi*.6))+abs(math.sin(4*math.pi*.1)-math.sin(4*math.pi*.6)),'expected':0,'tolerance':1e-12})
# 7 active/passive induction separation
b=rect(40,110,880,180)+text(70,152,'被动拾取线圈',25)+text(70,197,'外部磁通 Φ(t) 变化',23,T)+line(375,190,465,190,N,True)+text(490,197,'v = −N·dΦ/dt',27)+text(70,255,'线圈与目标相对固定、外场不变 → dΦ/dt = 0 → v = 0',22)
b+=rect(40,320,880,220)+text(70,362,'主动电感位置检测',25)
for xx,lab in [(65,'交变激励'),(350,'位置相关耦合'),(655,'接收 / 解调')]:
 b+=rect(xx,390,240,70,'#e2ece3',T,9)+text(xx+120,433,lab,23,N,'middle')
b+=line(307,425,347,425,N,True)+line(592,425,652,425,N,True)+text(70,510,'目标位置固定，内部激励仍变化 → 耦合幅相仍可携带静态位置信息',22)
save('induction-boundary','都是线圈，静止目标能不能测要看激励从哪里来','上为被动拾取线圈法拉第定律，下为具有主动交流激励的位置检测概念链。',b,570)
# 8 current compensation negative feedback
b=rect(45,135,190,120)+text(140,181,'原边电流 Ip',24,N,'middle')+text(140,221,'Np 匝',22,T,'middle')+line(235,195,285,195,N,True)
b+=rect(285,135,315,120)+text(443,181,'磁芯残余安匝',24,N,'middle')+text(443,221,'Np·Ip − Ns·Is',25,T,'middle')+line(600,195,640,195,N,True)+rect(640,135,270,120)+text(775,181,'霍尔 / 误差放大',23,N,'middle')+text(775,221,'驱动补偿绕组',22,T,'middle')
b+=line(775,255,775,350,N,True)+rect(485,350,330,100)+text(650,389,'补偿电流 Is 经 Ns 匝',24,N,'middle')+text(650,427,'方向选为抵消原边磁通',21,T,'middle')+line(485,400,443,400)+line(443,400,443,255,N,True)
b+=text(40,503,'稳态且环路未限幅：Np·Ip ≈ Ns·Is；若测量电阻为 Rm，Vout = Is·Rm。',22)+text(40,548,'绕向与电流正方向需配套；量程、磁芯饱和与环路带宽仍需核对。',22,T)
save('current-feedback','闭环磁式电流检测：用反向安匝逼近零磁通','原边正安匝减去补偿安匝，残余驱动补偿电流。概念负反馈框图，不是可直接接线原理图。',b,580)
# 9 multilayer conceptual
b=''
for base,title,midlabel in [(70,'GMR：金属间隔层','非磁性金属（示例 Cu）'),(515,'TMR：绝缘隧穿势垒','超薄绝缘势垒（示例 MgO）')]:
 b+=text(base,110,title,25)
 for y,fill,lab in [(145,T,'自由磁化层'),(225,'#ede0c3',midlabel),(305,N,'参考磁化层')]:
  b+=rect(base,y,365,66,fill,fill,5)+text(base+(230 if fill in [T,N] else 183),y+43,lab,21,'#fffdf6' if fill in [T,N] else N,'middle')
 b+=line(base+20,178,base+90,178,'#fffdf6',True)+line(base+20,338,base+90,338,'#fffdf6',True)
b+=text(40,432,'上图仅示意两层磁化方向平行的状态；反平行时通常为较高电阻状态。',22)+text(40,481,'GMR：自旋相关散射；TMR：自旋相关隧穿。',24,T)+text(40,526,'层结构非按比例；未指定GMR电流几何，也未表达真实工艺与偏置磁路。',21)
save('mr-structures','GMR与TMR：中间那一层改变了输运机制','金属间隔自旋阀和绝缘隧穿磁结的概念层结构。两磁化层平行，用同向箭头表示。',b)
# exact algebra checks
checks += [{'name':'bridge 3.3V differential','actual':3.3*(.99/2-1.01/2),'expected':-.033},{'name':'field units mT to G','actual':.001*1e4,'expected':10},{'name':'noise displacement um','actual':(.5/50)/2*1000,'expected':5}]
for q in checks:assert abs(q['actual']-q['expected'])<=q.get('tolerance',1e-10),q
(r/'data/magnetic-learning-diagram-checks-20261027.json').write_text(json.dumps({'checks':checks,'svgs':sorted(p.name for p in d.glob('*.svg'))},ensure_ascii=False,indent=2))
print('Created 9 SVGs; numerical checks',len(checks))
