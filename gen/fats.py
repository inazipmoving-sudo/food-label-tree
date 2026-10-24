# Restructure Macronutrients > Fats (idempotent; run after gen.py writes ../tree.txt)
import os
P=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','tree.txt')
L=open(P).read().splitlines()
a=L.index(' Fats') if ' Fats' in L else [i for i,l in enumerate(L) if l.startswith(' Fats ::')][0]
b=a+1
while L[b].startswith('  '): b+=1
leaves={}
for l in L[a+1:b]:
    if '|' in l: leaves[l.strip().split('|')[0]]=l.strip()
used=set()
def g(*names):
    o=[]
    for n in names: o.append(leaves[n]);used.add(n)
    return o
def rest(pred): 
    o=[n for n in leaves if n not in used and pred(n)];used.update(o);return [leaves[n] for n in o]
mono=g('Oleic acid (omega-9)','Palmitoleic acid (omega-7)','Erucic acid (omega-9)','Myristoleic acid (C14:1)','Petroselinic acid (C18:1 n-12)','Gondoic acid (C20:1 n-9)','Nervonic acid (C24:1 n-9)','Ricinoleic acid')
w3=g('ALA (alpha-linolenic acid)','SDA (stearidonic acid)','ETA (eicosatetraenoic acid)','EPA (eicosapentaenoic acid)','DPA (docosapentaenoic acid)','DHA (docosahexaenoic acid)')
w6=g('Linoleic acid (LA)','Gamma-linolenic acid (GLA)','Eicosadienoic acid (C20:2 n-6)','DGLA (dihomo-gamma-linolenic acid)','Arachidonic acid (AA)','Adrenic acid (C22:4 n-6)','Pinolenic acid')
opu=g('Punicic acid','Mead acid (C20:3 n-9)')
tr_ind=g('Elaidic acid')
tr_nat=g('Vaccenic acid','Trans-palmitoleic acid (C16:1 t9)','Conjugated linoleic acid (CLA)','Rumenic acid (CLA c9,t11)','CLA t10,c12')
sat=g('Butyric acid (C4:0)','Caproic acid (C6:0)','Caprylic acid (C8:0)','Capric acid (C10:0)','Lauric acid (C12:0)','Myristic acid (C14:0)','Pentadecanoic acid (C15:0)','Palmitic acid (C16:0)','Margaric acid (C17:0)','Stearic acid (C18:0)','Arachidic acid (C20:0)','Behenic acid (C22:0)','Lignoceric acid (C24:0)')
other=rest(lambda n:True)
I=lambda d,xs:[' '*d+x for x in xs]
N=[' Fats :: All fats provide 9 kcal/g. Stored body fat is mostly unsaturated triglycerides (oleic acid dominant): firmer near the cooler skin, softer deeper in.',
'  Unsaturated :: Double bonds put kinks in the chains, so they cannot pack tightly; liquid at room temperature.',
'   Monounsaturated :: One double bond (oleic acid is the main one).']+I(4,mono)+[
'   Polyunsaturated :: Two or more double bonds.',
'    Omega-3 :: First double bond 3 carbons from the methyl (omega) end: ALA, SDA, ETA, EPA, DPA, DHA.']+I(5,w3)+[
'    Omega-6 :: First double bond 6 carbons from the omega end: LA, GLA, DGLA, AA and others.']+I(5,w6)+[
'    Other polyunsaturated :: Conjugated or omega-9 polyunsaturated fatty acids.']+I(5,opu)+[
'  Saturated :: No double bonds: straight chains pack tightly, so solid at room temperature. Fully hydrogenating an unsaturated fat makes it saturated.']+I(3,sat)+[
'  Trans fat :: Mostly man-made. Partial hydrogenation flips some cis double bonds to trans (hydrogens on opposite sides), straightening the chain so it packs and solidifies like saturated fat. Small amounts occur naturally in ruminant meat and dairy.',
'   Industrial (partial hydrogenation) :: Made when oils are partially hydrogenated; raises LDL and lowers HDL.']+I(4,tr_ind)+[
'   Natural ruminant trans :: Formed by bacteria in the stomachs of cows, sheep and goats; found in small amounts in dairy and meat.']+I(4,tr_nat)+[
'  Other lipids :: Glycerides, phospholipids, sterols and related fat-like compounds.']+I(3,other)
assert len(used)==len(leaves) and sum('|' in x for x in N)==len(leaves)
L[a:b]=N
open(P,'w').write('\n'.join(L)+'\n')
print('fat leaves',len(leaves),'other',len(other))
