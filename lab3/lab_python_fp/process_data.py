import json
import sys
from field import field
from gen_random import gen_random
from unique import Unique
from print_result import print_result
from cm_timer import cm_timer_1


path = sys.argv[1]

with open(path) as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name'), ignore_case=True))


@print_result
def f2(jobs):
    return filter(lambda job: job.startswith('программист'), jobs)


@print_result
def f3(jobs):
    return map(lambda job: job + ' с опытом Python', jobs)


@print_result
def f4(jobs):
    jobs = list(jobs)
    salary = gen_random(len(jobs), 100000, 200000)

    return [job + f', зарплата {salary} руб' for salary, job in zip(salary, jobs)]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
