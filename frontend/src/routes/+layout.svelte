<script lang="ts">
    import Navbar from '$lib/components/Navbar.svelte';
    import { onMount } from 'svelte';

    import '../app.css';
    import { api } from '$lib/api/client';
    import { elements } from '$lib/stores/elements';
  import { scrollToTop } from '$lib/utils/globalHelpers';

    let { children } = $props();

    let loading = true;
    let error: string | null = null;
    let showScrollButton = $state<boolean>(false);
    
    onMount(async () => {
        if ($elements.length > 0) return;

        try {
            const response = await api.get('/elements/');
            $elements = response.data;
        } catch (e) {
            error = 'Failed to load elements';
            console.error(e);
        } finally {
            loading = false;
        }
    });

    onMount(() => {
        // Add scroll event listener
        window.addEventListener('scroll', () => {
            showScrollButton = window.scrollY > 500; // Show button after scrolling 500px
        });

        // Cannot live in an async onMount function
        return () => {
            window.removeEventListener('scroll', () => {
                showScrollButton = window.scrollY > 500;
            });
        };
    })
</script>

<div class="min-h-screen">
    <Navbar />

    <main class="max-w-7xl mx-auto mt-16 py-6 px-4 sm:px-6 lg:px-8">
        {@render children()}
    </main>

    {#if showScrollButton}
        <button
            onclick={scrollToTop}
            class="fixed bottom-8 right-8 p-3 bg-gray-800 hover:bg-gray-700 text-white rounded-full shadow-lg transition-all duration-300 opacity-90 hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-600"
            aria-label="Scroll to top"
        >
            <svg 
                xmlns="http://www.w3.org/2000/svg" 
                class="h-6 w-6" 
                fill="none" 
                viewBox="0 0 24 24" 
                stroke="currentColor"
            >
                <path 
                    stroke-linecap="round" 
                    stroke-linejoin="round" 
                    stroke-width="2" 
                    d="M5 10l7-7m0 0l7 7m-7-7v18"
                />
            </svg>
        </button>
    {/if}
</div>

<style>
    /* Optional: Add fade animation */
    button {
        animation: fade-in 0.3s ease-in-out;
    }

    @keyframes fade-in {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 0.9;
            transform: translateY(0);
        }
    }
</style>