from flask import Flask, render_template, request 

import smtplib

from werkzeug.utils import redirect


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
        server.login("araujofabio2012@gmail.com", "flamengo2019")
        server.sendmail(email,"araujofabio2012@gmail.com", msg.encode('utf-8'))
        
        
        # envio automático de confirmação 
        thanks = f'Confirmação de email recebido.\nObrigado por entrar em contato, {name}. \n\n'
        
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("araujofabio2012@gmail.com", "flamengo2019")
        server.sendmail("araujofabio2012@gmail.com", email, thanks.encode('utf-8'))
        
        
    return redirect('/')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)