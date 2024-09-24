This is a package to make common plots such as stacked plots and comparison
plots.

Cosmetics.py determines how to format the input histograms. 

RootPlottingCore.py defines the core plotting functions.

Stack.py is the executable to make stacked histograms.

stackConfig.py is a local config example to produce stacked histograms.

The command is: python Stack.py -l stackConfig.py -b

The package is independent from the analysis software. As long as the
histograms are compatible, the users can use outputs from various workflows.
