# 1. 기본 데이터 준비 (최소 3개 등록 조건 충족)
prompts = [
    {"title": "블로그 글 작성 도우미", "content": "SEO 최적화 블로그 글...", "category": "텍스트 생성", "favorite": False},
    {"title": "제품 썸네일 생성", "content": "매력적인 썸네일...", "category": "이미지 생성", "favorite": True},
    {"title": "뉴스 요약 프롬프트", "content": "오늘자 뉴스 요약...", "category": "자동화", "favorite": False}
]

# 2. 메뉴 보여주기 함수
def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("0. 종료")
    # 나머지 메뉴도 여기에 추가하세요

# 3. 프로그램 실행 뼈대 (무한 반복)
def main():
    while True:
        show_menu()
        choice = input("선택: ")

        if choice == '1':
            print("추가 기능을 실행합니다.")
            # 앞으로 여기에 add_prompt() 같은 함수를 만들어 연결합니다.
        elif choice == '2':
            print("목록 기능을 실행합니다.")
        elif choice == '0':
            print("프로그램을 종료합니다.")
            break # while 반복문을 탈출하여 프로그램 종료
        else:
            print("잘못된 번호입니다. 다시 입력해주세요.")

# 프로그램 시작
main()