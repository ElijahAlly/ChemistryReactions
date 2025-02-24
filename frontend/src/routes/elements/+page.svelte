<script lang="ts">
    import { onMount } from 'svelte';
    import { api } from '$lib/api/client';
    import type { Element } from '$lib/types/elements';
    import List from '$lib/components/Elements/List.svelte';
    import PeriodicTable from '$lib/components/Elements/PeriodicTable.svelte';
    import Table from '$lib/components/Elements/Table.svelte';
    import Text from '$lib/components/Elements/Text.svelte';
  import Sidebar from '$lib/components/Elements/Sidebar.svelte';

    let elements: Element[] = [];
    let loading = true;
    let error: string | null = null;

    let currentView = '';

    onMount(async () => {
        try {
            const response = await api.get('/elements/');
            console.log(response.data); 
            elements = response.data;
        } catch (e) {
            error = 'Failed to load elements';
            console.error(e);
        } finally {
            loading = false;

            const hash = window.location.hash.slice(1);
            currentView = hash || 'cards';
        }
    });
</script>

<div>
    <Sidebar currentView={currentView} updateCurrentView={(view: string) => currentView = view}/>
    <div class="space-y-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-gray-900">Every Known Element</h1>
            <!-- <a href="/elements/new" class="btn btn-primary">
                Add Element
            </a> -->
        </div>

        {#if loading}
            <div class="text-center py-8">
                <div class="animate-spin h-8 w-8 border-4 border-primary-500 border-t-transparent rounded-full mx-auto"></div>
                <p class="mt-2 text-gray-600">Loading elements...</p>
            </div>
        {:else if error}
            <div class="text-red-500 text-center py-8 card">
                <p>{error}</p>
                <button class="btn btn-primary mt-4" on:click={() => window.location.reload()}>
                    Retry
                </button>
            </div>
        {:else if elements.length === 0}
            <div class="text-center py-8 card">
                <p class="text-gray-600">No elements found</p>
                <!-- <a href="/elements/new" class="btn btn-primary mt-4 inline-block">
                    Add Your First Elements
                </a> -->
            </div>
        {:else}
            <div class="mt-4">
                {#if currentView === 'cards'}
                    <List {elements} />
                {:else if currentView === 'periodic'}
                    <PeriodicTable {elements} />
                {:else if currentView === 'table'}
                    <Table {elements} />
                {:else if currentView === 'text'}
                    <Text {elements} />
                {/if}
            </div>
        {/if}
    </div>
</div>