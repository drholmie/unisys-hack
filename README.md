# unisys-hack

### dist-test

`dist-test.py` is used to test out how different sampling rates can be compared. Using approximate computing, we change
the sampling rate to user specified constraints. The one we use here is to trade off between energy and time, the constraint
is the confidence level of the hypothesis that the distributions are the same. To know more about how this is done click [here](https://stats.stackexchange.com/questions/354035/how-to-compare-the-data-distribution-of-2-datasets)

We use the traffic datasets from citypulse to simulate an IoT environment for traffic. In the completed demo, the first few runs
of the samping will be done to calibrate it to the right user specified level of trade off between energy and accuracy of data
collection. After its calibrated, it continues running in the enery efficient mode.

### Prerequisites:

- Openwhisk
- Perf
- Ubuntu 18.04
- Python 3.5+
- Flask
- Ansible

### Instructions to use (without using openwhisk)

- Run files `smart.py` and `traffictest.py`in separate terminals
