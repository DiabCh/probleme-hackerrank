from calendar import isleap
# def is_leap(year):
#     leap = False
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 100 == 0 and year % 400 == 0:
#                 leap = True
#                 return leap
#             else:
#                 leap=False
#                 return leap
#         else:
#             leap = True
#             return leap
#     else:
#         leap = False
#         return leap

# def is_leap(year, leap=False):
#     if year % 4 == 0 and year % 100 != 0 or year % 100 == 0 and year % 400 == 0:
#         leap = True

    # return leap
def is_leap(year):
    return isleap(year)

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)

year = 2000
print (is_leap(year))