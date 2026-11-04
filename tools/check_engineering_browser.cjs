const {chromium}=require('playwright');
const fs=require('fs');
(async()=>{
 const base=process.argv[2]||'http://127.0.0.1:18780';
 const out=process.argv[3]||'/private/tmp/site-write-20261024';
 const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
 const page=await browser.newPage();const errors=[];page.on('pageerror',e=>errors.push(e.message));
 const data=JSON.parse(fs.readFileSync(out+'/engineering-check.json','utf8'));
 const checks=[];
 const extraRoutes=['/','/wiki/','/companies/seiko-npc/',...['smd-01b','resolute-rl','rod-280','posital-ktd-s100b-1609'].map(x=>'/models/'+x+'/'),...['resolution-accuracy','inl','latency','self-calibration','angle-noise','interfaces','crc','spi-ssi','abz','pole-pairs','singleturn-multiturn','mounting','magnetic-encoder','inductive-encoder','vernier','amr','tmr','vertical-hall','optical-encoder','absolute-incremental','eccentricity'].map(x=>'/wiki/basics/'+x+'/'),...['servo-motor','robot-joint','linear-motor','gearbox','water-meter','pneumatic-cylinder','closed-loop-stepper','brushless-dc-motor'].map(x=>'/applications/'+x+'/')];
 for(const width of [1440,360]){
  await page.setViewportSize({width,height:1000});
  for(const slug of [''].concat(data.items.map(x=>x.slug))){
   const route=slug?'/topics/guides/'+slug+'/':'/topics/';
   await page.goto(base+route,{waitUntil:'networkidle'});
   const result=await page.evaluate(()=>({width:innerWidth,scroll:document.documentElement.scrollWidth,h1:document.querySelectorAll('h1').length,math:[...document.querySelectorAll('.content math')].map(x=>({width:x.getBoundingClientRect().width,display:getComputedStyle(x).display})),font:getComputedStyle(document.querySelector('.content')).fontSize}));
   if(result.scroll>width+1)throw Error('page overflow '+width+' '+slug+' '+result.scroll);
   if(result.h1!==1)throw Error('h1 '+slug);
   if(result.math.some(m=>m.display==='block'))throw Error('MathML block regression '+slug);
   checks.push({width,route,...result});
   if(['','velocity-noise','system-acceptance-record','optical-tolerance-evidence','measurement-tools'].includes(slug))await page.screenshot({path:out+'/'+(slug||'index')+'-'+width+'.png',fullPage:true});
  }
  for(const route of extraRoutes){await page.goto(base+route,{waitUntil:'networkidle'});const res=await page.evaluate(()=>({scroll:document.documentElement.scrollWidth,h1:document.querySelectorAll('h1').length}));if(res.scroll>width+1||res.h1!==1)throw Error('extended layout '+width+' '+route+' '+JSON.stringify(res));checks.push({width,route,...res});}
 }
 await page.goto(base+'/topics/guides/measurement-tools/',{waitUntil:'networkidle'});
 const text=async id=>page.locator('#'+id+' output').innerText();
 let s=await text('frequency-tool');if(!s.includes('409,600')||!s.includes('102,400'))throw Error('frequency defaults '+s);
 s=await text('latency-tool');if(!s.includes('2.52')||!s.includes('0.36'))throw Error('latency defaults '+s);
 s=await text('statistics-tool');if(!s.includes('2.1602469')||!s.includes('0.816496581'))throw Error('stats 123 '+s);
 await page.locator('#statistics-tool textarea').fill('5,5,5');await page.locator('#statistics-tool button').click();s=await text('statistics-tool');if(!s.includes('RMS：5')||!s.includes('总体σ（N）：0'))throw Error('stats bias '+s);
 await page.locator('#statistics-tool textarea').fill('1,,3');await page.locator('#statistics-tool button').click();if(!(await text('statistics-tool')).includes('空字段'))throw Error('missing-field check');
 await page.locator('#statistics-tool textarea').fill('1e309');await page.locator('#statistics-tool button').click();if(!(await text('statistics-tool')).includes('有限数值'))throw Error('finite check');
 await page.locator('#frequency-tool input[name=rpm]').fill('0');await page.locator('#frequency-tool button').click();if(!(await text('frequency-tool')).includes('合计：0'))throw Error('zero speed');
 await page.goto(base+'/?q=采样',{waitUntil:'networkidle'});await page.locator('[data-search-kind=guide]').click();if(await page.locator('#portal-search-list a').count()===0)throw Error('guide search');
 await page.locator('#portal-search-clear').click();await page.locator('#portal-search-input').fill('TLE5012 离轴');if(!(await page.locator('#portal-search-list').innerText()).includes('TLE5012B'))throw Error('search clear regression');
 if(errors.length)throw Error('browser errors '+errors.join(';'));
 fs.writeFileSync(out+'/browser-check.json',JSON.stringify({pages:checks,calculatorCases:7,searchCases:2,errors},null,2));
 await browser.close();console.log('PASS '+checks.length+' page/viewport checks, calculators and search');
})().catch(e=>{console.error(e);process.exit(1)});
