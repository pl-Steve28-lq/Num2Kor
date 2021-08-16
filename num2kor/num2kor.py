from enum import Enum

class Format(Enum):
  Null = 0
  Mixed = 1
  NoDots = 10
  Lingual = 100
  Spaced = 1000
  SpacedLingual = 10000

def toHangeul(num):
  return '영일이삼사오육칠팔구'[num]
  
def __numToKor(num, option):
  unit = list("천백십") + ['']
  if option == Format.NoDots: return str(num)
  if option == Format.Mixed: return f'{num:,}'
  linflag = option in (Format.Null, Format.Spaced)
  a, b = num//1000, num//100 %10
  c, d = num//10 %10, num%10
  def format(x):
    i, t = x
    u = unit[i]
    if t == 0: return ''
    if t == 1: return f'{"일"*(linflag or i == 3)}{u}'
    return f'{toHangeul(t)}{u}' 
  return ''.join(map(
    format,
    enumerate((a, b, c, d))
  ))

def numToKor(num, option=Format.Null):
  unit = [''] + list("만억조경해자양구간정재극")
  idx = 0
  res = []
  spaced = option not in (Format.Null, Format.Lingual)
  while num:
    num, val = num//10000, num%10000
    res.append(__numToKor(val, option) + unit[idx])
    idx += 1
  return (' '*spaced).join(reversed(res))