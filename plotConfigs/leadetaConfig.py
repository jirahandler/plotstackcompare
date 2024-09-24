outputPath = "compare_plot_eta_c_run3.root"

taskSetup = {
  "Xmax"   : 3.7,
  "Xmin"   : -3.7,
  "Ymin"   : 0,
  "Ymax"   : 0.1,
  "nameX"  : "leading c-jet #eta ",
  "nameY"  : "Number of Jets",
  "name"   : "leadeta_c",
  "doLogy" : 0,
  "rebinFactor" : 1,
  "doFraction"  : 0,
  "doRatio" : 0,
  "masterLabel" : "#nu + LQ(#rightarrow#nu c)",
  "lumi" : -1, #58791.6 + 44630.6 + 33402.2 + 3244.54, #11925.1,
  "cme"  : 13,
  "relErrMax" : 10,
  "scaleToData" : 1,
  "sort" : 1,
  "ratioYLabel" : "",
  "ratioYmin" : 0,
  "ratioYmax" : 2.5,
  "normalized" : 1,
}
compareSources = {
  "1" : {
    "filePath"    :   "/afs/cern.ch/work/s/sgoswami/public/taunvnvlq/run_100001/out.root",
    "histPath"    :   ["eta1_c"],
    "color"       :   4,
    "style"       :   21,
    "drawOption"  :   "hist",
    "legendLabel" :   "m_{LQ} = 0.5 TeV",
  },
  "2" : {
    "filePath"    :   "/afs/cern.ch/work/s/sgoswami/public/taunvnvlq/run_100002/out.root",
    "histPath"    :   ["eta1_c"],
    "color"       :   2,
    "style"       :   22,
    "drawOption"  :   "hist",
    "legendLabel" :   "m_{LQ} = 1 TeV",
  },
  "3" : {
    "filePath"    :   "/afs/cern.ch/work/s/sgoswami/public/taunvnvlq/run_100003/out.root",
    "histPath"    :   ["eta1_c"],
    "color"       :   6,
    "style"       :   23,
    "drawOption"  :   "hist",
    "legendLabel" :   "m_{LQ} = 1.4 TeV",
  },
  "4" : {
    "filePath"    :   "/afs/cern.ch/work/s/sgoswami/public/taunvnvlq/run_100004/out.root",
    "histPath"    :   ["eta1_c"],
    "color"       :   7,
    "style"       :   24,
    "drawOption"  :   "hist",
    "legendLabel" :   "m_{LQ} = 2 TeV",
  },
  "5" : {
    "filePath"    :   "/afs/cern.ch/work/s/sgoswami/public/taunvnvlq/run_100005/out.root",
    "histPath"    :   ["eta1_c"],
    "color"       :   8,
    "style"       :   25,
    "drawOption"  :   "hist",
    "legendLabel" :   "m_{LQ} = 2.5 TeV",
  },
  "6" : {
    "filePath"    :   "/afs/cern.ch/work/s/sgoswami/public/taunvnvlq/run_100006/out.root",
    "histPath"    :   ["eta1_c"],
    "color"       :   9,
    "style"       :   26,
    "drawOption"  :   "hist",
    "legendLabel" :   "m_{LQ} = 2.8 TeV",
  },
}
