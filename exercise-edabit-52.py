def get_best_student(grades):
  best_avg=0
  best_student=""
  for x in grades:
    if (sum(grades[x]))/len(grades[x]) >= best_avg:
      best_avg=sum(grades[x])/len(grades[x])
      best_student=x
  return(best_student)

print(get_best_student({
  "John": [100, 90, 80],
  "Bob": [100, 70, 80]
}))
