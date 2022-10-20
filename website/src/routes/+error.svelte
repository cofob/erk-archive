<script lang="ts">
	import { Heading, Meta } from "$lib/components";

	import { page } from "$app/stores";
</script>

<Meta
	title="Ошибка"
	description={$page.status == 404
		? "Страница не найдена."
		: "Произошла непредвиденная ошибка. Повторите запрос позже."}
	noindex
/>

<div class="text-center pt-8">
	<Heading level={1}>
		{#if $page.status == 404}
			Ошибка 404
		{:else}
			Ошибка {$page.status}
		{/if}
	</Heading>
	{#if $page.error?.message !== undefined}
		<p class="pt-1 text-xl">
			{#if $page.status == 404}
				Страница не найдена
			{:else}
				{$page.error?.message}
			{/if}
		</p>
	{/if}
	<a href="/" class="hover:underline" data-sveltekit-reload>На главную?</a>
</div>
