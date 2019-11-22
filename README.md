# TA-Lib Service

This repository contains a service wrapper for the [TA-Lib](https://github.com/mrjbq7/ta-lib)
package. It makes the TA-Lib functions accessible through the use of
[RPyC](https://rpyc.readthedocs.io/en/latest/).

## Requirements
To use the TA-Lib service will require an installation of Python 3.5 or higher. You also need to
install [TA-Lib](http://ta-lib.org/). See the Troubleshooting section at
https://github.com/mrjbq7/ta-lib for more information.


## Installation
You can install the TA-Lib from PyPI:
```
pip install margin-talib-service
```
Or checkout the sources and run the setup.py file:
```
python setup.py install
```

## Starting the service
After the installation of the service, it can be started as follows:
```
margin-talib-service
```
or
```
python -m margin_talib_service
```

The usage includes a parameter port that is set to a default value.
```
usage: margin-talib-service [-h] [-p PORT]

Start a service that grants access to TA-Lib for margin strategies.

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Specify the port that the service is binding to.
```

You may need to specify the port, if the default port is already in use. The service will
indicate this with the following error message:
```
Creating server on port 18861
Chosen port 18861 on localhost is already in use, please specify a different port.
```

Starting the service correctly will result in the following output:
```
Creating server on port 18861
Starting TA-Lib service...
```

<a name="accessing"></a>
## Accessing the service
In your margin Python Strategy add
```
import rpyc
TALIB_SERVICE_PORT=18861
connection = rpyc.connect("localhost", TALIB_SERVICE_PORT)
talib = connection.root
np = talib.remote_np()
```
to the top. For margin to find the rpyc package you will have to link or copy the package into 
`.margin/python-packages` in your user home folder depending on your OS.

If you specified a different port before when starting the service, adapt the variable
`TALIB_SERVICE_PORT` accordingly.

You can now access all the functions of the TA-Lib through the `talib` variable:
```
close = np.random.random(100)
result = talib.SMA(close)
```

**Note: The forwarding to the TA-Lib service only works with the forwarded numpy that is
created by `np = talib.remote_np()`. Do not use a locally included numpy version for this.**


## Troubleshooting
If your Python Strategy shows the error
```
TypeError: Argument 'real' has incorrect type (expected numpy.ndarray, got numpy.ndarray)
```
you must be using a different numpy version than the TA-Lib service.
Ensure that you follow all the steps in [Accessing the service](#accessing-the-service) and then
only use the remote numpy defined in the variable `np` instead of including numpy locally.
