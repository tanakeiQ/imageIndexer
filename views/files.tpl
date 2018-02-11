%rebase('layout.tpl',title='ディレクトリ一覧',files='True')
<style>
    div.files {
        margin: 0 2%;
    }
    h1, h2, h3 {
        margin-top:2em;
    }
    .center {
        text-align: center;
    }
    .directory {
        margin-top: 15px;
        padding-top: 15px;
    }
    .directory:nth-child(3n+1) {
        margin-left: 0;
    }
    .directory:nth-child(n+4) {
        border-top: 1px solid lightgray;
    }
    .thumbnails img {
        width: 48%;
    }
    .memo {
        text-align: center;
        font-size: 20px;
    }
    .path {
        margin: 0;
    }
    .description {
        border-top: 1px dashed darkgray;
        background-color: #ececec;
        padding: 2px;
    }
</style>
<div class="files">
    <h2 class="center">
        ディレクトリ一覧
    </h2>
    <h5 class="center">
        ディレクトリを選択すると、ディレクトリ内の画像一覧が表示されます
    </h5>
    <div class="row">
        % for route in routes.keys():
            % if len(routes[route]) > 0:
                <div class="four columns directory">
                    <div class="thumbnails">
                        % for index in routes[route]:
                            <img alt="" src="/static/thumb/{{index['thumbnail']}}">
                        % end
                    </div>
                    <div class="description">
                        <p class="memo">
                            {{routes[route][0]['description']}}
                        </p>
                        <p class="path">
                            {{routes[route][0]['path']}}
                        </p>
                    </div>
                </div>
            % end
        % end
    </div>
</div>