import ciw
import matplotlib.pyplot as plt

N = ciw.create_network(
    Arrival_distributions=[["Exponential", 0.2]],
    Service_distributions=[["Exponential", 0.1]],
    Number_of_servers=[3],
)
ciw.seed(1)
Q = ciw.Simulation(N)
Q.simulate_until_max_time(1440)
recs = Q.get_all_records()
waits = [r.waiting_time for r in recs]
avgwaits = sum(waits) / len(waits)
print(avgwaits)
plt.hist(waits)
plt.show()
