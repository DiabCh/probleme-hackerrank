
student_marks = {'Krishna': [67.00, 68.00, 69.00],
                   'Arjun': [70.00, 98.00, 63.00],
                   'Malika': [52.00, 56.00, 60.00],
                  }

query_name = 'Krishna'

sum = 0.00
for x in student_marks[query_name]:
    sum += x
average = round(sum / len(student_marks[query_name]), 2)
formatted_float = "{:.2f}".format(average)
print(formatted_float)
