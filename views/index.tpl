%rebase('layout.tpl',title='ImageIndexer')
<div class="routes container">
    <style>
        .menus {
            margin-top: 30px;
            text-align: center;
            font-size: 32px;
        }
        .menus a {
            text-decoration: none;
            color: #495763;
        }
        .menus a:hover {
            color: lightgray;
        }
        .settings th, .settings td {
            text-align: left;
        }
    </style>
    <h2 class="center">
        ImageIndexer
    </h2>
    <div class="row">
        <div class="columns menus">
            <a href="/routes">
                <p>
                    ルーティング設定
                </p>
            </a>
            <a href="/files">
                <p>
                    ディレクトリ一覧
                </p>
            </a>
        </div>
    </div>
    <div class="row">
        <div class="columns settings">
            <table class="u-full-width">
                <thead>
                    <tr>
                        <th style="width: 30%;">
                            Setting
                        </th>
                        <th style="width: 70%;">
                            Value
                        </th>
                    </tr>
                </thead>
                <tbody>
                    % for config in configs:
                    <tr>
                        <td>{{config}}</td>
                        <td>{{configs.get(config)}}</td>
                    </tr>
                    % end
                </tbody>
            </table>
        </div>
    </div>
</div>