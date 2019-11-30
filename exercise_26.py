
def avg_grade():
 dividend=0
 divisor=0
 for x in notes_i_take:
  average=(notes_i_take[x][0]+notes_i_take[x][1])/2
  dividend=dividend+(lesson_hours[x]*average)
  divisor=divisor+lesson_hours[x]
 return(dividend/divisor)

lesson_hours={}
notes_i_take={}

lessons_file=open("exercise_26_lessons.txt","r")

for x in lessons_file:
 splited_line=x.split(";")
 lesson=splited_line[0]
 hours=int(splited_line[1])
 note_1=int(splited_line[2])
 note_2=int(splited_line[3])
 lesson_hours[lesson]=hours
 notes_i_take[lesson]=[note_1,note_2]

lessons_file.close()

for x in lesson_hours:
  txt="lesson: {0}\nhours per week: {1} \nnotes: {2} {3}\n"
  print(txt.format(x,lesson_hours[x],notes_i_take[x][0],notes_i_take[x][1]))

weighted_average=avg_grade()
print(round(weighted_average,2))
