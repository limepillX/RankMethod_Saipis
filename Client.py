def find_expert_value(expert_marks):
    w = [[] for i in range(len(expert_marks))]
    sum_marks_all = []
    end_marks = []

    experts_count = len(expert_marks)
    marks_count = len(expert_marks[0])
    for i in range(experts_count):
        sum_marks = 0
        print(f'Оценки {i + 1}\n | ', end='')
        for j in range(marks_count):
            print(expert_marks[i][j], end=' | ')
            sum_marks += expert_marks[i][j]
        sum_marks_all.append(sum_marks)
        print("\n")

    for i in range(experts_count):
        for j in range(marks_count):
            w[i].append(round(expert_marks[i][j] / sum_marks_all[i], 3))

    max_in_list = 0
    for j in range(marks_count):
        end_marks.append(round(((w[0][j] + w[1][j]) / experts_count), 3))
        if end_marks[j] > max_in_list:
            max_in_list = end_marks[j]
            index = j + 1

    print(f'Искомые веса целей : {end_marks}\nЛучший студент : {index}')


find_expert_value([[9.85, 8], [7.3, 8], [8.25, 8], [6.8, 8], [9.31, 8], [4.78, 8], [7.98, 8], [5.76, 8], [10.0, 8], [9.98, 8], [8.45, 8], [7.75, 8], [8.15, 8], [6.73, 8], [9.82, 8], [5.78, 8], [6.98, 8]]
)
