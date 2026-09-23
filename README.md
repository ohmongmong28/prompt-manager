Markdown
#📝 나만의 프롬프트 관리 프로그램 (Prompt Manager)

파편화되어 흩어져 있는 GenAI 지시문(프롬프트)을 체계적으로 수집, 분류, 검색 및 즐겨찾기 관리할 수 있는 파이썬 콘솔 기반 데이터 관리 애플리케이션입니다.

* **GitHub 저장소 URL**: `https://github.com/ohmongmong28/prompt-manager`
* **개발 언어**: Python 3.10+
* **버전 관리**: Git / GitHub

---

## 1. ⚙️ 개발 및 실행 환경 점검

### 요구 환경 및 버전 점검
프로그램 실행 전 터미널에서 아래 명령어로 환경을 점검합니다.
```bash
# 파이썬 버전 확인 (Python 3.10 이상 필수)
python --version

# Git 설치 버전 확인
git --version

# Git 전역 사용자 설정 정보 확인 (user.name, user.email, init.defaultbranch=main)
git config --list
Git 초기 설정 명령어Bashgit config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
git config --global init.defaultBranch main
샘플 저장소 Clone 검증 로그Git의 원격 저장소 복제 기능을 검증하기 위해 오픈소스 샘플 저장소를 내려받아 디렉터리 구조를 확인하였습니다.Bash$ git clone [https://github.com/octocat/Spoon-Knife.git](https://github.com/octocat/Spoon-Knife.git)
Cloning into 'Spoon-Knife'...
remote: Enumerating objects: 16, done.
remote: Total 16 (delta 0), reused 0 (delta 0), pack-reused 16
Receiving objects: 100% (16/16), done.

$ ls Spoon-Knife
README.md  index.html  styles.css
2. 🚀 실행 방법 및 사용자 인터페이스실행 명령어Bashpython main.py
메인 메뉴 구성 및 허용 입력 범위프로그램 실행 시 무한 루프(while True)를 통해 메뉴를 유지하며, 사용자는 0 ~ 7 범위의 정수만 입력할 수 있습니다. 허용 범위 외 문자나 숫자가 입력되면 즉시 안내 메시지를 출력하고 메뉴로 복귀합니다.Plaintext=========================
=== 나만의 프롬프트 관리 ===
=========================
1. 프롬프트 추가
2. 프롬프트 목록
3. 카테고리별 조회
4. 프롬프트 검색
5. 프롬프트 상세 보기
6. 즐겨찾기 관리
7. 즐겨찾기 목록
0. 종료
=========================
선택 (0~7): 
메인 루프 제어 설계 의도while True 반복문 채택 이유: 콘솔 프로그램 특성상 1회 실행 후 프로세스가 꺼지는 것을 방지하고, 사용자가 명시적으로 작업을 끝내기 전까지 상태(추가된 프롬프트, 즐겨찾기 토글)를 메모리에 유지하기 위해 채택했습니다.종료 조건: 사용자가 메뉴에서 0을 입력하면 break 문이 호출되어 루프를 탈출하고 정상 종료됩니다.3. 🏗️ 아키텍처 및 함수 분리 설계 근거단일 함수에 코드가 집중되는 스파게티 코드를 방지하고, 유지보수성과 가독성을 극대화하기 위해 단일 책임 원칙(SRP)에 기반하여 기능별로 함수를 분리했습니다.함수명분리 목적 및 역할show_menu()UI 출력 전담: 메인 메뉴 화면을 콘솔에 렌더링add_prompt()입력 및 검증: 새 프롬프트 입력값 유효성 검사 후 데이터베이스(리스트)에 추가show_list()전체 조회: 현재 저장된 모든 프롬프트의 기본 메타데이터(카테고리, 제목, 즐겨찾기) 나열show_by_category()조건 필터링: 특정 카테고리 인덱스를 선택받아 일치하는 항목만 추출하여 출력search_prompt()부분 문자열 탐색: 제목 및 내용에 검색 키워드가 포함된 프롬프트 탐색show_detail()단건 상세 조회: 특정 번호 프롬프트의 본문 및 상세 스펙 서식화 출력manage_favorite()상태 변경: 지정된 프롬프트의 favorite 불리언 값을 토글(True ↔ False)show_favorites()조건 필터링: favorite == True 상태인 프롬프트만 모아서 출력main()진입점(Controller): 사용자 입력을 받아 각 기능 함수로 라우팅하는 무한 루프 제어4. 💾 데이터 구조 설계 및 선택 근거데이터 모델링: List[Dict]프롬프트 목록은 딕셔너리를 원소로 가지는 리스트(prompts = [{...}, {...}]) 구조를 채택했습니다.Pythonprompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다...",
        "category": "텍스트 생성",
        "favorite": True
    }
]
필드 접근 방식 예시제목 확인: prompts[0]["title"]즐겨찾기 여부 확인: prompts[0]["favorite"]새 프롬프트 추가: prompts.append(new_prompt)List와 Dict 선택 근거 및 장단점 비교자료형프로젝트 내 역할장점단점 및 극복 방안리스트 (List)프롬프트 카드들을 순서대로 저장하는 컨테이너• 등록 순서 보장• 인덱스(0, 1, 2...)를 통한 고유 번호 매핑 용이• append()로 빠른 추가 가능• 특정 키 탐색 시 $O(N)$ 시간 소요→ 소규모 콘솔 데이터 특성상 성능 저하 미미함딕셔너리 (Dict)1개 프롬프트의 개별 속성(제목, 내용 등)을 표현• Key-Value 구조로 직관적인 필드명 접근• 추후 필드 확장(작성일자, 태그 등)이 매우 유연함• Key 중복 불가→ 고정된 스키마 키(title, content 등)를 사용하여 안정성 확보5. 🛡️ 입력 검증, 충돌 처리 및 검색 정책1) 입력 검증 정책 (Validation)공백 및 빈값 처리: input().strip()을 적용하여 사용자가 실수로 공백 문자만 입력하거나 엔터만 친 경우(if not value:) 경고 메시지를 띄우고 다시 입력을 유도합니다.숫자 및 범위 검증: choice.isdigit()로 문자열 입력 여부를 1차 검증하고, 1 <= int(choice) <= len(...) 범위를 벗어날 경우 예외 메시지를 출력합니다.입력 길이 및 문자 제한: 현재 콘솔 환경에서는 특수문자 및 다국어 입력을 허용하며, 1자 이상의 유효 문자를 필수로 요구합니다.2) 중복 제목 충돌 처리 규칙 (Conflict Policy)동일한 제목의 프롬프트가 등록될 경우 식별 혼란이 발생할 수 있습니다.설계 규칙: add_prompt() 실행 시 기존 prompts 리스트에 동일한 title이 존재하는지 사전 점검(any(p["title"] == title for p in prompts))합니다.처리 방침: 중복이 발견될 경우 등록을 즉시 거부하거나, 사용자 동의를 받아 제목 뒤에 (복사본) 또는 순번 넘버링(블로그 글 작성 도우미 (2))을 자동으로 부여하는 규칙을 적용합니다.3) 검색 알고리즘 및 매칭 정책구현 방식: 파이썬의 in 연산자를 활용한 부분 문자열 매칭(Sub-string matching)을 수행합니다.Pythonresults = [p for p in prompts if keyword in p["title"] or keyword in p["content"]]
대소문자 매칭 정책: 현재는 완전 일치 방식을 사용하나, 사용자 편의를 위해 keyword.lower() in p["title"].lower() 형태로 대소문자를 구분하지 않는(Case-insensitive) 검색 정책으로 확장이 권장됩니다.6. 📂 카테고리 관리 및 코드 확장 가이드지원 카테고리 정의텍스트 생성: 블로그, 보고서, 이메일 등 텍스트 결과물 생성 지시문이미지 생성: Midjourney, DALL-E 등 프롬프트 및 비주얼 키워드영상 생성: 영상 콘티, 숏폼 스크립트 작성용 프롬프트페르소나: 특정 전문가 역할을 부여하는 페르소나 설계 프롬프트자동화: 업무 프로세스 자동화 및 파이프라인 프롬프트기타: 범용 및 기타 자유 형식 지시문카테고리 변경 시 코드 수정 위치카테고리 목록은 main.py 파일의 상단 전역 상수 CATEGORIES에 중앙 집중식으로 관리됩니다.Python# main.py 파일 상단 (약 25번째 라인)
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]
카테고리 추가/삭제: 위 리스트에 문자열을 추가하거나 삭제하면 add_prompt(), show_by_category() 메뉴에 동적으로 즉시 반영됩니다.주의 사항: 기존에 등록된 데이터의 category 값과 불일치가 발생하지 않도록 기본 등록 데이터(prompts)의 카테고리 값도 함께 점검해야 합니다.7. 💾 데이터 영속화(Persistence) 설계 방안현재 프로그램은 메모리(RAM) 기반으로 동작하므로 프로그램 종료 시 데이터가 초기화됩니다. 이를 파일로 영구 보관하기 위한 설계 방안은 다음과 같습니다.포맷 선정: JSON (JavaScript Object Notation)선정 이유: 파이썬의 List[Dict] 구조와 JSON 포맷은 1:1로 직접 매핑(직렬화/역직렬화)되며, 파이썬 내장 라이브러리 json을 통해 추가 패키지 설치 없이 구현 가능합니다. (CSV는 중복 쉼표 및 개행문자가 포함된 긴 프롬프트 본문을 다루기에 부적합함)영속화 구현 예시 코드:Pythonimport json

# 저장하기 (프로그램 종료 시 호출)
def save_to_file(prompts, filepath="prompts.json"):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=2)

# 불러오기 (프로그램 시작 시 호출)
def load_from_file(filepath="prompts.json"):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
8. 🌿 Git 형상 관리 및 브랜치 전략1) 커밋 정책 (Commit Convention)기능 단위로 커밋을 세분화하여 변경 의도를 명확히 파악할 수 있도록 작성했습니다.구분커밋 메시지 예시적용 내용docsdocs: 프로젝트 초기화 및 README 작성저장소 설정 및 초기 문서화featfeat: 기본 데이터 및 메인 메뉴 구조 생성메뉴 루프 및 기본 프롬프트 3개 등록featfeat: 프롬프트 추가 기능 구현add_prompt() 함수 및 유효성 검사featfeat: 프롬프트 목록 조회 기능 구현show_list() 기능 브랜치 작업featfeat: 카테고리별 프롬프트 조회 기능 구현카테고리 필터링 기능 추가featfeat: 프롬프트 검색 기능 구현키워드 검색 로직 구현featfeat: 프롬프트 상세 보기 기능 구현본문 서식화 출력 구현featfeat: 즐겨찾기 관리 및 목록 조회 기능 구현즐겨찾기 토글 및 전용 목록 기능 추가refactorrefactor: 메뉴 복귀 전 대기 기능 추가 및 UI 개선인터페이스 개선 및 git pull 동기화docsdocs: 프로젝트 설계 및 기능 문서 최종 보완README 아키텍처 및 상세 가이드 완성2) 브랜치 전략 및 병합 (Branch & Merge)main 브랜치의 안정성을 유지하기 위해 신규 기능은 별도의 피처 브랜치(feature/...)에서 개발 후 병합하는 전략을 취했습니다.브랜치 분리 기준: 독립적인 1개 기능 단위 (예: 프롬프트 목록 조회 기능)병합 시점: 해당 기능의 단위 테스트 및 예외 처리가 정상 동작함을 검증한 시점Bash# 1. 기능 개발을 위한 브랜치 생성 및 전환
git checkout -b feature/prompt-list

# 2. 기능 구현 후 브랜치 커밋
git add main.py
git commit -m "feat: 프롬프트 목록 조회 기능 구현"

# 3. main 브랜치 복귀 및 병합
git checkout main
git merge feature/prompt-list

# 4. 원격 저장소 푸시
git push origin main
3) 병합 충돌(Merge Conflict) 해결 절차여러 작업자가 동일한 코드 영역을 동시에 수정하여 병합 충돌이 발생할 경우 다음 절차를 따릅니다.충돌 원인 확인: Git 터미널에서 CONFLICT (content): Merge conflict in main.py 경고 확인코드 수정: 충돌 파일(main.py)을 열어 Git 충돌 마커(<<<<<<<, =======, >>>>>>>)를 확인하고 올바른 코드를 수동 병합검증 및 커밋: 문법 오류 및 프로그램 실행 테스트를 거친 후 git add main.py 및 git commit을 수행하여 병합 완료9. 📸 프로그램 실행 예시 로그Plaintext=== 프롬프트 목록 ===
1. [텍스트 생성] 블로그 글 작성 도우미 ⭐
2. [이미지 생성] 제품 썸네일 생성
3. [페르소나] IT 컨설턴트 페르소나

총 3개의 프롬프트

=== 프롬프트 상세 보기 ===
번호 입력: 1

────────────────────────────────────────
제목: 블로그 글 작성 도우미
카테고리: 텍스트 생성
즐겨찾기: ⭐
────────────────────────────────────────
내용:
당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요. 서론, 본론, 결론 구조를 갖추고, 매력적인 제목 3개를 제안해주세요.
────────────────────────────────────────
