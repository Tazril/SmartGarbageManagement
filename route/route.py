from influxdb import InfluxDBClient
client = InfluxDBClient(host='172.17.0.1', port=8086, username='telegraf', password='telegraf')
client.switch_database('dustbins')

# Get all dustbin measurements from the database dusbins
all_dustbins = client.get_list_measurements()
cc = [ r['name'] for r in all_dustbins if r['name'][:7] == "dustbin"]
cd = {}

# filter all dustbins havinf fill percentage above 90
for dustbin in cc:
	res = client.query('SELECT * FROM %s order by desc LIMIT 1'% dustbin)
	res = list(res)[0][0]['fill%']
	if res > 90:
		cd[dustbin] = res
		# print(res)
print(cd)

# Notify by sms to the desired recipent (Cleaning Office) about the dustbins to be cleared
import requests

url = "https://www.fast2sms.com/dev/bulk"
mobile = 8503934XXX
message = " Clean in order " + str(res)
print(message)
payload = {'sender_id': 'FSTSMS', 'numbers': mobile, 'message': message, 'flash': 0, 'language':'english','route':'p'}

headers = {
    'authorization': "<AuthToken>",
    'cache-control': "no-cache",
    'content-type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

# Using Travelling Salesman Problem Solving approach to find shortest route to cover all dustbins

import mlrose, random
import numpy as np

N = len(cd)
dist_list = []
dd = list(cd.keys())
print(dd)

# Mocking distance list between all dustbins
for i in range(N):	
	for j in range(i+1,N):
		dist_list.append((i,j,random.randint(10,1000)))

print(dist_list)

# Initialize fitness function object using dist_list
fitness_dists = mlrose.TravellingSales(distances = dist_list)
problem_fit = mlrose.TSPOpt(length = N, distances = dist_list, maximize=False)
best_state, best_fitness = mlrose.genetic_alg(problem_fit, random_state = 2)
res = [ dd[i] for i in best_state]
print(res)




#Plotting the dustbin as node graph to show the path
import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
mm = {}
for i in range(len(dd)):	mm[i]=dd[i]
# print(mm)

ls = []
for i in range(1,len(res)):
	ls.append((res[i-1],res[i]))

ls.append((res[0],res[-1]))
G.add_edges_from(ls)

H=nx.relabel_nodes(G,mm,copy=True)
# print(H.edges())
nx.draw_networkx(H)
plt.savefig("simple_path.png") # save as png
plt.show() # display

