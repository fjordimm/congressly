import type { Config } from "tailwindcss";

export default {
	content: [
        // Include everything inside src/app
        "./src/app/**/*.{js,jsx,ts,tsx}",
    
        // If you have other folders that contain components (e.g., src/components)
        // you can add them here as well:
        "./src/components/**/*.{js,jsx,ts,tsx}",
      ],
	theme: {
		extend: {
			fontFamily: {
				sans: [
					'"Inter"',
					"ui-sans-serif",
					"system-ui",
					"sans-serif",
					'"Apple Color Emoji"',
					'"Segoe UI Emoji"',
					'"Segoe UI Symbol"',
					'"Noto Color Emoji"',
				],
				'lilita': ['"Lilita One"', 'sans-serif'],
				'maven': ['"Maven Pro"', 'sans-serif'],
        		'sunflower': ['"Sunflower"', 'sans-serif'],
			},
			colors: {
				dark_red: "#780000",
				light_red: "#C1121F",
                cream: "#FDF0D5",
                dark_blue: "#003049",
                light_blue: "#669BBC",
			},
			backgroundImage: {
				"background-green-gradient": 'linear-gradient(180deg, #87A26A 0%, #3D5941 89%, #2B4737 100%)'
			}
		},
	},
} satisfies Config;
