puzzle_input = r'''&zq -> fd, gk, pp, ph, ss, dr, pl
%qg -> jh, nk
%lm -> lg, qm
%fk -> lr
%pp -> hh
%bf -> sj, qm
&qm -> kb, jl, bs, kx, bl, cz, dd
%db -> dc, jn
%kl -> dc, qv
%xm -> jh
%ss -> zq, nd
%vq -> bh, dc
%bl -> bs
%fd -> gk
&dc -> tx, vq, ct, df, fx
%dj -> zq, pp
%fv -> vj, zq
%pv -> lm, qm
%dg -> zz, jh
%fc -> fk
%qv -> dc, db
&ls -> rx
&tx -> ls
%vl -> fc
%dr -> fd
&dd -> ls
%kx -> jl
%sj -> qm, bl
%vj -> zq
%nk -> jh, vl
%xr -> kr, jh
&nz -> ls
%cz -> bf
%ms -> qm
%ct -> fx
%lg -> qm, ms
%lr -> dg
%pl -> dr
%rt -> zq, dj
%jn -> dc
%zz -> zm
%kf -> kl, dc
%jl -> cz
%hh -> fv, zq
%df -> mr
&jh -> zz, lr, vl, fc, nz, fk, qg
%fx -> hq
%hq -> df, dc
%kb -> qm, kx
&ph -> ls
broadcaster -> kb, vq, ss, qg
%nd -> pl, zq
%gk -> rt
%mr -> dc, kf
%bs -> pv
%bh -> dc, ct
%kr -> jh, xm
%zm -> xr, jh
'''

from enum import Enum
# Each component has this structure:
# [type inputs outputs state pulses]
PartType = Enum('PartType', ['BROADCASTER', 'FLIPFLOP', 'CONJUNCTION', 'UNTYPED'])

PartIndex = Enum('PartIndex', ['TYPE','INPUTS','OUTPUTS','STATE','PULSES'], start=0)

module = dict()

for line in puzzle_input.splitlines():
  parts = line.replace("-> ", "").replace(",","").split()
  name = parts[0]
  outputs = parts[1:]
  if( name[0] == '%' ):
    ctype = PartType.FLIPFLOP
    name = name[1:]
  elif( name[0] == '&' ):
    ctype = PartType.CONJUNCTION
    name = name[1:]
  else:
    ctype = PartType.BROADCASTER
  
  if name not in module:
    module[name] = [PartType.UNTYPED,[],[],0,[]]
  
  module[name][PartIndex.TYPE.value] = ctype
  module[name][PartIndex.OUTPUTS.value] = outputs
  
  for p in outputs:
    if p not in module:
      module[p] = [PartType.UNTYPED,[name],[],0,[]]
    else:
      module[p][PartIndex.INPUTS.value].append(name)

for p in module:
  print(p, module[p])