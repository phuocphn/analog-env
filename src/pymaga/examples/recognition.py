import pymaga
import os
import glob

from loguru import logger
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=str)
args = parser.parse_args()


def recognize(circuit: pymaga.Circuit, fname) -> pymaga.StructRecResult:
    print("[B] Structure Result".center(100, "*"))
    structRec_inst = pymaga.StructRec()
    structureLib: pymaga.StructRec = structRec_inst.createStructureLibrary(
        "StructRec/xml/AnalogLibrary.xml",
        "examples/StructureRecognition/deviceTypes.xcat",
    )
    structureResult = structureLib.recognize(circuit)
    print(structureResult)
    structureResult.writeXml(fname)
    print("[E] Structure Result".center(100, "*"))


def process_structural_recognition(fname, output_dir="outputs/"):
    structrec_fname = os.path.join(
        output_dir,
        os.path.basename(fname).replace(".ckt", "_structure_result.xml"),
    )

    circuit = pymaga_io.readInCircuit(
        circuit_filepath=fname,  # "examples/StructureRecognition/input.ckt",
        supplynet_filepath="examples/StructureRecognition/supplyNets.xcat",
        mapping_filepath="examples/StructureRecognition/HSpiceMapping.xcat",
        devicetype_filepath="examples/StructureRecognition/deviceTypes.xcat",
    )
    recognize(circuit, structrec_fname)


def write_partitioning_result(circuit: pymaga.Circuit, save_path):
    circuitAnalysis = pymaga.CircuitAnalysis()
    partitioningResult = circuitAnalysis.getPartitioningResult(circuit)
    print(partitioningResult)
    partitioningResult.writeXmlPartitioningResult(save_path)


def process_partitioning(
    fname,
    output_dir="outputs/",
):
    partitioning_fname = os.path.join(
        output_dir,
        os.path.basename(fname).replace(".ckt", "_partioning_result.xml"),
    )

    circuit = pymaga_io.readInCircuit(
        circuit_filepath=fname,  # "examples/StructureRecognition/input.ckt",
        supplynet_filepath="examples/StructureRecognition/supplyNets.xcat",
        mapping_filepath="examples/StructureRecognition/HSpiceMapping.xcat",
        devicetype_filepath="examples/StructureRecognition/deviceTypes.xcat",
    )
    try:
        write_partitioning_result(circuit, partitioning_fname)
        return True
    except:
        print("error when passing circuit: ", fname)
        return False


if __name__ == "__main__":
    NETLIST_FILE = args.file
    pymaga_io = pymaga.IOCore()
    process_structural_recognition(NETLIST_FILE)
    process_partitioning(NETLIST_FILE)
