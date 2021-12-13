import networkx as nx
import pygeoip
import sys

def load_and_display_file(graph_fn, dat_fn):
        graph1 = nx.read_graphml(graph_fn)
        # graph1 = nx.read_graphml('127.0.1.1_l14340.cs.jmu.edu_2018-03-18-06-45-12-700579-bitcoingraph-cleaned.graphml')
        all_nodes = graph1.nodes()
        dat = dat_fn

        # node count
        print('1.) How many Bitcoin nodes does the Bitcoin network in the data file have? ')
        print()
        print(' ', len(all_nodes))
        print()

        all_edges = graph1.edges()

        # edge count
        print('2.) How many edges does the Bitcoin network in the data file have? ')
        print()
        print(' ', len(all_edges))
        print()

        # loop for largest node degrees
        max = 0
        max_list = []
        print('3.) What is the largest node degree? Which node(s) have this degree? ')
        print()
        for i in all_nodes:
                if (graph1.degree(i) > max):
                        max = graph1.degree(i)
                        max_list.append(i)
                        max_node = i

        print(" Node:", max_node, "Degree:", graph1.degree(max_list[-1]))
        print()

        # loop for smallest node degrees
        min = 0
        min_list = []
        print('4.) What is the smallest node degree? Which node(s) have this degree? ')
        print()
        for j in all_nodes:
                if (graph1.degree(j) <= min):
                        min = graph1.degree(j)
                        min_list.append(j)
        for min_node in min_list:
                print(" Node:", min_node, "Degree:", graph1.degree(min_node))
        print()

        # top ten nodes with highest degree (descending order)
        print('5.) Find out the 10 nodes that have the highest degrees. For each node, print in descending order of degrees')
        print()
        dict = {}
        ip = []
        degree = []
        for node in all_nodes:
                ip.append(node)
                degree.append(graph1.degree(node))
        for i in range(len(all_nodes)):
                dict[ip[i]] = degree[i]
        sort = sorted(dict.items(), key = lambda x: x[1], reverse=True)
        for i in range(10):
                print("Node: ", sort[i][0], "Degree: ", sort[i][1], "Country: ", lookup(sort[i][0], dat))
        print()

        # top 5 countries with highest node count , in descending order of nodes
        print('6.) Find the 5 countries that have the highest number of Bitcoin nodes. For each country, print in descending order of nodes')
        print()
        degree2 = []
        for node in all_nodes:
                degree2.append(lookup(node, dat))

        country_count = {}
        for node in degree2:
                countries = country_count.keys()
                i = 0
                for k in countries:
                        if str(node) == k:
                                country_count[str(node)] = country_count[str(node)] + 1
                                i = 1
                if i == 0:
                        country_count.update({str(node): 1})

        sorted_countries = sorted(country_count.items(), key = lambda item: item[1], reverse=True)
        for i in range(5):
                print(str(sorted_countries[i]))
        print()

def lookup(inIP, dat_fn):
        GEOIP = pygeoip.GeoIP(dat_fn, pygeoip.MEMORY_CACHE)
        country = GEOIP.country_name_by_addr(inIP)
        return country

def main():
        arg_num = len(sys.argv)
        if arg_num == 1:
                return
        load_and_display_file(sys.argv[1], sys.argv[2])

if __name__=="__main__":
    main()