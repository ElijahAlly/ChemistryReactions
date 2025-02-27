<script lang="ts">
  import { elements, elementsSortedByAtomicNumber, elementsSortedByAtomicWeight, elementsSortedByBlock, elementsSortedByGroup, elementsSortedByName, elementsSortedByPeriod } from "$lib/stores/elements";
  import type { ElementType } from "$lib/types/elements";
  import SortBy from "../ui/SortBy.svelte";
    
    type ElementSortValue = 'name' | 'atomic_number' | 'atomic_weight' | 'group' | 'period' | 'block';
    type ElementSortLabel = 'Name' | 'Atomic Number' | 'Atomic Weight' | 'Group' | 'Period' | 'Block';

    const options = new Map<ElementSortValue, ElementSortLabel>([
        ['name', 'Name'],
        ['atomic_number', 'Atomic Number'],
        ['atomic_weight', 'Atomic Weight'],
        ['group', 'Group'],
        ['period', 'Period'],
        ['block', 'Block']
    ]);
    let curOption = $state<ElementSortValue>('atomic_number');
    let reverseList = $state<boolean>(false);

    const filteredAndSortedElements: ElementType[] = $derived.by(() => {
        let elements: ElementType[] = [];
        
        switch (curOption) {
            case 'name':
                elements = $elementsSortedByName;
                break;
        
            case 'atomic_number':
                elements = $elementsSortedByAtomicNumber;
                break;
        
            case 'atomic_weight':
                elements = $elementsSortedByAtomicWeight;
                break;
        
            case 'block':
                elements = $elementsSortedByBlock;
                break;
        
            case 'group':
                elements = $elementsSortedByGroup;
                break;
        
            case 'period':
                elements = $elementsSortedByPeriod;
                break;
        
            default:
                break;
        }

        // Create a new array when reversing (otherwise the original array is reversed and the state does not update)
        return reverseList ? [...elements].reverse() : elements;
    });
</script>

<div class="flex flex-col">
    <div class="flex justify-between items-center mt-3 mb-9 border-b-2 p-2">
        <SortBy {options} bind:curOption bind:reverseList />
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {#each filteredAndSortedElements as element}
            <div class="card hover:shadow-lg transition-shadow">
                <h2 class="text-xl font-semibold text-gray-900 mb-2">
                    {element.name} ({element.symbol})
                </h2>
                <p class="text-gray-600 mb-4">Atomic Number: {element.atomic_number}</p>
                <p class="text-gray-600 mb-4">Group: {element.group}</p>
                <p class="text-gray-600 mb-4">Period: {element.period}</p>
                <p class="text-gray-600 mb-4">Block: {element.block}</p>
                <p class="text-gray-600 mb-4">Atomic Weight: {element.atomic_weight.toFixed(3)}</p>
                <p class="text-gray-600 mb-4">Origin: {element.origin}</p>
                <p class="text-gray-600 mb-4">Density: {element.density}</p>
                <hr />
                <p class="text-gray-600 mb-4 mt-4">Phase: {element.phase || '-'}</p>
                <p class="text-gray-600 mb-4">Melting Point: {element.melting_point || '-'}</p>
                <p class="text-gray-600 mb-4">Boiling Point: {element.boiling_point || '-'}</p>
                <p class="text-gray-600 mb-4">Specific Heat: {element.specific_heat || '-'}</p>
                <p class="text-gray-600 mb-4">Electronegativity: {element.electronegativity || '-'}</p>
                <p class="text-gray-600 mb-4">Abundance: {element.abundance || '-'}</p>
                <!-- <p class="text-gray-600 mb-4">Electron Affinity: {element.electron_affinity}</p> -->
                <a
                    href="/elements/{element.id}"
                    class="text-primary-600 hover:text-primary-700 font-medium"
                >
                    View Details →
                </a>
            </div>
        {/each}
    </div>
</div>