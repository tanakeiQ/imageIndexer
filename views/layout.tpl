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
            .nav-bar {
                position: fixed;
                right: 0;
                bottom: 0;
                margin-right: 30px;
                margin-bottom: 15px;
            }
            .nav-bar li {
                list-style: none;
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
            li {
                list-style: none;
            }
        </style>
        <link crossorigin="anonymous" href="https://cdnjs.cloudflare.com/ajax/libs/jquery.wookmark/2.1.2/css/main.min.css" integrity="sha256-WvO2mkFS3pHQrVbp3UVMqYvouzjg9qI/1Gpv8mvCF3w=" rel="stylesheet"/>
    </head>
    <body>
        %include
        <div class="nav-bar">
            <li>
                <a href="/">
                    <i class="ion ion-lg ion-home">
                    </i>
                </a>
            </li>
            <li>
                <a href="/routes">
                    <i class="ion ion-lg ion-folder">
                    </i>
                </a>
            </li>
            <li>
                <a href="/files">
                    <i class="ion ion-lg ion-images">
                    </i>
                </a>
            </li>
        </div>
    </body>
    <script crossorigin="anonymous" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" src="http://code.jquery.com/jquery-3.3.1.min.js">
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/1.7.1/clipboard.min.js">
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/masonry/4.2.1/masonry.pkgd.min.js" integrity="sha256-D3o+8eRzMxa6mD+EDWrS5rMcEaAhISmCnRLdQ8kS2t4=" crossorigin="anonymous">
    </script>
    <script>
        $(function() {
            var clipboard = new Clipboard('.copy-clipboard');

            $('.directory-wrapper').masonry({
                percentPosition: true,
                columnWidth: 50,
                itemSelector: '.directory',
                transitionDuration: '.5s',
                resize: true
            });
        });
    </script>
</html>
% if defined('script'):
<script src="/static/js/{{script}}.js">
</script>
% end
