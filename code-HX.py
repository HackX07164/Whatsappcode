import random
import getpass
import os
############style####################

# Set Colors ######

N = '\033[0m'

W = '\033[1;37m'

B = '\033[1;34m'

R = '\033[1;31m'

G = '\033[1;32m'

Y = '\033[1;33m'

C = '\033[1;36m'

print (R+"""
                       ,ood8888booo,
                    ,oda8a888a888888bo,
                 ,od88888888aa888aa88a8bo,
               ,da8888aaaa88a888aaaa8a8a88b,
              ,oa888aaaa8aa8888aaa8aa8a8a88o,
             ,88888aaaaaa8aa8888a8aa8aa888a88,
             8888a88aaaaaa8a88aa8888888a888888
             888aaaa88aa8aaaa8888; ;8888a88888
             Y888a888a888a8888;'   ;888888a88Y
              Y8a8aa8a888a88'      ,8aaa8888Y
               Y8a8aa8aa8888;     ;8a8aaa88Y
                `Y88aa8888;'      ;8aaa88Y'
        ,,;;;;;;;;'''''''         ;8888Y'
     ,,;                         ,888P
   ,;  ,;,                      ;""
  ;       ;          ,    ,    ,;
 ;  ;,    ;     ,;;;;;   ;,,,  ;
;  ; ;  ,' ;  ,;      ;  ;   ;  ;
; ;  ; ;  ;  '        ; ,'    ;  ;
`;'  ; ;  '; ;,       ; ;      ; ',
     ;  ;,  ;,;       ;  ;,     ;;;
      ;,,;             ;,,;
#####################################""")
print('')
input(Y+"victim number : ")
print(G+"")
def GetPassword(data):
        Max = 6
        password=""
        while len(password) != Max:
                value = random.choice(data)
                password += value
        return password
data ='1234567890'
for i in range(1):
        print(GetPassword(data))
