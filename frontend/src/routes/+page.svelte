<script lang="ts">
    import { onMount } from 'svelte';

    let words = ['Simulate', 'Analyze', 'Discover'];
    let currentIndex = 0;
    let displayWord = words[0];
    
    const features = [
        {
            title: 'Molecules',
            description: 'Browse and manage molecular structures',
            href: '/molecules',
            icon: '🧬'
        },
        {
            title: 'Elements',
            description: 'Browse the periodic table and element properties',
            href: '/elements',
            icon: '⚛️'
        },
        {
            title: 'Reactions',
            description: 'Create and simulate chemical reactions',
            href: '/reactions',
            icon: '⚗️'
        },
        {
            title: 'Simulations',
            description: 'View and analyze simulation results',
            href: '/simulations',
            icon: '📊'
        }
    ];

    onMount(() => {
        const interval = setInterval(() => {
            currentIndex = (currentIndex + 1) % words.length;
            displayWord = words[currentIndex];
        }, 3000);

        return () => clearInterval(interval);
    });
</script>

<div class="text-center">
    <h1 class="text-4xl font-bold text-gray-900 mb-4">
        {displayWord} Chemical Reactions
    </h1>
    <p class="text-xl text-gray-600 mb-8">
        Visualize and simulate chemical reactions in real-time
    </p>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        {#each features as feature}
            <a
                href={feature.href}
                class="card hover:shadow-lg transition-shadow"
            >
                <div class="text-4xl mb-4">{feature.icon}</div>
                <h2 class="text-2xl font-semibold text-gray-900 mb-2">
                    {feature.title}
                </h2>
                <p class="text-gray-600">{feature.description}</p>
            </a>
        {/each}
    </div>
</div>