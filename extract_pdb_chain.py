"""
extract_pdb_chain.py

Extracts specified chains from a PDB file and writes them into a new PDB file.

Usage:
    python extract_pdb_chain.py -p input_pdb_path -c ABC -o output_file_path

Arguments:
    -p, --pdb       Path to the input PDB file.
    -c, --chains    Chain identifiers to extract (e.g., 'A', 'AB', 'XYZ').
    -o, --output    Path to the output PDB file containing only the specified chains.

Example:
    python extract_pdb_chain.py -p 1abc.pdb -c AB -o 1abc_AB_only.pdb


Author: Allon Goldberg, 5/15/25
"""

from Bio.PDB import *
import argparse

def extract_chains(input_pdb,chains_to_keep,output_file):
    parser = PDBParser()
    io = PDBIO()

    class ChainSelect(Select):
        def accept_chain(self, chain):
            if chain.id in chains_to_keep:
                return 1
            else:
                return 0
        
    structure = parser.get_structure("inp_pdb", input_pdb)
    io.set_structure(structure)
    io.save(output_file,ChainSelect())

    return

def main():
    parser = argparse.ArgumentParser(description="Extract specific chains from a PDB file.")
    parser.add_argument("-p", "--pdb", required=True, help="Path to the input PDB file.")
    parser.add_argument("-c", "--chains", required=True, help="Chain identifiers to extract (e.g., 'AB').")
    parser.add_argument("-o", "--output", required=True, help="Path to the output PDB file.")

    args = parser.parse_args()

    extract_chains(args.pdb, args.chains, args.output)
    return
    

if __name__ == "__main__":
    main()
