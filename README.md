## Example Python program about queues (W.I.P)

These are my experiments with ciw package used for queueing theory simulations


At the same time Im going to use this repo as good example for explaining 

* pre-commit hooks
* black formatter
* flake8 




## Queue terminology


  * First In First Out (FIFO): serve the customer who has been waiting for the longest time.


### Arrival rate, service rate, dropout rate

The most important notation:

  * λ: arrival rate. This measures how fast new items are coming into the queue.

  * μ: service rate. This measures how fast items in the queue are being handled.

  * σ: dropout rate. This measures how fast items are skipping out the queue unhandled.

Examples:

  * λ = μ means the arrival rate equals the service rate; the queue is staying the same size, other than dropouts.

  * λ > μ means the arrival rate is greater than the service rate; the queue is getting larger, other than dropouts.

  * λ < μ means the arrival rate is less than the service rate; the queue is getting smaller, other than dropouts.


### Utilization ratio

The most important notation that summarizes a queue:

  * ρ: utilization ratio = λ / μ

Examples:

  * ρ = 1 means the arrival rate is equal to the service rate; the queue is staying the same size.

  * ρ > 1 means the arrival rate is greater than the service rate; the queue is getting larger.

  * ρ < 1 means the arrival rate is less than the service rate; the queue is getting smaller.

  
### Little's Law

> Little's law is a theorem by John Little which states: the long-term average number L of customers in a stationary system
> is equal to the long-term average effective arrival rate λ multiplied by the average time W that a 
> customer spends in the system.

Example notation:

  * L is the long-term average number of customers in the system.

  * λ is the long-term average effective arrival rate.

  * W is the average time that a customer spends in the system.

  * L = λ W is Little's law.









