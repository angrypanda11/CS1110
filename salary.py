import urllib.request
import re


def name_to_url(name):

    if ',' in name:
        name_1 = name.lower()
        name_2 = name_1.strip().split(',')
        name_3 = name_2[1] + '-' + name_2[0]
        final_name = name_3.strip()
        return final_name

    # if '-' in name and ',' not in name:
    #     return name

    if ' ' in name:
        name_1 = name.lower()
        name_2 = name_1.replace(' ', '-')
        return name_2

    else:
        return name


def jobtitle(name):
    name_1 = name_to_url(name)
    stream = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/uva2016/' + name_1)
    job_title = re.compile('Job title: (.*)<br')
    for line in stream:
        line = str(line)

        for m in job_title.finditer(line):
            job = m.group(1)
            # print(job)
            return job


def salary(name):
    name_1 = name_to_url(name)
    stream = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/uva2016/' + name_1)
    salary = re.compile('>\$(.*)<')

    for line in stream:
        line = str(line)
        for m in salary.finditer(line):
            salaray_1 = m.group(1)
            salaray_2 = salaray_1.replace(',', '')
            salaray_3 = float(salaray_2)
            money = str(salaray_3)
            return money


def ranking(name):
    name_1 = name_to_url(name)
    stream = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/uva2016/' + name_1)
    ranks = re.compile('<tr><td>University of Virginia rank</td><td>(.*) of 7,927</td></tr>')
    for line in stream:
        line = str(line)
        for m in ranks.finditer(line):
            rank = m.group(1)
            return rank


def report(name):
    try:
        job = jobtitle(name)
    except:
        job = None

    try:
        money = salary(name)
    except:
        money = 0

    try:
        rank = ranking(name)
        if rank is None:
            rank = 0
    except:
        rank = 0

    return job, money, rank
