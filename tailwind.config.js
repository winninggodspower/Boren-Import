/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/*.{html,js}",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {
      fontFamily: {
        "be-vietnam": ["Be Vietnam Pro", "sans-serif"],
        "inter": ["Inter", "sans-serif"],
      },
      colors: {
        'primary': 'rgba(34, 52, 249, 1)',
        'primary-dark': 'rgba(3, 19, 192, 1)',
        'custom-gray': '#5C5B5B',
        'custom-gray-2': '#303031',
      }
    },
    plugins: [
      require('flowbite/plugin')
    ],
  }
}
