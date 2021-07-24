from flask import Flask, render_template, redirect, request 

import smtplib
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        subject = request.form['subject']
        name =  request.form['name']
        email = request.form['email']
        text =  request.form['message']
        
        # recebendo a mensagem enviado 
        msg = f'''Subject: {subject}\n\nNome: {name}\nEmail:({email})\n\n Mensagem:\n\n{text}'''
        
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("araujofabio2012@gmail.com", "dfbg hehk pmnq vkth")
        server.sendmail(email,"araujofabio2012@gmail.com", msg.encode('utf-8'))
        server.quit()
        
        # envio automático de confirmação 
        subject = 'Fábio Araujo - Developer'
        thanks = f'Subject: {subject}\nConfirmação de email recebido.\nObrigado por entrar em contato, {name}.\n\n\nCópia da sua Mensagem:\n {text}\n\nContatos:\nhttps://fharaujo.herokuapp.com/ \n\n GitHub: https://github.com/fharaujo\n\nLindedIn: https://www.linkedin.com/in/fharaujo/'
        
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("araujofabio2012@gmail.com", "dfbg hehk pmnq vkth")
        server.sendmail("araujofabio2012@gmail.com", email, thanks.encode('utf-8'))
        server.quit()
        
        
    return render_template('index.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)