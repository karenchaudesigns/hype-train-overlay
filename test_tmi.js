const fs = require('fs');
const content = fs.readFileSync('tmi.min.js', 'utf8');
const events = [...content.matchAll(/\.emit\("([^"]+)"/g)].map(m => m[1]);
console.log([...new Set(events)]);
