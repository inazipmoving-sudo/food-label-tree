import json
lines=[l.rstrip() for l in open('tree.txt') if l.strip()]
root={"name":"Everything on a food label","children":[]};stack=[(-1,root)]
for l in lines:
    d=len(l)-len(l.lstrip(' '));t=l.strip()
    while stack[-1][0]>=d: stack.pop()
    p=stack[-1][1]
    if '|' in t:
        n,w,f=(t.split('|')+[''])[:3];p.setdefault('children',[]).append({"name":n,"what":w,"does":f})
    else:
        node={"name":t,"children":[]};p.setdefault('children',[]).append(node);stack.append((d,node))
foods=[c for c in root['children'] if c['name'].startswith('Ingredients')][0]
root['children'].remove(foods);foods['name']='Foods'
json.dump({'compounds':root,'foods':foods},open('data.json','w'),indent=1)
open('data.js','w').write('window.TREE='+json.dumps(root)+';window.FOODS='+json.dumps(foods)+';')
c=lambda n:sum(map(c,n['children'])) if 'children' in n else 1
print(c(root),c(foods))
