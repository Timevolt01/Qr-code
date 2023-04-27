from flask import Flask, request, make_response
import qrcode
import io

app = Flask(__name__)

@app. route('/qr', methods=[ 'GET' ] )
def qr():
    # Get the URL from the query string
    url = request.args.get( 'url')

    # Create a QR code image
    img = qrcode.make(url)
    # Save the QR code image to a buffer
    buffer = io.BytesIO()
    img.save(buffer, forjat= 'PNG')
    buffer.seek(0)

    # Create the response object
    response = make_response(buffer.getvalue())
    response.mimetype ='image/png'
   
    # Return the response
    return response

if __name__=="__main__":
    app.run()