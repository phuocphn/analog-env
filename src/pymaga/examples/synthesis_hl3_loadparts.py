import pymaga
import os

from loguru import logger
from utils import get_circuit_tree


def synthesis_level3():
    if True:
        circuitInformation = pymaga.CircuitInformation()
        circuitParameter = pymaga.CircuitParameter()

        # set diffential amplifiers
        circuitParameter.setFullyDifferential(True)
        circuitInformation.setCircuitParameter(circuitParameter)
    else:
        circuitInformation = pymaga.CircuitInformation().init()

    # initilize HL1
    deviceLevel = pymaga.DeviceLevel()

    # initilize HL2
    structuralLevel = pymaga.StructuralLevel(deviceLevel, circuitInformation)

    transconductances = pymaga.Transconductances(structuralLevel, circuitInformation)
    transconductances.initializeAllTransconductances(structuralLevel)
    # print(transconductances)

    """
    **Stage Bias**
    - Function: A stage bias supplies a transconductance with defined current. 
    - There are two types exist, but in the current implementation, we only have stage biases with current output.
    """
    stagebiases = pymaga.StageBiases(structuralLevel)
    # print(stagebiases)

    loadparts = pymaga.LoadParts(structuralLevel)
    # print(loadparts)

    # amplificationStagesSubBlockLevel = pymaga.AmplificationStagesSubBlockLevel(
    #     structuralLevel, circuitInformation
    # )
    # loads = pymaga.Loads(amplificationStagesSubBlockLevel)
    # # print(loads)

    variants = [
        "createTwoTransistorsLoadPartsLoadPartsPmosVoltageBiases",
        "createFourTransistorsLoadPartsLoadPartsPmosVoltageBiases",
        "createTwoTransistorsLoadPartsLoadPartsNmosVoltageBiases",
        "createFourTransistorsLoadPartsLoadPartsNmosVoltageBiases",
        "createLoadPartsPmosTwoTransistorCurrentBiasesDifferentSources",
        "createLoadPartsNmosTwoTransistorCurrentBiasesDifferentSources",
        "createLoadPartsPmosFourTransistorCurrentBiases",
        "createLoadPartsNmosFourTransistorCurrentBiases",
        "createLoadPartsPmosCurrentBiases",
        "createLoadPartsNmosCurrentBiases",
        "createLoadPartsPmosVoltageBiases",
        "createLoadPartsNmosVoltageBiases",
        "createLoadPartsPmosMixed",
        "createLoadPartsNmosMixed",
        "createLoadPartsPmosFourTransistorMixed",
        "createLoadPartsNmosFourTransistorMixed",
    ]
    for idx, variant in enumerate(variants):
        loadpart = getattr(loadparts, variant)()
        # print(loadpart)
        variant_name = variant.replace("create", "")
        print("\n--------------------------")
        print(f"\n Variant Name: {variant_name}")
        print(f"\n Number of circuits: {len(loadpart)}")
        print("\n--------------------------")

        for circuit in loadpart:
            print(get_circuit_tree(circuit))
            print("++++++++++++++++++++++++")
        print("****************************************************" * 2)

        # write to file
        with open(
            f"library/HL3/loadparts/{idx}-{variant_name}-{len(loadpart)}.log", "w"
        ) as fw:
            fw.write("\n--------------------------")
            fw.write(f"\n Variant Name: {variant_name}")
            fw.write(f"\n Number of circuits: {len(loadpart)}")
            fw.write("\n--------------------------")

            for circuit in loadpart:
                fw.write("\n")
                fw.write(get_circuit_tree(circuit))
                fw.write("\n++++++++++++++++++++++++")
            fw.write("\n" + "****************************************************" * 2)


if __name__ == "__main__":
    logger.info(f"current dir: {os.getcwd()}")
    synthesis_level3()
