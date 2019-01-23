from sanic import Sanic, response

from mission.run import (html_parser,
                         get_games_app_category,
                         get_games_app_names)


app = Sanic()
URL = 'https://play.google.com/store/apps/category/GAME'


@app.route('TEST/test.html', methods=frozenset(('GET', )))
async def test(request):
    return response.html('\n'.join(list(html_parser())))


@app.route('', methods=frozenset(('GET', )))
async def search(request):
    search = request.args.get('search', [])
    if not search:
        return response.json({'result': True})

    search = search[0]
    categories = [category for category in get_games_app_category(URL)()
                  if search in category]
    games = [game for game in get_games_app_names(URL)()
             if search in game]
    return response.json({'categories': categories, 'games': games})



def start():
    app.run(host="0.0.0.0", port=8002)
