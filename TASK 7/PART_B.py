import cv2 as cv2
import numpy as np

image = cv2.imread('maze.jpg')                                      #USING IMAGE PROCESSING FOR NOISE REDUCTION


dst = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)



height, width, channels = dst.shape


iter = 1
b=[]                                                        #STORING PIXEL VALUES IN LIST b (ROW-MAJOR)
for i in range(int(width / 10), width, int(width / 5)):     # 1 = YELLOW BLOCK
    a=[]                                                    # 0 = BLUE BLOCK
    for j in range(int(height / 10), height, int(height / 5)):
        
        
        pixel_value = image[int(i), int(j)]
        if pixel_value[0] > pixel_value[1]:
            a.append(0)
        else :
            a.append(1)

    b.append(a)




grid = b                                                    #PATH PLANNING FINDING ALL POSSIBLE ROUTES
goal = (4, 4)

def fun(i, j, a, goal, path, c):
    c.append((i, j))  # Append the current position to the path
    if (i, j) == goal:
        path.append(c)  # Append the path to the result
    else:
        if i < 4 and a[i + 1][j] == 1:
            fun(i + 1, j, a, goal, path, c.copy())  # Pass a copy of the current path
        if j < 4 and a[i][j + 1] == 1:
            fun(i, j + 1, a, goal, path, c.copy())  # Pass a copy of the current path

n = []
k = [(0, 0)]
fun(0, 0, grid, goal, n, k)


length = []                                                 #FINDING THE SHORTEST ROUTE
for i in n:
    length.append(len(i))
min=25
for l in length:
    if min > l:
        min = l
index = length.index(min)
short_path = n[index]



temp_img = cv2.imread('maze.jpg')

for i in short_path: 
    temp = (i[0]+1, i[1]+1)
    temp_img = cv2.putText ( temp_img, str(temp), (5+50*i[1],25+50*i[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0) ,2 )

cv2.imshow("eart",temp_img)
cv2.waitKey(0)