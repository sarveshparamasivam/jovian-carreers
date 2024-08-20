from flask import Flask, render_template,jsonify

app = Flask(__name__)
JOBS = [
  {
    'id':1,
    'title':"Data Analyst",
    'location':"Bengaluru",
    'salary':"10,00,000"
  },
  {
    'id':2,
    'title':"Data Scientist",
    'location':"Delhi",
    'salary':"5,00,000"
  },
  {
    'id':3,
    'title':"Software Engineer",
    'location':"Hyderabad",
    'salary':"8,00,000"
  },
  {
    'id':4,
    'title':"Web Developer",
    'location':"Chennai",
    'salary':"1000000"
  },
  {
    'id':5,
    'title':"SOftware Developer",
    'location':"Bengaluru",
    'salary':"1000000"
  }
]

@app.route('/')
def hello_world():
  return render_template("home.html",jobs = JOBS,companyname="Jovian")
  
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
