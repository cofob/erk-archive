<script lang="ts">
	let value: string;

	window.Telegram.WebApp.MainButton.setText("Подтвердить")
		.show()
		.onClick(function () {
			const data = JSON.stringify({ value });
			window.Telegram.WebApp.sendData(data);
			window.Telegram.WebApp.close();
		});
</script>

<input type="text" class="bg-neutral-700" placeholder="Текст..." required bind:value />
