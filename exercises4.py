# cd /Users/bkatchmar/GitHub/InflowPythonExercises
# python3 exercises4.py

def calculator(first, second, **options):
    if options.get("action") == "addition":
        print("Result of addition: %d" % (first + second))
    else:
        print("No Operation Selected")
    
calculator(1,2)
calculator(2,2,action="addition")