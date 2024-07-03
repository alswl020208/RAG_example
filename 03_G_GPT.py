from openai import OpenAI

# OpenAI API 키 설정
client = OpenAI(api_key='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')


# GPT-4 모델에 요청 보내기
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "꽁꽁고양이 밈 알려줘"}
    ],
    max_tokens=150,  # 응답에서 생성할 최대 토큰 수
    temperature=0.1  # 텍스트 생성의 창의성 수준
)

# 응답 출력
print(response.choices[0].message.content.strip())

