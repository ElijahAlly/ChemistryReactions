<script lang="ts">
    import type { Element } from "$lib/types/elements";

    export let elements: Element[];
</script>

<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    {#each elements as element}
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
            <p class="text-gray-600 mb-4">Phase: {element.phase}</p>
            <hr />
            <p class="text-gray-600 mb-4 mt-4">Density: {element.density || '-'}</p>
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