<script lang="ts">
    import { onMount } from 'svelte';
    import { api } from '$lib/api/client';
    import type { Molecule } from '$lib/types/molecule';

    let molecules: Molecule[] = [];
    let loading = true;
    let error: string | null = null;

    onMount(async () => {
        try {
            const response = await api.get('/molecules');
            molecules = response.data;
        } catch (e) {
            error = 'Failed to load molecules';
            console.error(e);
        } finally {
            loading = false;
        }
    });
</script>

<div class="space-y-6">
    <div class="flex justify-between items-center">
        <h1 class="text-3xl font-bold text-gray-900">Molecules</h1>
        <a href="/molecules/new" class="btn btn-primary">
            Add Molecule
        </a>
    </div>

    {#if loading}
        <div class="text-center py-8">
            <div class="animate-spin h-8 w-8 border-4 border-primary-500 border-t-transparent rounded-full mx-auto"></div>
            <p class="mt-2 text-gray-600">Loading molecules...</p>
        </div>
    {:else if error}
        <div class="text-red-500 text-center py-8 card">
            <p>{error}</p>
            <button class="btn btn-primary mt-4" on:click={() => window.location.reload()}>
                Retry
            </button>
        </div>
    {:else if molecules.length === 0}
        <div class="text-center py-8 card">
            <p class="text-gray-600">No molecules found</p>
            <a href="/molecules/new" class="btn btn-primary mt-4 inline-block">
                Add Your First Molecule
            </a>
        </div>
    {:else}
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {#each molecules as molecule}
                <div class="card hover:shadow-lg transition-shadow">
                    <h2 class="text-xl font-semibold text-gray-900 mb-2">
                        {molecule.name}
                    </h2>
                    <p class="text-gray-600 mb-1">Formula: {molecule.formula}</p>
                    <p class="text-gray-600 mb-4">
                        Weight: {molecule.molecular_weight.toFixed(3)}
                    </p>
                    <a
                        href="/molecules/{molecule.id}"
                        class="text-primary-600 hover:text-primary-700 font-medium"
                    >
                        View Details →
                    </a>
                </div>
            {/each}
        </div>
    {/if}
</div>
