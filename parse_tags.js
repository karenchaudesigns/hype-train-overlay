const https = require('https');
https.get('https://dev.twitch.tv/docs/irc/tags', res => {
    let data = '';
    res.on('data', chunk => data += chunk);
    res.on('end', () => {
        const matches = [...data.matchAll(/msg-id=([a-zA-Z0-9_\-]+)/g)];
        const ids = [...new Set(matches.map(m => m[1]))];
        console.log("msg-ids found:");
        console.log(ids);
    });
});
