import type { ElementType } from '$lib/types/elements';
import { writable, derived, get } from 'svelte/store';

export const elements = writable<ElementType[]>([]);

export const elementsSortedByName = derived(elements, (elements) => {
    return [...elements].sort((a, b) => a.name.localeCompare(b.name));
});

export const elementsSortedByAtomicNumber = derived(elements, (elements) => {
    return [...elements].sort((a, b) => a.atomic_number - b.atomic_number);
});

export const elementsSortedByAtomicWeight = derived(elements, (elements) => {
    return [...elements].sort((a, b) => a.atomic_weight - b.atomic_weight);
});

export const elementsSortedByGroup = derived(elements, (elements) => {
    return [...elements].sort((a, b) => a.group - b.group);
});

export const elementsSortedByPeriod = derived(elements, (elements) => {
    return [...elements].sort((a, b) => a.period - b.period);
});

export const elementsSortedByBlock = derived(elements, (elements) => {
    return [...elements].sort((a, b) => a.block.localeCompare(b.block));
});

export const getElementByName = (name: string): ElementType | undefined => {
    return get(elements).find((element) => element.name === name) || undefined;
}