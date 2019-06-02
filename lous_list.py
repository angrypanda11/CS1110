import urllib.request

# stream = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/louslist')
# listing = stream.readlines()
# # .strip().split('|')  # .decode('utf-8')
# # print(listing)


def instructors(department):
    instructor_list = []

    streaming = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/louslist/' + department.upper())

    for column in streaming:
        organized = column.decode('utf-8').strip().split('|')
        instructor = organized[4]
        if '+' in instructor:
            instructor = instructor[:-2].strip()
        # if len(instructor) < 3:
        #     continue
        if instructor not in instructor_list:
            instructor_list.append(instructor)
    return sorted(instructor_list)
# print(instructors('BME'))


def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    class_list = []
    final_list = []
    streaming = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/louslist/' + dept_name)

    for line in streaming:
        organize = line.decode('utf-8').strip().split('|')

        class_name = organize[0]
        if dept_name in class_name:
            class_list.append(organize)

    for line in streaming:
        organize = line.decode('utf-8').strip().split('|')
        if has_seats_available is True and int(organize[15]) > int(organize[16]):
            class_list.append(organize)
            if has_seats_available == False:
                continue

    for line in streaming:
        organize = line.decode('utf-8').strip().split('|')
        class_level = int(organize[1])

        if level is not None and len(level) == 4:
            if int(level[0]) == int(class_level[0]):
                class_list.append(organize)
            # if level is None:
            #     continue

    for line in streaming:
        organize = line.decode('utf-8').strip().split('|')
        start_time = int(organize[12])
        if not_before is not None:
            if start_time < int(not_before):
                class_list.append(organize)
            # if not_before is None:

    for line in streaming:
        organize = line.decode('utf-8').strip().split('|')
        start_time = int(organize[12])
        if not_after is not None:
            if start_time > int(not_after):
                class_list.append(organize)

    if class_list not in final_list:
        final_list.append(class_list)

    return final_list

# print(class_search('BME', False))