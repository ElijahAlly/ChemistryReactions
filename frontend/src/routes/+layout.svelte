<script lang="ts">
    import Navbar from '$lib/components/Navbar.svelte';

    import '../app.css';

    let { children } = $props();
</script>

<div class="min-h-screen">
    <Navbar />

    <main class="max-w-7xl mx-auto mt-16 py-6 px-4 sm:px-6 lg:px-8">
        {@render children()}
    </main>
</div>