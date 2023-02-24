from flask import Flask, request, redirect
#import urllib.parse
import urlparse

app = Flask(__name__)

# Define a new route that will handle incoming HTTP requests
@app.route('/callback')
def callback():
    # Extract the authorization code from the query parameters
    code = request.args.get('code')

    # Construct the redirect URL that includes the authorization code
    redirect_uri = 'https://perfect-super-andesaurus.glitch.me/callback'
    client_id = '1077998429097181184'
    client_secret = 'gR_5nyVCdeai86ly1eryVC4V4DgcbX9v'
    scope = 'https://discord.com/api/oauth2/authorize?client_id=1077998429097181184&permissions=274877975616&scope=bot'
    discord_auth_url = 'https://discordapp.com/api/oauth2/authorize?response_type=code&client_id={0}&scope={1}&redirect_uri={2}'
    discord_auth_url = discord_auth_url.format(client_id, scope, urllib.parse.quote(redirect_uri, safe=''))

    token_endpoint = 'https://discordapp.com/api/oauth2/token'

    # Send the redirect response to the user's web browser or the Discord API
    response = redirect(discord_auth_url)
    return response

# Start the web server on port 5000
if __name__ == '__main__':
    app.run(port=5000, debug=True)