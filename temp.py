#!/usr/bin/env python3
# space_server_full.py
# Single-file server that serves a full HTML/JS Space Explorer game
# with inventory, station shop (tabs), landing animation, black-market, and save/load.

from http.server import BaseHTTPRequestHandler, HTTPServer
import json, os

HOST = "localhost"
PORT = 3333
SAVE_FILE = "savegame.json"

# Ensure save file exists
if not os.path.exists(SAVE_FILE):
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump({}, f)

HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Space Explorer — Full Station Edition</title>
<style>
:root{--bg:#000814;--accent:#62dafb}
html,body{height:100%;margin:0;background:linear-gradient(180deg,var(--bg),#000012);color:#eaf6ff;font-family:Inter,Arial,Helvetica,sans-serif;overflow:hidden}
#ui,#hud,#missions{position:fixed;z-index:40}
#ui{left:12px;top:12px}
#hud{right:12px;top:12px;text-align:right}
#missions{left:12px;bottom:12px;background:rgba(1,6,20,0.6);padding:10px;border-radius:8px;max-width:420px}
button{background:var(--accent);border:0;padding:8px 12px;border-radius:6px;cursor:pointer;color:#002;font-weight:700}
canvas{display:block;margin:0 auto;border-radius:8px;box-shadow:0 10px 40px rgba(0,0,0,0.6)}
#game{background:#000012}
#minimap{position:fixed;right:12px;bottom:12px;width:200px;height:140px;background:rgba(0,0,0,0.45);border-radius:6px;padding:6px;z-index:40}
.centerScreen{position:fixed;left:50%;top:50%;transform:translate(-50%,-50%);text-align:center;z-index:80}
.hidden{display:none}
.panel{position:fixed;left:50%;top:60px;transform:translateX(-50%);width:420px;background:#071428;padding:14px;border-radius:10px;border:1px solid rgba(255,255,255,0.05);z-index:90}
.panel.large{width:760px}
.smalltext{font-size:12px;opacity:0.9}
.tabbar{display:flex;gap:8px;margin-bottom:8px}
.tabbar button{padding:6px 10px;background:transparent;border:1px solid rgba(255,255,255,0.06);color:#eaf6ff;cursor:pointer;border-radius:6px}
.fadeOverlay{position:fixed;left:0;top:0;width:100%;height:100%;background:#000;opacity:0;pointer-events:none;z-index:95;transition:opacity 400ms ease}
.scaleZoom{transform-origin:center center; transition:transform 500ms ease}
</style>
</head>
<body>

<div id="ui">
  <div>Score: <span id="score">0</span></div>
  <div>Coins: <span id="coins">0</span></div>
  <div>Health: <span id="health">100</span></div>
  <div>Fuel: <span id="fuel">100</span></div>
</div>

<div id="hud">
  <div>Enemies: <span id="enemies">0</span></div>
  <div>Lasers: <span id="lasers">0</span></div>
  <div>Upgrades: <span id="upgradesCount">0</span></div>
</div>

<div id="missions">
  <strong>Mission</strong>
  <div id="missionText">Collect 20 stars. (0/20)</div>
  <div style="margin-top:8px">
    <button id="saveBtn" class="small">Save Progress</button>
    <button id="loadBtn" class="small">Load Progress</button>
    <button id="restartBtn" class="small">Restart</button>
    <button id="shopBtn" class="small">Shop (S)</button>
    <button id="invBtn" class="small">Inventory (I)</button>
    <button id="mapBtn" class="small">Galaxy (G)</button>
  </div>
  <div style="margin-top:8px" class="smalltext">Controls: ← → rotate • Z = thrust • X = shoot • C = dash • P = pause • Double-click = teleport</div>
</div>

<canvas id="game" width="1100" height="700"></canvas>
<canvas id="minimap" width="200" height="140"></canvas>

<div class="centerScreen" id="startScreen">
  <h1 style="margin:0 0 10px 0">Space Explorer — Full Station Edition</h1>
  <div style="margin-bottom:12px">Collect items, fight enemies, visit stations and upgrade your ship.</div>
  <button id="startBtn">Start Game</button>
  <div style="margin-top:10px;font-size:13px;opacity:0.9">Background audio uses WebAudio — allow when prompted.</div>
</div>

<!-- Panels -->
<div id="shopUI" class="panel hidden" aria-hidden="true">
  <h3>🛒 Space Shop</h3>
  <div>Coins: <span id="shopCoins">0</span></div>
  <div id="shopList" style="max-height:260px;overflow:auto;margin-top:10px"></div>
  <div style="text-align:right;margin-top:10px"><button id="closeShop">Close</button></div>
</div>

<div id="inventoryUI" class="panel hidden" aria-hidden="true">
  <h3>📦 Inventory</h3>
  <div id="inventoryList" style="max-height:260px;overflow:auto;margin-top:8px">No items</div>
  <div style="text-align:right;margin-top:10px"><button id="closeInv">Close</button></div>
</div>

<div id="stationUI" class="panel large hidden" aria-hidden="true">
  <h3 id="stationName">Station</h3>
  <div class="tabbar">
    <button data-tab="Weapons">Weapons</button>
    <button data-tab="Upgrades">Upgrades</button>
    <button data-tab="Resources">Resources</button>
    <button data-tab="BlackMarket">Black Market</button>
  </div>
  <div style="display:flex;gap:12px">
    <div style="flex:1">
      <div id="stationContent" style="max-height:320px;overflow:auto;padding:6px"></div>
    </div>
  </div>
  <div style="text-align:right;margin-top:10px"><button id="leaveStation">Leave Station</button></div>
</div>

<div id="fade" class="fadeOverlay"></div>

<script>
// ==================== Globals & Canvas Setup ====================
const canvas = document.getElementById('game');
const ctx = canvas.getContext('2d');
const mm = document.getElementById('minimap');
const mmCtx = mm.getContext('2d');
const W = canvas.width, H = canvas.height;

let keys = {}, running=false, paused=false;
let ship, stars, planets, enemies, bullets, explosions, items, bosses;
let score = 0, coins = 0, lastTime = 0;
let tripleShots = 0, freezeActive = false, megaBlast = 0;

// Upgrades structure (saved)
let upgrades = {
  speed: { level:1, max:5, costs:[100,150,250,400,600], values:[1,1.15,1.3,1.45,1.65] },
  damage:{ level:1, max:5, costs:[120,170,260,420,650], values:[12,15,18,22,28] },
  firerate:{ level:1, max:5, costs:[80,130,200,320,500], values:[0.22,0.18,0.14,0.10,0.07] },
  health:{ level:1, max:5, costs:[100,150,250,380,600], values:[100,130,160,200,250] },
  shield:{ level:1, max:5, costs:[90,140,200,300,450], values:[50,70,90,120,150] },
  fuel:{ level:1, max:5, costs:[60,110,180,260,400], values:[1,0.9,0.78,0.65,0.55] }
};

// Shop definitions
let shopItems = [
  { name: "Fuel Cell", cost: 30, category:"Resources", description: "Refuels +20" },
  { name: "Shield Core", cost: 60, category:"Upgrades", description: "Permanent +20 shield" },
  { name: "Triple Shot Module", cost: 120, category:"Weapons", description: "Unlock triple-shot" },
  { name: "Mega Blast", cost: 200, category:"Weapons", description: "Unlock mega-blast" },
  { name: "Hull Upgrade", cost: 80, category:"Upgrades", description: "+25 Max HP" }
];

// Black market and rare shop
let blackMarket = {
  name: "Shadow Exchange",
  items: [
    {name:"Illegal Plasma Core", cost:350, category:"Upgrades", desc:"+50 Max HP"},
    {name:"Prototype Railgun", cost:600, category:"Weapons", desc:"High damage"},
    {name:"Cloak Device", cost:500, category:"Upgrades", desc:"Temporary stealth"}
  ]
};

let rareShop = {
  items:[
    {name:"Quantum Reactor", cost:900, category:"Upgrades", desc:"Massive power boost"},
    {name:"Dark Matter Shells", cost:700, category:"Weapons", desc:"Bullet damage x3"},
    {name:"Warp Lens", cost:1000, category:"Upgrades", desc:"Faster map travel"}
  ],
  active:[]
};
function rollRareShop(){ rareShop.active = []; for(let i=0;i<2;i++) rareShop.active.push(rareShop.items[Math.floor(Math.random()*rareShop.items.length)]); }
rollRareShop();

// Stations
let stations = [{ x: 600, y: 400, r: 88, name: "Alpha Station", shop: shopItems }];
let docking = false, dockProgress = 0, insideStation = false;
let stationBackground = new Image(); stationBackground.src = "station_bg.png"; // optional

// Game data (for save/load)
let gameData = {
  coins: 0,
  inventory: [],
  shipState: {},
  upgrades: upgrades,
  planets: [],
  missions: []
};

// Audio
let audioCtx = null;
function initAudio(){
  if(audioCtx) return;
  audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  const osc = audioCtx.createOscillator(); const g = audioCtx.createGain();
  osc.type='sine'; osc.frequency.value=48; g.gain.value=0.015; osc.connect(g); g.connect(audioCtx.destination); osc.start();
}
function playLaser(){ if(!audioCtx) return; const o=audioCtx.createOscillator(), g=audioCtx.createGain(); o.type='square'; o.frequency.value=900+Math.random()*120; g.gain.value=0.06; o.connect(g); g.connect(audioCtx.destination); o.start(); g.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime+0.12); setTimeout(()=>o.stop(),160); }
function playExplode(){ if(!audioCtx) return; const len=audioCtx.sampleRate*0.22; const buf=audioCtx.createBuffer(1,len,audioCtx.sampleRate); const d=buf.getChannelData(0); for(let i=0;i<len;i++) d[i]=(Math.random()*2-1)*Math.exp(-3*i/len); const s=audioCtx.createBufferSource(); s.buffer=buf; const g=audioCtx.createGain(); g.gain.value=0.22; s.connect(g); g.connect(audioCtx.destination); s.start(); }
function playPickup(){ if(!audioCtx) return; const o=audioCtx.createOscillator(), g=audioCtx.createGain(); o.type='sine'; o.frequency.value=640; g.gain.value=0.06; o.connect(g); g.connect(audioCtx.destination); o.start(); g.gain.exponentialRampToValueAtTime(0.0001,audioCtx.currentTime+0.22); setTimeout(()=>o.stop(),260); }

// =============== Init / Reset =================
function resetGame(){
  ship = { x: W/2, y: H/2, vx:0, vy:0, angle:-Math.PI/2, r:14, health:100, fuel:100, shield:0, triple:false, mega:false, dashCooldown:0 };
  stars = []; planets = []; enemies = []; bullets = []; explosions = []; items = []; bosses = [];
  score = 0; coins = 0; tripleShots = 0; freezeActive = false; megaBlast = 0;
  for(let i=0;i<20;i++) stars.push({ x: Math.random()*W, y: Math.random()*H, r: 4 + Math.random()*4, picked:false });
  const planetNames = ['Aqualon','Pyronox','Verdita','Kestros','Lumina','Obsidia','Ravine','Zeta'];
  for(let i=0;i<6;i++) planets.push({ x: 100 + Math.random()*(W-200), y: 80 + Math.random()*(H-160), r: 28 + Math.random()*48, type: Math.random()<0.7?'friendly':'hostile', name: planetNames[i]||'Planet'+i });
  for(let i=0;i<4;i++) spawnEnemy();
  for(let i=0;i<2;i++) items.push({ x: 40 + Math.random()*(W-80), y: 40 + Math.random()*(H-80), type: (Math.random()<0.6?'fuel':'shield'), r:12, taken:false });
  applyUpgrades();
  updateUI();
}

// -- spawn enemy / boss
function spawnEnemy(){
  const side = Math.random();
  const x = side < 0.5 ? (Math.random()<0.5? -40 : W+40) : Math.random()*W;
  const y = side >= 0.5 ? (Math.random()<0.5? -40 : H+40) : Math.random()*H;
  enemies.push({ x,y, vx:0, vy:0, r:12 + Math.random()*8, hp: 60 + Math.random()*40, speed: 30 + Math.random()*50, lastShot:0, frozen:0, boss:false });
}
function spawnBoss(){
  bosses.push({ x: W/2, y: -120, vx:0, vy:50, r:60, hp:1000, lastShot:0, phase:0, boss:true });
}

// =============== Upgrades apply
function applyUpgrades(){
  let u = upgrades;
  for(const k in u) { if(u[k].level < 1) u[k].level = 1; if(u[k].level > u[k].max) u[k].level = u[k].max; }
  thrustMultiplier = u.speed.values[u.speed.level-1];
  playerDamage = u.damage.values[u.damage.level-1];
  fireCooldown = u.firerate.values[u.firerate.level-1];
  maxHealth = u.health.values[u.health.level-1];
  maxShield = u.shield.values[u.shield.level-1];
  fuelDrainMultiplier = u.fuel.values[u.fuel.level-1];
  ship.health = Math.min(ship.health || maxHealth, maxHealth);
  ship.shield = Math.min(ship.shield || maxShield, maxShield);
  document.getElementById('upgradesCount').textContent = Object.values(upgrades).reduce((a,b)=>a+b.level,0);
}

// dynamic values
let thrustMultiplier = 1, playerDamage = 12, fireCooldown = 0.22, lastFireTime = 0;
let maxHealth = 100, maxShield = 50, fuelDrainMultiplier = 1;

// =============== Physics / Game Loop
function physics(dt){
  if(freezeActive) dt *= 0.5;
  if(keys['arrowleft']) ship.angle -= 3.5 * dt;
  if(keys['arrowright']) ship.angle += 3.5 * dt;
  if(keys['z'] && ship.fuel > 0){
    const thrust = 160;
    ship.vx += Math.cos(ship.angle) * thrust * dt * thrustMultiplier;
    ship.vy += Math.sin(ship.angle) * thrust * dt * thrustMultiplier;
    ship.fuel = Math.max(0, ship.fuel - 14 * dt * fuelDrainMultiplier);
  } else {
    ship.vx *= 0.999; ship.vy *= 0.999;
  }
  if(keys['c'] && ship.fuel > 10 && ship.dashCooldown <= 0){
    ship.vx += Math.cos(ship.angle) * 260;
    ship.vy += Math.sin(ship.angle) * 260;
    ship.fuel -= 6;
    ship.dashCooldown = 1.2;
  }
  ship.dashCooldown = Math.max(0, (ship.dashCooldown || 0) - dt);

  ship.x += ship.vx * dt; ship.y += ship.vy * dt;
  if(ship.x < -40) ship.x = W + 40;
  if(ship.x > W + 40) ship.x = -40;
  if(ship.y < -40) ship.y = H + 40;
  if(ship.y > H + 40) ship.y = -40;

  // collect stars
  for(const s of stars){
    if(s.picked) continue;
    const d = Math.hypot(s.x - ship.x, s.y - ship.y);
    if(d < ship.r + s.r + 6){
      s.picked = true; score += 10; coins += 5;
      explosions.push({ x: s.x, y: s.y, t:0, r: s.r * 6 });
      if(Math.random() < 0.2) items.push({ x: s.x+Math.random()*20-10, y: s.y+Math.random()*20-10, type: 'triple', r:12 });
    }
  }

  // items pickup
  for(let i=items.length-1;i>=0;i--){
    const it=items[i];
    const d = Math.hypot(it.x - ship.x, it.y - ship.y);
    if(d < ship.r + (it.r||12)){
      playPickup(); applyPower(it.type || 'fuel'); items.splice(i,1);
    }
  }

  // bullets move
  for(let i=bullets.length-1;i>=0;i--){
    const b = bullets[i];
    b.x += b.vx * dt; b.y += b.vy * dt; b.life -= dt;
    if(b.life <= 0 || b.x < -120 || b.x > W+120 || b.y < -120 || b.y > H+120) bullets.splice(i,1);
  }

  // enemies AI
  for(let ei = enemies.length-1; ei >= 0; ei--){
    const e = enemies[ei];
    if(e.frozen && e.frozen > 0) { e.frozen = Math.max(0, e.frozen - dt); continue; }
    const dx = ship.x - e.x, dy = ship.y - e.y;
    const dist = Math.hypot(dx,dy) || 1;
    const ax = dx / dist, ay = dy / dist;
    e.vx += ax * e.speed * dt * (dist > 120 ? 1 : -0.6);
    e.vy += ay * e.speed * dt * (dist > 120 ? 1 : -0.6);
    const vmag = Math.hypot(e.vx, e.vy);
    if(vmag > e.speed) { e.vx = e.vx/vmag * e.speed; e.vy = e.vy/vmag * e.speed; }
    e.x += e.vx * dt; e.y += e.vy * dt;

    e.lastShot = (e.lastShot || 0) + dt;
    if(e.lastShot > 1.0 && dist < 380){
      e.lastShot = 0;
      const spd = 220;
      bullets.push({ x:e.x, y:e.y, vx:(dx/dist)*spd, vy:(dy/dist)*spd, owner:'enemy', life:6 });
    }

    if(dist < e.r + ship.r){
      const dmg = 18 * dt;
      if(ship.shield > 0) ship.shield = Math.max(0, ship.shield - dmg);
      else ship.health -= dmg;
      e.vx *= -0.5; e.vy *= -0.5;
    }
  }

  // bosses behavior
  for(const b of bosses){
    b.phase += dt;
    b.x = W/2 + Math.cos(b.phase*0.5) * 220;
    b.y = Math.min(b.y + b.vy*dt, 120 + Math.sin(b.phase)*10);
    b.lastShot = (b.lastShot || 0) + dt;
    if(b.lastShot > 0.6){
      b.lastShot = 0;
      const pieces = 12;
      for(let a=0;a<pieces;a++){
        const ang = a*(Math.PI*2/pieces) + Math.random()*0.06;
        const spd = 180;
        bullets.push({ x: b.x + Math.cos(ang)*b.r, y: b.y + Math.sin(ang)*b.r, vx: Math.cos(ang)*spd, vy: Math.sin(ang)*spd, owner:'enemy', life:4 });
      }
    }
  }

  // bullets collisions handled later
  handleCollisions();

  // explosions
  for(let i=explosions.length-1;i>=0;i--){
    const ex = explosions[i];
    ex.t += dt;
    if(ex.t > 0.8) explosions.splice(i,1);
  }

  // fuel drain
  ship.fuel = Math.max(0, ship.fuel - 1.2 * dt);

  // docking
  updateStationDocking(dt);

  // pickup spawn
  if(Math.random() < 0.006) items.push({ x:40+Math.random()*(W-80), y:40+Math.random()*(H-80), type: (Math.random()<0.6 ? 'fuel' : 'shield'), r:12 });

  if(ship.health <= 0){ running = false; setTimeout(()=>alert('Game Over — refresh to play again'),50); }

  updateUI();
}

function handleCollisions(){
  for(let i=bullets.length-1;i>=0;i--){
    const b = bullets[i];
    if(b.owner === 'player'){
      for(let j=enemies.length-1;j>=0;j--){
        const e = enemies[j];
        const d = Math.hypot(b.x - e.x, b.y - e.y);
        if(d < e.r + 6){
          e.hp -= (b.dmg || playerDamage);
          bullets.splice(i,1); explosions.push({ x:e.x, y:e.y, t:0, r:e.r*6 });
          if(e.hp <= 0){
            score += 40; coins += 20; enemies.splice(j,1);
            if(Math.random() < 0.12) items.push({ x:e.x, y:e.y, type:'triple', r:12 });
            if(Math.random() < 0.08) spawnBoss();
          }
          break;
        }
      }
    } else {
      const d = Math.hypot(b.x - ship.x, b.y - ship.y);
      if(d < ship.r + 4){
        if(ship.shield > 0) ship.shield = Math.max(0, ship.shield - 12);
        else ship.health -= 12;
        bullets.splice(i,1); explosions.push({ x:ship.x + (Math.random()*20-10), y:ship.y + (Math.random()*20-10), t:0, r:18 });
      }
    }
  }
}

// apply powerups
function applyPower(type){
  if(type === 'triple'){ tripleShots = Math.min(3, tripleShots + 2); }
  if(type === 'freeze'){ freezeActive = true; setTimeout(()=>freezeActive=false, 7000); for(let e of enemies) e.frozen = 2; }
  if(type === 'mega'){ megaBlast = Math.min(3, megaBlast + 1); }
  if(type === 'fuel'){ ship.fuel = Math.min(100, ship.fuel + 30); }
  if(type === 'shield'){ ship.shield = Math.min(maxShield, ship.shield + 20); }
}

// fire
function firePlayer(){
  if(!running) return;
  const now = performance.now() / 1000;
  if(now - lastFireTime < fireCooldown) return;
  lastFireTime = now;

  const spd = 520;
  if(tripleShots > 0){
    const angles = [0, 0.14, -0.14];
    angles.forEach(a => {
      bullets.push({ x: ship.x + Math.cos(ship.angle + a)*ship.r, y: ship.y + Math.sin(ship.angle + a)*ship.r,
        vx: Math.cos(ship.angle + a) * spd + ship.vx*0.2, vy: Math.sin(ship.angle + a) * spd + ship.vy*0.2,
        owner:'player', life:1.2, dmg: playerDamage });
    });
    tripleShots = Math.max(0, tripleShots - 1);
  } else {
    bullets.push({ x: ship.x + Math.cos(ship.angle)*ship.r, y: ship.y + Math.sin(ship.angle)*ship.r,
      vx: Math.cos(ship.angle) * spd + ship.vx*0.2, vy: Math.sin(ship.angle) * spd + ship.vy*0.2,
      owner:'player', life:1.2, dmg: playerDamage });
  }

  if(megaBlast > 0){
    for(let i=enemies.length-1;i>=0;i--){
      const e = enemies[i];
      const d = Math.hypot(e.x - ship.x, e.y - ship.y);
      if(d < 220){
        e.hp -= (megaBlast * 90);
        if(e.hp <= 0){
          score += 40; coins += 20; enemies.splice(i,1);
        }
      }
    }
    megaBlast = Math.max(0, megaBlast - 1);
  }

  playLaser();
}

// ==================== Render
function render(){
  // background
  ctx.fillStyle = '#000012'; ctx.fillRect(0,0,W,H);

  // parallax stars
  for(let i=0;i<90;i++){
    const sx = (i*71) % W, sy = (i*131) % H;
    ctx.fillStyle = 'rgba(255,255,255,' + (0.02 + ((i%7)/20)) + ')';
    ctx.fillRect((sx + ship.vx*0.01) % W, (sy + ship.vy*0.01) % H, 2, 2);
  }

  // planets
  planets.forEach(p => {
    const grd = ctx.createRadialGradient(p.x - p.r*0.2, p.y - p.r*0.2, p.r*0.2, p.x, p.y, p.r*1.2);
    grd.addColorStop(0, p.type === 'friendly' ? '#2ea6c4' : '#7a2b3a');
    grd.addColorStop(1, '#000012');
    ctx.beginPath(); ctx.fillStyle = grd; ctx.arc(p.x, p.y, p.r, 0, Math.PI*2); ctx.fill();
    ctx.strokeStyle = 'rgba(255,255,255,0.03)'; ctx.lineWidth = 2; ctx.stroke();
    ctx.font = '12px Inter,Arial'; ctx.fillStyle = 'rgba(255,255,255,0.85)'; ctx.fillText(p.name, p.x - p.r + 6, p.y - p.r - 6);
  });

  // items
  items.forEach(it => {
    ctx.beginPath(); ctx.fillStyle = (it.type==='fuel' ? '#9be7ff' : (it.type==='triple' ? '#ffd27a' : '#ffd28a')); ctx.arc(it.x, it.y, it.r||8, 0, Math.PI*2); ctx.fill();
  });

  // stars
  stars.forEach(s => { if(!s.picked){ ctx.beginPath(); ctx.fillStyle='#fff9c9'; ctx.arc(s.x,s.y,s.r,0,Math.PI*2); ctx.fill(); } });

  // bullets
  bullets.forEach(b => { ctx.beginPath(); ctx.fillStyle = b.owner==='player' ? '#a9f0ff' : '#ffa3a3'; ctx.arc(b.x,b.y,3,0,Math.PI*2); ctx.fill(); });

  // enemies
  enemies.forEach(e => {
    ctx.save(); ctx.translate(e.x,e.y); ctx.rotate(Math.atan2((ship.y - e.y),(ship.x - e.x)));
    ctx.fillStyle = '#ff9b9b'; ctx.beginPath(); ctx.moveTo(0,-e.r); ctx.lineTo(e.r*0.7,e.r); ctx.lineTo(-e.r*0.7,e.r); ctx.closePath(); ctx.fill();
    ctx.fillStyle = '#000'; ctx.fillRect(-e.r, -e.r-8, e.r*2, 5);
    ctx.fillStyle = '#76ff92'; let hpW = Math.max(0, (e.hp/100) * e.r*2); ctx.fillRect(-e.r, -e.r-8, hpW, 5);
    ctx.restore();
  });

  // bosses
  bosses.forEach(b => {
    ctx.save(); ctx.translate(b.x,b.y);
    ctx.fillStyle = '#ff7aef'; ctx.beginPath(); ctx.arc(0,0,b.r,0,Math.PI*2); ctx.fill();
    ctx.fillStyle = '#000'; ctx.fillRect(-b.r, -b.r-12, b.r*2, 8);
    ctx.fillStyle = '#ff6b6b'; ctx.fillRect(-b.r, -b.r-12, Math.max(0,(b.hp/1000)*b.r*2), 8);
    ctx.restore();
  });

  // ship
  ctx.save(); ctx.translate(ship.x, ship.y); ctx.rotate(ship.angle);
  ctx.beginPath(); ctx.arc(0,0, ship.r+6, 0, Math.PI*2); ctx.fillStyle = 'rgba(80,200,255,0.035)'; ctx.fill();
  ctx.beginPath(); ctx.moveTo(18,0); ctx.lineTo(-12,10); ctx.lineTo(-6,0); ctx.lineTo(-12,-10); ctx.closePath(); ctx.fillStyle = '#cfe9ff'; ctx.fill();
  ctx.strokeStyle = '#38b6ff'; ctx.lineWidth=1; ctx.stroke();
  if(keys['z'] && ship.fuel > 0){ ctx.beginPath(); ctx.moveTo(-8,-7); ctx.lineTo(-26,0); ctx.lineTo(-8,7); ctx.closePath(); ctx.fillStyle='orange'; ctx.fill(); }
  ctx.restore();

  // explosions
  explosions.forEach(ex => {
    const p = ex.t / 0.8; const radius = ex.r * (0.2 + p);
    ctx.beginPath(); ctx.arc(ex.x, ex.y, radius, 0, Math.PI*2); ctx.fillStyle = 'rgba(255,160,80,' + (0.9 - p) + ')'; ctx.fill();
  });

  // stations
  stations.forEach(s => {
    ctx.strokeStyle = 'cyan'; ctx.beginPath(); ctx.arc(s.x, s.y, s.r, 0, Math.PI*2); ctx.stroke();
    ctx.fillStyle = 'white'; ctx.font = '12px Inter,Arial'; ctx.fillText(s.name, s.x - 30, s.y - s.r - 6);
  });

  // docking bar
  if(docking){
    ctx.fillStyle='rgba(0,255,255,0.25)'; ctx.fillRect(0,H-28, W * (dockProgress||0), 28);
    ctx.fillStyle='white'; ctx.font='14px Inter,Arial'; ctx.fillText('Docking...', 10, H-8);
  }

  // minimap
  mmCtx.fillStyle='rgba(0,0,4,0.6)'; mmCtx.fillRect(0,0,mm.width,mm.height);
  const scaleX = mm.width / W, scaleY = mm.height / H;
  planets.forEach(p => { mmCtx.fillStyle = p.type==='friendly' ? '#2ee0ff' : '#ff8a8a'; mmCtx.beginPath(); mmCtx.arc(p.x*scaleX, p.y*scaleY, Math.max(2, p.r*scaleX*0.16), 0, Math.PI*2); mmCtx.fill(); });
  enemies.forEach(e => { mmCtx.fillStyle = '#ffb3b3'; mmCtx.fillRect(e.x*scaleX-2, e.y*scaleY-2, 4,4); });
  bosses.forEach(b => { mmCtx.fillStyle = '#ff3333'; mmCtx.fillRect(b.x*scaleX-4, b.y*scaleY-4, 8,8); });
  mmCtx.fillStyle = '#9ef'; mmCtx.beginPath(); mmCtx.arc(ship.x*scaleX, ship.y*scaleY, 3, 0, Math.PI*2); mmCtx.fill();
}

// =============== Station Docking (requires proximity + 's' press)
let shopOpen = false;
function updateStationDocking(dt){
  if(insideStation) return;
  for(const s of stations){
    const d = Math.hypot(ship.x - s.x, ship.y - s.y);
    const near = d < s.r + 40;
    if(near && keys['s'] && !shopOpen){
      // begin docking sequence
      docking = true; dockProgress = 0; shopOpen = true;
      break;
    }
  }
  if(docking){
    dockProgress = Math.min(1, (dockProgress || 0) + dt * 0.8);
    // landing animation fade-in
    document.getElementById('fade').style.opacity = (dockProgress * 0.9).toString();
    if(dockProgress >= 1){
      docking = false; dockProgress = 0; document.getElementById('fade').style.opacity = '0.95';
      // landing animation completed, open station interior after slight delay
      setTimeout(()=>{ openStation(); document.getElementById('fade').style.opacity = '0'; }, 500);
    }
  }
}

// open station interior UI (landing animation plays before)
function openStation(){
  insideStation = true;
  document.getElementById('stationName').innerText = stations[0].name;
  populateStationUI(stations[0]);
  document.getElementById('stationUI').classList.remove('hidden');
  document.getElementById('stationUI').setAttribute('aria-hidden','false');
  // ensure shop hidden
  document.getElementById('shopUI').classList.add('hidden');
  document.getElementById('shopUI').setAttribute('aria-hidden','true');
  // animate scale a little for the interior (CSS transition handles smoothness)
  canvas.classList.add('scaleZoom');
  canvas.style.transform = 'scale(0.92)';
  setTimeout(()=>{ canvas.style.transform = ''; canvas.classList.remove('scaleZoom'); }, 450);
}

function leaveStation(){
  insideStation = false;
  document.getElementById('stationUI').classList.add('hidden');
  document.getElementById('stationUI').setAttribute('aria-hidden','true');
}

// populate station UI with tabs and items
function populateStationUI(st){
  const content = document.getElementById('stationContent');
  const tabButtons = document.querySelectorAll('#stationUI .tabbar button');
  tabButtons.forEach(btn => {
    btn.onclick = () => {
      // highlight and show category content
      tabButtons.forEach(b=>b.style.outline='none');
      btn.style.outline = '2px solid rgba(98,218,251,0.25)';
      showStationCategory(btn.dataset.tab, st);
    };
  });
  // default to Weapons
  tabButtons[0].click();
}

function showStationCategory(cat, st){
  const content = document.getElementById('stationContent');
  content.innerHTML = '';
  if(cat === 'BlackMarket'){
    content.innerHTML = '<h4>Black Market</h4>';
    blackMarket.items.forEach(it=>{
      const el = document.createElement('div'); el.style.padding='6px 0'; el.innerHTML = `<strong>${it.name}</strong> - ${it.cost} <div style="font-size:12px;opacity:0.85">${it.desc}</div><button style="margin-top:6px">Buy</button>`;
      el.querySelector('button').onclick = ()=>{ buyStationItem(it); };
      content.appendChild(el);
    });
    return;
  }
  // list station shop items with category filtering
  const list = st.shop || shopItems;
  list.filter(it=>it.category === cat).forEach(it=>{
    const el = document.createElement('div'); el.style.padding='6px 0';
    el.innerHTML = `<strong>${it.name}</strong> - ${it.cost} <div style="font-size:12px;opacity:0.85">${it.description}</div><button style="margin-top:6px">Buy</button>`;
    el.querySelector('button').onclick = ()=>{ buyStationItem(it); };
    content.appendChild(el);
  });
  // rare items when on Upgrades tab
  if(cat === 'Upgrades'){
    const hr = document.createElement('div'); hr.style.marginTop='8px'; hr.innerHTML = '<strong>Rare Offers</strong>'; content.appendChild(hr);
    rareShop.active.forEach(it=>{
      const el = document.createElement('div'); el.style.padding='6px 0'; el.innerHTML = `<em>${it.name}</em> - ${it.cost} <div style="font-size:12px;opacity:0.85">${it.desc}</div><button style="margin-top:6px">Buy</button>`; el.querySelector('button').onclick = ()=>{ buyStationItem(it); }; content.appendChild(el);
    });
  }
}

function buyStationItem(item){
  if(coins < item.cost){ alert('Not enough coins'); return; }
  coins -= item.cost; gameData.inventory.push(item.name);
  applyItemEffect(item.name); updateUI(); refreshInventory(); alert('Purchased '+item.name);
}
function applyItemEffect(name){
  if(name === 'Fuel Cell') ship.fuel = Math.min(100, ship.fuel + 30);
  if(name === 'Shield Core') ship.shield = Math.min(maxShield, ship.shield + 20);
  if(name === 'Hull Upgrade') { ship.health = Math.min(maxHealth + 25, ship.health + 25); maxHealth += 25; }
  if(name === 'Triple Shot Module') tripleShots = Math.max(tripleShots, 3);
  if(name === 'Mega Blast') megaBlast = Math.max(megaBlast, 1);
  if(name === 'Illegal Plasma Core'){ ship.health += 50; }
  if(name === 'Prototype Railgun'){ playerDamage += 20; }
}

// ==================== Shop UI functions ====================
function toggleShop(){
  const s = document.getElementById('shopUI');
  if(insideStation){ openStation(); return; }
  if(!s.classList.contains('hidden')) { s.classList.add('hidden'); s.setAttribute('aria-hidden','true'); }
  else { refreshShop(); s.classList.remove('hidden'); s.setAttribute('aria-hidden','false'); }
}
function refreshShop(){
  document.getElementById('shopCoins').innerText = coins;
  const list = document.getElementById('shopList'); list.innerHTML = '';
  shopItems.forEach((it, idx) => {
    const div = document.createElement('div'); div.style.borderBottom='1px solid #222'; div.style.padding='8px 0';
    div.innerHTML = `<strong>${it.name}</strong> - ${it.cost} <div style="font-size:12px;opacity:0.85">${it.description}</div><button style="margin-top:6px">Buy</button>`;
    div.querySelector('button').onclick = ()=>{ buyShopItem(idx); };
    list.appendChild(div);
  });
  // black market and rare display
  const bm = document.createElement('div'); bm.style.marginTop='6px'; bm.innerHTML = '<strong>Black Market</strong>'; list.appendChild(bm);
  blackMarket.items.forEach(it=>{ const el=document.createElement('div'); el.style.padding='6px 0'; el.innerHTML=`<em>${it.name}</em> - ${it.cost} <button>Buy</button>`; el.querySelector('button').onclick=()=>{ if(coins<it.cost){alert('no coins');return;} coins-=it.cost; gameData.inventory.push(it.name); applyItemEffect(it.name); updateUI(); refreshInventory(); alert('bought '+it.name); }; list.appendChild(el); });
  const rareHeader = document.createElement('div'); rareHeader.style.marginTop='6px'; rareHeader.innerHTML = '<strong>Rare Today</strong>'; list.appendChild(rareHeader);
  rareShop.active.forEach(it=>{ const el=document.createElement('div'); el.style.padding='6px 0'; el.innerHTML=`<em>${it.name}</em> - ${it.cost} <button>Buy</button>`; el.querySelector('button').onclick=()=>{ if(coins<it.cost){alert('no coins');return;} coins-=it.cost; gameData.inventory.push(it.name); applyItemEffect(it.name); updateUI(); refreshInventory(); alert('bought '+it.name); }; list.appendChild(el); });
}
function buyShopItem(idx){
  const it = shopItems[idx];
  if(coins < it.cost){ alert('Not enough coins'); return; }
  coins -= it.cost; gameData.inventory.push(it.name);
  applyItemEffect(it.name); updateUI(); refreshInventory(); alert('Purchased '+it.name);
}

// ==================== Inventory UI
function toggleInventory(){
  const inv = document.getElementById('inventoryUI');
  if(inv.classList.contains('hidden')) { inv.classList.remove('hidden'); inv.setAttribute('aria-hidden','false'); refreshInventory(); }
  else { inv.classList.add('hidden'); inv.setAttribute('aria-hidden','true'); }
}
function refreshInventory(){
  const box = document.getElementById('inventoryList'); box.innerHTML = '';
  if(!gameData.inventory || gameData.inventory.length===0){ box.innerHTML = '<i>No items</i>'; return; }
  gameData.inventory.forEach((it, i) => { const d = document.createElement('div'); d.style.padding='6px 0'; d.textContent = it; box.appendChild(d); });
}

// ==================== Save / Load
function saveGame(){
  const payload = {
    coins: coins,
    inventory: gameData.inventory,
    shipState: { x: ship.x, y: ship.y, health: ship.health, fuel: ship.fuel, shield: ship.shield },
    upgrades: upgrades,
    planets: planets,
    missions: []
  };
  fetch('/save', { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload) })
    .then(r => r.json()).then(j => { alert('Saved'); });
}
function loadGame(){
  fetch('/load').then(r => r.json()).then(data => {
    if(!data || !data.shipState){ alert('No save found'); return; }
    coins = data.coins || 0;
    gameData.inventory = data.inventory || [];
    const s = data.shipState || {};
    ship.x = s.x || ship.x; ship.y = s.y || ship.y; ship.health = s.health || ship.health; ship.fuel = s.fuel || ship.fuel; ship.shield = s.shield || ship.shield;
    if(data.upgrades) upgrades = data.upgrades;
    if(data.planets) planets = data.planets;
    updateUI(); refreshInventory(); alert('Loaded');
  });
}

// Buttons wiring
document.getElementById('saveBtn').onclick = saveGame;
document.getElementById('loadBtn').onclick = loadGame;
document.getElementById('restartBtn').onclick = ()=>{ resetGame(); };
document.getElementById('shopBtn').onclick = toggleShop;
document.getElementById('invBtn').onclick = toggleInventory;
document.getElementById('mapBtn').onclick = ()=>{ alert('Galaxy panel - not fully implemented'); };
document.getElementById('closeShop').onclick = ()=>{ document.getElementById('shopUI').classList.add('hidden'); };
document.getElementById('closeInv').onclick = ()=>{ document.getElementById('inventoryUI').classList.add('hidden'); };
document.getElementById('leaveStation').onclick = ()=>{ leaveStation(); };

// Hotkeys
window.addEventListener('keydown', e => {
  keys[e.key.toLowerCase()] = true;
  if(e.key === 'p') paused = !paused;
  if(e.key === 'x') { firePlayer(); }
  if(e.key === 's' || e.key === 'S') { /* docking handled in updateStationDocking */ }
  if(e.key === 'i' || e.key === 'I') toggleInventory();
  if(e.key === 'g' || e.key === 'G') { alert('Galaxy panel (work-in-progress)'); }
});
window.addEventListener('keyup', e => { keys[e.key.toLowerCase()] = false; });

// dblclick teleport
canvas.addEventListener('dblclick', e => {
  const rect = canvas.getBoundingClientRect();
  ship.x = (e.clientX - rect.left) * (canvas.width / rect.width);
  ship.y = (e.clientY - rect.top) * (canvas.height / rect.height);
  ship.vx = ship.vy = 0;
});

// update UI
function updateUI(){
  document.getElementById('score').textContent = score;
  document.getElementById('coins').textContent = coins;
  document.getElementById('health').textContent = Math.max(0, Math.round(ship.health));
  document.getElementById('fuel').textContent = Math.round(ship.fuel);
  document.getElementById('enemies').textContent = enemies.length;
  document.getElementById('lasers').textContent = bullets.length;
  document.getElementById('shopCoins').textContent = coins;
  document.getElementById('upgradesCount').textContent = Object.values(upgrades).reduce((a,b)=>a+b.level,0);
  const collected = stars.filter(s=>s.picked).length;
  document.getElementById('missionText').textContent = `Collect 20 stars. (${collected}/20)`;
}

// main loop
function loop(ts){
  if(!running) { lastTime = ts; requestAnimationFrame(loop); return; }
  const dt = Math.min(0.05, (ts - lastTime)/1000);
  lastTime = ts;
  if(!paused) physics(dt);
  render();
  requestAnimationFrame(loop);
}

// start
document.getElementById('startBtn').onclick = () => {
  document.getElementById('startScreen').style.display = 'none';
  initAudio(); resetGame(); running = true; lastTime = performance.now(); requestAnimationFrame(loop);
};

// auto spawns and boss timer
setInterval(()=>{ if(running && Math.random() < 0.35) spawnEnemy(); }, 5000);
let bossTicker = 0;
setInterval(()=>{ if(running) { bossTicker++; if(bossTicker > 45 && Math.random() < 0.12){ spawnBoss(); bossTicker = 0; } } }, 1000);

// initialize
resetGame(); updateUI();

</script>
</body>
</html>
"""

# ---------------- HTTP Handler with save/load endpoints ----------------
class Handler(BaseHTTPRequestHandler):
    def _set_common_headers(self, code=200, ctype="text/html"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.end_headers()

    def do_GET(self):
        if self.path in ('/', '/index.html'):
            self._set_common_headers(200, "text/html; charset=utf-8")
            self.wfile.write(HTML.encode('utf-8'))
        elif self.path == '/load':
            try:
                with open(SAVE_FILE, 'r', encoding='utf-8') as f:
                    data = f.read()
            except Exception:
                data = "{}"
            self._set_common_headers(200, "application/json; charset=utf-8")
            self.wfile.write(data.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/save':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length).decode('utf-8') if length else ''
            try:
                parsed = json.loads(body) if body else {}
                with open(SAVE_FILE, 'w', encoding='utf-8') as f:
                    json.dump(parsed, f, ensure_ascii=False, indent=2)
                self._set_common_headers(200, "application/json; charset=utf-8")
                self.wfile.write(json.dumps({"status":"saved"}).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(str(e).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

# ---------------- Run server ----------------
def run():
    print(f"Serving Space Explorer on http://{HOST}:{PORT}")
    server = HTTPServer((HOST, PORT), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.server_close()

if __name__ == '__main__':
    run()
