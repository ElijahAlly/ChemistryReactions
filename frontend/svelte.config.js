import adapter from '@sveltejs/adapter-node';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://svelte.dev/docs/kit/integrations
	// for more information about preprocessors
	preprocess: vitePreprocess(),

	kit: {
		adapter: adapter({
			// Custom options for the node adapter
			out: 'build',
			precompress: false,
			envPrefix: '',
			polyfill: true
		}),
		// Add any additional SvelteKit configurations if needed
		csrf: {
			checkOrigin: false
		}
	}
};

export default config;
