import os
import re

source_file = r"D:\Work Station\02_Projects\01_Jewelry_ERP\modules\m01-Kiem_Soat_Nguyen_Lieu\docs_draft\04_1_US_CS1_Detailed.md"
out_dir = r"D:\Work Station\02_Projects\01_Jewelry_ERP\modules\m01-Kiem_Soat_Nguyen_Lieu\docs_draft\04_User_Stories_CS1"

os.makedirs(out_dir, exist_ok=True)

with open(source_file, 'r', encoding='utf-8') as f:
    text = f.read()

matches = list(re.finditer(r'^# ✅(CS1\.E1\.US-\d+).*?$', text, re.MULTILINE))

if not matches:
    print("No User Stories found to split.")
    exit(0)

count = 0
for i, match in enumerate(matches):
    start = match.start()
    end = matches[i+1].start() if i + 1 < len(matches) else len(text)
    chunk = text[start:end].strip()
    
    first_line = chunk.split('\n')[0]
    prefix_match = re.search(r'(CS1\.E1\.US-\d+)', first_line)
    
    if prefix_match:
        prefix = prefix_match.group(1).replace('.', '_')
        filename = f"{prefix}.md"
    else:
        filename = f"US_Unknown_{count}.md"
        
    out_path = os.path.join(out_dir, filename)
    
    # Remove the artifact filename header from the actual MD body to make it cleaner
    clean_chunk = re.sub(r'^# ✅.*?\.doc\n\-+\n', '', chunk, flags=re.MULTILINE).strip()
    
    with open(out_path, 'w', encoding='utf-8') as out_f:
        out_f.write(clean_chunk)
    count += 1

print(f"Successfully split into {count} markdown files.")
