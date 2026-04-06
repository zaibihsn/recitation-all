import os

c = [7, 286, 200, 176, 120, 165, 206, 75, 129, 109, 123, 111, 43, 52, 99, 128, 111, 110, 98, 135,
     112, 78, 118, 64, 77, 227, 93, 88, 69, 60, 34, 30, 73, 54, 45, 83, 182, 88, 75, 85,
     54, 53, 89, 59, 37, 35, 38, 29, 18, 45, 60, 49, 62, 55, 78, 96, 29, 22, 24, 13,
     14, 11, 11, 18, 12, 12, 30, 52, 52, 44, 28, 28, 20, 56, 40, 31, 50, 40, 46, 42,
     29, 19, 36, 25, 22, 17, 19, 26, 30, 20, 15, 21, 11, 8, 8, 19, 5, 8, 8, 11, 11, 8,
     3, 9, 5, 4, 7, 3, 6, 3, 5, 4, 5, 6]
cum = [0]*115
for i in range(1,115): cum[i] = cum[i-1] + c[i-1]

d = "/home/zaibi/code/recitation-all"
rs = ["bandar-baleela", "ahmed-ibn-ali-al-ajmy", "minshawi-kids-repeat", "abdullah-hamad-abu-sharida"]

for r in rs:
    p = os.path.join(d, r)
    n = 0
    if not os.path.exists(p): continue
    for ch in os.listdir(p):
        if not ch.isdigit() or len(ch)!=3: continue
        ch_p = os.path.join(p, ch)
        ch_n = int(ch)
        
        files_to_rename = []
        for f in os.listdir(ch_p):
            if f.endswith('.opus') or f.endswith('.json'):
                ext = f.split('.')[-1]
                b = f.split('.')[0]
                v = None
                if len(b)==3 and b.isdigit(): v = int(b)
                elif len(b)==6 and b.startswith(ch): v = int(b[3:])
                else: continue
                if v < 1 or v > c[ch_n-1]: continue
                abs_v = cum[ch_n-1] + v
                nf = f"{ch_n:03d}{abs_v:03d}.{ext}.tmp"
                files_to_rename.append((f, nf))
        
        for f, nf in files_to_rename:
            os.rename(os.path.join(ch_p, f), os.path.join(ch_p, nf))
            
        for f in os.listdir(ch_p):
            if f.endswith('.tmp'):
                nf = f[:-4]
                os.rename(os.path.join(ch_p, f), os.path.join(ch_p, nf))
                n += 1
                
    print(f"Renamed {n} files in {r}")
