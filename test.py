__author__ = "Shobhit Kundu"
__copyright__ = "Copyright (C) 2020 Shobhit Kundu"
__license__ = "Public Demo"
__version__ = "1.0"

import Spk_Listen as ass
tmp = ass.AudioExchange()
tmp.speak('Hello friends Chai peelo')
cout = ''
i = 0
while True:
    print("~", i)
    statement = tmp.listen().lower()
    print(statement)
    if "danny" in statement.split() or "dani" in statement.split() or "dhani" in statement.split():
        tmp.speak("Listening")
        break
    i += 1
