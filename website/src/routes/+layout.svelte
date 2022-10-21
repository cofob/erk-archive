<script lang="ts">
	import "$lib/app.css";
	import { title } from "$lib/stores";

	window.Telegram.WebApp.ready();
</script>

<svelte:head>
	<link rel="preconnect" href={import.meta.env.VITE_IPFS_ENDPOINT} />
</svelte:head>

<div id="modal-zone" />

<main>
	<nav class="top-nav">
		<button on:click={window.Telegram.WebApp.close} class="link">Закрыть</button>
		<span>{$title}</span>
		<span />
	</nav>

	<slot />
</main>

<style lang="postcss">
	#modal-zone {
		position: absolute;
		top: 0px;
		left: 0px;
	}
</style>
