sub DOKURITSU {

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
<td width=50 align="center">������ ����</td>
<td width=400 bgcolor=$TD_C3>
	$zname��
</td>
</tr>
<tr><TD bgcolor=$TD_C1><center>��������</TD><TD bgcolor=$TD_C3>
<span style="font-size:9pt;"><font face="����"><input type="radio" name="cou_name1" value="1"></font></span><font color=#00A5FF face="����"><span style="font-size:9pt;">������(��) 
                        <input type="radio" name="cou_name1" value="2"></span><font color="#33CC66" face="����"><span style="font-size:9pt;">�˳���(��)</span><font color=#00A5FF face="����"><font color=#006400><span style="font-size:9pt;"> 
                        <input type="radio" name="cou_name1" value="3"></span><font color="#FF7897" face="����"><span style="font-size:9pt;">������(��)</span><font color=#00A5FF face="����"><font color=#006400><font color=#B9062F><span style="font-size:9pt;"><input type="radio" name="cou_name1" value="4"></span></font><font color="#9966CC" face="����"><span style="font-size:9pt;">�ʳ���(��)</span><font color=#00A5FF face="����"><font color=#006400><font color=#B9062F><font color=#800080><span style="font-size:9pt;"><input type="radio" name="cou_name1" value="5"></span></font></font><font color="#CCCCCC" face="����"><span style="font-size:9pt;">������(��)</span><font color=#00A5FF face="����"><font color=#006400><font color=#B9062F><font color=#800080><font color=#282828><span style="font-size:9pt;"><input type="radio" name="cou_name1" value="6"></span><font color=#D2691E><span style="font-size:9pt;">�ѳ���(��)<input type="radio" name="cou_name1" value="7"></span></font></font></font></font><font color="#A57451" face="����"><span style="font-size:9pt;">����(��)</span><input type="radio" name="cou_name1" value="8"></span><font color="#EEE12F" face="����"><span style="font-size:9pt;">�Ŷ�(��)</span><input type="radio" name="cou_name1" value="9"></span><font color="#009999" face="����"><span style="font-size:9pt;">����(��)</span></b></TD></tr>
</TABLE>
<br>
<input type=hidden name=mode value=49>
<input type=submit value=\"�����Ѵ�\"></form>


<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="���ƿ´�"></form></CENTER>
EOM

	&FOOTER;

	exit;

}

sub DOKURITSU2 {

	if($in{'no'} eq ""){&ERR("NO:�� �Էµ��� �ʾҽ��ϴ�.");}


	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($zcon);


	if($in{'cou_name1'} eq "1"){
		$in{'cou_name'} = "��";
		$in{'ele'} = "1";
	}elsif($in{'cou_name1'} eq "2"){
		$in{'cou_name'} = "��";
		$in{'ele'} = "2";
	}elsif($in{'cou_name1'} eq "3"){
		$in{'cou_name'} = "��";
		$in{'ele'} = "3";
	}elsif($in{'cou_name1'} eq "4"){
		$in{'cou_name'} = "��";
		$in{'ele'} = "4";
	}elsif($in{'cou_name1'} eq "5"){
		$in{'cou_name'} = "��";
		$in{'ele'} = "5";
	}elsif($in{'cou_name1'} eq "6"){
		$in{'cou_name'} = "��";
		$in{'ele'} = "6";
	}elsif($in{'cou_name1'} eq "7"){
		$in{'cou_name'} = "����";
		$in{'ele'} = "7";
	}elsif($in{'cou_name1'} eq "8"){
		$in{'cou_name'} = "�Ŷ�";
		$in{'ele'} = "8";
	}elsif($in{'cou_name1'} eq "9"){
		$in{'cou_name'} = "����";
		$in{'ele'} = "9";
	}


	open(IN,"$COUNTRY_LIST") or &ERR2('������ ���� �ʾҽ��ϴ�. err no :country');
	@COU_DATA = <IN>;
	close(IN);

	foreach(@COU_DATA){
		($xxcid,$xxname,$xxele,$xxnum,$xxins,$xxind,$xxall,$xxgold,$xxhp,$xxmaxhp,$xxstr,$xxvit,$xxagi)=split(/<>/);
	if($xxname eq $in{'cou_name'}){&ERR("�� ����� �̹� �����ϴ� �����Դϴ�.");}
	}

	open(IN,"./charalog/command/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	$mes_num = @COM_DATA;

	if($mes_num > $MAX_COM) { pop(@COM_DATA); }

	@NEW_COM_DATA=();$i=0;
	if($in{'no'} eq "all"){
		while(@NEW_COM_DATA < $MAX_COM){
			push(@NEW_COM_DATA,"$in{'mode'}<>$in{'ele'}<>$zname������ ����<>$tt<>$kpos<>$in{'cou_name'}<><>\n");
		}
		$no = $in{'no'};
	}else{
		foreach(@COM_DATA){
			($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/);
			$ahit=0;
			foreach(@no){
				if($i eq $_){
					$ahit=1;
					push(@NEW_COM_DATA,"$in{'mode'}<>$in{'cou_name1'}<>$zname���� ����<>$tt<>$kpos<>$in{'cou_name'}<><>\n");
					$lno = $_ + 1;
					$no .= "$lno,";
				}
			}
			if(!$ahit){
				push(@NEW_COM_DATA,"$_");
			}

			$i++;
		}
	}
	open(OUT,">./charalog/command/$kid.cgi") or &ERR('������ ���� �ʾҽ��ϴ�.');
	print OUT @NEW_COM_DATA;
	close(OUT);

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>������ �Է��߽��ϴ�. $COUNTRY_LIST</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="Ȯ��"></form></CENTER>
EOM

	&FOOTER;

	exit;

}
1;
