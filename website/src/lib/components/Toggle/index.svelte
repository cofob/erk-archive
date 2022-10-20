<!--
	@component
	Toggle component that can be used as a checkbox or a switch.

	@param checked State of the toggle.
	@param class Custom component classes that will be appended to the end.

	@example
	<script lang="ts">
		import { Toggle } from "$lib/components";

		let checked: boolean = false;
	</script>

	<Toggle bind:checked />
-->
<script lang="ts">
	export let checked: boolean = false;
</script>

<input type="checkbox" bind:checked class={$$restProps.class} />

<style lang="postcss">
	input {
		@apply relative bg-neutral-700 w-10 h-4 rounded-2xl appearance-none cursor-pointer my-1 motion-safe:transition-all checked:bg-blue-500
						after:absolute after:block after:-top-1 after:left-0 after:w-6 after:h-6 after:rounded-full after:motion-safe:transition-all after:bg-neutral-300
						after:checked:left-4;
	}
</style>
