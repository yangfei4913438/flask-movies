module.exports = {
  plugins: [
    require('postcss-import'),
    require('tailwindcss')('./tailwind.config.js'),
    require('autoprefixer'),
    require('postcss-nested'),
    require('postcss-nesting'),
    require('postcss-preset-env')({
      features: {'nesting-rules': false}
    }),
  ]
}