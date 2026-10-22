import json,copy
lines=[l.rstrip() for l in open('tree.txt') if l.strip()]
root={"name":"All compounds","children":[]};stack=[(-1,root)]
for l in lines:
    d=len(l)-len(l.lstrip(' '));t=l.strip()
    while stack[-1][0]>=d: stack.pop()
    p=stack[-1][1]
    if '|' in t:
        n,w,f=(t.split('|')+[''])[:3];p['children'].append({"name":n,"what":w,"does":f})
    else:
        node={"name":t,"children":[]};p['children'].append(node);stack.append((d,node))
foods=[c for c in root['children'] if c['name'].startswith('Ingredients')][0];root['children'].remove(foods)
paths={}
def walk(n,path):
    for c in n.get('children',[]):
        paths.setdefault(c['name'],(path+[c['name']],c));walk(c,path+[c['name']])
walk(root,[])
ORDER=["Macronutrients","Micronutrients","Bioactives","Additives","Water","Flavorings"]
ftree={"name":"Foods","children":[]};missing=[]
for g in foods['children']:
    G={"name":g['name'],"children":[]};ftree['children'].append(G)
    for f in g['children']:
        F={"name":f['name'],"food":f['what'],"children":[]};G['children'].append(F)
        for r in f['does'][5:].split('; '):
            if r not in paths: missing.append(r);continue
            path,node=paths[r];cur=F
            for seg in path[:-1]:
                nx=next((c for c in cur['children'] if c['name']==seg and 'children' in c),None)
                if not nx: nx={"name":seg,"children":[]};cur['children'].append(nx)
                cur=nx
            cur['children'].append({"name":r,"ref":r,"what":node.get('what',node['name']+' (category)'),"does":node.get('does','')})
            node.setdefault('found',[]).append(f['name'])
        F['children'].sort(key=lambda c:ORDER.index(c['name']) if c['name'] in ORDER else 99)
assert not missing,missing
json.dump({'foods':ftree,'compounds':root},open('data.json','w'),indent=1)
open('data.js','w').write('window.FOODS='+json.dumps(ftree)+';window.TREE='+json.dumps(root)+';')
c=lambda n:sum(map(c,n['children'])) if 'children' in n else 1
print('compound leaves',c(root),'food-tree compound entries',c(ftree),'foods',sum(len(g['children']) for g in ftree['children']))
