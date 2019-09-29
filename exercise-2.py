name= input("Name: ")
print("Long edge of the rectangle x:")
x= int(input())
print("Short edge of the rectangle y:")
y= int(input())
perimiter=2*(x+y)
area=x*y
txt="Dear {0} perimiter of the rectangle is: {1} ; area of the rectangle is: {2} "
print(txt.format(name,perimiter,area))
