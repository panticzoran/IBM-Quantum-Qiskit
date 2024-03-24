# Simple test that connets IBM Quantum infrastructure via the access channel using your 
# credentials, and prints the Qiskit version

import os

import qiskit
from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService(channel = "ibm_quantum", 
                               token =  os.environ['IBM_ACCESS_TOKEN'])

# Prints out the Qiskit version
print(qiskit.__version__)