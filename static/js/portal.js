(() => {
  'use strict';
  const form = document.getElementById('portal-search-form');
  if (!form) return;
  const input = document.getElementById('portal-search-input');
  const panel = document.getElementById('portal-results');
  const list = document.getElementById('portal-search-list');
  const count = document.getElementById('portal-search-count');
  const data = JSON.parse(document.getElementById('portal-search-data').textContent);
  const labels = {model:'型号资料', company:'公司与品牌', post:'文章', basic:'基础知识'};
  const normalize = value => value.normalize('NFKC').toLocaleLowerCase().replace(/[\s\-‐‑–—_·]/g, '');
  let kind = '';
  let limit = 24;
  const more = document.getElementById('portal-search-more');
  function render(scroll = false) {
    const query = input.value.trim();
    if (!query) { panel.hidden = true; return; }
    const tokens = query.split(/\s+/).map(normalize).filter(Boolean);
    const found = data.filter(item => (!kind || item.kind === kind) && tokens.every(token => normalize(item.title+' '+item.description+' '+item.keywords).includes(token)));
    found.sort((a,b) => {
      const score = item => (normalize(item.title) === normalize(query) ? 100 : 0) + (normalize(item.title).includes(normalize(query)) ? 20 : 0) + (item.kind === 'model' ? 4 : item.kind === 'company' ? 2 : 0);
      return score(b)-score(a);
    });
    panel.hidden = false;
    document.getElementById('portal-results-title').textContent = '“'+query+'”的搜索结果';
    list.replaceChildren();
    count.textContent = found.length ? '找到 '+found.length+' 项'+(found.length>limit?'，当前显示前 '+limit+' 项。':'。') : '没有找到匹配内容。可以试试完整型号、品牌或较短的技术关键词。';
    more.hidden = found.length <= limit;
    found.slice(0,limit).forEach(item => {
      const a = document.createElement('a');a.className='search-result';a.href=item.url;
      const badge=document.createElement('span');badge.className='result-kind';badge.textContent=labels[item.kind];
      const title=document.createElement('strong');title.textContent=item.title;
      const desc=document.createElement('p');desc.textContent=item.description;
      a.append(badge,title,desc);list.append(a);
    });
    const url = new URL(location.href);url.searchParams.set('q',query);history.replaceState(null,'',url);
    if(scroll) panel.scrollIntoView({behavior: matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth',block:'start'});
  }
  form.addEventListener('submit',event=>{event.preventDefault();render(true);});
  input.addEventListener('input',()=>{limit=24;render(false);});
  more.addEventListener('click',()=>{limit+=24;render(false);});
  document.querySelectorAll('[data-query]').forEach(button=>button.addEventListener('click',()=>{limit=24;input.value=button.dataset.query;render(true);}));
  document.querySelectorAll('[data-search-kind]').forEach(button=>button.addEventListener('click',()=>{limit=24;kind=button.dataset.searchKind;document.querySelectorAll('[data-search-kind]').forEach(x=>{x.classList.toggle('active',x===button);x.setAttribute('aria-pressed',String(x===button));});render(false);}));
  document.getElementById('portal-search-clear').addEventListener('click',()=>{panel.hidden=true;input.value='';const url=new URL(location.href);url.searchParams.delete('q');history.replaceState(null,'',url);input.focus();});
  const initial=new URLSearchParams(location.search).get('q');if(initial){input.value=initial;render(false);}
})();
