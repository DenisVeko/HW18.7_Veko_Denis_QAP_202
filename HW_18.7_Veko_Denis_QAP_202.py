import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Удалить оценку ученика по предмету
        3. Редактировать оценку ученика по предмету
        4. Вывести средний балл по всем предметам по каждому ученику
        5. Вывести средний балл одного ученика по всем предметам
        6. Вывести все оценки по всем ученикам
        7. Вывести все оценки определенного ученика
        8. Добавить ученика
        9. Удалить ученика
        10. Редактировать данные ученика
        11. Добавить новый предмет
        12. Удалить предмет
        13. Редактировать название предмета
        14. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценки ученика по предмету')
        print(f'Ученики: {students}')
        student = input('Введите имя ученика: ')
        if student in students:
            print(f'Предметы: {classes}')
            class_ = input('Введите предмет: ')
            if class_ in classes:
                mark = int(input('Введите оценку: '))
                students_marks[student][class_].append(mark)
                print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
                print(f'\t{student} - {class_} - {students_marks[student][class_]}')
            else:
                print('ОШИБКА: неверное название предмета')
        else:
            print('ОШИБКА: неверное имя ученика')

    elif command == 2:
        print('2. Удалить оценку ученика по предмету')
        print(f'Ученики: {students}')
        student = input('Введите имя ученика: ')
        if student in students:
            print(f'Предметы: {classes}')
            class_ = input('Введите предмет: ')
            if class_ in classes:
                print(f'\t{student} - {class_} - {students_marks[student][class_]}')
                mark_del = int(input('Введите порядковый номер удаляемой оценки: '))
                n = students_marks[student][class_].pop(mark_del-1)
                print(f'Для {student} по предмету {class_} удалена оценка {n}')
                print(f'\t{student} - {class_} - {students_marks[student][class_]}')
            else:
                print('ОШИБКА: неверное название предмета')
        else:
            print('ОШИБКА: неверное имя ученика')

    elif command == 3:
        print('3. Редактировать оценку ученика по предмету')
        print(f'Ученики: {students}')
        student = input('Введите имя ученика: ')
        if student in students:
            print(f'Предметы: {classes}')
            class_ = input('Введите предмет: ')
            if class_ in classes:
                print(f'\t{student} - {class_} - {students_marks[student][class_]}')
                mark_change = int(input('Введите порядковый номер редактируемой оценки: '))
                n = students_marks[student][class_].pop(mark_change-1)
                mark_new = int(input('Введите новую оценку: '))
                students_marks[student][class_].insert(mark_change-1, mark_new)
                print(f'Для {student} по предмету {class_} изменена оценка {n} на оценку {mark_new}')
                print(f'\t{student} - {class_} - {students_marks[student][class_]}')
            else:
                print('ОШИБКА: неверное название предмета')
        else:
            print('ОШИБКА: неверное имя ученика')

    elif command == 4:
        print('4. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {round(marks_sum / marks_count, 2)}')
            print()

    elif command == 5:
        print('5. Вывести средний балл одного ученика по всем предметам')
        print(f'Ученики: {students}')
        student = input('Введите имя ученика: ')
        if student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                mark_avg = round(marks_sum / marks_count, 2)
                print(f'{class_} - {mark_avg}')
            print()
        else:
            print(f'ОШИБКА: неверное имя ученика')
            print()

    elif command == 6:
        print('6. Вывести все оценки по всем ученикам')
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()

    elif command == 7:
        print('7. Вывести все оценки определенного ученика')
        print(f'Ученики: {students}')
        student = input('Введите имя ученика: ')
        if student in students:
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
                print()
        else:
            print(f'ОШИБКА: неверное имя ученика')
            print()

    elif command == 8:
        print('8. Добавить ученика: ')
        print(f'Ученики: {students}')
        student_new = input('Введите имя НОВОГО ученика: ')
        students.append(student_new)
        students.sort()
        print(f'Ученики: {students}')
        students_marks[student_new] = {}
        for class_ in classes:
            students_marks[student_new][class_] = []

    elif command == 9:
        print('9. Удалить ученика')
        print(f'Ученики: {students}')
        student_del = input('Введите имя УДАЛЯЕМОГО ученика: ')
        if student_del in students:
            students.remove(student_del)
            del students_marks[student_del]
            students.sort()
            print(f'Ученик {student_del} удален из списка')
            print(f'Ученики: {students}')
        else:
            print(f'Неверное имя ученика')
            print()

    elif command == 10:
        print('10. Редактировать данные ученика')
        print(f'Ученики: {students}')
        student_change = input('Введите имя ученика, данные которого необходимо ИЗМЕНИТЬ: ')
        if student_change in students:
            student_new = input('Введите НОВЫЕ данные ученика: ')
            students.append(student_new)
            students_marks[student_new] = students_marks[student_change]
            del students_marks[student_change]
            students.remove(student_change)
            students.sort()
            print(f'Данные ученика {student_change} изменены на {student_new}')
            print(f'Ученики: {students}')

        else:
            print()
            print(f'ОЩИБКА: Неверно введено имя ученика')
            print()

    elif command == 11:
        print(f'11. Добавить новый предмет')
        print(classes)
        new_class = input('Введите название нового предмета: ')
        classes.append(new_class)
        for student in students_marks:
            students_marks[student][new_class] = []
        print()
        print(f'Новый предмет "{new_class}" добавлен в список')
        print(classes)

    elif command == 12:
        print(f'12. Удалить предмет')
        print(f'Список предметов: {classes}')
        del_class = input('Введите название УДАЛЯЕМОГО предмета: ')
        if del_class in classes:
            classes.remove(del_class)
            for student in students_marks:
                del students_marks[student][del_class]
            print()
            print(f'Предмет {del_class} удален из списка предметов')
            print(f'Актуальный список предметов: {classes}')

        else:
            print(f'Ошибка: неверное название предмета. Уточните название предмета.')
            print(f'Список предметов: {classes}')

    elif command == 13:
        print(f'13. Редактировать название предмета')
        print(f'Список предметов: {classes}')
        change_class = input('Введите название РЕДАКТИРУЕМОГО предмета: ')
        if change_class in classes:
            new_class = input('Введите НОВОЕ название предмета: ')
            classes.append(new_class)
            for student in students_marks:
                students_marks[student][new_class] = []
                students_marks[student][new_class] = students_marks[student][change_class]
            classes.remove(change_class)
            for student in students:
                del students_marks[student][change_class]
            print(f'Актуальный список предметов:')
            print(f'{classes}')
        else:
            print(f'Ошибка: неверное название предмета. Уточните название предмета.')
            print(f'Список предметов: {classes}')

    elif command == 14:
        print('14. Выход из программы')
        break

    elif command > 14 or command <= 0:
        print('Неверный номер команды. Обратитесь к списку команд.')
        print('''
                Список команд:
                1. Добавить оценки ученика по предмету
                2. Удалить оценку ученика по предмету
                3. Редактировать оценку ученика по предмету
                4. Вывести средний балл по всем предметам по каждому ученику
                5. Вывести средний балл одного ученика по всем предметам
                6. Вывести все оценки по всем ученикам
                7. Вывести все оценки определенного ученика
                8. Добавить ученика
                9. Удалить ученика
                10. Редактировать данные ученика
                11. Добавить новый предмет
                12. Удалить предмет
                13. Редактировать название предмета
                14. Выход из программы
                ''')
