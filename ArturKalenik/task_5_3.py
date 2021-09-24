from operator import itemgetter


def transform_basis_file(all_students):
    """
    Opens the file and rewrites the tuple of names and data of all students in the list
    :param all_students: file CSV with unsorted students
    :return: list of unsorted students
    """

    with open(all_students, 'r') as file:
        data = file.read().split('\n')
        students_list = []
        for i in data:
            students_list.append(tuple(i.split(',')))
        return students_list


def reinvent_lists(students_age, all_students, number):
    """
    1>  Implement a function which receives file path and returns names of top performer students
    2>  Implement a function which receives the file path with srudents info
        and writes CSV student information to the new file in descending order of age.

    :param students_age: empty file for writing
    :param all_students: CSV - file students
    :param number: 5
    :return: sorted file by students age, names of top performer students
    """

    students_list = transform_basis_file(all_students)
    age_student = sorted(students_list, key=itemgetter(1, 1), reverse=True)
    top_performer_students = sorted(students_list, key=itemgetter(2, 2), reverse=True)
    top = []
    with open(students_age, 'w') as age:
        for i in age_student:
            age.writelines(','.join(i) + '\n')
    for i in top_performer_students[0:number]:
        top.append(i[0])
    return top


if __name__ == '__main__':
    students = "data_files/students.csv"
    elder_age = "data_files/students_order_of_age.csv"
    number_students = int(input())
    print(reinvent_lists(elder_age, students, number_students))
