import streamlit as st
import re
import math

st.title("Chemie-Hilfe")

# Dictionary of atomic masses for elements
atomic_masses = {
    'H': 1.008, 'He': 4.0026, 'Li': 6.94, 'Be': 9.0122, 'B': 10.81, 'C': 12.011, 'N': 14.007, 'O': 15.999, 'F': 18.998, 'Ne': 20.180,
    'Na': 22.990, 'Mg': 24.305, 'Al': 26.982, 'Si': 28.085, 'P': 30.974, 'S': 32.06, 'Cl': 35.45, 'Ar': 39.948, 'K': 39.098, 'Ca': 40.078,
    'Sc': 44.956, 'Ti': 47.867, 'V': 50.942, 'Cr': 51.996, 'Mn': 54.938, 'Fe': 55.845, 'Co': 58.933, 'Ni': 58.693, 'Cu': 63.546, 'Zn': 65.38,
    'Ga': 69.723, 'Ge': 72.63, 'As': 74.922, 'Se': 78.971, 'Br': 79.904, 'Kr': 83.798, 'Rb': 85.468, 'Sr': 87.62, 'Y': 88.906, 'Zr': 91.224,
    'Nb': 92.906, 'Mo': 95.95, 'Tc': 98, 'Ru': 101.07, 'Rh': 102.91, 'Pd': 106.42, 'Ag': 107.87, 'Cd': 112.41, 'In': 114.82, 'Sn': 118.71,
    'Sb': 121.76, 'Te': 127.60, 'I': 126.90, 'Xe': 131.29, 'Cs': 132.91, 'Ba': 137.33, 'La': 138.91, 'Ce': 140.12, 'Pr': 140.91, 'Nd': 144.24,
    'Pm': 145, 'Sm': 150.36, 'Eu': 151.96, 'Gd': 157.25, 'Tb': 158.93, 'Dy': 162.50, 'Ho': 164.93, 'Er': 167.26, 'Tm': 168.93, 'Yb': 173.05,
    'Lu': 174.97, 'Hf': 178.49, 'Ta': 180.95, 'W': 183.84, 'Re': 186.21, 'Os': 190.23, 'Ir': 192.22, 'Pt': 195.08, 'Au': 196.97, 'Hg': 200.59,
    'Tl': 204.38, 'Pb': 207.2, 'Bi': 208.98, 'Th': 232.04, 'Pa': 231.04, 'U': 238.03, 'Np': 237, 'Pu': 244, 'Am': 243, 'Cm': 247, 'Bk': 247,
    'Cf': 251, 'Es': 252, 'Fm': 257, 'Md': 258, 'No': 259, 'Lr': 262, 'Rf': 267, 'Db': 270, 'Sg': 271, 'Bh': 270, 'Hs': 277, 'Mt': 276,
    'Ds': 281, 'Rg': 282, 'Cn': 285, 'Nh': 286, 'Fl': 289, 'Mc': 290, 'Lv': 293, 'Ts': 294, 'Og': 294
}

def calculate_molar_mass(formula):
    elements = re.findall(r'([A-Z][a-z]*)(\d*)', formula)
    molar_mass = 0
    for (element, count) in elements:
        count = int(count) if count else 1
        molar_mass += atomic_masses[element] * count
    return molar_mass

st.header("Molar Mass Calculator")

formula = st.text_input("Enter the chemical formula (e.g., H2O, CO2):")
if formula:
    try:
        molar_mass = calculate_molar_mass(formula)
        st.write(f"The molar mass of {formula} is {molar_mass:.2f} g/mol")
    except KeyError:
        st.write("Invalid element symbol in formula.")
        st.header("Stoffmassenrechner")

        molar_mass_input = st.number_input("Enter the molar mass (g/mol):", min_value=0.0, format="%.2f")
        amount_of_substance = st.number_input("Enter the amount of substance (mol):", min_value=0.0, format="%.2f")

        if molar_mass_input and amount_of_substance:
            mass = molar_mass_input * amount_of_substance
            st.write(f"The mass of the substance is {mass:.2f} g")
            st.header("Concentration Calculator")

            mass_of_solute = st.number_input("Enter the mass of solute (g):", min_value=0.0, format="%.2f")
            volume_of_solution = st.number_input("Enter the volume of solution (L):", min_value=0.0, format="%.2f")

            if mass_of_solute and volume_of_solution:
                concentration = mass_of_solute / volume_of_solution
                st.write(f"The concentration of the solution is {concentration:.2f} g/L")
                st.header("pH Calculator")

                concentration_of_hydrogen_ions = st.number_input("Enter the concentration of hydrogen ions (mol/L):", min_value=0.0, format="%.2e")

                if concentration_of_hydrogen_ions:
                    pH = -math.log10(concentration_of_hydrogen_ions)
                    st.write(f"The pH of the solution is {pH:.2f}")