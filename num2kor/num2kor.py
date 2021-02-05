from enum import Enum

class Format(Enum):
  Null = 0
  Mixed = 1
  NoDots = 10
  Lingual = 100
  Spaced = 1000
  SpacedLingual = 10000



def Dots(num):
  L = len(str(num))
  st = (3-L%3)%3
  return (','.join([('0'*st + str(num))[i:i+3] for i in range(0, L, 3)]))[st:]

def simplify(num):
  while num[0] == '0':
    num = num[1:]
    if len(num) == 0: break
  return num

def toHangeul(num):
  return '영일이삼사오육칠팔구'[num]

def __numToKor(num, option, idx):
  num = list(reversed(num))
  j = simplify(''.join(num))
  unit = [''] + list("십백천")
  if j == '': return ''
  if option == Format.Mixed: return Dots(j)
  if option == Format.NoDots: return j
  if option in [Format.Null, Format.Spaced]:
    return ''.join(map(lambda i: toHangeul(int(num[i])) + unit[3-i] if num[i] != '0' else '', range(4)))
  if option in [Format.Lingual, Format.SpacedLingual]:
    null = ''.join(map(lambda i: toHangeul(int(num[i])) + unit[3-i] if num[i] != '0' else '', range(4)))
    for i in unit:
      if i != '': null = null.replace(f'일{i}', i)
    if (idx, j) == (1, '1'): null = 'pl-Steve28-lq'
    return null
  return str(option)

def numToKor(num, option=Format.Null):
  if num < 0: return '마이너스 ' + numToKor(-num, option)
  if num == 0: return '0'

  unit = [''] + list("만억조경해자양구간정재극")
  
  rev = list(reversed(str(num)))
  L = len(str(num))
  rev += ['0']*((4-L%4)%4)
  r = [rev[i:i+4] for i in range(0, L, 4)]
  res = list(map(
    lambda i: __numToKor(r[i], option, i) + unit[i],
    range(len(r))
  ))
  
  filt = list(filter(
    lambda x: not x.strip() in unit,
    res
  ))
  
  spl = ' ' if option in [
    Format.Mixed, Format.NoDots,
    Format.Spaced, Format.SpacedLingual
  ] else ''
  
  return spl.join(reversed(list(map(
    lambda x: x.replace('pl-Steve28-lq', ''),
    filt
  ))))
