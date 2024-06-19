/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/*.{html,js}",
    "./templates/**/*.{html,js}",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {
      fontFamily: {
        "be-vietnam": ["beVietnam", "sans-serif"],
        "inter": ["Inter", "sans-serif"],
      },
      colors: {
        'primary': 'rgba(34, 52, 249, 1)',
        'primary-dark': 'rgba(3, 19, 192, 1)',
        'custom-gray': '#5C5B5B',
        'custom-gray-2': '#303031',
        'custom-gray-3': '#322F2F',
        'custome-white': 'rgba(217, 217, 217, 0)',
      }
    },
    plugins: [
      require('flowbite/plugin')
    ],
  }
}