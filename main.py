# ==========================================
# 1. 기본 프롬프트 데이터 (최소 3개 등록)
# ==========================================
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요. 서론, 본론, 결론 구조를 갖추고, 매력적인 제목 3개를 제안해주세요.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "제품 썸네일 생성",
        "content": "미니멀하고 세련된 스타일의 제품 대표 썸네일 이미지를 생성해주세요. 흰색 배경에 부드러운 자연광 그림자가 드리워진 고화질 3D 렌더링 스타일입니다.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": "당신은 포춘 500대 기업을 자문하는 클라우드 & AI 전문 IT 컨설턴트입니다. 비즈니스 관점에서 최신 기술 트렌드와 비용 최적화 방안을 간결하게 제시해주세요.",
        "category": "페르소나",
        "favorite": False
    }
]

# 미리 정의된 카테고리 목록
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]


# ==========================================
# 2. 프롬프트 추가 기능
# ==========================================
def add_prompt():
    print("\n=== 프롬프트 추가 ===")
    
    while True:
        title = input("제목: ").strip()
        if title:
            break
        print("⚠️ 제목은 비어있을 수 없습니다. 다시 입력해주세요.")

    while True:
        content = input("내용: ").strip()
        if content:
            break
        print("⚠️ 내용은 비어있을 수 없습니다. 다시 입력해주세요.")

    print("\n카테고리 선택:")
    for idx, category in enumerate(CATEGORIES, start=1):
        print(f"{idx}) {category}")

    while True:
        choice = input("선택 (번호 입력): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            selected_category = CATEGORIES[int(choice) - 1]
            break
        print("⚠️ 목록에 있는 번호를 입력해주세요.")

    new_prompt = {
        "title": title,
        "content": content,
        "category": selected_category,
        "favorite": False
    }

    prompts.append(new_prompt)
    print("\n🎉 프롬프트가 성공적으로 추가되었습니다!")


# ==========================================
# 3. 프롬프트 목록 보기 기능 (신규 추가!)
# ==========================================
def show_list():
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for idx, p in enumerate(prompts, start=1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{idx}. [{p['category']}] {p['title']}{star}")

    print(f"\n총 {len(prompts)}개의 프롬프트")


# ==========================================
# 4. 메인 메뉴 화면 출력 함수
# ==========================================
def show_menu():
    print("\n" + "=" * 25)
    print("=== 나만의 프롬프트 관리 ===")
    print("=" * 25)
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")
    print("=" * 25)


# ==========================================
# 5. 프로그램 실행 루프 (진입점)
# ==========================================
def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "0":
            print("\n프로그램을 종료합니다. 이용해 주셔서 감사합니다!")
            break
        elif choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()  # 목록 조회 연결!
        elif choice == "3":
            print("\n[안내] 카테고리별 조회 기능은 다음 단계에서 구현됩니다.")
        elif choice == "4":
            print("\n[안내] 프롬프트 검색 기능은 다음 단계에서 구현됩니다.")
        elif choice == "5":
            print("\n[안내] 프롬프트 상세 보기 기능은 다음 단계에서 구현됩니다.")
        elif choice == "6":
            print("\n[안내] 즐겨찾기 관리 기능은 다음 단계에서 구현됩니다.")
        elif choice == "7":
            print("\n[안내] 즐겨찾기 목록 기능은 다음 단계에서 구현됩니다.")
        else:
            print("\n⚠️ 올바른 번호를 입력해주세요 (0~7).")


if __name__ == "__main__":
    main()