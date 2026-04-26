import logging

logging.basicConfig(filename = 'Logging/practice_4.log', 
                    level = logging.DEBUG, filemode= 'a', 
                    format = '%(asctime)s - %(levelname)s - %(message)s',
                    datefmt= '%Y-%m-%d %H:%M:%S')

try:
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))

    result = a/b
    print("Result = ",result)

except ZeroDivisionError as msg:
    logging.error("Error  is - %s",msg)
    print("Something went wrong!")
except ValueError as msg:
    logging.error("Error  is - %s",msg)    
    print("Invalid Input!")