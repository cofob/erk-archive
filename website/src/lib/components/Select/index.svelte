<!--
	@component
	Select component that can be used as a dropdown.

	@param options Dictionary with key as group name and value as array of options, or list of options.
		If dictionary key is `__global` when it placed outside option groups.
	@param value Value of the selected option. If it equals to `unselectable_text`, then it will be undefined.
	@param unselectable If `true`, the first option will be `--select--` (`unselectable_text`).
	@param unselectable_text Text of the first option.
	@param class Custom component classes that will be appended to the end.

	@example
	<script lang="ts">
		import { Select } from "$lib/components";

		let value: string;
	</script>

	<Select options={["1", "2", "3"]} bind:value />

	{#if value}
		<p>You selected {value}</p>
	{/if}

	@example
	<script lang="ts">
		import { Select } from "$lib/components";

		let value: string;
	</script>

	<Select options={{"__global": ["1", "2", "3"], "test": ["a", "b", "c"], "group2": ["e", "f", "g"]} bind:value />

	{#if value}
		<p>You selected {value}</p>
	{/if}
-->
<script lang="ts">
	import { joinRestprops } from "$lib/utils";

	export let options: Record<string, string[]> | string[];
	export let value: string | undefined = undefined;
	export let unselectable: boolean = true;
	export let unselectable_text: string = "--select--";

	let select_value: string = unselectable_text;
	$: value = select_value == unselectable_text ? undefined : select_value;
</script>

<select class={joinRestprops($$restProps, "bg-neutral-700 p-1 rounded-md")} bind:value={select_value}>
	{#if Array.isArray(options)}
		{#if unselectable}
			<option>{unselectable_text}</option>
		{/if}
		{#each options as option}
			<option>{option}</option>
		{/each}
	{:else}
		{#if unselectable}
			<option>{unselectable_text}</option>
		{/if}
		{#if options["__global"]}
			{#each options["__global"] as option}
				<option>{option}</option>
			{/each}
		{/if}
		{#each Object.entries(options) as [group, group_options]}
			{#if group != "__global"}
				<optgroup label={group}>
					{#each group_options as option}
						<option>{option}</option>
					{/each}
				</optgroup>
			{/if}
		{/each}
	{/if}
</select>
