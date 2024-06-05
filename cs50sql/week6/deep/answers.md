# From the Deep

In this problem, you'll write freeform responses to the questions provided in the specification.

## Random Partitioning

The advantage of random partitioning is the distribution of the data is evenly distributed to each server. The disadvantage is query have to be run on all server everytime which increase query time and defeating the purpose of sharding.

## Partitioning by Hour

The advantage of partitioning by hour is data easily found and you can run query on a single server which mean low query time and doesn't overload other server. The disadvantage some hours has more data than other hours the server that host the most data will be overload.

## Partitioning by Hash Value

The advantage of partitioning by hash value is the data will be distributed evenly and also easy to find which mean you only need query one server. The disanvatage is either more cpu power needed for hashing the timestamp each query or more space needed to store hash table for timestamp.
