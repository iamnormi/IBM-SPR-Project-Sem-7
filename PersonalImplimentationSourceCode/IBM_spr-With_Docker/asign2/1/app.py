from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("user")
        email = request.form.get("email")
        phone = request.form.get("phone")
        return   "Name is : " + name + ", \nEmail is : " + email +   ", Mobile Number is : "+ phone
    return render_template("register.html")

if __name__=='__main__':
    app.run()
