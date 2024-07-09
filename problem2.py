c_points= [9,7,7,9,7,7,9]
k=7
l,r=0,len(c_points)-k
total = sum(c_points[r:])
res = total

while r < len(c_points):
    total +=(c_points[1]-c_points[r])
    res = max(res,total)
    l+=1
    r+=1
print(res)