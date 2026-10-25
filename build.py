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
# Regroup (Oct 25, 2026): the top level mirrors Nutrition 101 -- Macronutrients, Micronutrients, Non-Nutrients.
# Non-Nutrients holds the five Module 3 branches in module order; Antinutrients is gathered from leaves that sat
# in Bioactives > Other bioactives. Only moves: every node and its fields are kept (asserted below).
def leaves(n,path=()):
    if 'children' not in n: yield (n['name'],n['what'],n['does'],n.get('found','')); return
    for c in n['children']: yield from leaves(c,path)
_before=sorted(leaves(root))
NN_ORDER=['Additives','Antinutrients','Processing','Bioactives','Flavorings']
ANTI=['Phytic acid','Oxalic acid','Lectins (phytohaemagglutinin)','Trypsin inhibitors','Cyanogenic glycosides (amygdalin, linamarin)']
top={c['name']:c for c in root['children']}
assert set(top)=={'Macronutrients','Micronutrients','Bioactives','Additives','Flavorings','Processing'},list(top)
oth=next(c for c in top['Bioactives']['children'] if c['name']=='Other bioactives')
byname={c['name']:c for c in oth['children']}
anti={"name":"Antinutrients","note":"Compounds that get in the way of absorbing other nutrients, and the ways cooking and processing lower them. Tannins (Bioactives > Polyphenols), goitrogenic glucosinolates (Bioactives > Glucosinolates and derivatives) and solanine (Bioactives > Alkaloids and methylxanthines) also act as antinutrients and stay with their families.","children":[byname[x] for x in ANTI]}
oth['children']=[c for c in oth['children'] if c['name'] not in ANTI]
top['Antinutrients']=anti
nn={"name":"Non-Nutrients","note":"Everything on a label that is not a nutrient, in the order of Module 3 of Nutrition 101.","children":[top[x] for x in NN_ORDER]}
root['children']=[top['Macronutrients'],top['Micronutrients'],nn]
assert sorted(leaves(root))==_before
json.dump(root,open('data.json','w'),indent=1)
open('data.js','w').write('window.TREE='+json.dumps(root)+';')
c=lambda n:sum(map(c,n['children'])) if 'children' in n else 1
print(c(root))
