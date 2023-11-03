$(document).ready(function () {
  $('INPUT#btn_translate').click(function(){
    let langCode = $('INPUT#language_code').val();
    $.getJSON(
      'https://www.fourtonfish.com/hellosalut/hello/',
      { lang: langCode },
      function (data) {
        $('DIV#hello').text(data.hello);
      }
    );
  });
});
