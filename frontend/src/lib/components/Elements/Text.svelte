<script lang="ts">
    import { elements } from "$lib/stores/elements";

    let separator = '_';
    let elementSeparator = '__';
    let copySuccess = false;
    let textDiv: HTMLDivElement;

    async function copyToClipboard() {
        try {
            await navigator.clipboard.writeText(textDiv.innerText);
            copySuccess = true;
            setTimeout(() => copySuccess = false, 2000); // Reset after 2 seconds
        } catch (err) {
            console.error('Failed to copy text:', err);
        }
    }
</script>

<div class="p-4 font-mono">
    <nav class="flex flex-col mb-4 border-b">
        <div class="flex flex-col my-3">
            <h3>Seperate the element properties with a custom separator:</h3>
            <input 
                value={separator}
                on:input={(e: any) => separator = e?.target?.value || ''} 
                type="text" 
                placeholder="Separator _ (underscore)" 
                minlength="1"
                maxlength="99"
                class="border focus:border-teal-600 hover:border-teal-300 p-2 rounded-md outline-none focus:outline-none focus-within:outline-none"
            />
        </div>
        <div class="flex flex-col my-3">
            <h3>Seperate the elements with a custom separator:</h3>
            <input 
                value={elementSeparator}
                on:input={(e: any) => elementSeparator = e?.target?.value || ''} 
                type="text" 
                placeholder="Element Separator __ (double underscore)" 
                minlength="1"
                maxlength="99"
                class="border focus:border-teal-600 hover:border-teal-300 p-2 rounded-md outline-none focus:outline-none focus-within:outline-none"
            />
        </div>
    </nav>
    <div class="relative">
        {#if copySuccess}
            <button class="bg-green-500 text-white px-3 py-1 rounded-md">
                Copied!
            </button>
        {:else}
            <button 
                on:click={copyToClipboard}
                class="px-3 py-1 bg-primary-500 text-white rounded-md hover:bg-primary-600 transition-colors"
            >
                Copy
            </button>
        {/if}
        <div bind:this={textDiv} class="w-full max-w-full break-words whitespace-pre-wrap overflow-x-auto p-4 font-mono">
            {#each $elements as element}
                {element.atomic_number}{separator}{element.name}{separator}{element.symbol}{separator}{element.atomic_weight.toFixed(3)}{elementSeparator}
            {/each}
        </div>
    </div>
</div>
