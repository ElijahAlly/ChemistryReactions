<script lang="ts">

    type Option = Map<string, string>

    let { 
        curOption = $bindable(), 
        reverseList = $bindable(), 
        options
    }: {
        curOption: string | undefined;
        reverseList: boolean;
        options: Option;
    } = $props();

</script>

<div class="flex items-center gap-2">
    <label for="sort-by" class="text-sm font-medium text-gray-700">Sort by:</label>
    <div class="inline-flex rounded-md shadow-sm">
        <div class="relative z-10">
            <select 
                id="sort-by" 
                bind:value={curOption}
                title="Select option to sort by"
                class="pl-3 pr-8 py-2 text-sm border border-gray-300 rounded-l-md focus:outline-none focus:ring-none bg-white appearance-none"
            >
                {#each [...options] as [value, label]}
                    <option {value}>{label}</option>
                {/each}
            </select>
            <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
            </div>
        </div>
        <button 
            title="Click to reverse results"
            onclick={() => reverseList = !reverseList}
            class="px-3 py-2 text-sm font-medium text-gray-700 bg-white border-t border-b border-r border-gray-300 rounded-r-md hover:bg-gray-50 focus:outline-none focus:ring-none"
        >
            {reverseList ? '↑' : '↓'}
        </button>
    </div>
</div>