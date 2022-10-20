// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
// and what to do when importing types

declare namespace App {
	interface ImportMetaEnv {
		VITE_IPFS_ENDPOINT: string;
	}

	interface ImportMeta {
		readonly env: ImportMetaEnv;
	}
}
