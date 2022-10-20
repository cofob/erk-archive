<!--
	@component
	Modal pop-up window.

	The component stores its state between opening and closing, so if you want to reset it, you have to do it yourself.

	@param title Modal title.
	@param buttons Array of buttons. Each button must have `text` and `callback` properties.
	@param closeable If true, modal can be closed by clicking on X button.
	@param close_icon Custom close icon.
	@param opened If true, it will open a modal page. Must be false when the component is created, otherwise it will blink on SSR.
	@param class Custom component classes that will be appended to the end.
	@slot Modal content.

	@example
	<script lang="ts">
		import toast from "svelte-french-toast";
		import { Heading, Modal } from "$lib/components";

		let opened: boolean; // false by-default
		let value: string;
	</script>

	<Modal
		title="Pancake selection"
		buttons={[
			{
				text: "Continue",
				callback: () => {
					if (value == "--select--") {
						toast.error("Please, select a pancake");
						return;
					}
					toast.success(`You selected ${value} pancacke!`);
					opened = false;
				},
			},
			{
				text: "Cancel",
				callback: () => {
					opened = false;
				},
			},
		]}
		bind:opened
	>
		<Heading level={2}>What pancacke do you prefer?</Heading>
		<select class="bg-neutral-700" bind:value>
			<option>--select--</option>
			<option>Chocolate</option>
			<option>Strawberry</option>
			<option>Vanilla</option>
		</select>
	</Modal>
-->
<script lang="ts">
	import { SvelteComponent, onMount } from "svelte";
	import X from "svelte-heros/X.svelte";

	import { joinRestprops } from "$lib/utils";

	interface Button {
		text: string;
		callback: () => void;
	}

	export let title: string;
	export let buttons: Button[] = [];
	export let closeable: boolean = true;
	export let close_icon: SvelteComponent = undefined;
	export let opened: boolean = false;

	let element: HTMLElement;

	onMount(() => {
		const modal_zone = document.getElementById("modal-zone");
		modal_zone.appendChild(element);
	});
</script>

<div
	bind:this={element}
	class={joinRestprops(
		$$restProps,
		"fixed top-0 left-0 w-screen min-h-screen z-10 bg-neutral-800 motion-safe:transition-all",
		opened ? "opacity-100 scale-100" : "pointer-events-none scale-90 opacity-0",
	)}
>
	<div class="w-full h-10 bg-blue-500 flex gap-x-2 items-center font-semibold pl-3">
		{#if closeable}
			<svelte:component
				this={close_icon ? close_icon : X}
				on:click={() => {
					opened = false;
				}}
			/>
		{/if}
		{title}
	</div>
	<div class="p-2">
		<slot />
	</div>
	{#if buttons.length != 0}
		<div class="absolute bottom-0 w-full h-10 border-t border-neutral-500 flex items-center my-1">
			<div class="absolute right-0 mr-1 flex gap-x-2 flex-row-reverse">
				{#each buttons as button}
					<button
						class="px-2 py-1 bg-blue-500 rounded-sm active:bg-blue-400 motion-safe:transition-colors"
						on:click={button.callback}>{button.text}</button
					>
				{/each}
			</div>
		</div>
	{/if}
</div>
