from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import collections
import itertools
import difflib
import pickle
import glob

authors_names = glob.glob("titles_authors/authors*")
titles_path = glob.glob("titles_authors/titles*")

authors = []
for author_name in authors_names:
    with open(author_name,"rb") as f:
        dat = pickle.load(f)    
    authors+=dat
titles = []
for author_name in titles_path:
    with open(author_name,"rb") as f:
        dat = pickle.load(f)    
    titles+=dat

print(len(titles))
print(len(authors))

auts = []
for author_list in authors:
    auts+=author_list

auts_set = set(auts)
auts_list = list(auts_set)

G = nx.Graph()

id_to_authors_dict = {idx:elem for idx, elem in enumerate(auts_list)}
authors_to_id_dict = {elem:idx for idx, elem in enumerate(auts_list)}

for idx, elem in enumerate(authors):
    if idx%10000 == 0:
        print(idx)
    if len(elem)>1:
        comb_list = list(itertools.combinations(elem, 2))
        for combination in comb_list:
            G.add_edge(authors_to_id_dict[combination[0]],authors_to_id_dict[combination[1]])
            
giant = max(nx.connected_components(G), key=len)

def you_in_largest(giant, name):
    try:
        au1 = authors_to_id_dict[name]
    except:
        raise KeyError(f"No person {name} found in authors")
    return au1 in giant

def shortest_path(G, giant, name_1, name_2):
    au1 = ""
    au2 = ""
    if name_1 in authors_to_id_dict:
        au1 = authors_to_id_dict[name_1]
    else:
        au1 = "UNKNOWN"
    if name_2 in authors_to_id_dict:
        au2 = authors_to_id_dict[name_2]
    else:
        au2 = "UNKNOWN"
    if au1 == "UNKNOWN":
        return True, f"First Author {name_1} Not Found!"
    if au2 == "UNKNOWN":
        return True, f"Second Author {name_2} Not Found!"
    try:
        path = nx.shortest_path(G, au1, au2)
        return False, [id_to_authors_dict[idx] for idx in path]
    except:
        name = ""
        if not you_in_largest(giant, name_1):
            name = " "+name_1
        if not you_in_largest(giant, name_2):
            if len(name)>0:
                name = ", and "+name_2
            else:
                name = au2
        return False, f"Can't Find a Path! {name} not in the largest graph and both not in the same subgraph."


def find_closest_name(auts_list, input_name, elements=1):
    return difflib.get_close_matches(input_name, auts_list)[:elements]
    
app = Flask(__name__)


@app.route("/")
def my_form():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def my_form_post():
    status_authors = None
    res = None

    first_author = request.form['fauthor']
    second_author = request.form['sauthor']
    try:
        search_bt = request.form['search_bt']
    except:
        search_bt = None

    names = None
    is_valid_path = False

    if search_bt is None:
        status_authors, res = shortest_path(G, giant, first_author, second_author)

        if not status_authors and not isinstance(res, str):
            res = "->".join(res)
            is_valid_path = True
    else:
        names = find_closest_name(auts_list, search_bt, 3)
        print(f' searching for {search_bt} found {names}')

    return render_template('index.html', sequencia = res, search=status_authors, closest_names=names, \
                            search_name=search_bt, is_valid_path=is_valid_path)

@app.route("/search", methods=['POST'])
def search():
    search_bt = request.form['search_bt']
    names = None

    names = find_closest(auts_list, search_bt, 3)

    return render_template('index.html', sequencia = res, search=status_authors, closest_names=names)



if __name__ == "__main__":
    app.run()#debug=True)
