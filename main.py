from flask import Flask,render_template,url_for,redirect,request
from base import get_connection

app = Flask (__name__)

@app.route('/accept/')
def accept():
    return render_template("accept.html")



@app.route("/sign up/", methods = ["GET","POST"])
def sign_up():
    if request.method == "POST":
        
        username = request.form.get("username")
        password = request.form.get("password")
        repeat_password = request.form.get("repeat_password")
        email_address = request.form.get("email_address")

        db = get_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM user WHERE username = ?", (username,))
        name = cursor.fetchone()

        if name is None:
            if password == repeat_password:
                cursor.execute("INSERT INTO user (username,password,repeat_password,email_address) VALUES (?,?,?,?)", (username,password,repeat_password,email_address))
                db.commit()
                cursor.close()

                return redirect(url_for('sign_in'))
            else:
                error = "Repeat password error !"
                return render_template('sign_up.html',error = error)
            
        else:
            usererror = "Bu username bant !"
            return render_template('sign_up.html',usererror = usererror)

        

    return render_template("sign_up.html", sign_up = "active", Title = "Sign up")



@app.route("/")
@app.route("/sign in/", methods = ["GET","POST"])
def sign_in():
    if request.method == "POST":
        
        username = request.form.get("username")
        password = request.form.get("password")

        db = get_connection()
        cursor = db.cursor()
        
        cursor.execute("SELECT * FROM user WHERE username = ?", (username,))
        user = cursor.fetchone()


        if user is not None:
            if user[2] == int(password):
                return redirect(url_for('accept'))
            else:
                return redirect(url_for('sign_up'))
                
        else:
            return redirect(url_for('sign_up'))
            
        
    return render_template("index.html", sign_in = 'active',Title = "Sign in")



if __name__ == "__main__":
    app.run()

        
            

        
        
