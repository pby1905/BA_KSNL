import markdown

try:
    with open('D:/Work Station/02_Projects/01_Jewelry_ERP/modules/m01-Kiem_Soat_Nguyen_Lieu/docs_draft/04_1_US_CS1_Detailed.md', 'r', encoding='utf-8') as f:
        text = f.read()
    html_content = markdown.markdown(text, extensions=['tables'])
    html_template = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Preview Detailed US - Control Stage 1</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif; line-height: 1.6; padding: 2rem; max-width: 1000px; margin: 0 auto; color: #111; background-color: #FAFAFA; }}
        .container {{ background-color: white; padding: 40px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }}
        table {{ border-collapse: collapse; width: 100%; margin-bottom: 1rem; }}
        th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
        th {{ background-color: #f6f8fa; }}
        h1, h2, h3 {{ color: #24292e; border-bottom: 1px solid #eaecef; padding-bottom: .3em; margin-top: 24px; }}
        code {{ background-color: rgba(27,31,35,.05); border-radius: 3px; font-size: 85%; margin: 0; padding: .2em .4em; }}
    </style>
</head>
<body>
    <div class="container">
    {html_content}
    </div>
</body>
</html>'''
    with open('D:/Work Station/preview.html', 'w', encoding='utf-8') as f:
        f.write(html_template)
    print('HTML generated successfully')
except Exception as e:
    print('Error:', e)
