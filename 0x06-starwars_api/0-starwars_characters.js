#!/usr/bin/node

const request = require('request');

function getMovieCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  
  request(url, (error, response, body) => {
    if (error) {
      console.log(`Error: ${error}`);
    } else if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const characterUrls = movieData.characters;

      characterUrls.forEach((characterUrl) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            console.log(`Error: ${error}`);
          } else if (response.statusCode === 200) {
            const characterData = JSON.parse(body);
            const characterName = characterData.name;
            console.log(characterName);
          } else {
            console.log(`Failed to retrieve character data for URL: ${characterUrl}`);
          }
        });
      });
    } else {
      console.log(`Failed to retrieve movie data for ID: ${movieId}`);
    }
  });
}

const movieId = process.argv[2];
if (!movieId) {
  console.log('Please provide a movie ID as a command-line argument.');
} else {
  getMovieCharacters(movieId);
}
