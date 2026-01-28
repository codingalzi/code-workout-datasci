# ...existing code...
import os
import json
import uuid

def regenerate_cell_ids(directory):
    # os.walk는 지정된 디렉토리부터 시작해서 모든 하위 폴더를 재귀적으로 순회합니다.
    print(f"📂 Searching for notebooks recursively in: {directory}")
    
    processed_files = 0
    
    for root, dirs, files in os.walk(directory):
        # 불필요한 폴더 건너뛰기 (_build, git, venv 등)
        if any(x in root for x in ["_build", ".ipynb_checkpoints", ".git", ".venv", "env"]):
            continue
            
        for file in files:
            if file.endswith(".ipynb"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        nb = json.load(f)
                    
                    if 'cells' not in nb:
                        continue
                        
                    # 모든 셀에 새로운 고유 ID 할당 및 metadata 정리
                    for cell in nb['cells']:
                        # 1. 표준 'id' 필드 갱신
                        cell['id'] = str(uuid.uuid4())
                        
                        # 2. metadata 내의 'id' 필드 제거 (중복의 원인)
                        if 'metadata' in cell and 'id' in cell['metadata']:
                            del cell['metadata']['id']
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(nb, f, indent=1, ensure_ascii=False)
                        
                    print(f"  ✓ Fixed: {file_path}")
                    processed_files += 1
                    
                except Exception as e:
                    print(f"  ✗ Error: {file_path} - {str(e)}")

    print(f"\n✨ 완료! 총 {processed_files}개의 노트북 파일이 수정되었습니다.")

if __name__ == "__main__":
    # 현재 폴더(.)를 시작점으로 지정하면 모든 하위 폴더를 탐색합니다.
    regenerate_cell_ids(".")