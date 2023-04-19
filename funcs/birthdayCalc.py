import datetime
from datetime import date

def birthday_calculator(birthdate: datetime.date):
    current_year_bd =birthdate.replace(year=date.today().year)
    return (current_year_bd - date.today()).days if current_year_bd > date.today() else (current_year_bd.replace(date.today().year+1) - date.today()).days

bd = date(2004, 7, 29)
print(birthday_calculator(bd))