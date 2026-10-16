/** Candycore holographic UI audio. No game recordings are bundled. */
let context=null;
let activeVoices=[];
let lastPlayed=0;
const presets={
  nav:{notes:[280,420],duration:0.13,type:'triangle',sweep:1.19,noise:0.012},
  pick:{notes:[560,760],duration:0.17,type:'sine',sweep:1.08,noise:0.016},
  clue:{notes:[330,505,760],duration:0.30,type:'triangle',sweep:1.08,noise:0.018},
  wrong:{notes:[265,210],duration:0.26,type:'triangle',sweep:0.74,noise:0.014},
  correct:{notes:[420,620,860],duration:0.31,type:'sine',sweep:1.11,noise:0.022},
  win:{notes:[392,523,659,932],duration:0.56,type:'triangle',sweep:1.04,noise:0.024},
  lose:{notes:[300,216,164],duration:0.42,type:'triangle',sweep:0.72,noise:0.012},
  reveal:{notes:[330,440,554,659,880,1108],duration:0.31,type:'sine',sweep:1.06,noise:0.020},
  'hover-classic':{notes:[220,330],duration:0.095,type:'triangle',sweep:1.3,noise:0.006},
  'hover-pixel':{notes:[310,465],duration:0.095,type:'square',sweep:1.65,noise:0.005},
  'hover-quote':{notes:[525,410],duration:0.10,type:'sine',sweep:.87,noise:0.006},
  'hover-ability':{notes:[350,700],duration:0.09,type:'triangle',sweep:1.18,noise:0.006},
  'hover-emoji':{notes:[680,760],duration:0.08,type:'sine',sweep:1.17,noise:0.004},
  'hover-map':{notes:[270,340],duration:0.12,type:'sawtooth',sweep:1.03,noise:0.004},
};
function burst(context,destination,start=0,length=0.02,level=0.01,cutoff=1400){
  const buffer=context.createBuffer(1,Math.max(1,Math.floor(context.sampleRate*length)),context.sampleRate);
  const data=buffer.getChannelData(0);
  for(let i=0;i<data.length;i++){data[i]=(Math.random()*2-1)*(1-i/data.length);}
  const source=context.createBufferSource();source.buffer=buffer;
  const filter=context.createBiquadFilter();filter.type='lowpass';filter.frequency.value=cutoff;
  const gain=context.createGain();gain.gain.setValueAtTime(level,start);gain.gain.exponentialRampToValueAtTime(0.0001,start+length);
  source.connect(filter);filter.connect(gain);gain.connect(destination);source.start(start);source.stop(start+length+0.01);
}
export function playSound(name,enabled=true){
  if(!enabled)return;
  try{
    const AudioContextImpl=globalThis.AudioContext||globalThis.webkitAudioContext;
    if(!AudioContextImpl)return;
    context??=new AudioContextImpl();
    if(context.state==='suspended')void context.resume();
    const now=context.currentTime;
    if(now-lastPlayed<0.06 && name==='nav')return;
    lastPlayed=now;
    const preset=presets[name]||presets.nav;
    const master=context.createGain();
    master.gain.value=name.startsWith('hover-')?0.065:name==='reveal'?0.22:0.23;
    const lowpass=context.createBiquadFilter();lowpass.type='lowpass';lowpass.frequency.value=name==='wrong'?1050:2400;
    const highpass=context.createBiquadFilter();highpass.type='highpass';highpass.frequency.value=120;
    master.connect(lowpass);lowpass.connect(highpass);highpass.connect(context.destination);
    const voices=[];
    burst(context,master,now+0.005,0.016,preset.noise||0.012,name==='wrong'?900:1500);
    preset.notes.forEach((pitch,index)=>{
      const oscillator=context.createOscillator();oscillator.type=preset.type;
      const amp=context.createGain();
      const begin=now+index*(name==='reveal'?0.11:name==='win'?0.065:0.028);
      const end=begin+preset.duration;
      oscillator.frequency.setValueAtTime(pitch,begin);
      oscillator.frequency.exponentialRampToValueAtTime(pitch*preset.sweep,end);
      amp.gain.setValueAtTime(0.0001,begin);
      amp.gain.exponentialRampToValueAtTime(Math.max(0.03,0.17/(index+1)),begin+0.02);
      amp.gain.exponentialRampToValueAtTime(0.0001,end);
      oscillator.connect(amp);amp.connect(master);
      oscillator.start(begin);oscillator.stop(end+0.01);
      voices.push(oscillator);
    });
    activeVoices.push(...voices);if(activeVoices.length>50)activeVoices=activeVoices.slice(-20);
  }catch{/* Sound is optional; the game always continues. */}
}
