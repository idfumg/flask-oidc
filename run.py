from flask import Flask, abort, session, g
from flask.ext.oidc import OpenIDConnect

app = Flask(__name__)

app.config['SECRET_KEY'] = 'very_secret_key'

app.config['OIDC_CLIENT_SECRETS'] = './client_secrets.json'
app.config['OIDC_ID_TOKEN_COOKIE_SECURE'] = False
app.config['OIDC_ID_TOKEN_COOKIE_NAME'] = 'oidc_id_token'
app.config['OIDC_ID_TOKEN_COOKIE_TTL'] = 60

oidc = OpenIDConnect(app, {})

@app.route('/login/')
@oidc.check
def login():
    email = g.oidc_id_token['email']

    if not email:
        return abort(404)

    session['email'] = email
    return "You was authorized as %s" % (email,)

if __name__ == '__main__':
    app.run(debug=True)
