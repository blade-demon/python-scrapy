import re

# 泛匹配
# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello.*Demo$', content)
# print(result)
# print(result.group())
# print(result.span())

# 匹配目标
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^Hello\s(\d+)\sWorld.*Demo$', content)
# print(result)
# print(result.group(1))
# print(result.span())


# 贪婪匹配
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*(\d+).*Demo$', content)
# print(result)
# print(result.group(1))
# print(result.span())

# 非贪婪匹配
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*?(\d+).*Demo$', content)
# print(result)
# print(result.group(1))
# print(result.span())

#匹配模式
content = "Hello 1234567 World_This" \
          " is a Regex Demo."
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print(result.group(1))