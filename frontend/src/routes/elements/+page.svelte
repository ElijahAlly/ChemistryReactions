<script lang="ts">
    import { onMount } from 'svelte';
    import List from '$lib/components/Elements/List.svelte';
    import PeriodicTable from '$lib/components/Elements/PeriodicTable.svelte';
    import Table from '$lib/components/Elements/Table.svelte';
    import Text from '$lib/components/Elements/Text.svelte';
    import Sidebar from '$lib/components/Elements/Sidebar.svelte';
    import { elements } from '$lib/stores/elements';
  import { scrollToTop } from '$lib/utils/globalHelpers';
    
    type CurrentView = 'list' | 'periodic' | 'table' | 'text';

    let currentView = $state<CurrentView>();

    onMount(async () => {
        const hash = window.location.hash.slice(1);
        currentView = (hash as CurrentView) || 'list';
    });

    $effect(() => {
        currentView;
        return scrollToTop();
    });
</script>

<div>
    <Sidebar bind:currentView />
    <div class="space-y-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-gray-900">Every Known Element</h1>
            <!-- <a href="/elements/new" class="btn btn-primary">
                Add Element
            </a> -->
        </div>

        {#if $elements.length === 0}
            <div class="text-center py-8 card">
                <p class="text-gray-600">Error getting elements.</p>
                <!-- <a href="/elements/new" class="btn btn-primary mt-4 inline-block">
                    Add Your First Elements
                </a> -->
            </div>
        {:else}
            <div class="mt-4">
                {#if currentView === 'list'}
                    <List />
                {:else if currentView === 'periodic'}
                    <PeriodicTable />
                {:else if currentView === 'table'}
                    <Table />
                {:else if currentView === 'text'}
                    <Text />
                {/if}
            </div>
        {/if}
    </div>
</div>