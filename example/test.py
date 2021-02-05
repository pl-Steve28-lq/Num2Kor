from num2kor import *

test = {
  (11_235_973_450, Format.Mixed): '112억 3,597만 3,450',
  (1_123_492_832_717, Format.NoDots): '1조 1234억 9283만 2717',
  (235_417_898_967_198, Format.Null): '이백삼십오조사천일백칠십팔억구천팔백구십육만칠천일백구십팔',
  (2_459_873_487_316, Format.Spaced): '이조 사천오백구십팔억 칠천삼백사십팔만 칠천삼백일십육',
  (1_231_123_111_121, Format.Lingual): '일조이천삼백십일억이천삼백십일만천백이십일',
  (12_341_234_573_721, Format.SpacedLingual): '십이조 삼천사백십이억 삼천사백오십칠만 삼천칠백이십일'
}

for num, form in test:
  res = test[(num, form)]
  res2 = numToKor(num, form)
  assert res == res2
print("Assertion Complete!")
