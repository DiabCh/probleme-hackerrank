#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print(f'Hello {first} {last} You just delved into python.')

if __name__ == '__main__':
    name = [input('What is your first name?'), input('What is your last name?')]
    print_full_name(name[0],name[1])