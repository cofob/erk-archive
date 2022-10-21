<script lang="ts">
	import { title } from "$lib/stores";
	import { WebAppTypes } from "$lib/types";

	let value: string;

	function submit() {
		const data = JSON.stringify({ type: WebAppTypes.TEST, value });
		window.Telegram.WebApp.sendData(data);
		window.Telegram.WebApp.close();
	}

	window.Telegram.WebApp.MainButton.setText("Подтвердить").show().onClick(submit);

	title.set("Тестовая страница");
</script>

<section>
	<input type="text" placeholder="Текст..." required bind:value />
</section>
<input type="button" value="Отправить" on:click={submit} />
