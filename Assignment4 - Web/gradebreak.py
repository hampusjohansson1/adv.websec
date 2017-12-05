import requests;
import warnings;
import operator;


def findTime(address,signature):
    hexArray = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"];
    winner = dict();
    win="";
    print(signature);

    for x in range(0, 10):
        temp = dict();
        for hex in hexArray:
            response = requests.get(address + signature + hex, verify=False);
            elapsedTime = response.elapsed;
            temp[hex] = elapsedTime.microseconds;

        win = max(temp, key=temp.get);

        if(not winner.keys().__contains__(win)):
            winner[win] = 0;
            winner[win] += 1;
        else:
             winner[win] += 1;

    value = max(winner, key=winner.get);

    print(winner);
    print(value);
    return str(value);

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    name = "Kalle";
    grade = "5";
    signature = "";

    address = "https://eitn41.eit.lth.se:3119/ha4/addgrade.php?name=" + name + "&grade=" + grade + "&signature=";

    for x in range (0,20):
        addressVal = findTime(address,signature);
        signature = signature + addressVal;

    print(signature);