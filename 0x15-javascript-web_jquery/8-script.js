$(document).ready(function() {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    data.results.forEach((movie) => {
	    $("ul#list_movies").append(`<li>${movie.title}</li>`);
			});
		}
	);
});
