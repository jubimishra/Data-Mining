Building a classifier to detect network intrusions

You are going to build a network intrusion detection, a predictive classifier capable of distinguishing intrusions, attacks, or bad connections from good, normal connections.

Each line in the training and test files summarizes one connection record. A connection is a sequence of network packets starting and ending at some well defined times, between which data flows to and from a source IP address to a target IP address under some well defined protocol. Each connection is labeled as either normal, or as an attack, with exactly one specific attack type. Attacks fall into three main categories:

DOS: denial-of-service, e.g. synchronized flooding;
R2L: unauthorized access from a remote machine, e.g. guessing password;
Probing: surveillance and other probing, e.g., port scanning.
Specifically, in the given dataset, there are eight types of attacks and a ninth class to indicate normal connections, as described below: 

Class Label	Attack category
back	DOS
ipsweep	Probing
neptune	DOS
portsweep	Probing
satan	Probing
smurf	DOS
teardrop	DOS
warezclient	R2L
Each connection record consists of features derived from a network connection and the packets transferred during that connection. The training file (train_id.csv) consists of 43 comma-separated values: a connection ID field, 41 features related to the connection, and one of the nine class labels listed above. Each line in the test file (test_id_unlabeled.csv) contains 42 comma-separated values (connection ID and 41 features). Note that the distribution of the categories may be different in the training and test datasets.