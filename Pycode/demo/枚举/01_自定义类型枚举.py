# 自定义类型枚举
from enum import Enum, unique

# @unique 装饰器可以帮助我们检查保证没有重复值
@unique
class Month(Enum):
    Jan = 'January'
    Feb = 'February'
    Mar = 'March'
    Apr = 'April'
    May = 'May'
    Jun = 'June'
    Jul = 'July'
    Aug = 'August'
    Sep = 'September '
    Oct = 'October'
    Nov = 'November'
    Dec = 'December'


if __name__ == '__main__':
    print(Month.Jan, '----------',
          Month.Jan.name, '----------', Month.Jan.value)
    for name, member in Month.__members__.items():
        print(name, '----------', member, '----------', member.value)
print(Month)

# 遍历month
for m in Month:
    print(m)

a = 'January'
print(Month(a))


# 个人理解：Month.Jan视为字典,即Month.Jan = {"Jan":'January'}。Month.Jan.name取key值。
       