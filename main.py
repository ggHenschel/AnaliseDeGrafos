import xmlImport as x
import networkx as nx
import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.widget import  Widget

class AnaliseDeGrafos(Widget):
    G = nx.DiGraph()
    def RunGraphDraw(self):
        path = self.f_path.text
        (G, D) = x.ImportPetri(path)
        print(nx.shortest_path(G, "source 1", "Archive claim"))
        nx.draw_networkx(G)
        plt.draw()
        plt.show()


class AnalisadorDeGrafosApp(App):
    def build(self):
        return AnaliseDeGrafos()



if __name__=='__main__':
    AnalisadorDeGrafosApp().run()

# (G,D) = x.ImportPetri('testePetri.pnml')
#
# print(nx.shortest_path(G,"source 1","Archive claim"))
#
# nx.draw_networkx(G)
# plt.draw()
# plt.show()
