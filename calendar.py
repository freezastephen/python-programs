week=["sun","mon","tue","wed","thur","fri","sat"]
for day in range(len(week)):
    print("%8s" % week[day]),
print 
month=10
days=31
start=2
pos=1
print 
while(pos<start):
  print("%8s" % " "),
  pos=pos+1
for i in range(1,32):
    if (pos % 7 >=1 and pos %7 <= 6):
        print ("% 8d" % i),
        pos=pos+1
    elif pos %7 == 0:
        print ("%8d" %i)
        pos=pos+1