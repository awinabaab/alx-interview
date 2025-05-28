#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

function fetchFilm (url) {
  const filmPromise = new Promise((resolve, reject) => {
    request(url, { json: true }, (error, response, film) => {
      if (error) {
        return reject(error);
      }

      if (response.statusCode !== 200) {
        return reject(new Error(`Status code: ${response.statusCode}`));
      }

      resolve(film);
    });
  });

  return filmPromise;
}

fetchFilm(URL)
  .then(async film => {
    const characterURLs = film.characters;

    for (const characterURL of characterURLs) {
      try {
        const character = await fetchFilm(characterURL);
        console.log(character.name);
      } catch (error) {
        console.error(error.message);
      }
    }
  }).catch(error => console.error(error.message));
