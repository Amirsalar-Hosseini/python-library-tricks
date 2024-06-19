import translators as ts
import time
txt = "hello my friend!!"
res = ts.google(txt, to_language='fa')
print(res)
holder = input("press enter to exit...")
time.sleep(10)