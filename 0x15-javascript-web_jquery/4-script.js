$(document).ready(function () {
	const divToggle_Header = $("DIV#toggle_header");
	$(divToggle_Header).click(function () {
		$("header").toggleClass("red green");
	});
});
