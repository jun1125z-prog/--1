
import streamlit as st
import random

# -----------------------------
# 1. 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="맞춤형 도서 추천 서비스",
    page_icon="📚",
    layout="wide"
)

# -----------------------------
# 2. 도서 데이터
# -----------------------------
books = [
    {
        "title": "아주 작은 습관의 힘",
        "author": "제임스 클리어",
        "category": "자기계발",
        "description": "작은 습관의 변화가 인생을 어떻게 바꾸는지 알려주는 책입니다.",
        "keywords": ["습관", "성공", "자기관리", "목표"]
    },
    {
        "title": "생각에 관한 생각",
        "author": "대니얼 카너먼",
        "category": "심리학",
        "description": "인간의 사고방식과 의사결정 과정을 이해할 수 있는 책입니다.",
        "keywords": ["심리", "인간", "생각", "행동"]
    },
    {
        "title": "코스모스",
        "author": "칼 세이건",
        "category": "과학",
        "description": "우주와 과학의 신비를 흥미롭게 설명하는 책입니다.",
        "keywords": ["우주", "과학", "천문학", "자연"]
    },
    {
        "title": "돈의 심리학",
        "author": "모건 하우절",
        "category": "경제",
        "description": "돈과 투자에 관한 인간의 심리와 행동을 설명합니다.",
        "keywords": ["경제", "돈", "투자", "금융"]
    },
    {
        "title": "데미안",
        "author": "헤르만 헤세",
        "category": "문학",
        "description": "자아를 찾아가는 한 인간의 성장 과정을 그린 소설입니다.",
        "keywords": ["소설", "성장", "인생", "문학"]
    },
    {
        "title": "혼자 공부하는 파이썬",
        "author": "윤인성",
        "category": "IT",
        "description": "파이썬 프로그래밍을 처음 배우는 사람을 위한 책입니다.",
        "keywords": ["파이썬", "코딩", "프로그래밍", "IT"]
    },
    {
        "title": "미움받을 용기",
        "author": "기시미 이치로, 고가 후미타케",
        "category": "심리학",
        "description": "아들러 심리학을 바탕으로 행복한 삶의 방향을 제시합니다.",
        "keywords": ["심리", "행복", "인간관계", "자기계발"]
    },
    {
        "title": "사피엔스",
        "author": "유발 하라리",
        "category": "역사",
        "description": "인류의 탄생부터 현대 사회까지 인류 역사를 살펴봅니다.",
        "keywords": ["역사", "인류", "사회", "인간"]
    },
    {
        "title": "부의 추월차선",
        "author": "엠제이 드마코",
        "category": "경제",
        "description": "경제적 자유와 부의 형성에 관한 관점을 제시합니다.",
        "keywords": ["경제", "돈", "성공", "재테크"]
    },
    {
        "title": "클린 코드",
        "author": "로버트 C. 마틴",
        "category": "IT",
        "description": "읽기 쉽고 유지보수하기 좋은 코드를 작성하는 방법을 설명합니다.",
        "keywords": ["코딩", "프로그래밍", "IT", "개발"]
    }
]

# -----------------------------
# 3. 도서 추천 함수
# -----------------------------
def recommend_books(topic, count):
    results = []

    topic = topic.strip().lower()

    for book in books:
        score = 0

        # 제목에 주제가 포함되는지 확인
        if topic in book["title"].lower():
            score += 3

        # 분야에 주제가 포함되는지 확인
        if topic in book["category"].lower():
            score += 3

        # 키워드에 주제가 포함되는지 확인
        for keyword in book["keywords"]:
            if topic in keyword.lower() or keyword.lower() in topic:
                score += 2

        # 설명에 주제가 포함되는지 확인
        if topic in book["description"].lower():
            score += 1

        if score > 0:
            results.append((score, book))

    # 관련성 점수가 높은 순서로 정렬
    results.sort(key=lambda x: x[0], reverse=True)

    return [book for score, book in results[:count]]

# -----------------------------
# 4. 웹앱 화면 구성
# -----------------------------
st.title("📚 나만의 맞춤형 도서 추천 서비스")

st.write(
    "관심 있는 주제를 입력하면 "
    "당신의 관심 분야에 맞는 도서를 추천해 드립니다."
)

st.divider()

# 사용자 입력
st.subheader("🔍 어떤 주제의 책을 찾으시나요?")

topic = st.text_input(
    "관심 분야 입력",
    placeholder="예: 심리학, 경제, 파이썬, 우주, 자기계발"
)

count = st.slider(
    "추천받을 도서 개수",
    min_value=1,
    max_value=10,
    value=5
)

# 추천 버튼
if st.button("📖 도서 추천받기", type="primary"):

    if not topic.strip():
        st.warning("관심 있는 주제를 입력해 주세요.")

    else:
        recommendations = recommend_books(topic, count)

        st.divider()
        st.subheader(f"✨ '{topic}' 관련 추천 도서")

        if recommendations:
            for i, book in enumerate(recommendations, 1):

                with st.container(border=True):
                    st.markdown(
                        f"### {i}. {book['title']}"
                    )

                    st.write(f"**저자:** {book['author']}")
                    st.write(f"**분야:** {book['category']}")
                    st.write(f"**책 소개:** {book['description']}")

        else:
            st.info(
                "관련 도서를 찾지 못했습니다. "
                "다른 키워드로 검색해 주세요."
            )

# -----------------------------
# 5. 랜덤 도서 추천
# -----------------------------
st.divider()
st.subheader("🎲 오늘의 랜덤 도서 추천")

if st.button("랜덤 도서 뽑기"):
    random_book = random.choice(books)

    st.success("오늘 추천하는 도서입니다!")

    st.markdown(f"### 📕 {random_book['title']}")
    st.write(f"**저자:** {random_book['author']}")
    st.write(f"**분야:** {random_book['category']}")
    st.write(random_book["description"])

# -----------------------------
# 6. 하단 안내
# -----------------------------
st.divider()

st.caption(
    "📚 나만의 맞춤형 도서 추천 서비스 | "
    "Python + Streamlit"
)
