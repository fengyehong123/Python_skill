d1 = {'name': 'Python', 'age': 27}
d2 = {'version': 3.6, 'platform': 'Mac'}
d3 = {'size': '59MB'}

# 方法一: 最不推荐的方式
a = {}
for key, value in d1.items():
    a[key] = value
for key, value in d2.items():
    a[key] = value
for key, value in d3.items():
    a[key] = value
print(a)  # {'name': 'Python', 'age': 27, 'version': 3.6, 'platform': 'Mac', 'size': '59MB'}

# 方法二: Python2和Python3中通用的方式,通过update()的方式
d1.update(d2)
d1.update(d3)
print(d1)  # {'name': 'Python', 'age': 27, 'version': 3.6, 'platform': 'Mac', 'size': '59MB'}

# 方法三: Python3.5版本之后才支持
d = {**d1, **d2, **d3}
print(d)  # {'name': 'Python', 'age': 27, 'version': 3.6, 'platform': 'Mac', 'size': '59MB'}

# 方法四: 字典解析式,一般不使用,麻烦
d1 = {'name': 'Python', 'age': 27}
d2 = {'version': 3.6, 'platform': 'Mac'}
d3 = {'size': '59MB'}

f = [a for a in [d1, d2, d3]]
print(f)  # [{'name': 'Python', 'age': 27}, {'version': 3.6, 'platform': 'Mac'}, {'size': '59MB'}]

g = {k: v for d in [d1, d2, d3] for k, v in d.items()}
print(g)  # {'name': 'Python', 'age': 27, 'version': 3.6, 'platform': 'Mac', 'size': '59MB'}


