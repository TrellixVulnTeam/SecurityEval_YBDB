# SecurityEval

This repository contains source code for the paper titled **SecurityEval Dataset: Mining Software Vulnerability Examples to Evaluate Machine Learning-Based Code Generation Output**. The project is submitted for The first edition of the International Workshop on Mining Software Repositories Applications for Privacy and Security (MSR4P&S '22). The paper describes the dataset for evaluating machine learning-based code generation output and application of the dataset to the code generation tools.

## Project Structure
- dataset.jsonl: dataset file in jsonl format. Every line contains a JSON object with the following fields:
  - `ID`: unique identifier of the sample.
  - `Prompt`: Prompt for the code generation model.
  - `Insecure_code`: code of the vulnerability example that may generate from the prompt.
- DatasetCreator.py: script to create the dataset from the folders: *Testcases_Prompt* and *Testcases_Insecure_Code*.
- Testcases_Prompt: folder containing the prompt files.
- Testcases_Insecure_Code: folder containing the insecure code files.
- Testcases_Copilot: folder containing the code generated by GitHub Copilot.
- Testcases_InCoder: folder containing the code generated by InCoder.
- Databases: folder containing the databases for the CodeQL analysis.
  - job_{copilot,incoder}.sh: scripts to run the CodeQL analysis.
- Result: folder containing the results of the evaluation.
  - DataTable.{csv,xlsx}: table of the CWE list with their source
  - testcases_copilot: folder containing result by running CodeQL on *Testcases_Copilot*
  - testcases_copilot.json: result by running Bandit on *Testcases_Copilot*
  - testcases_copilot.csv: result for manual analysis on *Testcases_Copilot*
  - testcases_incoder: folder containing result by running CodeQL on *Testcases_InCoder*
  - testcases_incoder.json: result by running Bandit on *Testcases_InCoder*
  - testcases_incoder.csv: result for manual analysis on *Testcases_InCoder*
  - testcases.json: contains the list of files and folders in *Testcases_Prompt*
  - CSVConvertor.py: script to convert the CSV files to from json file(i.e. testcases.json)

## Usage of the Analyzer
Dependencies:
- Python: 3.9.4
- CodeQL command-line toolchain:  2.10.0
- Bandit: 1.7.4

### Bandit
```
virtualenv bandit-env
python3 -m venv bandit-env
source bandit-env/bin/activate
pip install bandit
bandit -r Testcases_Copilot -f json -o Result/testcases_copilot.json 
bandit -r Testcases_InCoder -f json -o Result/testcases_incoder.json
```
### CodeQL
Install CodeQL from here: https://codeql.github.com/docs/codeql-cli/getting-started-with-the-codeql-cli/
```
cd Testcases_Copilot
codeql database create --language=python  '/Users/lsiddiqsunny/Documents/Notre Dame/Research/SecurityEval/Databases/Testcases_Copilot_DB' # Use your own path to the database
cd ../Databases
sh job_copilot.sh

cd ..
cd Testcases_InCoder
codeql database create --language=python  '/Users/lsiddiqsunny/Documents/Notre Dame/Research/SecurityEval/Databases/Testcases_Incoder_DB' # Use your own path to the database
cd ../Databases
sh job_incoder.sh
```

## Abstract
Automated source code generation is currently a popular machine-learning-based task. It can be helpful for the software developer to write functionally correct code from the given context. But like human developers, the code generation model can produce vulnerable code, which can be prevalent in the software. For this reason, evaluating the code generation model is a must. We propose an evaluation dataset for this purpose. It contains 130 samples for 75 Common Weakness Enumeration (CWE), including 14 of the top 25 most common security weaknesses. We also demonstrate our dataset for evaluating one open-source model (i.e. InCoder) and one closed-source model (i.e. GitHub Copilot).

## Citation
```
 @software{Siddiq_SecurityEval_2022,
 author = {Siddiq, Mohammed Latif and Santos, Joanna C.S.},
 month = {7},
 title = {{SecurityEval Dataset: Mining Software Vulnerability Examples to Evaluate Machine Learning-Based Code Generation Output}},
 url = {https://github.com/s2e-lab/SecurityEval},
 version = {1.0.0},
 year = {2022}
 }
 ```
