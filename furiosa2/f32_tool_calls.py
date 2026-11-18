from kingkeras import get_llm
from langchain_core.tools import tool

#1. 도구 정의
@tool
def add(aaa: int, bbb: int) -> int: # 타입 힌트
    """두 정수를 더합니다.""" # 블럭 주석 
    return aaa + bbb

# print(add.name)     # 함수명
# print(add.description)  # add함수의 주석
# print(add.args)

################ llm 생성
llm = get_llm(max_tokens=200)

# 3. 도구 등록
llm_with_tools = llm.bind_tools([add])

# 4. 질문
response = llm_with_tools.invoke(
    "21과 32을 add로 더해줘."
)

#5. 결과확인
for call in response.tool_calls:
    result = add.invoke(call['args'])
    print("계산 결과 :", result)

# tool 이름 :  add
# 매개 변수 : {'aaa': 237341, 'bbb': 31321}
# 호출 ID :  call-fcd9a4bea7d14033bf6c07fcbebddda1