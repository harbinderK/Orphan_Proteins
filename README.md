Overview
This repository contains scripts for interacting with a STRING PostgreSQL database and processing Protein-Protein Interaction data. The goal is identifying orphan proteins that may be potential candidates for missing protein complex components. The scripts retrieve information from the database using input files and calculate scores from a list of neighbors.

Scripts Included
fetch_protein_id.py: This script retrieves protein IDs from a PostgreSQL database using an input file with protein external IDs (i.e., STRING identifiers).
get_nei_score.py: This script retrieves network node links (neighbors) from a PostgreSQL STRING network database using an input file with protein IDs, which is the output of the previous script. It filters the links using a combined score threshold (>= 0.7 or >= 700).
get_baysian_score.py: This script calculates scores from a list of neighbors obtained from the previous script provided as an input file. The lower the score, the stronger the interaction between two proteins. By selecting interactions with the minimum scores, we aim to make more accurate predictions for the missing proteins.

## Note
Ensure you have installed or access to the STRING database before running the scripts.
Update the database connection details (user, password, host, database) in the scripts to match your environment.

## Dependencies
Python 3.x
psycopg2
Locally installed full STRING database dumps from URL https://string-db.org/cgi/download. 

## Installation
Install the required dependencies using pip:
$ pip install psycopg2

## Usage
1. fetch_protein_id.py
This script retrieves protein IDs from the STRING “items” database using an input file with protein external IDs (STRING IDs) in single quotes (e.g., '511145.b0088'). Change the input file path to your requirements.

$ python fetch_protein_id.py input.txt > out_1.txt

2. get_nei_score.py
This script retrieves network node links from the STRING network database using an input file with node IDs. It filters the links based on a combined score threshold. Provide the input file containing node IDs as a command-line argument.

	$ python get_nei_score.py out_1.txt > out_2.txt
The script will output the network node links with combined scores greater than the threshold value provided in the script.
3. get_baysian_score.py
This script calculates scores from a list of neighbors provided as an input file. It computes the score based on the combined score values for each identifier. Provide the input file obtained from the previous script as a command-line argument. Rank the neighbors based on the Bayesian score. 
$ python get_baysian_score.py out_2.txt > out_3.txt

4. Run the following command in the terminal to sort the neighbors. 

$ sort -g -k2 out_3.txt > out_4.txt

## Acknowledgments
We would like to thank the creators and maintainers of the STRING database (https://string-db.org/) for providing an invaluable resource for protein-protein interaction data, which was essential for the development and testing of these scripts.
- STRING database: Szklarczyk D, Gable AL, Nastou KC, Lyon D, Kirsch R, Pyysalo S, Doncheva NT, Legeay M, Fang T, Bork P, Jensen LJ, von Mering C. The STRING database in 2021: customizable protein–protein networks, and functional characterization of user-uploaded gene/measurement sets. Nucleic acids research. 2021 Jan 8;49(D1):D605-12. doi:https://doi.org/10.1093%2Fnar%2Fgkaa1074 

Contact
For any questions or feedback, please contact harbin27_sit@jnu.ac.in.
