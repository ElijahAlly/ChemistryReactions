<script lang="ts">
    let { currentView, updateCurrentView } = $props();
</script>

<div class="fixed left-0 top-16 h-full w-48 px-4 py-9 border-r">
    <h2 class="text-md font-semibold mb-4">View Elements As:</h2>
    <nav class="space-y-2">
        <a 
            href="#cards"
            class="block p-2 hover:bg-gray-200 rounded"
            class:bg-gray-200={currentView === 'cards'}
            onclick={() => updateCurrentView('cards')}
        >
            Cards
        </a>
        <a 
            href="#periodic" 
            class="block p-2 hover:bg-gray-200 rounded"
            class:bg-gray-200={currentView === 'periodic'}
            onclick={() => updateCurrentView('periodic')}
        >
            Periodic Table
        </a>
        <a 
            href="#table" 
            class="block p-2 hover:bg-gray-200 rounded"
            class:bg-gray-200={currentView === 'table'}
            onclick={() => updateCurrentView('table')}
        >
            Data Table
        </a>
        <a
            href="#text" 
            class="block p-2 hover:bg-gray-200 rounded"
            class:bg-gray-200={currentView === 'text'}
            onclick={() => updateCurrentView('text')}
        >
            Plain Text
        </a>
    </nav>
</div>