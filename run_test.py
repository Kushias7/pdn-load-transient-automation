from src.load_transient_test import LoadTransientTest

if __name__ == "__main__":

    psu = "USB::0x05E6::2230::INSTR"
    load = "USB::0x05E6::2380::INSTR"
    scope = "USB::0x0957::DSOX6004A::INSTR"

    test = LoadTransientTest(psu, load, scope)

    loads = [0.5, 1.5, 2.5]

    result = test.run("SN001", loads)

    print(result)