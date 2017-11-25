# cd /Users/bkatchmar/GitHub/InflowPythonExercises
# python3 exercises5.py

def calculator(first, second, **options):
    result = 0
    
    try:
        if options.get("action") == "addition":
            result = (first + second)
        elif options.get("action") == "subtraction":
            result = (first - second)
        elif options.get("action") == "multiplication":
            result = (first * second)
        elif options.get("action") == "divided":
            result = (first / second)
        else:
            print("No Operation Selected")
            return
    except Exception as exe:
        print("An exception has occured, good finding out what it is; type %s" % (type(exe).__name__))
    
    print("The result of %s is %d" % (options.get("action"), result))

calculator(2,2,action="addition")
calculator(2,2,action="subtraction")
calculator(2,2,action="multiplication")
calculator(2,2,action="divided")
calculator(2,0,action="divided")