points=[[1,2], [0,4], [6,3,2], [1,3,1]]

sorted_points1=sorted(points)
print(sorted_points1)

sorted_points2=sorted(points, key=lambda x: (x[1]))
print(sorted_points2)

sorted_points3=sorted(points, key=lambda x: (x[1], x[0]))
print(sorted_points3)