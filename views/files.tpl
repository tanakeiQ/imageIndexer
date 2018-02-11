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
        <div class="four columns directory">
            <div class="thumbnails">
                <img alt="" src="/static/thumb/7fef0ed6-4b62-4973-9b04-0f951e912037_01.png">
                    <img alt="" src="/static/thumb/7fef0ed6-4b62-4973-9b04-0f951e912037_01.png">
                        <img alt="" src="/static/thumb/7fef0ed6-4b62-4973-9b04-0f951e912037_01.png">
                        </img>
                    </img>
                </img>
            </div>
            <div class="description">
                <p class="memo">
                    これはテストです
                </p>
                <p class="path">
                    files/design/TEST
                </p>
            </div>
        </div>
    </div>
</div>