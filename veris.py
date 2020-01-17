def polygonArea(numPoints, X=[],Y=[]):
    j = numPoints - 1
    area = 0
    for i in range(numPoints):
        area += (X[j]+X[i]) * (Y[j]-Y[i]) 
        j = i

    return area/2

for k in range(int(input())):
    walk = [x for x in input().split(' ')]
    direction = [ele[0] for ele in walk]
    length = [int(ele[1:len(ele)]) for ele in walk]
    
    n = len(direction)
    X = [None for _ in range(n+1)]
    Y = [None for _ in range(n+1)]
    X[0], Y[0] = 0, 0
    
    for i in range(n):
        if direction[i]=='E' :
            X[i+1] = X[i] + length[i]
            Y[i+1] = Y[i]
        
        elif direction[i]=='W' :
            X[i+1] = X[i] - length[i]
            Y[i+1] = Y[i]
        
        elif direction[i]=='N' :
            X[i+1] = X[i]
            Y[i+1] = Y[i]+ length[i]
        
        elif direction[i]=='S' :
            X[i+1] = X[i]
            Y[i+1] = Y[i]- length[i]
    
    print( "case #",k+1, "=", int(abs(polygonArea(n,X,Y))) )
			
