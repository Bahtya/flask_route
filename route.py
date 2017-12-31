from flask import Flask

from flask import render_template                        import qrcode

from flask import request

app=Flask(__name__)

@app.route('/png.html',methods=['GET','POST'])

def png():

    char=request.form.get('char')

    imgi=qrcode.make(char)

    imgi.save('QR.png')

    return render_template('png.html')

@app.route('/QR.png')

def png_url():

    return open( 'QR.png','rb').read()

@app.route('/')                                                                                
def index():                                                                                          
    return render_template('index.html')                                                          
    app.run(host='0.0.0.0')
