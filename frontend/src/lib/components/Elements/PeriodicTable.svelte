<script lang="ts">
    import { elements } from "$lib/stores/elements";
    import type { Element } from "$lib/types/elements";
    import { categories, getCategoryColor, getElementPosition } from "$lib/utils/elementHelpers";

    let highlightedCategory: string | null = null;

    const grid = Array(10).fill(null).map(() => Array(18).fill(null));

    $elements.forEach(element => {
        const pos = getElementPosition(element.atomic_number);
        grid[pos.y][pos.x] = element;
    });

    let selectedElement: Element = $elements[0]; // Default to Hydrogen

    const elementClass = 'aspect-square p-1 text-xs border rounded hover:shadow-md hover:border-black transition-shadow flex flex-col cursor-pointer';

    function isElementInCategory(element: Element, categoryName: string): boolean {
        switch(categoryName) {
            case 'Noble gases': return Number(element.group) === 18;
            case 'Reactive nonmetals': return [1, 6, 7, 8, 15, 16, 34].includes(element.atomic_number);
            case 'Halogens': return Number(element.group) === 17;
            case 'Metalloids': return [5, 14, 32, 33, 51, 52].includes(element.atomic_number);
            case 'Post-transition metals': return [13, 14, 15, 16].includes(Number(element.group)) && ![5, 14, 32, 33, 51, 52, 6, 7, 8, 15, 16, 34].includes(element.atomic_number);
            case 'Transition metals': return Number(element.group) >= 3 && Number(element.group) <= 12 && ![71, 103].includes(element.atomic_number);
            case 'Lanthanides': return element.atomic_number >= 57 && element.atomic_number <= 71;
            case 'Actinides': return element.atomic_number >= 89 && element.atomic_number <= 103;
            case 'Alkaline earth metals': return Number(element.group) === 2;
            case 'Alkali metals': return Number(element.group) === 1 && element.atomic_number !== 1;
            default: return false;
        }
    }
</script>

<div class="p-4 w-full">
    <div class="flex justify-around items-start">
        <div class="mb-4 flex gap-8 text-sm">
            <div>
                <h3 class="font-bold mb-2">Nonmetals</h3>
                <div>
                    {#each categories.nonmetals as category}
                        <div 
                            role="button"
                            tabindex="0"
                            class="flex items-center gap-2 hover:bg-gray-100 p-1 rounded cursor-pointer"
                            on:mouseenter={() => highlightedCategory = category.name}
                            on:mouseleave={() => highlightedCategory = null}
                            on:keydown={(e: any) => {
                                if (e.key === 'Enter' || e.key === ' ') {
                                    highlightedCategory = category.name;
                                }
                            }}
                            on:blur={() => highlightedCategory = null}
                        >
                            <div class={`w-4 h-4 rounded ${category.color}`}></div>
                            <span>{category.name}</span>
                        </div>
                    {/each}
                </div>
            </div>
            <div>
                <h3 class="font-bold mb-2">Metalloids</h3>
                <div>
                    {#each categories.metalloids as category}
                        <div 
                            role="button"
                            tabindex="0"
                            class="flex items-center gap-2 hover:bg-gray-100 p-1 rounded cursor-pointer"
                            on:mouseenter={() => highlightedCategory = category.name}
                            on:mouseleave={() => highlightedCategory = null}
                        >
                            <div class={`w-4 h-4 rounded ${category.color}`}></div>
                            <span>{category.name}</span>
                        </div>
                    {/each}
                </div>
            </div>
            <div>
                <h3 class="font-bold mb-2">Metals</h3>
                <div>
                    {#each categories.metals as category}
                        <div 
                            role="button"
                            tabindex="0"
                            class="flex items-center gap-2 hover:bg-gray-100 p-1 rounded cursor-pointer"
                            on:mouseenter={() => highlightedCategory = category.name}
                            on:mouseleave={() => highlightedCategory = null}
                        >
                            <div class={`w-4 h-4 rounded ${category.color}`}></div>
                            <span>{category.name}</span>
                        </div>
                    {/each}
                </div>
            </div>
        </div>
        <div class="flex flex-col items-center justify-center">
            <h3 class="font-bold mb-2">Element Block Legend</h3>
            <div class="border rounded p-2 w-36 relative">
                <div class={elementClass} style="background-color: {getCategoryColor(selectedElement)};">
                    <div class="flex justify-between items-start">
                        <div class="text-gray-600">{selectedElement.atomic_number}</div>
                        <div class="text-gray-600 text-[0.65rem]">{selectedElement.atomic_weight?.toFixed(3)}</div>
                    </div>
                    <div class="text-center font-bold mt-1">{selectedElement.symbol}</div>
                    <div class="text-center text-[0.65rem] truncate mb-1">{selectedElement.name}</div>
                </div>
                
                <!-- Atomic Number Arrow -->
                <div class="absolute -left-24 top-2 flex items-center">
                    <span class="text-[0.65rem]">Atomic Number</span>
                    <div class="w-6 h-[2px] bg-gray-400"></div>
                    <div class="w-0 h-0 border-t-[4px] border-t-transparent border-b-[4px] border-b-transparent border-l-[6px] border-l-gray-400"></div>
                </div>

                <!-- Atomic Weight Arrow -->
                <div class="absolute -right-28 top-2 flex items-center">
                    <div class="w-0 h-0 border-t-[4px] border-t-transparent border-b-[4px] border-b-transparent border-r-[6px] border-r-gray-400"></div>
                    <div class="w-6 h-[2px] bg-gray-400"></div>
                    <span class="text-[0.65rem]">Atomic Weight</span>
                </div>

                <!-- Symbol Arrow -->
                <div class="absolute -right-24 top-1/2 -translate-y-1/2 flex items-center">
                    <div class="w-0 h-0 border-t-[4px] border-t-transparent border-b-[4px] border-b-transparent border-r-[6px] border-r-gray-400"></div>
                    <div class="w-4 h-[2px] bg-gray-400"></div>
                    <span class="text-[0.65rem]">Symbol</span>
                </div>

                <!-- Name Arrow -->
                <div class="absolute -left-20 bottom-2 flex items-center">
                    <span class="text-[0.65rem]">Name</span>
                    <div class="w-6 h-[2px] bg-gray-400"></div>
                    <div class="w-0 h-0 border-t-[4px] border-t-transparent border-b-[4px] border-b-transparent border-l-[6px] border-l-gray-400"></div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="grid grid-cols-18 gap-0.5">
        {#each grid as row, y}
            {#each row as element, x}
                {#if element}
                    <button
                        class={elementClass}
                        class:mt-6={y === 7}
                        class:opacity-20={highlightedCategory && !isElementInCategory(element, highlightedCategory)}
                        style="background-color: {getCategoryColor(element)};"
                        on:click={() => selectedElement = element}
                        class:ring-2={selectedElement === element}
                        class:ring-black={selectedElement === element}
                    >
                        <div class="flex justify-between items-start">
                            <div class="text-gray-600">{element.atomic_number}</div>
                            <div class="text-gray-600 text-[0.65rem]">{element.atomic_weight?.toFixed(2)}</div>
                        </div>
                        <div class="text-center font-bold mt-1">{element.symbol}</div>
                        <div class="text-center text-[0.65rem] truncate mb-1">{element.name}</div>
                    </button>
                {:else}
                    {#if (y === 5 || y === 6) && x === 2}
                        <div
                            class={[elementClass, 'flex flex-col items-center justify-center h-full w-full']}
                            class:bg-stone-400={y === 5} 
                            class:bg-violet-400={y === 6}
                            class:opacity-20={highlightedCategory && (y === 5 ? highlightedCategory !== 'Lanthanides' : highlightedCategory !== 'Actinides')}
                        >
                            <p class="text-[0.65rem]">{y === 5 ? '57-71' : '89-103'}</p>
                            <p class="text-[9px]">{y === 5 ? 'Lanthanides' : 'Actinides'}</p>
                        </div>
                    {:else}
                        <div class="aspect-square"></div>
                    {/if}
                {/if}
            {/each}
        {/each}
    </div>
</div>

<style>
    .grid-cols-18 {
        grid-template-columns: repeat(18, minmax(0, 1fr));
        width: min(100%, calc(100vh * 1.8));
        margin: 0 auto;
    }

    * {
        transition: opacity 210ms ease-in-out;
    }
</style>