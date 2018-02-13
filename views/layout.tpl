<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
            <title>
                {{title or 'No title'}}
            </title>
            <link href="/static/css/normalize.css" rel="stylesheet">
            <link href="/static/css/skeleton.css" rel="stylesheet">
            <link rel="stylesheet" href="http://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css">
        </meta>
        <style>
            .ion {
                color: mediumpurple;
                font-size: 1.2em;
            }
            .ion:hover {
                color: #7c49e4;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        %include
    </body>
    <script
  src="http://code.jquery.com/jquery-3.3.1.min.js"
  integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
  crossorigin="anonymous"></script>
    </script>
    % if defined('script'):
    <script src="/static/js/{{script}}.js"></script>
    % end

</html>