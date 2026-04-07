import os
import json

base_dir = '/home/zaibi/code/recitation-all'
reciters = [
    'bandar-baleela', 
    'ahmed-ibn-ali-al-ajmy', 
    'minshawi-kids-repeat', 
    'abdullah-hamad-abu-sharida'
]

processed_count = 0

for reciter in reciters:
    reciter_dir = os.path.join(base_dir, reciter)
    if not os.path.isdir(reciter_dir):
        continue
        
    for ch in os.listdir(reciter_dir):
        ch_dir = os.path.join(reciter_dir, ch)
        if not os.path.isdir(ch_dir) or len(ch) != 3:
            continue
            
        for file in os.listdir(ch_dir):
            if file.endswith('.json'):
                fpath = os.path.join(ch_dir, file)
                try:
                    with open(fpath, 'r', encoding='utf-8') as f:
                        content = f.read().strip()
                        
                        # Already optimized?
                        if content.startswith('[['):
                            continue
                        if content == '[]':
                            continue
                            
                        data = json.loads(content)
                except Exception as e:
                    print(f"Error reading {fpath}: {e}")
                    continue
                    
                segments = data.get('segments', [])
                optimized = []
                for seg in segments:
                    if len(seg) >= 3:
                        idx = seg[0]
                        start = seg[1]
                        end = seg[2]
                        optimized.append([idx-1, idx, start, end])
                
                new_json = json.dumps(optimized, separators=(',', ':'))
                
                try:
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(new_json)
                    processed_count += 1
                except Exception as e:
                    print(f"Error writing {fpath}: {e}")

print(f"Optimized {processed_count} JSON files.")
