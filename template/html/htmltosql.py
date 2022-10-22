import sqlite3
import js
from js import console

data = sqlite3.connect('datas/data.db')
cursor = data.cursor()

# It might look like its erroring but py-script comes built-in with the js module so ITS FINE 

def handle():
    state = Element('inputState').element.value
    procedure = Element('inputProcedure').element.value
    cost = Element('inputCost').element.value
    gender = Element('inputGender').element.value
    age = Element('inputAge').element.value
    breakdown = Element('costBreakdown').element.value

    output = [procedure, cost, age, gender, state]

    cursor.execute("INSERT INTO entries VALUES(NULL, ?, datetime('now', 'localtime'), ?, ?, ?, ?)", output)
    data.close()
