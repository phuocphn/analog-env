import pymaga
import os

from loguru import logger
from utils import get_circuit_tree


def synthesis_level2():
    if True:
        circuitInformation = pymaga.CircuitInformation()
        circuitParameter = pymaga.CircuitParameter()

        # set diffential amplifiers
        circuitParameter.setFullyDifferential(True)
        circuitInformation.setCircuitParameter(circuitParameter)
    else:
        circuitInformation = pymaga.CircuitInformation().init()

    # Initialize HL1
    deviceLevel = pymaga.DeviceLevel()

    differentialpairs = pymaga.DifferentialPair(deviceLevel)
    # print(differentialpairs)
    currentbiases = pymaga.CurrentBiases(deviceLevel)
    # print(currentbiases)

    voltagebiases = pymaga.VoltageBiases(deviceLevel)
    # print(voltagebiases)

    for idx, variant_name in enumerate(
        ["getAllVoltageBiasesPmos", "getAllVoltageBiasesNmos"]
    ):

        return_circuits = getattr(voltagebiases, variant_name)()

        for circuit in return_circuits:
            print(get_circuit_tree(circuit))
            print("++++++++++++++++++++++++")
        print("****************************************************" * 2)

        # write to file
        with open(
            f"library/HL2/vb/{idx}-{variant_name}-{len(return_circuits)}.log", "w"
        ) as fw:
            fw.write("\n--------------------------")
            fw.write(f"\n Variant Name: {variant_name}")
            fw.write(f"\n Number of circuits: {len(return_circuits)}")
            fw.write("\n--------------------------")

            for circuit in return_circuits:
                fw.write("\n")
                fw.write(get_circuit_tree(circuit))
                fw.write("\n++++++++++++++++++++++++")
            fw.write("\n" + "****************************************************" * 2)


if __name__ == "__main__":
    logger.info(f"current dir: {os.getcwd()}")
    synthesis_level2()
