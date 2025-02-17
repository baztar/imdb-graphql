from flask import Flask
from flask_graphql import GraphQLView

from .database import init_db, session
from .schema import schema
app = Flask(__name__)
app.Debug = True

default_query = '''
{
  movie(imdbID: "7040874") {
    imdbID
  }
}
'''.strip()

app.add_url_rule(
    '/imdb',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


if __name__ == '__main__':
    init_db()
    app.run()
