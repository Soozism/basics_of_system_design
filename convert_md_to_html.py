#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown to HTML Converter for System Design Tutorial
This script converts all markdown files to HTML with proper styling and navigation
"""

import os
import re
import html
import json
from pathlib import Path
from datetime import datetime

# Configuration
INPUT_DIR = r"c:\Users\sooz\Desktop\system design\basics_of_system_design"
OUTPUT_DIR = r"c:\Users\sooz\Desktop\system design\basics_of_system_design\html_website"
CSS_PATH = "css/style.css"
JS_PATH = "js/script.js"

# HTML template
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="{css_path}">
    <meta name="description" content="{description}">
    <meta name="keywords" content="طراحی سیستم, مهندسی نرم‌افزار, معماری سیستم">
</head>
<body>
    <header>
        <div class="header-content">
            <a href="{home_link}" class="logo">طراحی سیستم</a>
            <nav>
                <ul class="nav-menu">
                    <li><a href="{home_link}">خانه</a></li>
                    <li><a href="{home_link}#basic-concepts">مفاهیم پایه</a></li>
                    <li><a href="{home_link}#main-components">اجزای اصلی</a></li>
                    <li><a href="{home_link}#scalable-systems">سیستم‌های مقیاس‌پذیر</a></li>
                    <li><a href="{home_link}#advanced-topics">موضوعات پیشرفته</a></li>
                    <li><a href="{home_link}#interviews">مصاحبه</a></li>
                </ul>
            </nav>
            <button class="mobile-menu-toggle">☰</button>
        </div>
    </header>

    <div class="container">
        <main class="main-content">
            <aside class="sidebar">
                {sidebar_content}
            </aside>

            <article class="content">
                <div class="breadcrumb">
                    {breadcrumb}
                </div>

                {content}

                <div class="alert alert-info" style="margin-top: 2rem;">
                    <strong>نکته:</strong> این مطلب بخشی از مجموعه آموزش طراحی سیستم است. برای مطالعه سایر مطالب، از منوی کناری استفاده کنید.
                </div>
            </article>
        </main>
    </div>

    <footer>
        <div class="footer-content">
            <p>&copy; 2024 آموزش طراحی سیستم - تمام حقوق محفوظ است</p>
            <p>آخرین به‌روزرسانی: {last_updated}</p>
        </div>
    </footer>

    <script src="{js_path}"></script>
</body>
</html>"""

def clean_text(text):
    """Clean and sanitize text for HTML"""
    return html.escape(text.strip())

def markdown_to_html(markdown_content):
    """Convert markdown content to HTML"""
    # Basic markdown to HTML conversion
    html_content = markdown_content
    
    # Headers
    html_content = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^#### (.*?)$', r'<h4>\1</h4>', html_content, flags=re.MULTILINE)
    
    # Bold and italic
    html_content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html_content)
    html_content = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html_content)
    
    # Code blocks
    html_content = re.sub(r'```(.*?)```', r'<pre><code>\1</code></pre>', html_content, flags=re.DOTALL)
    html_content = re.sub(r'`(.*?)`', r'<code>\1</code>', html_content)
    
    # Lists
    html_content = re.sub(r'^\- (.*?)$', r'<li>\1</li>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^\d+\. (.*?)$', r'<li>\1</li>', html_content, flags=re.MULTILINE)
    
    # Wrap list items in ul tags
    html_content = re.sub(r'(<li>.*?</li>)', r'<ul>\1</ul>', html_content, flags=re.DOTALL)
    
    # Paragraphs
    paragraphs = html_content.split('\n\n')
    html_paragraphs = []
    
    for para in paragraphs:
        para = para.strip()
        if para and not para.startswith('<'):
            html_paragraphs.append(f'<p>{para}</p>')
        else:
            html_paragraphs.append(para)
    
    html_content = '\n\n'.join(html_paragraphs)
    
    # Links
    html_content = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', html_content)
    
    # Tables (basic support)
    html_content = re.sub(r'\|(.*?)\|', r'<td>\1</td>', html_content)
    
    # Blockquotes
    html_content = re.sub(r'^> (.*?)$', r'<blockquote><p>\1</p></blockquote>', html_content, flags=re.MULTILINE)
    
    # Horizontal rules
    html_content = re.sub(r'^---$', r'<hr>', html_content, flags=re.MULTILINE)
    
    return html_content

def extract_title(markdown_content):
    """Extract title from markdown content"""
    lines = markdown_content.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    return "بدون عنوان"

def generate_breadcrumb(file_path, output_dir):
    """Generate breadcrumb navigation"""
    relative_path = os.path.relpath(file_path, output_dir)
    parts = relative_path.split(os.sep)
    
    breadcrumb = ['<a href="index.html">خانه</a>']
    
    current_path = ""
    for i, part in enumerate(parts[:-1]):  # Exclude the file name
        current_path = os.path.join(current_path, part)
        breadcrumb.append(f'<span>/</span>')
        breadcrumb.append(f'<span>{part}</span>')
    
    breadcrumb.append('<span>/</span>')
    breadcrumb.append(f'<span>{parts[-1]}</span>')
    
    return '\n'.join(breadcrumb)

def generate_sidebar(section_name):
    """Generate sidebar content based on section"""
    sidebar_content = f"""
    <h3>{section_name}</h3>
    <ul>
        <li><a href="../../../index.html">بازگشت به خانه</a></li>
        <li><a href="../../../index.html#basic-concepts">مفاهیم پایه</a></li>
        <li><a href="../../../index.html#main-components">اجزای اصلی</a></li>
        <li><a href="../../../index.html#scalable-systems">سیستم‌های مقیاس‌پذیر</a></li>
        <li><a href="../../../index.html#advanced-topics">موضوعات پیشرفته</a></li>
        <li><a href="../../../index.html#interviews">آمادگی مصاحبه</a></li>
    </ul>
    """
    return sidebar_content

def calculate_relative_paths(output_file_path, output_dir):
    """Calculate relative paths for CSS and JS files"""
    relative_path = os.path.relpath(output_file_path, output_dir)
    depth = len(relative_path.split(os.sep)) - 1
    
    if depth == 0:
        return "css/style.css", "js/script.js", "index.html"
    else:
        prefix = "../" * depth
        return f"{prefix}css/style.css", f"{prefix}js/script.js", f"{prefix}index.html"

def process_markdown_file(input_file, output_file, output_dir):
    """Process a single markdown file"""
    try:
        # Read markdown content
        with open(input_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Extract title and convert to HTML
        title = extract_title(markdown_content)
        html_content = markdown_to_html(markdown_content)
        
        # Generate navigation elements
        breadcrumb = generate_breadcrumb(output_file, output_dir)
        sidebar_content = generate_sidebar(title)
        
        # Calculate relative paths
        css_path, js_path, home_link = calculate_relative_paths(output_file, output_dir)
        
        # Create final HTML
        final_html = HTML_TEMPLATE.format(
            title=clean_text(title),
            description=clean_text(title),
            css_path=css_path,
            js_path=js_path,
            home_link=home_link,
            sidebar_content=sidebar_content,
            breadcrumb=breadcrumb,
            content=html_content,
            last_updated=datetime.now().strftime('%Y-%m-%d')
        )
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Write HTML file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_html)
        
        print(f"✓ Converted: {input_file} -> {output_file}")
        
    except Exception as e:
        print(f"✗ Error processing {input_file}: {str(e)}")

def main():
    """Main function to process all markdown files"""
    print("Starting markdown to HTML conversion...")
    
    # Find all markdown files
    input_path = Path(INPUT_DIR)
    output_path = Path(OUTPUT_DIR)
    
    markdown_files = []
    for md_file in input_path.rglob("*.markdown"):
        markdown_files.append(md_file)
    
    print(f"Found {len(markdown_files)} markdown files")
    
    # Process each file
    for md_file in markdown_files:
        # Calculate output path
        relative_path = md_file.relative_to(input_path)
        output_file = output_path / relative_path.with_suffix('.html')
        
        # Create directory structure
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Process the file
        process_markdown_file(str(md_file), str(output_file), str(output_path))
    
    print(f"\nConversion complete! {len(markdown_files)} files processed.")
    print(f"Output directory: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
