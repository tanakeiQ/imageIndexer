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
		th:first-child, td:first-child {
			width: 30px;
			text-align: right;
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
		button.copy-clipboard {
			width: 30%;
		}
    </style>
    <h5 class="center">
        path: '{{route['path']}}'<br>
        <span style="color: #443e3b;">{{len(indexes)}} 件</span>
    </h5>
    <div class="tbl-header">
        <table border="0" cellpadding="0" cellspacing="0">
            <thead>
                <tr>
                	<th>
                		No.
                	</th>
                    <th>
                        サムネイル
                    </th>
                    <th>
                        ファイル名
                    </th>
                    <th style="width: 120px;">
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
        	% no = 1
            <tbody>
                % for index in indexes:
                <tr>
                	<td>
                		{{no}}
                		% no += 1
                	</td>
                    <td>
                        <img src="/static/thumb/{{index['thumbnail']}}"/>
                    </td>
                    <td>
                        {{index['name']}}
                    </td>
                    <td style="width: 120px;">
                        {{index['ext']}}
                    </td>
                    <td>
                        {{index['path']}}
                    </td>
                    <td>
                    	% data = index['size']
						
						<% 
							ext = ['Byte', 'Kb', 'Mb', 'Gb']
							extCount = 0
							while data > 1000:
								data = data / 1000
								extCount += 1
							end
							data = '%s %s' % (round(data, 2), ext[extCount])
						%>
						{{data}}
                    </td>
                    <td>
                        <input id="copy-win-{{index['id']}}" type="text" value="{{'%s/%s' % (configs['batch.input_dir'], index['path'])}}">
                            <button class="copy-clipboard" data-clipboard-target="#copy-win-{{index['id']}}">
                                <i class="ion ion-lg ion-social-windows">
                                </i>
                            </button>
                            <input id="copy-osx-{{index['id']}}" type="text" value="{{'%s/%s' % (configs['batch.input_dir'], index['path'])}}">
                                <button class="copy-clipboard" data-clipboard-target="#copy-osx-{{index['id']}}">
                                    <i class="ion ion-lg ion-social-apple">
                                    </i>
                                </button>
                            </input>
                        </input>
                    </td>
                </tr>
                % end
            </tbody>
        </table>
    </div>
</div>