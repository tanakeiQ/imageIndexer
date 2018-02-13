<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
            <title>
                {{title or 'No title'}}
            </title>
            <link href="/static/css/normalize.css" rel="stylesheet">
                <link href="/static/css/skeleton.css" rel="stylesheet">
                    <link href="http://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css" rel="stylesheet">
                    </link>
                </link>
            </link>
        </meta>
        <style>
            .ion {
                color: #353232;
                font-size: 1.2em;
            }
            .ion:hover {
                color: #675b5b;
                cursor: pointer;
            }
            @import url(https://fonts.googleapis.com/css?family=Roboto:400,500,300,700);
            body {
                background: -webkit-linear-gradient(left, #25c481, #25b7c4);
                background: linear-gradient(to right, #25c481, #25b7c4);
                font-family: 'Roboto', sans-serif;
                color: white;
            }
            h1, h2, h3 {
                margin-top:2em;
            }
            h4,h5,h6 {
                margin-top: 1em;
            }
            .center {
                text-align: center;
            }
            input[type="email"], input[type="number"], input[type="search"], input[type="text"], input[type="tel"], input[type="url"], input[type="password"], textarea, select {
                background-color: rgba(0, 0, 0, 0.21);
                border: none;
                box-shadow: inset 0px 2px 4px 0px #636465;
            }
            .container {
                max-width: 1200px;
            }
            input[disabled] {
                border: none;
                background-color: inherit;
                text-align: center;
                box-shadow: none;
            }
            .button, button, input[type="submit"], input[type="reset"], input[type="button"] {
                border-color: white;
                color: white;
                font-size: 1.2em;
            }
            .button:hover, button:hover, input[type="submit"]:hover, input[type="reset"]:hover, input[type="button"]:hover {
                border-color: white;
                background-color: white;
                color: #3ebda2;
            }
            section{
                margin: 50px;
            }

            ::-webkit-scrollbar {
                width: 6px;
            } 
            ::-webkit-scrollbar-track {
                -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3); 
            } 
            ::-webkit-scrollbar-thumb {
                -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3); 
            }
        </style>
    </head>
    <body>
        %include
    </body>
    <script crossorigin="anonymous" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" src="http://code.jquery.com/jquery-3.3.1.min.js">
    </script>
</html>
% if defined('script'):
<script src="/static/js/{{script}}.js">
</script>
% end
