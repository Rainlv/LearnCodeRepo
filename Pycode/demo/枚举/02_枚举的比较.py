# Enum 类的枚举是不支持大小运算符的比较的。
# 使用 IntEnum 类进行枚举，就支持比较功能。


from enum import Enum


class User(Enum):
    Twowater = 98
    Liangdianshui = 30
    Tom = 12


Twowater = User.Twowater
Liangdianshui = User.Liangdianshui

print(Twowater == Liangdianshui, Twowater == User.Twowater)
print(Twowater is Liangdianshui, Twowater is User.Twowater)

try:
    print('\n'.join('  ' + s.name for s in sorted(User)))
except TypeError as err:
    print(' Error : {}'.format(err))

print("-" * 50 )

import enum

class User1(enum.IntEnum):
    Twowater = 98
    Liangdianshui = 30
    Tom = 12


try:
    print('\n'.join(s.name for s in sorted(User1)))
except TypeError as err:
    print(' Error : {}'.format(err))