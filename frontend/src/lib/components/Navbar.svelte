<script lang="ts">
    const navItems = [
        { href: '/', label: 'Home' },
        { href: '/molecules', label: 'Molecules' },
        { href: '/elements', label: 'Elements' },
        { href: '/reactions', label: 'Reactions' },
        { href: '/simulations', label: 'Simulations' },
    ];
</script>

<nav class="h-16 bg-white shadow-md fixed top-0 left-0 right-0">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
            <div class="flex items-center">
                <a href="/" class="text-xl font-bold text-primary-600">
                    Chemistry Reactions
                </a>
            </div>
            <div class="flex items-center space-x-4">
                {#each navItems as item}
                    <a
                        href={item.href}
                        class="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-primary-600 hover:bg-gray-100"
                    >
                        {item.label}
                    </a>
                {/each}
            </div>
        </div>
    </div>
</nav>