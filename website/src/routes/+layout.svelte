<script lang="ts">
	import "$lib/app.css";
	import { Heading } from "$lib/components";
</script>

<svelte:head>
	<link rel="preconnect" href={import.meta.env.VITE_IPFS_ENDPOINT} />
</svelte:head>

<noscript>
	<div class="text-center py-10">
		<Heading level={1}>Включите JS!</Heading>
		<p>Без него сайт не будет работать.</p>
	</div>
</noscript>

<div class="absolute top-0 left-0" id="modal-zone" />

<main data-sveltekit-prefetch>
	<slot />
</main>
