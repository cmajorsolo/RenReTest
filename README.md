# RenReTest
The solutuion is built with Python 3.6.1 and Pandas 0.20.2

# Considerations
There are two solutions provided. First one is FindDealsCoveredByRenRe.py, Second one is TheOtherSolution.py

1. FindDealsCoveredByRenRe.py
* is seperated by 4 parts so the functions can be reusable.
* I work out this solutuion first. The Utilities.extract_contract_info returns includes and excludes lists. The lists are
used to filter out the insurance covered by RenRe. Then the output file can be merged with the losses csv.

2. TheOtherSolution.py
* is one chunk, so the contract Json file is only read once. It reduced the reading time.
* After finished the first solution I was thinking if I could make the contract json file as a csv file. The final result
could be produced by merging the 3 csv files. The complexity could be reduced comparing with the solution
FindDealsCoveredByRenRe.py
However, pandas can not do filtering csv files without same indexes. So for creating the same data format,
more complexity produced during the process.

![alt text](https://raw.githubusercontent.com/cmajorsolo/RenReTest/master/comparing.png)