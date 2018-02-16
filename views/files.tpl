%rebase('layout.tpl',title='ディレクトリ一覧',script='files')
<style>
    div.files {
        margin: 0 2%;
    }
    .directory {
        margin-top: 15px;
        padding-top: 15px;
            width: calc(33.3333333333333% - 30px);
    }
    .directory:nth-child(3n+1) {
        margin-left: 0;
    }
    .directory:nth-child(n+4) {
        border-top: 1px solid lightgray;
    }
    .thumbnails {
        margin: 0 auto;
        text-align: center;
    }
    .thumbnails a:hover {
        opacity: 0.7;
    }
    .thumbnails img {
        width: 48%;
    }
    .memo {
        text-align: center;
        font-size: 20px;
    }
    .memo input {
        width: 90%;
    }
    .path {
        margin: 0;
    }
    .description {
        border: 1px solid lightblue;
        padding: 2px;
    }
    .active {
        display: initial;
    }
    .disactive {
        display: none
    }
</style>
<div class="files">
    <h2 class="center">
        ディレクトリ一覧
    </h2>
    <h5 class="center">
        ディレクトリを選択すると、ディレクトリ内の画像一覧が表示されます
    </h5>
    <div class="row directory-wrapper">
            % for route in routes.keys():
            % if len(routes[route]) > 0:
                <div class="directory">
                    <div class="thumbnails">
                        <a href="/files/{{routes[route][0]['id']}}">
                            % for index in routes[route]:
                            <img alt="" src="/static/thumb/{{index['thumbnail']}}">
                            % end
                        </a>
                    </div>
                    <div class="description">
                        <div class="memo">
                            <input data-id="{{routes[route][0]['id']}}" disabled="disabled" type="text" value="{{routes[route][0]['description']}}"/>
                            <span class="edit-description active">
                                <i class="ion-edit ion">
                                </i>
                            </span>
                            <span class="edited-description disactive">
                                <i class="ion-checkmark ion">
                                </i>
                            </span>
                        </div>
                        <p class="path">
                            {{routes[route][0]['path']}}
                        </p>
                    </div>
                </div>
            % end
        % end
    </div>
</div>