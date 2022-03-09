import pyvisa
import time
import numpy as np
import pandas as pd

class Instrument2400:

    def __init__(self):
        self.rm = pyvisa.ResourceManager()
        self.inst = self.rm.open_resource()
        if self.inst.write("*rst") == 6:
            print("The instrument is connected")

    def setup_parameters(self, curr, voltage):
        
