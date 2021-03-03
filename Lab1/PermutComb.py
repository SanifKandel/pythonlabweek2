#A school decides to replace the desk in three classrooms.Each desk sits two students. Given the no. of student in each
# class , print the smallest possible no of desk that can be purchased. the program should read three ints the no. of
# studentrs in each three classes, a,b,c respectively.

lr13 = int(input("lr13 students:"))
lr14 = int(input("lr14 students:"))
lr15 = int(input("lr15 students:"))

totalSt = lr13 + lr14 + lr15
desk = round(totalSt/2)
print (desk)