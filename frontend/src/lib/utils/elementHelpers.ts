import type { Element } from "$lib/types/elements";

export const getCategoryColor = (element: Element): string => {
    if (!element) return '#ffffff';
    
    // --- Metals ---

    // Lanthanides
    if (element.atomic_number >= 57 && element.atomic_number <= 71) return '#a8a29e'; // stone-400
    
    // Actinides
    if (element.atomic_number >= 89 && element.atomic_number <= 103) return '#a78bfa'; // violet-400


    // --- Nonmetals ---

    // Noble gases (group 18)
    if (Number(element.group) === 18) return '#fdba74'; // orange-300
    
    // Reactive nonmetals
    if (element.atomic_number === 1 
        || element.atomic_number === 6 
        || element.atomic_number === 7 
        || element.atomic_number === 8 
        || element.atomic_number === 15 
        || element.atomic_number === 16
        || element.atomic_number === 34
    ) return '#5eead4'; // teal-300

    // Halogens (group 17)
    if (Number(element.group) === 17) return '#a5b4fc'; // indigo-300
    

    // --- Metalloids ---
    
    if (element.atomic_number === 5
        || element.atomic_number === 14
        || element.atomic_number === 32
        || element.atomic_number === 33
        || element.atomic_number === 51 
        || element.atomic_number === 52
    ) return '#facc15'; // yellow-400'


    // --- Metals ---

    // Post-transition metals (groups 13-16, specific elements)
    if ([13, 14, 15, 16].includes(Number(element.group))) return '#cbd5e1'; // slate-300

    // Transition metals (groups 3-12)
    if (Number(element.group) >= 3 && Number(element.group) <= 12) return '#ffd699'; // orange-200

    // Alkaline earth metals (group 2)
    if (Number(element.group) === 2) return '#93c5fd'; // blue-300

    // Alkali metals (group 1, except H)
    if (Number(element.group) === 1 && element.atomic_number !== 1) return '#ff9999'; // red-300
    
    return '#ffffff';
};

export const getElementPosition = (atomicNumber: number) => {
    // Special cases for H and He
    if (atomicNumber === 1) return { x: 0, y: 0 };
    if (atomicNumber === 2) return { x: 17, y: 0 };
    
    // Li and Be
    if (atomicNumber <= 4) return { x: atomicNumber - 3, y: 1 };
    
    // B through Ne
    if (atomicNumber <= 10) return { x: atomicNumber + 7, y: 1 };
    
    // Na and Mg
    if (atomicNumber <= 12) return { x: atomicNumber - 11, y: 2 };
    
    // Al through Ar
    if (atomicNumber <= 18) return { x: atomicNumber - 1, y: 2 };
    
    // K and Kr
    if (atomicNumber <= 36) return { x: atomicNumber - 19, y: 3 };
    
    // Rb and Xe
    if (atomicNumber <= 54) return { x: atomicNumber - 37, y: 4 };
    
    // Cs and Ba
    if (atomicNumber <= 56) return { x: atomicNumber - 55, y: 5 };
    
    // La through Lu (Lanthanides)
    if (atomicNumber <= 71) return { x: 2 + (atomicNumber - 57), y: 7 }; // Lanthanides are placed in a separate row
    
    // Hf through Rn
    if (atomicNumber <= 86) return { x: atomicNumber - 69, y: 5 };
    
    // Fr and Ra
    if (atomicNumber <= 88) return { x: atomicNumber - 87, y: 6 };

    // Ac through Lr (Actinides)
    if (atomicNumber <= 103) return { x: 2 + (atomicNumber - 89), y: 8 }; // Actinides are placed in a separate row (below Lanthanides)
    
    // Rf through Og
    if (atomicNumber <= 118) return { x: atomicNumber - 101, y: 6 };
    
    return { x: 0, y: 0 };
}


export const  categories = {
    nonmetals: [
        { name: 'Noble gases', color: 'bg-orange-300' },
        { name: 'Reactive nonmetals', color: 'bg-teal-300' },
        { name: 'Halogens', color: 'bg-indigo-300' }
    ],
    metalloids: [
        { name: 'Metalloids', color: 'bg-yellow-400' }
    ],
    metals: [
        { name: 'Post-transition metals', color: 'bg-slate-300' },
        { name: 'Transition metals', color: 'bg-[#ffd699]' },
        { name: 'Lanthanides', color: 'bg-stone-400' },
        { name: 'Actinides', color: 'bg-violet-400' },
        { name: 'Alkaline earth metals', color: 'bg-blue-300' },
        { name: 'Alkali metals', color: 'bg-[#ff9999]' }
    ]
};