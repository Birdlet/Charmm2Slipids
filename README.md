# Charmm2Slipids
This is a simple Python3 script to convert non-protein from Charmm-GUI output to Amber forcefiled in Gromacs format.

Charmm-GUI is a web based app for building molecular dynamics simulation system for kinds of MD Engine. However, Charmm-GUI only support Charmm36 or Charmm36m force field currently (2018). Charmm36 is one of the best force filed for membrane protein simulation, and it supports plenty kinds of lipids and modified aminoacids. CgenFF is a small molecular force filed compatibale with Charmm36, but GAFF for Amber force field is more accurate for general small moleculars. Hence I write this script to convert POPC\CHOL membrane from Charmm-GUI to Amber compatible format, so I can use GAFF for ligands for a complex membrane protein system.

Atom names of Lipids in Charmm-GUI and Slipids are compatible, but the oder is sometim uncompatible. This script __charmm2slipid.py__ simply alter the order of POPC and SOL from Charmm-GUI output. Slpids force field is compatible with AMBER99SB/AMBER99SB-ILDN/AMBER03 force field, I provide two force filed with Slipids in gromacs format here AMBER99SB-ILDN/AMBE03. Anyone can copy to use them, but please they only support POPC/CHOL.

charmm-gui: http://charmm-gui.org/
Stockholm lipids (Slipids): http://www.fos.su.se/~sasha/SLipids/Downloads.html

## Supported chemicals
| Charmm | Amber | Name |
|--------|-------|------|
| POPC   | POPC  | 1-palmitoyl-2-oleoyl-sn-glycero-3-phosphocholine |
| CHL1   | CHOL  | Cholestrol |
| TI3P   | SOL   | Water |
| SOD    | NA    | Sodium |
| CHL    | CL    | Chlorine |

## Usage
>usage: charmm2slipid.py [-h] -i [INPUT] -o [OUTPUT]

>A script convert POPC in Charmm-Gui to Amber Slipids

>optional arguments:
  -h, --help            show this help message and exit
  -i [INPUT], --input [INPUT]
                        Input .gro file from Charmm-Gui
  -o [OUTPUT], --output [OUTPUT]
                        Output .gro file in Amber Slipids


## Strategy for insert protein into POPC membrane by Charmm-GUI and charmm2slipid
1. Obtain a membrane protein in OPM database or only use OPM membrane coordinates;
2. Provide membrane protein with membrane coordinates in .pdb format to Charmm-GUI;
3. Select POPC/CHOL for generating membrane in Charmm-GUI;
4. Generate Gromacs format output and download it from Charmm-GUI;
5. Convert .pdb file of membrane to .gro file;
6. Use charm2slipids script to convert it;
7. Now you get a Amber Slipids membrane system!
8. Insert protein in Amber force filed into membrane...
9. Simulation...