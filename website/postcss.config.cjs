require("dotenv").config();

let config = {
	plugins: {
		"postcss-import": {},
		tailwindcss: {},
		autoprefixer: {},
		"postcss-ipfs": {
			gateway: process.env.VITE_IPFS_ENDPOINT + "/",
		},
	},
};

if (process.env.PROD == "true") {
	config.plugins = {
		...config.plugins,
		cssnano: {
			preset: "advanced",
		},
		"postcss-discard-comments": {
			removeAll: true,
		},
	};
}

module.exports = config;
