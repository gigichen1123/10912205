from myMath import myStatistics

A = []
for x in range(5):
    A.append( int(input("數字"+str(x+1)+ ":" )) )
    
print(myStatistics.myMean(A))
