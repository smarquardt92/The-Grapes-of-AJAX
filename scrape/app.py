from flask import Flask, render_template, jsonify,redirect,request
from flask_pymongo import PyMongo
import scrape

app=Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_info"
mongo = PyMongo(app)

@app.route("/")
def home():
   wines=[]
   return render_template("index.html")


   
@app.route('/result',methods = ['POST'])
def result():
   result = request.form['Name']
   print(result)
   wines = []
   wines = scrape.scrape_all(result)
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = wines)

if __name__ == "__main__":
   app.run(debug=True)