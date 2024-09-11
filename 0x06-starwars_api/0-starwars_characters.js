#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];
const API_FILMS = 'https://swapi-api.alx-tools.com/api/films/';

request(API_FILMS + movieID, (err, res) => {
  if (err) {
    console.error(err);
  }
  const characterURLs = JSON.parse(res.body).characters;

  const resolved = Promise.all(characterURLs.map((characterURL) => {
    return new Promise((resolve, reject) => {
      request(characterURL, (err, res) => {
        if (err) {
          reject(err);
        } else {
          resolve(JSON.parse(res.body));
        }
      });
    });
  }));

  resolved.then((data) => {
    for (const character of data) {
      console.log(character.name);
    }
  });
});
