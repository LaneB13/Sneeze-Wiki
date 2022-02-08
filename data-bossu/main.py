# Made by Benji Lane
# email: benjiwolf08@icloud.com

# The main file: it starts the server

import api
from flask import Flask, render_template, request


def main():
    # commands()
    # server code

    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        return render_template('index.html')

    @app.route('/sneeze')
    def sneeze():
        name = request.args.get('search')
        if api.get_sneeze(name) != None:
            return render_template(
                'sneeze.html', title=api.get_title_of(name),
                body=api.get_body_of(name),
                upvotes=api.get_upvotes_of(name),
                creator=api.get_creator_of(name))

        return render_template('sneeze_not_found.html')

    @app.route('/create_sneeze')
    def create_sneeze():
        data = request.args.get('x')
        if data == None:
            return render_template('create_sneeze.html')

        with open('submissions/' + data.split('{\"name:\"')[0].split('\"')[3][0:]+'.json', 'w') as file:
            file.write(data)

        return render_template('thanks_for_submitting.html')

    app.run(port=8080)

    return


if __name__ == '__main__':
    main()
