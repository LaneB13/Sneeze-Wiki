# Made by Benji Lane
# email: benjiwolf08@icloud.com

# is used if you want to add anything to the data base manualy but not archaic

import api


def commands():
    i = input()

    if i == 'quit':
        return
    elif i == 'new':
        name = input('name: \n')
        print()
        title = input('title: \n')
        print()
        print()
        body = input('body: \n')

        api.new_sneeze(name, title, body)
    elif 'search ' in i:
        si = i.split('search ')[1]
        if api.get_sneeze(si) != None:
            print(api.get_title_of(si))
            print(api.get_body_of(si))
            print('upvotes:', api.get_upvotes_of(si))

            up_or_down = input('upvote/downvote: (u/d/n)\n')

            if 'u' in up_or_down:
                api.upvote(si)
            elif 'd' in up_or_down:
                api.downvote(si)

    print()
    commands()


if __name__ == '__main__':
    commands()
