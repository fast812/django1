#!/usr/bin/env bash
# 오류 나면 즉시 멈춤
set -o errexit 

# 1. 라이브러리 설치
pip install -r requirements.txt

# 2. 정적 파일 모으기
python manage.py collectstatic --no-input

# 3. 데이터베이스 적용 (마이그레이션)
python manage.py migrate
