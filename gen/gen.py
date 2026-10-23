import json,re,sys
sys.path.insert(0,'.');from additives_meta import M,GROUP,NOT;import micro
def parse(lines):
    root={'name':'root','children':[]};st=[(-1,root)]
    for l in lines:
        if not l.strip():continue
        d=len(l)-len(l.lstrip(' '));t=l.strip()
        while st[-1][0]>=d: st.pop()
        p=st[-1][1]
        if '|' in t:
            f=(t.split('|')+['','',''])[:4];p['children'].append({'name':f[0],'what':f[1],'does':f[2],'found':f[3]})
        else:
            n={'name':t,'children':[]};p['children'].append(n);st.append((d,n))
    return root
base=parse(open('base_tree.txt').read().splitlines())
F=dict(l.rstrip('\n').split('=',1) for l in open('base_found.txt') if '=' in l)
def fill(n):
    for c in n['children']:
        if 'children' in c: fill(c)
        elif not c['found']: c['found']=F.get(c['name'],'')
fill(base)
top={c['name']:c for c in base['children']}
def merge(dst,src):
    for c in src['children']:
        if 'children' in c:
            ex=next((x for x in dst['children'] if x['name']==c['name'] and 'children' in x),None)
            if ex: merge(ex,c)
            else: dst['children'].append(c)
        elif not any(x['name']==c['name'] for x in dst['children']): dst['children'].append(c)
# Micronutrients replaced
top['Micronutrients']['children']=parse(micro.lines())['children']
# Additives replaced
rows=json.load(open('fsa.json'));fix={'lsomalt':'Isomalt','lnosinic acid':'Inosinic acid'}
groups={}
last=None;sub=0
for sec,code,name in rows:
    name=re.sub(r'^\((i+)\)\s*','',name).replace('; not permitted for use in Northern Ireland','').replace('’',"'").replace('\u00ad','').replace('  ',' ').strip()
    name=fix.get(name,name)
    if code: last=code;sub=0;c=code
    else: sub+=1;c=last+('ii' if sub==1 else 'iii')
    g,orig,prod,*sp=M[last];lab,does=GROUP[g]
    leaf={'name':f'{name} ({c})','what':f'{lab}, {c} (EU/UK authorized)','does':sp[0] if sp else does,'found':(orig if orig else NOT)+'; typical products: '+prod}
    groups.setdefault(g,[]).append(leaf)
add=top['Additives'];add['children']=[{'name':'EU/UK authorized additives by function','children':[{'name':g,'children':groups[g]} for g in GROUP if g in groups]}]
merge(add,parse(open('add_add.txt').read().splitlines())['children'][0])
# Flavorings: keep base, drop old dupes, add compounds
merge(top['Macronutrients'],parse(open('add_macro.txt').read().splitlines())['children'][0])
merge(top['Bioactives'],parse(open('add_bio.txt').read().splitlines())['children'][0])
merge(top['Flavorings'],parse(open('add_flav.txt').read().splitlines())['children'][0])
miss=[]
def ser(n,d,o):
    for c in n['children']:
        if 'children' in c: o.append(' '*d+c['name']);ser(c,d+1,o)
        else:
            if not c['found'] or not c['what']: miss.append(c['name'])
            o.append(' '*d+'|'.join([c['name'],c['what'],c['does'],c['found']]))
o=[];ser(base,0,o)
assert not miss,miss
open('../tree.txt','w').write('\n'.join(o)+'\n')
cnt=lambda n:sum(map(cnt,n['children'])) if 'children' in n else 1
for c in base['children']:print(c['name'],cnt(c))
print('total',cnt(base))
# post-step: Water/Ethanol under Macronutrients + Processing category
L=open('../tree.txt').read().splitlines()
i=[k for k,l in enumerate(L) if l.startswith(' Alcohol (ethanol)|')][0]
L[i:i+1]=open('water_eth.txt').read().splitlines()
L+=open('proc.txt').read().splitlines()
open('../tree.txt','w').write('\n'.join(L)+'\n')  # add_proc
