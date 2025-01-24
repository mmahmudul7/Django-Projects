/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",  // Templates at the project level
    "./**/templates/**/*.html", // Templates inside apps
    './**/forms.py',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

