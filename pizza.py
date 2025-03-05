import argparse

p = argparse.ArgumentParser(prog='pizza')

p.add_argument("fobo", help= "first positional arguement which will be written first")
p.add_argument("bar", help= "second positional arguement which will be written second")

p.add_argument("-v", "--verbosity", help="increase output verbosity", type=int, choices=[0,1,2])

args = p.parse_args()


bool_verbosity = args.verbosity
first_word = args.fobo
second_word = args.bar

if args.verbosity ==2:
    print("VERY VERBOSE LOGS")
    print(bool_verbosity)
    print("The first positional argument was " + first_word + 
    ". The second positional argeumetn was " + second_word + ".")
elif args.verbosity ==1:
    print("VERBOSE LOGS")
    print(bool_verbosity)
    print (f"First = {first_word}, Second = {second_word}")
else:
    print(bool_verbosity)
    print(f"Running {__file__}")
    print(first_word,second_word)