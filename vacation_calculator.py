"""This script is made for calculate LEFT vacation days in Chile. Enjoy!."""
from prettytable import PrettyTable
from datetime import date
from dateutil.relativedelta import relativedelta

table = PrettyTable(
    [
        'DATE',
        'WORKED DAYS',
        'TOTAL VACATION DAYS',
        'LEFT VACATION DAYS'
    ]
)

# LEGAL VACATION DAYS
LEGAL_ANNUAL_VACATION_DAYS = 15

# MONTHS TO CALCULATE VACATIONS, 0 IS TODAY
MONTHS_TO_CALCULATE = [
    0,
    1,
    3,
    6,
    12
]

# USER INPUT DATA
year = int(
    input("Enter the year of contract [2018]: ") or "2018"
)
month = int(
    input("Enter the month of contract [01]: ") or "1"
)
day = int(
    input("Enter the day of contract [01]: ") or "1"
)
used_vacation_days = int(
    input("How many days of vacation did you use? : ") or "0"
)

contract_initial_date = date(year, month, day)
today = date.today()

for MONTH_TO_CALCULATE in MONTHS_TO_CALCULATE:
    reference_date = today + relativedelta(months=MONTH_TO_CALCULATE)
    delta = reference_date - contract_initial_date

    total_vacation_days = delta.days / 365 * LEGAL_ANNUAL_VACATION_DAYS
    left_vacation_days = total_vacation_days - used_vacation_days

    table.add_row(
        [
            reference_date,
            int(delta.days),
            int(total_vacation_days),
            int(left_vacation_days)
        ]
    )

print(table)
