/**
 * Get IPFS gateway link for IPFS path.
 * @param path IPFS path. Example: `/Qmhash/file.txt`
 * @returns
 */
export function ipfs(path: string): string {
	return import.meta.env.VITE_IPFS_ENDPOINT + "/ipfs" + path;
}

/**
 * Get IPFS gateway link for IPNS path.
 * @param path IPNS path. Example: `/ipfs.tech/index.html`
 * @returns
 */
export function ipns(path: string): string {
	return import.meta.env.VITE_IPFS_ENDPOINT + "/ipns" + path;
}

/**
 * Join provided args with space.
 * @returns Joined args with space.
 */
export function joinClasses(...args: string[] | string[][]): string {
	return args.flat(2).join(" ");
}

/**
 * Join classes and add `$$restProps.class`.
 *
 * Why we dont add `class` directly? Because this is JavaScript reserved keyword, and we can't simply expose it with `export let class`,
 * so we use Svelte special variable `$$restProps` that contains all passed arguments.
 *
 * @returns Joined args and `$$restProps.class` with space.
 */
export function joinRestprops(restprops: SvelteRestProps, ...args: any[]): string {
	return joinClasses([...args, restprops.class ? restprops.class : []]);
}
