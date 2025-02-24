import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import { svelteTesting } from "@testing-library/svelte/vite";

export default defineConfig({
    plugins: [sveltekit()],
    preview: {
		host: true,
		port: 10000,
		allowedHosts: [
			'localhost',
			'127.0.0.1',
			'.onrender.com',  // Allows all subdomains on render.com
			'chemistryreactionsfrontend.onrender.com',
            // When domain is purchased
			// 'chemistryreactions.org',
			// 'chemreactions.org',
		]
	},
	server: {
		host: true,
		port: 10000
	},
    test: {
        workspace: [{
            extends: "./vite.config.ts",
            plugins: [svelteTesting()],
            test: {
                name: "client",
                environment: "jsdom",
                clearMocks: true,
                include: ['src/**/*.svelte.{test,spec}.{js,ts}'],
                exclude: ['src/lib/server/**'],
                setupFiles: ['./vitest-setup-client.ts']
            }
        }, {
            extends: "./vite.config.ts",
            test: {
                name: "server",
                environment: "node",
                include: ['src/**/*.{test,spec}.{js,ts}'],
                exclude: ['src/**/*.svelte.{test,spec}.{js,ts}']
            }
        }]
    }
});