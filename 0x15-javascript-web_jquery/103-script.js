$(document).ready(function() {
  $('INPUT#btn_translate').click(function() {
    let languageCode = $('INPUT#language_code').val().toLowerCase();
    let url = 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode + '/';
  
    $.get(url, function(data) {
      $('DIV#hello').text(data.hello);
    });
  });

  $('INPUT#language_code').keypress(function(event) {
    if (event.keyCode === 13) {
      $('INPUT#btn_translate').click();
    }
  });
});
