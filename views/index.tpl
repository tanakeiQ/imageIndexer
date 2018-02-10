<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
            <title>
                Setting - Route
            </title>
        </meta>
    </head>
    <body>
        <div class="routes">
            <h1>
                ルート設定
            </h1>
            <h2>
                リソースのディレクトリルートとなるディレクトリを選択します
            </h2>
            <form action="/routes" method="POST">
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
                                <input ''}}="" else="" id="" if="" name="" route['is_enabled']="1" type="checkbox" {{'checked'=""/>
                            </td>
                            % for key in routes['column_key']:
                            <td>
                                {{route[key]}}
                            </td>
                            % end
                        </tr>
                        % end
                    </tbody>
                </table>
                <div class="buttons">
                	<input type="submit" value="更新する">
                </div>
            </form>
        </div>
    </body>
</html>