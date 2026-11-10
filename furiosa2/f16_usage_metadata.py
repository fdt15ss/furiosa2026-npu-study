from kingkeras import get_llm

llm = get_llm(max_tokens=500)

response = llm.invoke("NPU란 무엇인가")

print(response.content)
print("============================")
print(response.usage_metadata)

# {'input_tokens': 14, 'output_tokens': 500, 'total_tokens': 514,
#  'input_token_details': {'audio': 0, 'cache_read': 0},
#  'output_token_details': {'audio': 0, 'reasoning': 0}}