%rebase('layout.tpl',title='ファイル一覧', script='files.show')
<div class="route">
    <style>
		table{
		  width:100%;
		  table-layout: fixed;
		}
		.tbl-header {
		  background-color: rgba(255,255,255,0.3);
		 }
		.tbl-content {
		  height: 100%;
		  overflow-x:auto;
		  margin-top: 0px;
		  border: 1px solid rgba(255,255,255,0.3);
		}
		th{
		  padding: 20px 15px;
		  text-align: left;
		  font-weight: 500;
		  font-size: 14px;
		  color: #fff;
		  text-transform: uppercase;
		  text-align: center;
		}
		td{
		  padding: 15px;
		  text-align: left;
		  vertical-align:middle;
		  font-weight: 300;
		  font-size: 14px;
		  color: #fff;
		  border-bottom: solid 1px rgba(255,255,255,0.1);
		  text-align: center;
		}
        .ion {
            color: #353232;
        }
        .ion:hover {
            color: #675b5b;
            cursor: pointer;
        }
		.ion.ion-lg {
			font-size: 24px;
		}

		/* follow me template */
		.made-with-love {
		  margin-top: 40px;
		  padding: 10px;
		  clear: left;
		  text-align: center;
		  font-size: 10px;
		  font-family: arial;
		  color: #fff;
		}
		.made-with-love i {
		  font-style: normal;
		  color: #F50057;
		  font-size: 14px;
		  position: relative;
		  top: 2px;
		}
		.made-with-love a {
		  color: #fff;
		  text-decoration: none;
		}
		.made-with-love a:hover {
		  text-decoration: underline;
		}
    </style>
    <h2 class="center">
        ファイル一覧
    </h2>
    <h5 class="center">
        `{{route['path']}}` ディレクトリのファイル一覧です
    </h5>
    <div class="tbl-header">
        <table border="0" cellpadding="0" cellspacing="0">
            <thead>
                <tr>
                    <th>
                    	サムネイル
                    </th>
                    <th>
                        ファイル名
                    </th>
                    <th>
                        フォーマット
                    </th>
                    <th>
                        パス
                    </th>
                    <th>
                        サイズ
                    </th>
                    <th>
                    	コピー
                    </th>
                </tr>
            </thead>
        </table>
    </div>
    <div class="tbl-content">
        <table border="0" cellpadding="0" cellspacing="0">
            <!-- <thead></thead> -->
            <tbody>
                % for index in indexes:
                <tr>
                    <td>
                        <img src="/static/thumb/{{index['thumbnail']}}"/>
                    </td>
                    <td>
                        {{index['name']}}
                    </td>
                    <td>
                        {{index['ext']}}
                    </td>
                    <td>
                        {{index['path']}}
                    </td>
                    <td>
                        {{index['size']}}
                    </td>
                    <td>
						<i class="ion ion-lg ion-social-windows copy-win" data-path="{{index['path']}}"></i>
                    	<i class="ion ion-lg ion-social-apple copy-osx" data-path="{{index['path']}}"></i>
                    </td>
                </tr>
                % end
            </tbody>
        </table>
    </div>
</div>