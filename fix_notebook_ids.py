import json
import os
import uuid

notebook_dir = "/home/gslee/wGitHub/code-workout-datasci/jupyter-book"

for filename in os.listdir(notebook_dir):
    if filename.endswith(".ipynb"):
        filepath = os.path.join(notebook_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        # 모든 셀에 고유한 ID 할당
        for cell in nb['cells']:
            cell['id'] = str(uuid.uuid4())
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(nb, f, ensure_ascii=False, indent=1)
        
        print(f"✓ {filename} - 셀 ID 재생성 완료")

print("완료!")