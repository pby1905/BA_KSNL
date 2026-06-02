import os
import email
from html.parser import HTMLParser
import re
import glob
import shutil

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = []
    def handle_data(self, d):
        val = d.replace('\n', ' ').replace('\r', '').strip()
        if val:
            self.text.append(val)
    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'br':
            self.text.append('\n')
        elif tag.lower() == 'tr':
            self.text.append('\n')
    def handle_endtag(self, tag):
        if tag.lower() == 'td' or tag.lower() == 'th':
            self.text.append(' | ')
        elif tag.lower() == 'tr':
            self.text.append('\n')
        elif tag.lower() in ('p', 'div'):
            self.text.append('\n')
            
    def get_data(self):
        # clean up double spaces from join
        return re.sub(r'\n\s*\n', '\n', ''.join(self.text))

raw_dir = r"D:\Work Station\01_Raw_Inputs"
inbox_dir = os.path.join(raw_dir, "Kiem_Soat_Nguyen_Lieu_Inbox", "CS1_E1_Raw")
out_file = r"D:\Work Station\02_Projects\01_Jewelry_ERP\modules\m01-Kiem_Soat_Nguyen_Lieu\docs_draft\04_1_US_CS1_Detailed.md"

os.makedirs(inbox_dir, exist_ok=True)

files = glob.glob(os.path.join(raw_dir, "✅CS1.E1*.doc"))
files.sort()

with open(out_file, 'w', encoding='utf-8') as out:
    for file_path in files:
        filename = os.path.basename(file_path)
        out.write(f"\n\n# {filename}\n")
        out.write("-" * 80 + "\n\n")
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                msg = email.message_from_file(f)
                html = next((p.get_payload(decode=True).decode('utf-8', 'ignore') for p in msg.walk() if p.get_content_type() == 'text/html'), None)
                if html:
                    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL)
                    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
                    
                    s = MLStripper()
                    s.feed(html)
                    out.write(s.get_data() + "\n\n")
                else:
                    out.write("[No HTML content found]\n")
        except Exception as e:
            out.write(f"Error processing file: {e}\n")
            
        shutil.move(file_path, os.path.join(inbox_dir, filename))

print(f"Processed {len(files)} files.")
