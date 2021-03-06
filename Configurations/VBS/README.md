# mkROC script

Brief tutorial that shows how to use [mkROC](https://github.com/UniMiBAnalyses/PlotsConfigurations/blob/master/Configurations/VBS/mkROC.py) script.

----

## 1. What mkROC does

This script takes the rootFile (that contains histograms) produced by mkShapes with the option `--doHadd=True` as an input.

mkROC searches for a cut equal to '1' (i.e. only supercut is adopted). If it happens that this cut is not present, default cut adopted is the first one in _cuts.py_ 

It builds:

  * ROC curves for each background
  * Significance curves (x axis = signal efficiency) for each background
  * Significance curve (x axis = cut value) for each background and variable

Running _mkROC.py_ a directory called `RS_curves` is created: here canvas are saved both as _.png_ and as _.root_ 

## 2. Which data are rejected

Data rejected are on the left of the variable value (default). If rejecting data on the right is needed, you have to add `'SignalOnRight': -1` item to variables dictionaries.

## 3. Compulsory options
```
--inputFile=<pathtorootFile.root>
```
in order to let mkROC find the correct input file
```
--pycfg=<configurationfile.py>
```
in order to let mkROC find the correct configuration file

## 4. Other options
```
--line=1
```
it connects the points with a line
```
--grid=1
```
it draws a grid on canvas
```
--expanded=1
```
it calculates significance with the expanded formula (reccomended), instead of s/sqrt(b)
```
--markerSize=0.8
```
it sets markers size to 0.8 (as an example). Default markers size is 1
```
--thresholdEff=0.6
```
it draws an horizontal line at signal efficiency equal to 0.6 (as an example) in ROC curves canvas.
```
--ZmaxLine=1
```
it draws a vertical line corresponding to the maximum efficiency in significance canvas. It draws also an horizontal line in ROC canvas, at the corresponding signal efficiency.
