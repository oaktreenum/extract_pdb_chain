# extract_pdb_chain.py

A simple Python script using Biopython to extract specific chains from a PDB file and write them to a new file.

## Description

This script allows you to isolate one or more chains from a PDB file. It's useful when you want to analyze, visualize, or model only a subset of a structure.

## Requirements

- Python 3.x  
- Biopython (Install with `pip install biopython`)

## Usage

```
python extract_pdb_chain.py -p input_pdb_path -c ABC -o output_file_path
```

## Arguments

```
-p, --pdb: Path to the input PDB file.
-c, --chains: Chain identifiers to extract (e.g., 'A', 'AB', 'XYZ').
-o, --output: Path to the output PDB file that will contain only the specified chains.
```

## Example

```
python extract_pdb_chain.py -p 1abc.pdb -c AB -o 1abc_AB_only.pdb
```


## Author

Allon Goldberg
May 15, 2025
