"""利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam','LISA','barT'],输出：['Adam', 'Lisa', 'Bart']"""


def f(x):
    return x.title()


input_name = ['adam', 'LISA', 'barT']
rename = map(f, input_name)
print(list(rename))
