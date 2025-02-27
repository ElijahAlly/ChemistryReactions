<script lang="ts">
  import { elementsSortedByName, getElementByName } from "$lib/stores/elements";
  import type { Formula } from "$lib/types/molecule";

  let { formula = $bindable() } = $props();

  let formulaElements = $state<Formula[]>([]);
  let addElementCount = $state<number>(1);

  // Computed formula string
  $effect(() => {
    // console.log($state.snapshot(formulaElements))
    const updatedFormula = formulaElements
      .map(({ element, count }) => `${element?.symbol || ''}${count > 1 ? count : ''}`)
      .join('');
    formula = updatedFormula;
  });

  const addElement = (e: any) => {
    // Prevent default only if it's not from the input
    if (e.target.tagName !== 'INPUT') {
      e.preventDefault();
      
      // Add multiple elements based on addElementCount
      const newElements = Array(addElementCount).fill(null).map(() => ({
        element: $elementsSortedByName[0],
        count: 1
      }));
      
      formulaElements = [
        ...formulaElements,
        ...newElements
      ];
    }

    addElementCount = 1;
  }

  const removeElement = (index: number) => {
    formulaElements = formulaElements.filter((_, i) => i !== index);
  }

  const updateCount = (index: number, count: number) => {
    formulaElements = formulaElements.map((el, i) => 
      i === index ? { ...el, count } : el
    );
  }

  const updateElement = (index: number, elementName: string) => {
    if (!elementName) return;

    formulaElements = formulaElements.map((el, i) => {
      const element = getElementByName(elementName);
      if (!element) return el;
      if (i === index) {
        return { ...el, element };
      } else {
        return el;
      }
    });
  }

  const updateCustomMass = (index: number, mass: number | undefined) => {
    formulaElements = formulaElements.map((el, i) => 
      i === index ? { ...el, custom_mass: mass } : el
    );
  }

  const updateAddElementCount = (e: any) => {
    const newCount = parseInt(e.target?.value || '1');
    if (!newCount || newCount < 1) {
      addElementCount = 1;
    } else if (newCount > 118)  {
      addElementCount = 118;
    } else {
      addElementCount = newCount;
    }
  }
</script>

<div class="flex flex-col">
  <h3 class="text-xl font-bold text-gray-900 my-3">{ formula }</h3>
  <div class="flex flex-col gap-4">
    <div class="flex flex-col gap-2">
      {#each formulaElements as formulaElement, index}
        <div class="flex justify-between items-center p-2 rounded-sm hover:bg-slate-300" class:bg-slate-100={index % 2 === 0}>
          <div class="flex items-center gap-2">
            <select 
              bind:value={formulaElement.element}
              onchange={(e: any) => updateElement(index, (e.target?.value as string) || '')}
              class="px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            >
              {#each $elementsSortedByName as element}
                <option value={element}>
                  {element.symbol} - {element.name}
                </option>
              {/each}
            </select>

            <input 
              type="number"
              min="1"
              value={formulaElement.count || 1}
              oninput={(e: any) => updateCount(index, parseInt(e.target?.value || undefined))}
              class="w-20 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            />

            <label class="flex items-center gap-2">
              <input 
                type="checkbox"
                checked={formulaElement.custom_mass !== undefined}
                onchange={(e: any) => updateCustomMass(index, e.target?.checked ? formulaElement.element.atomic_weight : undefined)}
                class="h-4 w-4 text-blue-600 rounded border-gray-300 focus:ring-blue-500"
              />
              <span class="text-sm text-gray-700">Custom mass</span>
            </label>

            {#if formulaElement.custom_mass !== undefined}
              <input 
                type="number"
                step="0.001"
                value={formulaElement.custom_mass}
                oninput={(e: any) => updateCustomMass(index, parseFloat(e.target?.value || undefined))}
                class="w-24 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-none"
              />
            {/if}
          </div>

          <button 
            onclick={(e: any) => {e.preventDefault(); removeElement(index)}}
            class="px-3 py-2 bg-red-500 text-white rounded-md hover:bg-red-600 focus:outline-none focus:ring-none select-none"
          >
            Remove
          </button>
        </div>
      {/each}
    </div> 

    <button 
      onclick={addElement}
      class="max-w-fit px-3 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 focus:outline-none focus:ring-none select-none"
    >
      Add 
      <input 
        type="number"
        min="1"
        max="118"
        bind:value={addElementCount}
        onclick={(e) => {e.preventDefault(); e.stopPropagation();}}
        oninput={updateAddElementCount}
        class="w-24 p-1 text-slate-950 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-none"
      /> 
      Element{addElementCount > 1 ? 's' : ''}
    </button>
  </div>
</div>
