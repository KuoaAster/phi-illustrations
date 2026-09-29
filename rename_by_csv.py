import os
import csv
id_to_song = {}
with open('illustrations_chart.csv', mode='r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if len(row) >= 2:
            id_to_song[row[0].strip()] = row[1].strip()

print(f"📚 成功加载了 {len(id_to_song)} 首歌的对应关系！")
folder_path = r".\Texture2D"
count = 0
for filename in os.listdir(folder_path):
    if filename.startswith("Illustration #") and filename.endswith(".png"):
        song_id = filename.replace("Illustration #", "").replace(".png", "")
        
        if song_id in id_to_song:
            raw_name = id_to_song[song_id]
            safe_name = raw_name
            for char in ['/', '\\', ':', '*', '?', '"', '<', '>', '|']:
                safe_name = safe_name.replace(char, '_')
            new_name = f"{safe_name}.png"
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            
            # 防重名保护
            if os.path.exists(new_path):
                new_name = f"{id_to_song[song_id]}_{song_id}.png"
                new_path = os.path.join(folder_path, new_name)
                
            os.rename(old_path, new_path)
            count += 1
            print(f"✅ {filename} -> {new_name}")

print(f"🎉 大功告成！一共成功重命名了 {count} 张曲绘！")