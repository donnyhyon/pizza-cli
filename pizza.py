import argparse

p = argparse.ArgumentParser(prog='Pizza Dough Helper')

p.add_argument("-r", "--hydration", help= "hydration of final pizza dough", type=int, default=70)
p.add_argument("-n", "--numberOfBalls", help= "Number of pizza balls you want to make", type=int, default=10)
p.add_argument("-s", "--size", help="Size of balls", type=int, default=280)

p.add_argument("-p", "--poolish", help="If you want to use poolish, 1-100", type=int)
p.add_argument("-b", "--biga", help="If you want to use biga, 1-100", type=int)

args = p.parse_args()

def console_output(td, hy, f, w, s, o, y, h):
    print(f"""{numberOfballs} pizzas at {size}g makes:
Total Dough : {totalDough}g
Hydration   : {hydration}%
Flour       : {flour}g
Water       : {water}g
Salt        : {salt}g
Oil         : {oil}g
Yeast       : {yeast}g
Honey       : {honey}g
    """)


def check_in_range(value, min, max):
    if (value > max or value < min ):
        raise argparse.ArgumentTypeError(f"{value} is out of range, allowed values are {min}-{max}")
# Main

prefermentPercentage = 0
if (args.poolish):
    check_in_range(args.poolish,0,100)
    prefermentPercentage = args.poolish
if (args.biga):
    check_in_range(args.biga,0,100)
    prefermentPercentage = args.biga

hydration = args.hydration
numberOfballs = args.numberOfBalls
size = args.size
totalDough = numberOfballs * size
decimalPoint = 1

ratio = 100 + hydration
flour = round((totalDough / ratio) * 100 , decimalPoint)
water = round((totalDough / ratio) * hydration, decimalPoint)
salt = round(flour * 0.01, decimalPoint)
oil = round(flour * 0.01, decimalPoint)
yeast = round(flour * 0.005, decimalPoint)
honey = round(flour * 0.005, decimalPoint)

if (prefermentPercentage == 0):
    print("No preferment")
    console_output(totalDough,hydration,flour,water,salt,oil,yeast,honey)

if (args.biga):
    biga = totalDough * prefermentPercentage
    print(biga)