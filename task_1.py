'''Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.'''

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--name', type=str)
parser.add_argument('--working_hours', type=int)
parser.add_argument('--rate_per_hour', type=int, default=500)
parser.add_argument('--prize', type=int, default=500)

args = parser.parse_args()

result = (args.working_hours * args.rate_per_hour) + args.prize
print(f'привет {args.name}, заработная плата = {result} руб')

#1
