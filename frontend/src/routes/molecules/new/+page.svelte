<script lang="ts">
    import { api } from "$lib/api/client";
    import FormulaInput from "$lib/components/Molecules/FormulaInput.svelte";
    import Input from "$lib/components/ui/Input.svelte";
    import type { Molecule } from "$lib/types/molecule";

    let name = '';
    let formula = '';
    let smiles = '';
    let molecularWeight = 0;

    let loading = false;
    let error: string | null = null;
    let molecules: Molecule[] = [];

    const handleSubmit = async (event: any) => {
        event.preventDefault();
        // Handle form submission
        try {
            const response = await api.post('/molecules/new', { 
                name, 
                formula 
            });

            molecules.push(response.data);

        } catch (e) {
            error = 'Failed to load molecules';
            console.error(e);
        } finally {
            loading = false;
        }
    };
</script>

<div class="w-full">
    <h1 class="text-3xl font-bold text-gray-900 mb-4">Add a New Molecule</h1>
    <form on:submit={handleSubmit} class="flex flex-col w-full">
        <div class="py-4 border-t flex flex-col">
            <label for="name" class="font-medium mb-3">Name:</label>
            <Input type="text" id="name" name="name" value={name} required class="w-1/2" />
        </div>
        <div class="py-4 border-t flex flex-col">
            <label for="formula" class="font-medium mb-3">Formula:</label>
            <FormulaInput bind:formula />
        </div>
        <div class="py-4 border-t flex flex-col">
            <label for="smiles" class="font-medium mb-3">Smiles:</label>
            <Input type="text" id="smiles" name="smiles" value={smiles} required class="w-1/4" />
        </div>
        <div class="py-4 border-t flex flex-col">
            <label for="molecular_weight" class="font-medium mb-3">Molecular Weight:</label>
            <Input type="text" id="molecular_weight" name="molecular_weight" value={molecularWeight} required class="max-w-36" />
        </div>
        <button type="submit">Submit Molecule</button>
    </form>
    <div class="flex flex-col">
        {#each molecules as molecule}
           <div class="flex flex-row">
                <div class="flex flex-col">
                    <h2>{molecule.name}</h2>
                    <p>{molecule.formula}</p>
                    <p>{molecule.smiles}</p>
                    <p>{molecule.molecular_weight}</p>
                </div>
            </div>
        {/each}
    </div>
</div>