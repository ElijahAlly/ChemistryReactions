import type { Element } from "./elements";

export interface MoleculeProperties {
    logp?: number;
    polar_surface_area?: number;
    rotatable_bonds?: number;
    h_bond_donors?: number;
    h_bond_acceptors?: number;
}

export interface Molecule {
    id: number;
    
    name: string;
    formula: string;
    smiles: string;
    molecular_weight: number;
    properties?: MoleculeProperties;

    created_at?: string;
    updated_at?: string;
}

export interface MoleculeCreate {
    name: string;
    formula: string;
    smiles: string;
    molecular_weight: number;
}

export interface Formula {
    element: Element;
    count: number;
    custom_mass?: number;
};