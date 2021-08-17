# Num2Kor 
Convert Number into Korean Words! <br>
Inspired from [huskyhoochu/num-to-korean](https://github.com/huskyhoochu/num-to-korean)

## Download
`pip install num2kor`

## Features
```Python
def numToKor(num: int, option: Format = Format.Null) -> str

class Format(Enum):
  Null, Spaced,
  Mixed, NoDots,
  Lingual, SpacedLingual
```

## Example
```Python
from num2kor import *

NUMBER = 12_341_234_573_721

numToKor(NUMBER)    # '일십이조삼천사백일십이억삼천사백오십칠만삼천칠백이십일'

numToKor(NUMBER,    # '12조 3,412억 3,457만 3,721'
Format.Mixed)

numToKor(NUMBER,    # '12조 3412억 3457만 3721'
Format.NoDots)

numToKor(NUMBER,    # '일십이조 삼천사백일십이억 삼천사백오십칠만 삼천칠백이십일'
Format.Spaced)

numToKor(NUMBER,    # '십이조삼천사백십이억삼천사백오십칠만삼천칠백이십일'
Format.Lingual)

numToKor(NUMBER,    # '십이조 삼천사백십이억 삼천사백오십칠만 삼천칠백이십일'
Format.SpacedLingual)
```
