# importing Libraries
from flask import Flask, render_template, request, redirect  
import os

#initializing Flask app
app = Flask(__name__)                                        

picFolder = os.path.join('static','pics')
app.config['UPLOAD_FOLDER'] = picFolder

@app.route('/')                                              
def display():
    pic01 = os.path.join(app.config['UPLOAD_FOLDER'], 'mic.png')
    name01 = 'Speak'

#Function for rendering home page    
    return render_template('indexaudio.html', user_img = pic01, name= name01)

# Function for performing operation on Query given by user on Front-end
@app.route("/submit", methods=["POST"])
def submit():
    link = ''
    pic01 = os.path.join(app.config['UPLOAD_FOLDER'], 'mic.png')
    query = request.form.get("text")

    # Converting all query in lower case
    query01 = query.lower()
    
    # Creating logics for specific task 
    if "google" in query01:
        link = "google.com"
    elif "youtube" in query01:
        link = "youtube.com"
    elif "live event" in query01:
        link = f"localhost:4101/live"
    elif "view logs" in query01:
        link = f"localhost:4101/live"
    elif "view challan" in query01:
        link = f"localhost:4101/challan"
    elif "chalan" in query01:
        link = f"localhost:4101/challan"
    else:
        validate = 'please speak valid query'
        return render_template('indexaudio.html',user_img = pic01, name=validate)



#Returning link related user commands with Desired o/p
    return redirect('http://' +str(link))

if __name__=='__main__':
    app.run(debug= True, port = 5011)
