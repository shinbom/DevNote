#!/usr/bin/env python3
"""
GitBook 프로젝트의 모든 마크다운 파일에 수정일을 업데이트하는 파이썬 스크립트
"""

import os
import subprocess
import re
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
EXCLUDE_DIRS = {'.git', 'node_modules', '.gitbook', 'scripts'}

def get_git_date(file_path, date_type='modified'):
    """Git에서 파일의 날짜 정보 가져오기"""
    try:
        if date_type == 'modified':
            cmd = ['git', 'log', '-1', '--format=%ad', '--date=short', str(file_path)]
        else:  # created
            cmd = ['git', 'log', '--reverse', '--format=%ad', '--date=short', str(file_path)]
            cmd.extend(['|', 'head', '-n', '1'])
        
        result = subprocess.run(cmd, cwd=PROJECT_ROOT, capture_output=True, text=True, shell=True)
        
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
        else:
            # Git 히스토리가 없는 경우 파일 시스템 날짜 사용
            stat = file_path.stat()
            return datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d')
    except Exception as e:
        print(f"Git 날짜 조회 오류 {file_path}: {e}")
        # 파일 시스템 날짜 사용
        stat = file_path.stat()
        return datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d')

def has_frontmatter(content):
    """Frontmatter가 있는지 확인"""
    return content.startswith('---\n')

def parse_frontmatter(content):
    """Frontmatter 파싱"""
    frontmatter_regex = r'^---\n([\s\S]*?)\n---'
    match = re.match(frontmatter_regex, content)
    
    if not match:
        return None, None, 0
    
    frontmatter_text = match.group(1)
    frontmatter = {}
    
    for line in frontmatter_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            frontmatter[key.strip()] = value.strip().strip('"\'')
    
    return frontmatter, match.group(0), len(match.group(0))

def extract_title_from_content(content):
    """문서 내용에서 첫 번째 # 제목 추출"""
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('# '):
            return line[2:].strip()
        elif line.startswith('#'):
            return line[1:].strip()
    return ""

def create_frontmatter(modified_date, created_date=None, title=""):
    """Frontmatter 생성"""
    date = created_date or modified_date
    title_text = title if title else ""
    return f"""---
title: {title_text}
description: ""
created: {date}
modified: {modified_date}
tags: []
---"""

def update_frontmatter(frontmatter, modified_date, title=""):
    """Frontmatter 업데이트"""
    frontmatter['modified'] = modified_date
    
    # title이 비어있고 문서에서 추출한 title이 있으면 업데이트
    if not frontmatter.get('title') and title:
        frontmatter['title'] = title
    
    frontmatter_lines = ['---']
    for key, value in frontmatter.items():
        frontmatter_lines.append(f"{key}: {value}")
    frontmatter_lines.append('---')
    
    return '\n'.join(frontmatter_lines)

def update_markdown_file(file_path):
    """마크다운 파일에 수정일 업데이트"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified_date = get_git_date(file_path, 'modified')
        created_date = get_git_date(file_path, 'created')
        title = extract_title_from_content(content)
        
        new_content = content
        
        if has_frontmatter(content):
            frontmatter, frontmatter_text, content_start = parse_frontmatter(content)
            if frontmatter:
                updated_frontmatter = update_frontmatter(frontmatter, modified_date, title)
                new_content = updated_frontmatter + content[content_start:]
        else:
            # Frontmatter가 없는 경우 추가
            frontmatter = create_frontmatter(modified_date, created_date, title)
            new_content = frontmatter + '\n\n' + content
        
        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Updated: {file_path.relative_to(PROJECT_ROOT)}")
            return True
        
        return False
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")
        return False

def find_all_markdown_files(directory):
    """모든 마크다운 파일 찾기"""
    markdown_files = []
    
    for root, dirs, files in os.walk(directory):
        # 제외할 디렉토리 필터링
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(Path(root) / file)
    
    return markdown_files

def main():
    """메인 함수"""
    print('🔍 GitBook 마크다운 파일 수정일 업데이트 시작...\n')
    
    markdown_files = find_all_markdown_files(PROJECT_ROOT)
    print(f'📄 총 {len(markdown_files)}개의 마크다운 파일을 찾았습니다.\n')
    
    updated_count = 0
    
    for file_path in markdown_files:
        if update_markdown_file(file_path):
            updated_count += 1
    
    print(f'\n✨ 작업 완료! {updated_count}개의 파일이 업데이트되었습니다.')
    
    if updated_count > 0:
        print('\n💡 팁:')
        print('   - 변경사항을 확인하시려면: git diff')
        print('   - 변경사항을 커밋하시려면: git add . && git commit -m "Update modified dates in markdown files"')

if __name__ == '__main__':
    main()
