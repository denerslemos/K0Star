# K0Star -> K0s + Pions skim code using HTCondor

Code to produce jets from the CMS HiForest and V0 skims from Dener. 

## Intructions

Setup CMSSW (just for root versioning)
```
export SCRAM_ARCH=el9_amd64_gcc12
cmsrel CMSSW_13_0_5
cd CMSSW_13_0_5/src
cmsenv
```
Inside of the src folder, download the code using
```
git clone git@github.com:denerslemos/K0Star.git
cd K0Star
mkdir -p cond
```
Before compile the code you must check the [sub_skim.sh](https://github.com/denerslemos/K0Star/blob/main/sub_skim.sh) lines 4 (CMSSW/src) and 6 (.../K0Star) and replace by your own folders.

Once this steps are done you can compile the code with
```
g++ -O2 K0Star.C `root-config --libs` `root-config --cflags` -o K0Star
```
This will create the executable: ```K0Star``` 

After that you will need your VOMS certificate, do it using
```
voms-proxy-init -rfc -voms cms --out voms_proxy.txt --hours 200
```
that creates a certificate file valid for 200 hours: voms_proxy.txt

After that you will submit jobs by using [HTCondor_submit.py](https://github.com/denerslemos/K0Star/blob/main/HTCondor_submit.py):
```
python3 HTCondor_submit.py -i input_text_file -v v0_input_file -o output_name_file -n X -s Y -c Z -p Q
```
 - input_text_file: is the text file (use it without the .txt extension) with inputs and can be found in the folder DATA_SAMPLES each .root input will be a job
 - v0_input_file: is the K0s text file (use it without the .txt extension) with inputs that are also at DATA_SAMPLES. For each PD the code will match all V0 .root files with one input_text_file
 - output_name_file: output file name (use it without the .root extension), it will automatically include a counter for each input. You can use paths to save on EOS.
 - X: 0 or 1 for no multiplicity cut for MB sample, 2 for HM185 [185,250] and 3 for HM250 [250,inf]
 - Y: name for the submission files, I have used HTcondor_sub_ + some information from the sample, PD, MB, ... + pgoing or Pbgoing.
 - Z: CMSSW folder you give ```cmsenv```
 - Q: PWD of the folder you are at (or where you wanna run your code)
It will automatically include a counter for each input


