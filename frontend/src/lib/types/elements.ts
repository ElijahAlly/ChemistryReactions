export interface ElementType {
    id: number;
    name: string;

    atomic_number: number;
    atomic_weight: number;
    symbol: string;
    group: number;
    period: number;
    block: string;
    origin: string;
    phase: string;

    density?: number;
    melting_point?: number;
    boiling_point?: number;
    specific_heat?: number;
    electronegativity?: number;
    abundance?: number;
    // category: string;

    created_at?: string;
    updated_at?: string;
}