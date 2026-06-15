from flask import Flask, render_template, jsonify

app= Flask(__name__)
JOBS= [
    {
        id: 1,
        'tittle': 'Data Analyst',
        'Location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        id: 2,
        'tittle': 'Data Scientist',
        'Location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        id: 3,
        'tittle': 'Frontend Engineer',
        'Location': 'Remote',
        'salary': 'Rs. 12,00,000'
    },
    {
        id: 4,
        'tittle': 'Backend Engineer',
        'Location': 'San Fran, USA',
        'salary': '$120,000'
    },
    
]
@app.route("/")
def Hello():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host= '0.0.0.0', debug= True)