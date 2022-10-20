<!--
	@component
	`H<level>` component with pre-defined style set.

	@param level Component level from 1 (`<h1>`) to 6 (`<h6>`).
	@param element Replace default `h<level>` HTML element with custom, `<p>` (`p`), for example.
	@param class Custom component classes that will be appended to the end.
	@slot Default slot for component content.

	@example
	<script lang="ts">
		import { Heading } from "$lib/components";
	</script>

	<Heading level={1}>Heading 1</Heading>
	<Heading level={2} element="p">p element</Heading>
-->
<script lang="ts">
	import { joinRestprops } from "$lib/utils";

	export let level: 1 | 2 | 3 | 4 | 5 | 6;
	export let element: string | undefined = undefined;

	const by_level = {
		1: "font-black text-neutral-100 text-4xl sm:text-5xl md:text-7xl",
		2: "font-black text-neutral-100 text-3xl sm:text-4xl md:text-6xl",
		3: "font-bold text-neutral-100 text-2xl sm:text-3xl md:text-5xl",
		4: "font-bold text-neutral-100 text-xl sm:text-2xl md:text-4xl",
		5: "font-semibold text-neutral-100 text-lg sm:text-xl md:text-3xl",
		6: "font-semibold text-neutral-100 text-md sm:text-lg md:text-2xl",
	};
</script>

<svelte:element this={element ? element : `h${level}`} class={joinRestprops($$restProps, by_level[level])}>
	<slot />
</svelte:element>
