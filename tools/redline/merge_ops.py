"""Собрать ops-файлы разделов в один ops-файл для build_all.py.
usage: python3 -I merge_ops.py OUT.py ops_8_1.py ops_8_2.py ...
Из каждого берутся E, INS; NOTES[1:] (причины правок) ставятся перед первым
абзацем раздела CROP[0]. HEAD, MOVE, NOTES, BODY, LIST дописываются в OUT.py вручную."""
import sys, importlib.util
out, files = sys.argv[1], sys.argv[2:]
E, INS, SEC = {}, {}, {}
for f in files:
    s = importlib.util.spec_from_file_location('o', f); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    for k, v in m.E.items():
        assert k not in E, (f, k); E[k] = v
    for k, v in m.INS.items():
        assert k not in INS, (f, k); INS[k] = v
    SEC[getattr(m, 'CROP', (0,))[0]] = list(m.NOTES[1:])
with open(out, 'w', encoding='utf-8') as w:
    w.write(f'E = {E!r}\nINS = {INS!r}\nSECNOTES = {SEC!r}\nHEAD = None\nMOVE = None\nNOTES = []\nBODY, LIST = 2, 2\n')
print('ok', len(E), len(INS), len(SEC))
