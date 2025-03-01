from flask import  render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm, ForgotPass
from flaskblog import app
from flaskblog.models import User, Post

posts = [
    {
        'author': "John Doe",
        'title': "Introduction to Python",
        "content": "Python is a versatile programming language used for various applications such as web development, data analysis, and machine learning.",
        "date_posted": "2025-02-01"
    },
    {
        'author': "Jane Smith",
        'title': "Top 10 JavaScript Frameworks",
        "content": "Explore popular frameworks like React, Vue, and Angular to enhance your web development projects.",
        "date_posted": "2025-02-02"
    },
    {
        'author': "Michael Brown",
        'title': "Why Cybersecurity Matters",
        "content": "Learn the importance of safeguarding your digital assets in today's interconnected world.",
        "date_posted": "2025-02-03"
    },
    {
        'author': "Emily White",
        'title': "AI in Healthcare",
        "content": "Artificial Intelligence is revolutionizing healthcare by improving diagnostics and personalized treatments.",
        "date_posted": "2025-02-04"
    },
    {
        'author': "David Green",
        'title': "Best Coding Practices",
        "content": "Writing clean and maintainable code is essential for long-term project success.",
        "date_posted": "2025-02-05"
    },
    {
        'author': "Sophia Black",
        'title': "Understanding Blockchain",
        "content": "Blockchain is the backbone of cryptocurrencies and has potential applications in various industries.",
        "date_posted": "2025-02-06"
    },
    {
        'author': "Daniel Garcia",
        'title': "Guide to Remote Work",
        "content": "Tips and tools for staying productive while working from home.",
        "date_posted": "2025-02-07"
    },
    {
        'author': "Olivia Turner",
        'title': "Exploring Space Technologies",
        "content": "The advancements in space technology are opening new frontiers for exploration.",
        "date_posted": "2025-02-08"
    },
    {
        'author': "Liam Carter",
        'title': "The Rise of FinTech",
        "content": "FinTech is changing how we manage our finances with innovative solutions.",
        "date_posted": "2025-02-09"
    },
    {
        'author': "Ava Martinez",
        'title': "Ethical AI: A Discussion",
        "content": "As AI grows more powerful, ensuring ethical practices in its deployment becomes crucial.",
        "date_posted": "2025-02-10"
    },
    {
        'author': "Ethan Wilson",
        'title': "Cloud Computing Essentials",
        "content": "Cloud computing has revolutionized how businesses manage their IT infrastructure.",
        "date_posted": "2025-02-11"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account Created for {form.username.data}!", "success")
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "james@mail.com" and form.password.data == "123456":
            flash(f"Logged in successfully", "success")
            return redirect(url_for('home'))
        else:
            flash(f"Login Unsuccessful. Please Try Again!", "danger")
            return redirect(url_for('login'))

    return render_template('login.html', title='Login',form=form) 

@app.route("/forgot_password", methods=['GET','POST'])
def forgotPass():
    form = ForgotPass()
    if form.validate_on_submit():
        flash(f"Password Reset Successfully", "success")
        return redirect(url_for('home'))
    return render_template('forgotPass.html', title='Forgot Password', form=form)
    # else:
    #     flash(f"Unable to Reset Your Password", "danger")
    #     return redirect(url_for('forgotPass'))