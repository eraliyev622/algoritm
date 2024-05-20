def double_char(matn):
    s=len(matn)
    m=""
    for i in range (s):
        m=matn[i]*2+m
    print(m)  
double_char("the")    
def count_hi(s):
   if s.count("cat") and s.count ("dog"):
      print(True)
   else :
      print(False)
