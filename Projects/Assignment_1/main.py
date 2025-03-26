import argparse 
import logging 

# Configure logging
logging.basicConfig(
    filename="calculator.log",
    format='%(asctime)s %(message)s',
    filemode='a'
)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Parse command-line arguments
def parse_args():
    parser = argparse.ArgumentParser(description="Calculator")
    
    # Argument for operations 
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-a", "--addition", help="Performs addition", action="store_true")
    group.add_argument("-s", "--subtraction", help="Performs subtraction", action="store_true")
    group.add_argument("-m", "--multiplication", help="Performs multiplication", action="store_true")
    group.add_argument("-d", "--division", help="Performs Division", action="store_true")

    # Argument for significant figures 
    parser.add_argument("-f", "--significant-figures", type=int, default=2, help="How many significant figures (default: 2)")
    
    # Argument for values 
    parser.add_argument("num_1", type=float, help="Give a positive integer (value 1)")
    parser.add_argument("num_2", type=float, help="Give a positive integer (value 2)")

    args = parser.parse_args()
    return args 

# Format Function 
def format_result(value, sig_figs): 
    return float(f"{value:.{sig_figs}g}")

# Addition Function 
def addition(num_1, num_2, sig_figs=2):
    result = num_1 + num_2 
    # Log 
    logger.debug(f"Addition: {num_1} + {num_2} = {result}")
    return format_result(result, sig_figs)

# Subtraction Function 
def subtraction(num_1, num_2, sig_figs=2):
    result = num_1 - num_2 
    # Log 
    logger.debug(f"Subtraction: {num_1} - {num_2} = {result}")
    return format_result(result, sig_figs)

# Multiplication Function 
def multiplication(num_1, num_2, sig_figs=2): 
    result = num_1 * num_2
    # Log 
    logger.debug(f"Multiplication: {num_1} * {num_2} = {result}")
    return format_result(result, sig_figs)

# Division Function 
def division(num_1, num_2, sig_figs=2):
    if num_2 == 0:
        logger.error("Division by zero error")
        return "Error: Division by zero"
    result = num_1 / num_2
    logger.debug(f"Division: {num_1} / {num_2} = {result}")
    return format_result(result, sig_figs)

# Operation 
def main():
    args = parse_args()
    sig_figs = max(1, min(args.significant_figures, 10))  # Limit to a reasonable range

    operations = {
        "addition": addition, 
        "subtraction": subtraction, 
        "multiplication": multiplication, 
        "division": division,
    }

    for operation, func in operations.items(): 
        if getattr(args, operation):
            result = func(args.num_1, args.num_2, sig_figs)
            print(f"Result: {result}")
            break 

if __name__ == "__main__":
    main()
