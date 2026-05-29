import email
from html.parser import HTMLParser
import sys
import re

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = []
    def handle_data(self, d):
        d = d.strip()
        if d:
            self.text.append(d)
    def get_data(self):
        return '\n'.join(self.text)

def main():
    try:
        with open(r'd:\Work Station\01_Raw_Inputs\Kiem_Soat_Nguyen_Lieu_Inbox\MC-1.+Product+Requirement.doc', 'r', encoding='utf-8', errors='ignore') as f:
            msg = email.message_from_file(f)
            html = next((p.get_payload(decode=True).decode('utf-8', 'ignore') for p in msg.walk() if p.get_content_type() == 'text/html'), None)
            
            if html:
                # Basic cleanup
                html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL)
                html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
                
                s = MLStripper()
                s.feed(html)
                # print first 5000 chars
                result = s.get_data()
                with open('output_utf8.md', 'w', encoding='utf-8') as out_f:
                    out_f.write(result)
            else:
                print("No HTML found")
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
