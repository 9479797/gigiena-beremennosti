"""redline: E{idx: new_text}; old/new diff by words; deleted = red strike, inserted = plain."""
import sys, re, copy, difflib, importlib.util
import docx
from docx.oxml.ns import qn
from lxml import etree
src, mod, out = sys.argv[1:4]
s = importlib.util.spec_from_file_location('x', mod); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
d = docx.Document(src); P = d.paragraphs
W = qn
def bold(r):
    rp = r.find(W('w:rPr')); b = rp.find(W('w:b')) if rp is not None else None
    return b is not None and b.get(W('w:val')) not in ('0', 'false')
def mk(rpr, text, dele=False, ins=False):
    r = etree.Element(W('w:r')); rp = copy.deepcopy(rpr) if rpr is not None else etree.Element(W('w:rPr'))
    for t in ('w:strike', 'w:color', 'w:highlight'):
        e = rp.find(W(t))
        if e is not None: rp.remove(e)
    if dele:
        rp.append(etree.Element(W('w:strike'))); c = etree.Element(W('w:color')); c.set(W('w:val'), 'C00000'); rp.append(c)
    elif ins:
        c = etree.Element(W('w:color')); c.set(W('w:val'), '7030A0'); rp.append(c)
    r.append(rp); t = etree.SubElement(r, W('w:t')); t.text = text
    t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve'); return r
tok = lambda s: re.findall(r'\s+|[\wёЁ\-]+|[^\w\s]', s)
for i, new in m.E.items():
    p = P[i]._p; rs = [c for c in p if c.tag == W('w:r')]
    old = P[i].text
    lead_rs = []
    for r in rs:
        if bold(r): lead_rs.append(r)
        else: break
    lead = ''.join(''.join(t.text or '' for t in r.iter(W('w:t'))) for r in lead_rs)
    if lead and new.startswith(lead) and old.startswith(lead):
        old_b, new_b = old[len(lead):], new[len(lead):]
    else:
        lead_rs = []; old_b, new_b = old, new
    plain = [r for r in rs if not bold(r)] or rs
    base = plain[0].find(W('w:rPr'))
    for c in list(p):
        if c.tag in (W('w:r'), W('w:proofErr')) and c not in lead_rs: p.remove(c)
    a, b = tok(old_b), tok(new_b)
    ops = difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes()
    # coalesce: short equal islands (< 4 word tokens) between changes become part of the change
    segs = []
    for op, i1, i2, j1, j2 in ops:
        words = sum(1 for t in a[i1:i2] if re.match(r'[\wёЁ]', t))
        if op == 'equal' and words < 4 and segs and segs[-1][0] == 'chg':
            segs[-1] = ('chg', segs[-1][1], i2, segs[-1][3], j2)
        elif op == 'equal':
            segs.append(('eq', i1, i2, j1, j2))
        else:
            if segs and segs[-1][0] == 'chg':
                segs[-1] = ('chg', segs[-1][1], i2, segs[-1][3], j2)
            elif len(segs) >= 2 and segs[-1][0] == 'eq' and sum(1 for t in a[segs[-1][1]:segs[-1][2]] if re.match(r'[\wёЁ]', t)) < 4 and segs[-2][0] == 'chg':
                e = segs.pop(); c = segs.pop(); segs.append(('chg', c[1], i2, c[3], j2))
            else:
                segs.append(('chg', i1, i2, j1, j2))
    for op, i1, i2, j1, j2 in segs:
        if op == 'eq': p.append(mk(base, ''.join(a[i1:i2])))
        else:
            if i2 > i1:
                p.append(mk(base, ''.join(a[i1:i2]).rstrip(), True))
                if j2 > j1 and re.match(r'[\wёЁ«(]', b[j1]) and not ''.join(b[j1:j2]).startswith(' ') and j1 > 0 and b[j1-1] not in '«("„ ': p.append(mk(base, ' '))
            if j2 > j1: p.append(mk(base, ''.join(b[j1:j2]), ins=True))
d.save(out); print('saved', out, len(m.E))
