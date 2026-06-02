import os
import markdown
import re

# Path definitions
us_folder = r"D:\Work Station\02_Projects\01_Jewelry_ERP\modules\m01-Kiem_Soat_Nguyen_Lieu\user_stories"
output_file = r"D:\Work Station\CS1_UserStories_Dashboard.html"

# CSS for Premium Aesthetic
css = """
body { font-family: 'Inter', -apple-system, sans-serif; background: #f0f2f5; color: #1a1a1a; line-height: 1.6; margin: 0; padding: 0; }
.sidebar { width: 300px; position: fixed; height: 100vh; background: #ffffff; border-right: 1px solid #e1e4e8; overflow-y: auto; padding: 20px; box-sizing: border-box; }
.content { margin-left: 300px; padding: 40px; max-width: 900px; }
.card { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); margin-bottom: 40px; border: 1px solid #eee; }
h1 { color: #000; border-bottom: 3px solid #0052cc; padding-bottom: 10px; font-size: 28px; }
h2 { color: #0052cc; margin-top: 30px; border-bottom: 1px solid #eee; padding-bottom: 5px; }
h3 { color: #333; background: #f8f9fa; padding: 10px; border-left: 4px solid #0052cc; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 14px; }
th, td { border: 1px solid #e1e4e8; padding: 12px; text-align: left; }
th { background: #f6f8fa; font-weight: 600; }
.nav-item { display: block; padding: 10px; color: #444; text-decoration: none; border-radius: 6px; margin-bottom: 5px; font-size: 14px; transition: 0.2s; }
.nav-item:hover { background: #f0f7ff; color: #0052cc; }
.badge { display: inline-block; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; margin-right: 5px; }
.badge-epic { background: #e3f2fd; color: #1976d2; }
.tag-us { color: #666; font-family: monospace; }
blockquote { border-left: 5px solid #ff9800; background: #fffde7; padding: 15px; margin: 0; border-radius: 0 8px 8px 0; }
"""

html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>CS1 - User Stories Dashboard</title>
    <style>{css}</style>
</head>
<body>
    <div class="sidebar">
        <h2 style="font-size: 18px; color: #333;">📋 Mục lục US</h2>
        <nav id="navbar">
            {{NAV_ITEMS}}
        </nav>
    </div>
    <div class="content">
        <div style="margin-bottom: 40px;">
            <h1 style="border:none; margin:0;">💎 Jewelry ERP - Material Control</h1>
            <p style="color:#666;">Control Stage 1: Tiếp nhận nguyên liệu khách (Approved Version)</p>
        </div>
        {{CONTENT_ITEMS}}
    </div>
</body>
</html>
"""

def generate():
    files = [f for f in os.listdir(us_folder) if f.startswith("CS1_E1_US_") and f.endswith(".md")]
    files.sort()
    
    nav_html = ""
    content_html = ""
    
    for filename in files:
        with open(os.path.join(us_folder, filename), 'r', encoding='utf-8') as f:
            md_content = f.read()
            
            # Extract Title
            title_match = re.search(r'^# 🏷️ \[(.*?)\] (.*)', md_content, re.MULTILINE)
            us_id = title_match.group(1) if title_match else filename
            us_title = title_match.group(2) if title_match else filename
            anchor = us_id.replace('.', '_')
            
            # Generate Nav
            nav_html += f'<a href="#{anchor}" class="nav-item"><b>{us_id}</b><br><span style="font-size:12px; color:#888;">{us_title}</span></a>\n'
            
            # Convert MD to HTML (Handle tables and alerts)
            body_html = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'nl2br'])
            
            # Wrap in card
            content_html += f'<div id="{anchor}" class="card">{body_html}</div>\n'

    final_html = html_template.replace("{NAV_ITEMS}", nav_html).replace("{CONTENT_ITEMS}", content_html)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print(f"Dashboard created: {output_file}")

if __name__ == "__main__":
    generate()
