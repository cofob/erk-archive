<!--
	@component
	Meta component that fill meta infromation in `<head>` for
	search robots and users.

	@param title Page title. Visible to user. Required for every page.
	@param title_postfix Page title suffix.
	@param description Page description.
	@param cover Cover image for URL preview (such as Discord, Telegram, Twitter).
	@param noindex If true then robots won't index this page.
	@slot Additional content. Same as `<svelte:head>`.

	@example
	<script lang="ts">
		import { Meta } from "$lib/components";
	</script>

	<Meta title="Page title" title_postfix="Page title postfix" description="Page description" cover="https://example.com/cover.png" noindex>
		<meta name="author" content="Author name" />
	</Meta>
-->
<script lang="ts">
	export let title: string;
	export let title_postfix = " — Автозалив";
	export let description: string | null = null;
	export let cover: string | null = null;
	export let noindex = true;

	const title_str = title + title_postfix;
</script>

<svelte:head>
	<title>{title_str}</title>

	<meta content={title_str} name="title" />
	<meta content={title_str} property="og:title" />
	<meta content={title_str} property="twitter:title" />

	{#if description != null}
		<meta content={description} name="description" />
		<meta content={description} property="og:description" />
		<meta content={description} property="twitter:description" />
	{/if}

	{#if cover != null}
		<meta content="website" property="og:type" />
		<meta content="summary_large_image" property="twitter:card" />
		<meta content={cover} property="og:image" />
		<meta content={cover} property="twitter:image" />
	{/if}

	{#if noindex}
		<meta name="robots" content="noindex" />
	{:else}
		<meta content="index, follow" name="robots" />
	{/if}
	<slot />
</svelte:head>
