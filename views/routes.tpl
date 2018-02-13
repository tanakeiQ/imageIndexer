%rebase('layout.tpl',title='ルート設定',script='routes')
<style>
    table {
        width: 100%;
    }
    thead th, tbody td {
        text-align:center;
    }
    h1, h2, h3 {
        margin-top:2em;
    }
    .center {
        text-align: center;
    }
</style>
<div class="routes container">
    <h2 class="center">
        ルート設定
    </h2>
    <h5 class="center">
        リソースのディレクトリルートを選択します
    </h5>
    <form id="form_routes" action="/routes" method="POST">
        <div class="row">
            <div class="columns">
                <table border="0" cellpadding="0" cellspacing="0">
                    <thead>
                        <th>
                            有効化
                        </th>
                        % for key in routes['column']:
                        <th>
                            {{key}}
                        </th>
                        % end
                    </thead>
                    <tbody>
                        % for route in routes['result']:
                        <tr>
                            <td>
                                % if route['is_enabled'] is 1:
                                    <input type="checkbox" id="is_enabled" data-id="{{route['id']}}" data-is-enabled="true" checked />
                                % else:
                                    <input type="checkbox" id="is_enabled" data-id="{{route['id']}}" data-is-enabled="false" />
                                % end
                            </td>
                            % for key in routes['column_key']:
                            <td>
                                {{route[key] if route[key] is not None else '□' }}
                            </td>
                            % end
                        </tr>
                        % end
                    </tbody>
                </table>
            </div>
        </div>
        <div class="row">
            <div class="offset-by-three six columns">
                <input class="button-primary" style="width: 100%;" type="submit" value="更新する">
                </input>
            </div>
        </div>
    </form>
</div>