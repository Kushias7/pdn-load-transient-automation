import csv
from datetime import datetime
from instruments import PSU, ElectronicLoad, Oscilloscope

class LoadTransientTest:

    def __init__(self, psu, eload, scope):
        self.psu = PSU(psu)
        self.eload = ElectronicLoad(eload)
        self.scope = Oscilloscope(scope)

    def run(self, board_sn, steps):

        self.psu.setup()
        self.scope.configure()

        results = []

        for load in steps:
            self.eload.set_current(load)
            ripple = self.scope.measure_vpp()
            waveform = self.scope.capture_waveform()

            timestamp = datetime.now().isoformat()
            status = "PASS" if ripple < 0.05 else "FAIL"

            results.append([timestamp, board_sn, load, ripple, status])

            with open(f"waveform_{board_sn}_{load}.txt", "w") as f:
                f.write(waveform)

        with open(f"results_{board_sn}.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp","board_sn","load","vpp","status"])
            writer.writerows(results)

        return results