from flask import Flask, render_template
import pandas as pd

app=Flask(__name__)

stations = pd.read_csv("data_small_/stations.txt", skiprows=17)
stations = stations[["STAID","STANAME                                 "]]

#first page
@app.route("/")#decorator- decorates the function home()
#when the user visits the url="/home" , the function home() is called
def home():
    return render_template("home.html",data=stations.to_html())


#second page
@app.route("/api/v1/<station>/<date>")#decorator- decorates the function about()
#when the user visits the url="/about/" , the function about() is called
def about(station,date):
    filename="data_small_/TG_STAID"+str(station).zfill(6)+".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature=df.loc[df["    DATE"]==date]["   TG"].squeeze()/10
    return {"station":station,
            "date":date,
            "temperature":temperature}


@app.route("/api/v1/<station>")
def all_dates(station):
    filename = "data_small_/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result=df.to_dict(orient="records")
    return result


@app.route("/api/v1/year/<station>/<year>")
def one_year(station,year):
    filename = "data_small_/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"]=df["    DATE"].astype(str)
    result=df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result




if __name__=="__main__":
    app.run(debug=True)#debug=True will allow the showing of errors on the webpage





"""if some other flask app is running at the same time as this flask app or , 
any 2 flask apps are running at the same time 
then change the port else will not run.
changing port: app.run(debug=True,port=5001(or something))"""

#the two standards of returning data via a rest API are dictionary and list