<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
            <link crossorigin="anonymous" href="https://cdnjs.cloudflare.com/ajax/libs/handsontable/0.35.1/handsontable.min.css" integrity="sha256-Ml4ToKoA1TZWxVWAFJN4zdvMgm+kVviJlzBZm0c363c=" rel="stylesheet"/>
            <link crossorigin="anonymous" href="https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css" integrity="sha256-2YQRJMXD7pIAPHiXr0s+vlRWA7GYJEK0ARns7k2sbHY=" rel="stylesheet"/>
            <title>
                TEST
            </title>
        </meta>
    </head>
    <body>
        <form>
            <input type="text" id="search" style="width: 50%;font-size: 40px; line-height:1.3em;">
        </form>
        <div id="grid"></div>
    </body>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
    <script crossorigin="anonymous" integrity="sha256-PWAUi+35yh+xxj3S0hx6TYSI48V/RdMVfTZ2qvF3+uU=" src="https://cdnjs.cloudflare.com/ajax/libs/handsontable/0.35.1/handsontable.full.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.quicksearch/2.4.0/jquery.quicksearch.min.js" integrity="sha256-hD1kpQcVntR40eMx9uED+E4HAjD2OJkLIFcP6ukVd+g=" crossorigin="anonymous"></script>
    <script id="json-data">
      var data = {{ !data }}
    </script>
    <script>
    document.addEventListener("DOMContentLoaded", function() {
      var grid = document.getElementById('grid');
      var searchField = document.getElementById('search_field');
      var hot;

      hot = new Handsontable(grid, {
          data: data,
          colHeaders: ['サムネイル', 'ファイル名', '拡張子', 'ファイルパス', 'ファイルサイズ', 'width', 'height'],
          columns: [{
              data: "filename",
              renderer: coverRenderer,
              editor: false
          }, {
              data: "name",
              editor: false
          }, {
              data: "ext",
              editor: false
          }, {
              data: "path",
              editor: false
          }, {
              data: "size",
              editor: false
          }, {
              data: "w",
              editor: false
          }, {
              data: "h",
              editor: false
          }],
          className: "htCenter htMiddle",
          afterInit: function() {
            $('input#search').quicksearch('table tbody tr');
          }
      });

      var _data = document.getElementById('json-data');
      _data.parentNode.removeChild(_data);

      function coverRenderer(instance, td, row, col, prop, value, cellProperties) {
          var escaped = Handsontable.helper.stringify(value),
              img;

          img = document.createElement('IMG');
          img.src = '/static/thumb/' + value;
          td.style.backgroundColor = 'black';
          td.style.height = '300px';
          td.style.width = '300px';
          td.style.verticalAlign = 'middle';
          td.style.textAlign = 'center';
          Handsontable.dom.addEvent(img, 'mousedown', function(e) {
              e.preventDefault(); // prevent selection quirk
          });
          Handsontable.dom.empty(td);
          td.appendChild(img);
          return td;
      }
    });
    </script>
</html>
