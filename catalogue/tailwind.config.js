/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {},
    colors: {
      'atracktive-black': '#172018',
      'atracktive-blue-grey': '#93a79f',
      'atracktive-brown': '#4a412d',
      'atracktive-brown-2': '#2e1511',
      'atracktive-green': '#022d1f',
      'atracktive-green-2': '#2e4438',
      'atracktive-grey': '#515c5c',
      'atracktive-grey-white': '#f3f3f3',
      'atracktive-light-green': '#5e7447',
      'atracktive-light-green-2': '#5c7344',
      'atracktive-tan': '#b5ab84',
      'atracktive-tan-2': '#b6a881',
      'atracktive-tan-3': '#7f7f5d',
      'atracktive-tan-4': '#9a9c78',
      'atracktive-tan-5': '#a48d6c',
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

