import pyvisa

class PSU:
    def __init__(self, resource):
        self.rm = pyvisa.ResourceManager()
        self.inst = self.rm.open_resource(resource)

    def setup(self, voltage=5, current=3):
        self.inst.write(f"VOLT {voltage}")
        self.inst.write(f"CURR {current}")
        self.inst.write("OUTP ON")

class ElectronicLoad:
    def __init__(self, resource):
        self.rm = pyvisa.ResourceManager()
        self.inst = self.rm.open_resource(resource)

    def set_current(self, current):
        self.inst.write(f"CURR {current}")

class Oscilloscope:
    def __init__(self, resource):
        self.rm = pyvisa.ResourceManager()
        self.inst = self.rm.open_resource(resource)

    def configure(self):
        self.inst.write(":TIMebase:SCALe 1e-3")
        self.inst.write(":CHAN1:SCALe 0.5")
        self.inst.write(":TRIGger:EDGE:SOURce CHAN1")

    def measure_vpp(self):
        return float(self.inst.query(":MEASure:VPP? CHAN1"))

    def capture_waveform(self):
        data = self.inst.query(":WAV:DATA?")
        return data