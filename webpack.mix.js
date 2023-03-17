const mix = require('laravel-mix');

mix.react('resources/src/index.js', 'public/js')
    .sass('resources/src/assets/scss/shards-dashboard.scss', 'public/css');
