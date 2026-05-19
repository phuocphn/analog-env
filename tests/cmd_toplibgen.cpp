#include <iostream>
#include <chrono>

#include "Core/incl/Common/Backtrace.h"
#include "Synthesis/incl/TopologyLibraryGeneration.h"
#include "Synthesis/incl/LocalOptionsTopologyLibraryGeneration.h"
#include "Log/incl/LogMacros.h"

int main(int argc, char *argv[]) {

    try{
    	auto start = std::chrono::high_resolution_clock::now();
        Core::installBacktraceExceptionHandler();

        // Prepare command-line arguments
        int final_argc;
        char** final_argv;
        char* argv_default[3];

        if (argc == 1)
        { 
            // Use default arguments without Control framework overhead
            final_argc = 3;
            argv_default[0] = "cmd_toplibgen";
            argv_default[1] = "--HSPICE-netlist-dir";
            argv_default[2] = "outputs/TopologyGen-20260519";
            final_argv = argv_default;
        }
        else
        {
            final_argc = argc;
            final_argv = argv;
        }

        // Directly instantiate and run TopologyLibraryGeneration without Control framework
        Synthesis::LocalOptionsTopologyLibraryGeneration localOptions("Allowed options for topology library generation");
        localOptions.parse(final_argc, final_argv);

        Synthesis::TopologyLibraryGeneration analysis;
        analysis.setLocalOptions(localOptions);
        analysis.initialize();
        analysis.compute();
        analysis.write();

    	auto end = std::chrono::high_resolution_clock::now();
    	auto diff = end - start;
    	int timeHours = std::chrono::duration_cast<std::chrono::hours>(diff).count();
    	int timeMinutes = std::chrono::duration_cast<std::chrono::minutes>(diff).count() - timeHours * 60;
    	int timeSeconds = std::chrono::duration_cast<std::chrono::seconds>(diff).count() - timeHours * 3600 - timeMinutes * 60;
    	std::cout << "\nProgram runtime: " << timeHours << "h " << timeMinutes << "min " << timeSeconds << "s" << std::endl;
        return 0;
    }
    catch(Core::BacktraceException* ex)
    {
        std::cerr << *ex << std::endl;
        delete ex;
        return -1;
    }


    return 0;
}