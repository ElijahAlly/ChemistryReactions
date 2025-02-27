<script lang="ts">
    import { elements } from "$lib/stores/elements";
</script>

<div class="overflow-x-auto">
    <table class="min-w-full table-auto">
        <thead>
            <tr class="bg-gray-100">
                <th class="px-4 py-2">Number</th>
                <th class="px-4 py-2">Symbol</th>
                <th class="px-4 py-2">Name</th>
                <th class="px-4 py-2">Atomic Mass</th>
                <th class="px-4 py-2">Category</th>
            </tr>
        </thead>
        <tbody>
            {#each $elements as element}
                <tr class="border-b hover:bg-gray-50">
                    <td class="px-4 py-2 text-center">{element.atomic_number}</td>
                    <td class="px-4 py-2 text-center font-semibold">{element.symbol}</td>
                    <td class="px-4 py-2">{element.name}</td>
                    <td class="px-4 py-2 text-right">{element.atomic_weight.toFixed(3)}</td>
                    <!-- <td class="px-4 py-2">{element.category}</td> -->
                </tr>
            {/each}
        </tbody>
    </table>
</div>