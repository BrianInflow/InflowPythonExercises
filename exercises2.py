# cd /Users/bkatchmar/GitHub/InflowPythonExercises
# python3 exercises2.py

currencies = [
    {"Country":"United States","Name":"Dollar","Code":"USD"},
    {"Country":"Great Britain","Name":"Pound","Code":"GBP"},
    {"Country":"Eurozone","Name":"Euro","Code":"EUR"},
    {"Country":"Japan","Name":"Yen","Code":"JPY"}
]

currencies.append({"Country":"South Korea","Name":"Won","Code":"KRW"})

for currency in currencies:
    print("%s - %s - %s" % (currency["Country"], currency["Name"], currency["Code"]))
    
    if currency["Code"] == "USD":
        print("My Native Currency!")