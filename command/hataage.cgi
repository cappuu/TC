sub HATAAGE {

	if($in{'no'} eq ""){&ERR("NO:�� �Էµ��� �ʾҽ��ϴ�.");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN($kpos);

	open(IN,"$COUNTRY_LIST") or &ERR2('������ ���� �ʾҽ��ϴ�. err no :country');
	@COU_DATA = <IN>;
	close(IN);
	foreach(@COU_DATA){
		($x2cid,$x2name,$x2ele,$x2mark)=split(/<>/);
		$cou_name[$x2cid] = "$x2name";
		$cou_ele[$x2cid] = "$x2ele";
		$cou_mark[$x2cid] = "$x2mark";
		$mark[$x2ele] = 1;
	}

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR("���� ���� ����");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);

	@tmp = map {(split /<>/)[10]} @CL_DATA;
	@CL_DATA = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];
	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}

	&HEADER;
	$no = $in{'no'} + 1;

	print <<"EOM";
<hr size=0><CENTER><font size=4><b>-- �� �� --</b></font><hr size=0>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
$no_list
<TABLE width="450" bgcolor=$TABLE_C cellpadding="2" cellspacing="1">
<tr bgcolor=$TD_C1>
<td width=50 align="center">���ø�</td>
<td width=400 bgcolor=$TD_C3>
	$zname
</td>
</tr>
<tr bgcolor=$TD_C1>
<td width=50 align="center">������</td>
<td width=400 bgcolor=$TD_C3>
	<input type="text" name="cou_name" size="10" value="$in{'cou_name'}" maxlength="8">��<br>
	���ο� ������ ��Ī�� �������ּ���.
</td>
</tr>
<tr><TD bgcolor=$TD_C1><center>�� �� ��</TD><TD bgcolor=$TD_C3>
EOM
	$i=0;
	foreach(@ELE_BG){print "<input type=radio name=ele value=\"$i\"><font color=$ELE_BG[$i]>��</font> \n";$i++;}
	print <<"EOM";
<br><BGSOUND SRC="http://home.megapass.co.kr/~kjs503/mbg.wma" volume=0 loop=infinite>������ ���� ������ �ּ���. <b>(�Ͼ���� ���� ������. �۾��� �� �Ⱥ��Դϴ�.)</b></TD></tr>
</TABLE>
<input type=hidden name=mode value=41>
<input type=submit value=\"�Ǳ��Ѵ�\"></form>


<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="���ƿ´�"></form></CENTER>
EOM

	&FOOTER;

	exit;

}
1;
