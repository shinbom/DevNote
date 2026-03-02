#!/usr/bin/env python3
"""
YAML Frontmatter에서 특수문자가 포함된 title만 따옴표로 감싸는 스크립트
"""

import os
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
EXCLUDE_DIRS = {'.git', 'node_modules', '.gitbook', 'scripts'}

def fix_special_chars_in_title(file_path):
    """파일의 title 필드에서 특수문자가 있는 경우 따옴표로 감싸기"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Frontmatter가 있는지 확인
        if not content.startswith('---\n'):
            return False
        
        # Frontmatter 부분 추출
        frontmatter_match = re.match(r'^---\n([\s\S]*?)\n---', content)
        if not frontmatter_match:
            return False
        
        frontmatter_text = frontmatter_match.group(1)
        original_frontmatter = frontmatter_match.group(0)
        
        # title 라인 찾기 및 수정
        lines = frontmatter_text.split('\n')
        modified = False
        new_lines = []
        
        for line in lines:
            if line.startswith('title:'):
                # title 값 추출
                colon_index = line.find(':')
                if colon_index > 0:
                    title_value = line[colon_index + 1:].strip()
                    
                    # 모든 title을 따옴표로 감싸기 (이미 감싸져 있지 않은 경우)
                    if not (title_value.startswith('"') and title_value.endswith('"')):
                        title_value = f'"{title_value}"'
                        line = f'title: {title_value}'
                        modified = True
                
            new_lines.append(line)
        
        if modified:
            # 새로운 Frontmatter 생성
            new_frontmatter = '---\n' + '\n'.join(new_lines) + '\n---'
            new_content = new_frontmatter + content[frontmatter_match.end():]
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Fixed: {file_path.relative_to(PROJECT_ROOT)}")
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Error fixing {file_path}: {e}")
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
    print('🔧 YAML Frontmatter title 특수문자 수정 시작...\n')
    
    markdown_files = find_all_markdown_files(PROJECT_ROOT)
    print(f'📄 총 {len(markdown_files)}개의 마크다운 파일을 검사합니다.\n')
    
    fixed_count = 0
    
    for file_path in markdown_files:
        if fix_special_chars_in_title(file_path):
            fixed_count += 1
    
    print(f'\n✨ 작업 완료! {fixed_count}개의 파일이 수정되었습니다.')
    
    if fixed_count > 0:
        print('\n💡 팁:')
        print('   - 변경사항을 확인하시려면: git diff')
        print('   - 변경사항을 커밋하시려면: git add . && git commit -m "Fix special characters in YAML frontmatter titles"')

if __name__ == '__main__':
    main()
