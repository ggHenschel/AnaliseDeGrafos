import networkx as nx
import matplotlib.pyplot as plt
from xml.dom import minidom

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

def ImportPetri(path):
    xlmdoc = minidom.parse(path)

    transitionlist = xlmdoc.getElementsByTagName('transition')
    placelist = xlmdoc.getElementsByTagName('place')
    edgelist = xlmdoc.getElementsByTagName('arc')
    Graph = nx.DiGraph()

    print(len(edgelist))

    Dict = {0:0}

    for transition in transitionlist:
        #print(transition.attributes['id'].value,getText(transition.getElementsByTagName('name')[0].getElementsByTagName('text')[0].childNodes))
        Dict.update({transition.attributes['id'].value:getText(transition.getElementsByTagName('name')[0].getElementsByTagName('text')[0].childNodes)})
        Graph.add_node(getText(transition.getElementsByTagName('name')[0].getElementsByTagName('text')[0].childNodes))

    for place in placelist:
        if place.attributes.getNamedItem('id')!=None:
            #print(place.attributes['id'].value)
            Dict.update({place.attributes['id'].value:getText(place.getElementsByTagName('name')[0].getElementsByTagName('text')[0].childNodes)})
            Graph.add_node(getText(place.getElementsByTagName('name')[0].getElementsByTagName('text')[0].childNodes))


    for edge in edgelist:
        #print(edge.attributes['source'].value,edge.attributes['target'].value)
        Graph.add_edge(Dict[edge.attributes['source'].value],Dict[edge.attributes['target'].value])

    # print(Graph.nodes(data=True))
    # print(Graph.edges())
    #
    # nx.draw_networkx(Graph,pos=nx.spectral_layout(Graph),with_labels=False)
    # nx.draw_networkx_labels(Graph,pos=nx.spectral_layout(Graph))
    # plt.draw()
    # plt.show()
    return (Graph,Dict)