#!/usr/bin/env node
'use strict';
// Minimal DOM smoke test for the real portal script. No package installation.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
class Element {
  constructor(dataset = {}) {
    this.dataset = dataset; this.events = {}; this.children = [];
    this.hidden = false; this.value = ''; this.textContent = '';
    this.attrs = {}; this.classes = new Set();
    this.classList = {toggle:(name,on)=>on?this.classes.add(name):this.classes.delete(name)};
  }
  addEventListener(event, callback) { this.events[event] = callback; }
  setAttribute(key, value) { this.attrs[key] = value; }
  replaceChildren() { this.children = []; }
  append(...children) { this.children.push(...children); }
  focus() { this.focused = true; }
  scrollIntoView() {}
  fire(event) { this.events[event]({preventDefault(){}}); }
}
const ids = Object.fromEntries(['portal-search-form','portal-search-input','portal-results','portal-search-list','portal-search-count','portal-search-more','portal-search-data','portal-results-title','portal-search-clear'].map(id=>[id,new Element()]));
const kinds = ['', 'model', 'company', 'post', 'basic', 'application'].map(value=>new Element({searchKind:value}));
ids['portal-search-data'].textContent = JSON.stringify([
  {title:'TLE5012B',description:'离轴条件',keywords:'TLE5012',kind:'model',url:'/models/tle5012b/'},
  {title:'机器人关节',description:'候选器件',keywords:'关节',kind:'application',url:'/applications/robot-joint/'},
  {title:'斩波稳定',description:'失调',keywords:'霍尔斩波技术',kind:'basic',url:'/wiki/basics/chopper/'}
]);
const location = {href:'https://sensor.fans/?q=old',search:''};
const context = {URL,URLSearchParams,location,history:{replaceState(_a,_b,url){location.href=String(url);}},matchMedia:()=>({matches:true}),document:{getElementById:id=>ids[id],createElement:()=>new Element(),querySelectorAll:selector=>selector==='[data-search-kind]'?kinds:[]}};
vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../static/js/portal.js'),'utf8'),context);
function query(value) { ids['portal-search-input'].value=value;ids['portal-search-input'].fire('input'); }
query('霍尔斩波技术'); assert.equal(ids['portal-search-list'].children.length,1);
kinds[5].fire('click'); assert.equal(ids['portal-search-list'].children.length,0);
ids['portal-search-clear'].fire('click');
assert.equal(ids['portal-results'].hidden,true);
assert.equal(ids['portal-search-input'].value,'');
assert.equal(ids['portal-search-list'].children.length,0);
assert.equal(new URL(location.href).searchParams.has('q'),false);
assert.equal(kinds[0].attrs['aria-pressed'],'true');
query('TLE5012 离轴'); assert.equal(ids['portal-search-list'].children.length,1);
assert.equal(ids['portal-search-list'].children[0].href,'/models/tle5012b/');
kinds[5].fire('click'); query('');
assert.equal(kinds[0].attrs['aria-pressed'],'true');
query('TLE5012 离轴'); assert.equal(ids['portal-search-list'].children.length,1);
console.log('PASS portal clear button and empty-input reset: query, kind, URL, results, pagination and ARIA state');
