# Moises Fernandes 
# Python Script Writing Drills (Utilizing argparse, logging and if main idiom)
# Making it "Natural"
    # Take in inputs like " +, -, *, /"
    # Float -> allow user to select significant figures (some answer will be decimals)
# Explore Logging 

import argparse 
import logging 

logging.basicConfig(filename = "calculator.log"
                    format = '%(asctime)s %(message)s',
                    filemode = 'a')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def parse_args():
    parser = argparse.ArgumentParser(description= "Calculator")
    # Argument for operations 
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a","--addition", help = "Performs addition", action = "store_true")
    group.add_argument("-s","--subtraction", help = "Performs subtraction", action = "store_true")
    group.add_argument("-m","--multiplication", help = "Performs multiplication", action = "store_true")
    group.add_argument('-d',"--divison", help = "Performs Division", action = "store_true")
    # Argument for significant figures 
    parser.add_argument("-f","--significat-figure", type = int, default = 2, help = "How many significant figures")
    # Argument for values 
    parser.add_argument("num_1", type = float, help = "Give a positive integer (value 1)")
    parser.add_argument("num_2", type = float, help = "Give a positive integer (value 2)")

    args = parser.parse_args()
    return args 

def main(args):
    sig_figs = args.significant_figures
    if args.addition:
        result = addition(args.num_1,args.num_2,sig_figs)
        print("The addition results of {} and {} is {} ".format(args.num_1,args.num_2,result))
    elif args.subtraction: 
        result = subtraction(args.num_1, args.num_2, sig_figs)
        print("The subtraction results of {} and {} is {} ".format(args.num_1,args.num_2,result))
    elif args.multiplication:
        result = multiplication(args.num_1,args.num_2)
        print("The multiplication results of {} and {} is {} ".format(args.num_1,args.num_2,result))
    elif args.division:
        result = division(args.num_1, args.num_2) 
        print("The division results of {} and {} is {} ".format(args.num_1,args.num_2,result))
    else: 
        print( "Please use a specificed operation")

# Addition Function 
def addition (num_1,num_2, sig_figs = 2):
    sum = num_1 + num_2 
    # Log 
    logger.debug(f"num_1 : {num_1}")
    logger.debug(f"num_2 : {num_2}")
    logger.debug(f"sum :{sum}")
    return float(f"{sum:{sig_figs}g}")

# Subtraction Function 
def subtraction (num_1, num_2, sig_figs = 2):
    diff = num_1 - num_2 
    # Log 
    logger.debug(f"num_1 : {num_1}")
    logger.debug(f"num_2: {num_2}")
    logger.debug(f"diff :{diff}")
    return float(f"{diff:{sig_figs}g}")

def multiplication (num_1, num_2, sig_figs = 2): 
    product = num_1 * num_2
    # Log 
    logger.debug(f"num_1 : {num_1}")
    logger.debug(f"num_2: {num_2}")
    logger.debug(f"product :{product}")
    return float(f"{product:{sig_figs}g}")
 
def division(num_1, num_2, sig_figs = 2): 
    quotient = num_1 * num_2
    # Log 
    logger.debug(f"num_1 : {num_1}")
    logger.debug(f"num_2: {num_2}")
    logger.debug(f"product :{quotient}")
    return float(f"{quotient:{sig_figs}g}")

# Operation 
if __name__ == "__main__":
    args = parse_args()
    main(args)


