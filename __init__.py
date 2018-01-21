

from flask import Flask, request, render_template
import os
from pyt import breakToWords
from pyt import getImportantKeys
from pyt import breakAndGetKeys

app = Flask(__name__)

def getSectionLink(name):
    return {
        'a': "https://www.khanacademy.org/science/physics/forces-newtons-laws",
        'b': "https://www.khanacademy.org/science/physics/work-and-energy",
        'c': "https://www.khanacademy.org/science/physics/thermodynamics",
        'd': "https://www.khanacademy.org/science/physics/electric-charge-electric-force-and-voltage"
    }.get(name, "https://www.google.com")

def getSectionName(name):
    return {
        'a': "Force/Motion",
        'b': "Energy",
        'c': "Thermodynamics",
        'c': "Electricity"
    }.get(name, "Force/Motion")


def getKeyWords():
    return getImportantKeys()
    
    

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    
    a = [format(request.form['text'])]
    
    countedSelectedWords = breakAndGetKeys(a)
    
    #test print
    for alreadyCounted in countedSelectedWords:
        print(alreadyCounted[0] + " " + str(alreadyCounted[1]) + " " + str(alreadyCounted[2]) )
    
    
    # getSection with machine learning
    section = 'b'
    
    return render_template('element.html', message = getSectionName(section), link = getSectionLink(section))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3002))
    app.run(host = '0.0.0.0', port = port, debug = True)





