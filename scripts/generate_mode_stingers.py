"""Six new original non-licensed UI mode-entry stingers; 48kHz PCM WAV."""
from pathlib import Path
import numpy as np,wave,math
root=Path(__file__).resolve().parents[1]/'assets/sfx'
SR=48000
modes={
'classic':(220,330,494),
'pixel':(310,622,930),
'quote':(184,276,368),
'ability':(268,536,804),
'emoji':(440,660,880),
'map':(147,220,440),
}
for name,notes in modes.items():
 dur=.66;t=np.arange(int(SR*dur),dtype=np.float32)/SR
 sig=np.zeros(t.shape,dtype=np.float32)
 for n,f in enumerate(notes):
  offset=n*.085
  age=np.maximum(0,t-offset)
  env=(1-np.exp(-age*160))*np.exp(-age*(7+n*2))*(t>=offset)
  sweep=f*(1+(0.16 if n%2 else -.09)*np.exp(-age*9))
  phase=2*np.pi*(f*age+(f*0.12)*(1-np.exp(-age*11))/11)
  wave1=np.sin(phase)+.24*np.sin(phase*2)+.12*np.sin(phase*3)
  sig+=env*wave1*(.32/(n+1))
 # soft tape-ish low rumble and tone
 sig+=.03*np.sin(2*np.pi*64*t)*np.exp(-t*8)
 sig*=np.minimum(1.0,(dur-t)*28)
 peak=max(1e-9,float(np.max(abs(sig))))
 data=np.clip(sig/peak*.43,-.95,.95)
 out=(data*32767).astype('<i2')
 with wave.open(str(root/f'enter-{name}.wav'),'wb') as w:
  w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes(out.tobytes())
print('Authored six original mode-entry WAV stingers.')
