# Made by Benji Lane
# email: benjiwolf08@icloud.com

# This code edits the data base (note data base files are stored in xml)

import os


# getting things from the data base

def get_sneeze(name):
    cname = name.replace(' ', '_')

    try:
        with open(f'sneezes/{cname}.xml', 'r') as f:
            return f.read()
    except:
        return


def get_title_of(name):
    try:
        sneeze = get_sneeze(name)
        return sneeze.split('title')[1].split('<')[0][1:]
    except:
        return


def get_body_of(name):
    try:
        sneeze = get_sneeze(name)
        return sneeze.split('body')[1].split('<')[0][1:]
    except:
        return


def get_upvotes_of(name):
    try:
        sneeze = get_sneeze(name)
        return sneeze.split('upvotes')[1].split('<')[0][1:]
    except:
        return


def get_creator_of(name):
    try:
        sneeze = get_sneeze(name)
        return sneeze.split('creator')[1].split('<')[0][1:]
    except:
        return


# putting things in the data base

def new_sneeze(name, title, body):
    try:
        if os.path.exists(f'sneezes/{name}.xml'):
            return 'that sneeze already exists'
    except:
        return

    cname = name.replace(' ', '_')

    with open(f'sneezes/{cname}.xml', 'w') as f:
        try:
            f.write(f'<title>{title}</title>\n')
            f.write(f'<body>{body}</body>\n')
            f.write(f'<upvotes>0</upvotes>\n')
        except:
            return


def upvote(name):
    try:
        new_upvote = int(get_upvotes_of(name)) + 1

        with open(f'sneezes/{name}.xml', 'r') as f:
            read = f.read()

        with open(f'sneezes/{name}.xml', 'w') as f:
            f.write(read.replace(read.split('upvotes')[1].split('<')[0][1:], str(new_upvote)))
    except:
        return


def downvote(name):
    try:
        new_upvote = int(get_upvotes_of(name)) - 1

        with open(f'sneezes/{name}.xml', 'r') as f:
            read = f.read()

        with open(f'sneezes/{name}.xml', 'w') as f:
            f.write(read.replace(read.split('upvotes')[1].split('<')[0][1:], str(new_upvote)))
    except:
        return
