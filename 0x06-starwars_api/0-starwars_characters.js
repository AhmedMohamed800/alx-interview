#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
request(`https://swapi-api.alx-tools.com/api/films/${movieId}/`, (error, _, body) => {
    if (error) {
        console.error('Error:', error);
    } else {
        const film = JSON.parse(body);
        const characters = film.characters;
        characters.forEach((characterUrl) => {
            request(characterUrl, (error, _, body) => {
                if (error) {
                    console.error('Error:', error);
                } else {
                    const character = JSON.parse(body);
                    console.log(character.name);
                }
            });
        });
    }
});
