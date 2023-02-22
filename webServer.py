from flask import Flask, request, redirect
import urllib.parse

app = Flask(__name__)

# Define a new route that will handle incoming HTTP requests
@app.route('/callback')
def callback():
    # Extract the authorization code from the query parameters
    code = request.args.get('code')

    # Construct the redirect URL that includes the authorization code
    redirect_uri = 'http://localhost:5000/callback'
    client_id = 'BOT_CLIENT_ID'
    client_secret = 'BOT_CLIENT_SECRET'
    scope = 'identify%20guilds'
    discord_auth_url = 'https://discordapp.com/api/oauth2/authorize?response_type=code&client_id={0}&scope={1}&redirect_uri={2}'
    discord_auth_url = discord_auth_url.format(client_id, scope, urllib.parse.quote(redirect_uri, safe=''))

    token_endpoint = 'https://discordapp.com/api/oauth2/token'
    redirect_uri = 'http://localhost:5000/callback'

    # Send the redirect response to the user's web browser or the Discord API
    response = redirect(discord_auth_url)
    return response

# Start the web server on port 5000
if __name__ == '__main__':
    app.run(port=5000, debug=True)