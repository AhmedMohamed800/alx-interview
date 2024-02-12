#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
request(`https://swapi-api.alx-tools.com/api/films/${movieId}/`, (error, _, body) => {
    if (error) {
        console.error('Error:', error);
    } else {
        const film = JSON.parse(body);
        const characters = film.characters;

        const charactersName = characters.map(
            url => new Promise((resolve, reject) => {
                request(url, (promiseErr, __, charactersReqBody) => {
                    if (promiseErr) {
                        reject(promiseErr);
                    }
                    resolve(JSON.parse(charactersReqBody).name);
                });
            }));

        Promise.all(charactersName)
            .then(charactersNames => console.log(charactersNames.join('\n')))
            .catch(errors => console.log(errors));
    }
});
