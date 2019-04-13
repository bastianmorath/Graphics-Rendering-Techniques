'''
 This script generates the vertices, materials and faces for Assignment 3 of 'Graphics Rendering Techniques'. 
 It generates a cube with a chequed pattern and a light-block in the middle
'''

text_file = open("new_model.txt", "w")

k = 10 # Number of faces per width. Min 6!
l = 0.5


# VERTICES
text_file.write(str(5*(k+1)*(k+1) +8) + "\n")

# Face left
for z in range(-int(k/2), int(k/2) + 1):
    for x in range(-int(k/2), int(k/2)+ 1):
        text_file.write(str(x) + " " + str(-int(k/2)) + " " + str(z) + "\n")

# Face back

for z in range(-int(k/2), int(k/2)+ 1):
    for y in range(-int(k/2), int(k/2)+ 1):
        text_file.write(str(-int(k/2)) + " " + str(y) + " " + str(z) + "\n")

# Face right

for z in range(-int(k/2), int(k/2)+ 1):
    for x in range(-int(k/2), int(k/2)+ 1):
        text_file.write(str(x) + " " + str(int(k/2)) + " " + str(z) + "\n")

# Face bottom

for x in range(-int(k/2), int(k/2)+ 1):
    for y in range(-int(k/2), int(k/2)+ 1):
        text_file.write(str(x) + " " + str(y) + " " + str(-int(k/2)) + "\n")

# Face top

for z in range(-int(k/2), int(k/2)+ 1):
    for y in range(-int(k/2), int(k/2)+ 1):
        text_file.write(str(int(k/2))+ " " + str(y) + " " + str(z) + "\n")

# Light cube in middle

text_file.write(str(l) + " " + str(-l) + " " + str(-l) + "\n")
text_file.write(str(l) + " " + str(l) + " " + str(-l) + "\n")
text_file.write(str(l) + " " + str(l) + " " + str(l) + "\n")
text_file.write(str(l) + " " + str(-l) + " " + str(l) + "\n")
text_file.write(str(-l) + " " + str(-l) + " " + str(-l) + "\n")
text_file.write(str(-l) + " " + str(l) + " " + str(-l) + "\n")
text_file.write(str(-l) + " " + str(l) + " " + str(l) + "\n")
text_file.write(str(-l) + " " + str(-l) + " " + str(l) + "\n")

# MATERIALS

text_file.write(str(6) + "\n")
# light
text_file.write("0.78 0.78 0.78 \n")
text_file.write("60.0 60.0 60.0 \n")
# white
text_file.write("0.75 0.75 0.75 \n")
text_file.write("0.0 0.0 0.0 \n")
 # black
text_file.write("0.0 0.0 0.0 \n")
text_file.write("0.0 0.0 0.0 \n")
 # red
text_file.write("0.7 0.0 0.0 \n")
text_file.write("0.0 0.0 0.0 \n")
# blue
text_file.write("0.0 0.0 0.7 \n")
text_file.write("0.0 0.0 0.0 \n")
# green
text_file.write("0.0 0.7 0.0 \n")
text_file.write("0.0 0.0 0.0 \n")


# SURFACES
text_file.write(str(5*k*k + 6) + "\n")


num = 0
# Face bottom

for i in range(0, k):
    for j in range(0, k):
        if ((j % 2 == 0) and (i % 2 ==1)) or ((j % 2 == 1) and (i % 2 ==0)): # Material
            text_file.write(str(1) + "\n")
        else:
            text_file.write(str(2)+ "\n")
        text_file.write(str(1)+ "\n")
        text_file.write(str(i*(k+1) +j + num +1) + " " + str(i*(k+1) +j + num) 
        +  " " + str((i+1)*(k+1) +j+ num ) + " " + str((i+1)*(k+1) +j+ num +1 ) + "\n")

num += (k+1)*(k+1) 

# Face left

for i in range(0, k):
    for j in range(0, k):
        if ((j % 2 == 0) and (i % 2 ==1)) or ((j % 2 == 1) and (i % 2 ==0)): # Material
            text_file.write(str(1) + "\n")
        else:
            text_file.write(str(2)+ "\n")

        text_file.write(str(1)+ "\n")
        text_file.write(str(i*(k+1) +j +num) + " " + str(i*(k+1) +j + 1+ num) 
        +  " " + str((i+1)*(k+1) +j+ num +1) + " " + str((i+1)*(k+1) +j+ num ) + "\n")

num += (k+1)*(k+1) 

# Face top

for i in range(0, k):
    for j in range(0, k):
        if ((j % 2 == 0) and (i % 2 ==1)) or ((j % 2 == 1) and (i % 2 ==0)): # Material
            text_file.write(str(1) + "\n")
        else:
            text_file.write(str(2)+ "\n")

        text_file.write(str(1)+ "\n")
        text_file.write(str(i*(k+1) +j + num) + " " + str(i*(k+1) +j + 1+ num) 
        +  " " + str((i+1)*(k+1) +j+ num +1) + " " + str((i+1)*(k+1) +j+ num ) + "\n")

num += (k+1)*(k+1) 

#face back
for i in range(0, k):
    for j in range(0, k):
        if ((j % 2 == 0) and (i % 2 ==1)) or ((j % 2 == 1) and (i % 2 ==0)): # Material
            text_file.write(str(1) + "\n")
        else:
            text_file.write(str(2)+ "\n")

        text_file.write(str(1)+ "\n")
        text_file.write(str(i*(k+1) +j +1 + num) + " " + str(i*(k+1) +j + num) 
        +  " " + str((i+1)*(k+1) +j+ num ) + " " + str((i+1)*(k+1) +j+ 1 +num ) + "\n")

num += (k+1)*(k+1) 
#face right
for i in range(0, k):
    for j in range(0, k):
        if ((j % 2 == 0) and (i % 2 ==1)) or ((j % 2 == 1) and (i % 2 ==0)): # Material
            text_file.write(str(1) + "\n")
        else:
            text_file.write(str(2)+ "\n")

        text_file.write(str(1)+ "\n")
        text_file.write(str(i*(k+1) +j + 1+ num) + " " + str(i*(k+1) +j + num) 
        +  " " + str((i+1)*(k+1) +j+ num) + " " + str((i+1)*(k+1) +j+ num + 1 ) + "\n")

# Light cube
num += (k+1)*(k+1) 

text_file.write(str(0) + "\n")
text_file.write(str(1) + "\n")
text_file.write(str(num) + " " + str(num+1) +  " " + str(num+2) + " " + str(num+3) + "\n")
text_file.write(str(0) + "\n")
text_file.write(str(1) + "\n")
text_file.write(str(num+1) + " " + str(num+5) +  " " + str(num+6) + " " + str(num+2) + "\n")
text_file.write(str(0) + "\n")
text_file.write(str(1) + "\n")
text_file.write(str(num+5) + " " + str(num+4) +  " " + str(num+7) + " " + str(num+6) + "\n")
text_file.write(str(0) + "\n")
text_file.write(str(1) + "\n")
text_file.write(str(num) + " " + str(num+3) +  " " + str(num+7) + " " + str(num+4) + "\n")
text_file.write(str(0) + "\n")
text_file.write(str(1) + "\n")
text_file.write(str(num+3) + " " + str(num+2) +  " " + str(num+6) + " " + str(num+7) + "\n")
text_file.write(str(0) + "\n")
text_file.write(str(1) + "\n")
text_file.write(str(num) + " " + str(num+4) +  " " + str(num+5) + " " + str(num+1) + "\n")


text_file.close()
