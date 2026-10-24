import json,copy
lines=[l.rstrip() for l in open('tree.txt') if l.strip()]
root={"name":"All compounds","children":[]};stack=[(-1,root)]
for l in lines:
    d=len(l)-len(l.lstrip(' '));t=l.strip()
    while stack[-1][0]>=d: stack.pop()
    p=stack[-1][1]
    if '|' in t:
        n,w,f,fd=(t.split('|')+['',''])[:4];p['children'].append({"name":n,"what":w,"does":f,**({'found':fd} if fd else {})})
    else:
        nm,_,note=t.partition(' :: ');node={"name":nm,**({'note':note} if note else {}),"children":[]};p['children'].append(node);stack.append((d,node))
ing=[c for c in root['children'] if c['name'].startswith('Ingredients')]
for c in ing: root['children'].remove(c)
import os
F=dict(l.rstrip('\n').split('=',1) for l in open('found.txt') if '=' in l) if os.path.exists('found.txt') else {}
miss=[]
def walk(n,top):
    for c in n.get('children',[]):
        t=top or c['name']
        if 'children' in c: walk(c,t)
        elif c.get('found'): pass
        elif c['name'] in F: c['found']=F[c['name']]
        else: miss.append(c['name'])
walk(root,None);assert not miss,miss
json.dump(root,open('data.json','w'),indent=1)
open('data.js','w').write('window.TREE='+json.dumps(root)+';')
c=lambda n:sum(map(c,n['children'])) if 'children' in n else 1
print(c(root))
