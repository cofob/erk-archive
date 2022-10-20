<!--
	@component
	Checkbox component that can be used as a checkbox or a switch.

	@param checked State of the toggle.
	@param class Custom component classes that will be appended to the end.

	@example
	<script lang="ts">
		import { Checkbox } from "$lib/components";

		let checked: boolean = false;
	</script>

	<Checkbox bind:checked />
-->
<script lang="ts">
	export let checked: boolean = false;
</script>

<input type="checkbox" bind:checked class={$$restProps.class} />

<style lang="postcss">
	input {
		@apply relative bg-neutral-700 w-6 h-6 rounded-sm appearance-none cursor-pointer motion-safe:transition-all checked:bg-blue-500
						after:absolute after:block after:border-white after:top-[3px] after:left-2 after:rotate-45 after:border-b-2 after:border-r-2
						after:opacity-0 after:h-[14px] after:w-2 after:transition-all
						after:checked:opacity-100;
	}
</style>
