<script lang="ts">
	import "$lib/app.css";
	import { Heading } from "$lib/components";
</script>

<svelte:head>
	<link rel="preconnect" href={import.meta.env.VITE_IPFS_ENDPOINT} />
</svelte:head>

<!-- Background -->
<div class="min-h-screen min-w-screen bg-neutral-800 text-neutral-200">
	<!-- App -->
	<app class="hidden lg:block" data-sveltekit-prefetch>
		<div class="absolute top-0 left-0" id="modal-zone" />
		<slot />
	</app>

	<!-- Mobile stub -->
	<div class="block lg:hidden text-center py-10">
		<Heading level={4}>Слишком маленький экран</Heading>
		<Heading level={5} element="p">Зайдите с компьютера</Heading>
	</div>

	<!-- Noscript error -->
	<noscript>
		<div class="text-center py-10">
			<Heading level={1}>Включите JS!</Heading>
			<p>Без него сайт не будет работать.</p>
		</div>
	</noscript>
</div>
